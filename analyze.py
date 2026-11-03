"""How much of the tau2-bench text leaderboard is separable from noise?

Downloads the public per-simulation results that back the leaderboard
(results.json in Sierra's public S3 bucket), recomputes pass^k per
submission and domain, compares it with the pass^k reported in each
submission.json, and bootstraps over tasks to get confidence intervals
and paired comparisons between neighbors on the leaderboard.

Standard library only. Run: python3 analyze.py
"""
import gzip
import json
import random
import re
import urllib.parse
import urllib.request
from collections import defaultdict
from math import comb
from pathlib import Path

BUCKET = "https://sierra-tau-bench-public.s3.us-west-2.amazonaws.com"
DOMAINS = ("airline", "retail", "telecom", "banking_knowledge")
CACHE = Path("cache")
BOOT = 5000
SEED = 0


def list_keys():
    keys, token = [], None
    while True:
        url = f"{BUCKET}/?list-type=2&prefix=submissions/&max-keys=1000"
        if token:
            url += "&continuation-token=" + urllib.parse.quote(token)
        xml = urllib.request.urlopen(url).read().decode()
        keys += re.findall(r"<Key>([^<]+)</Key>", xml)
        m = re.search(r"<NextContinuationToken>([^<]+)</NextContinuationToken>", xml)
        if not m:
            return keys
        token = m.group(1)


def fetch_json(key):
    path = CACHE / key
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(urllib.request.urlopen(f"{BUCKET}/{key}").read())
    raw = path.read_bytes()
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    return json.loads(raw)


def pass_hat_k(trials_by_task, k):
    """tau2-bench's pass^k (metrics/agent_metrics.py): mean over tasks of
    C(successes, k) / C(trials, k), only defined up to the smallest per-task trial count."""
    if k > min(len(t) for t in trials_by_task.values()):
        return None
    vals = [comb(sum(t), k) / comb(len(t), k) for t in trials_by_task.values()]
    return 100 * sum(vals) / len(vals)


def boot_ci(per_task, rng):
    """95% percentile CI for pass^1 by resampling tasks."""
    tasks = list(per_task)
    means = []
    for _ in range(BOOT):
        s = [per_task[rng.choice(tasks)] for _ in tasks]
        means.append(100 * sum(sum(t) / len(t) for t in s) / len(s))
    means.sort()
    return means[int(0.025 * BOOT)], means[int(0.975 * BOOT) - 1]


def paired_diff(a, b, rng):
    """Paired bootstrap over shared tasks: CI of pass^1(a) - pass^1(b)."""
    shared = sorted(set(a) & set(b))
    rate = lambda t: sum(t) / len(t)
    diffs = []
    for _ in range(BOOT):
        s = [rng.choice(shared) for _ in shared]
        diffs.append(100 * sum(rate(a[t]) - rate(b[t]) for t in s) / len(s))
    diffs.sort()
    point = 100 * sum(rate(a[t]) - rate(b[t]) for t in shared) / len(shared)
    return point, diffs[int(0.025 * BOOT)], diffs[int(0.975 * BOOT) - 1], len(shared)


def main():
    rng = random.Random(SEED)
    keys = list_keys()
    pat = re.compile(r"^submissions/([^/]+)/trajectories/(" + "|".join(DOMAINS) + r")/results\.json$")
    rows = []
    for key in keys:
        m = pat.match(key)
        if not m:
            continue
        sub, domain = m.groups()
        try:
            meta = fetch_json(f"submissions/{sub}/submission.json")
        except Exception:
            meta = {}
        if meta.get("submission_type", "standard") != "standard" or meta.get("modality", "text") != "text":
            continue
        res = fetch_json(key)
        # Same rules as tau2-bench: drop infrastructure errors, success is reward == 1.
        per_task = defaultdict(list)
        infra = 0
        for sim in res["simulation_index"]:
            if sim.get("termination_reason") == "infrastructure_error":
                infra += 1
                continue
            r = sim.get("reward")
            per_task[sim["task_id"]].append(1 if (r is not None and abs(r - 1) <= 1e-6) else 0)
        reported = (meta.get("results") or {}).get(domain) or {}
        rows.append({
            "sub": sub,
                        "domain": domain,
            "tasks": len(per_task),
            "trials": max(len(t) for t in per_task.values()),
            "sims": sum(len(t) for t in per_task.values()),
            "infra": infra,
            "agent": f"{res['info'].get('agent_info', {}).get('llm')} ({(res['info'].get('agent_info', {}).get('llm_args') or {}).get('reasoning_effort')})",
            "per_task": per_task,
            "ours": {k: pass_hat_k(per_task, k) for k in (1, 2, 3, 4)},
            "reported": {k: reported.get(f"pass_{k}") for k in (1, 2, 3, 4)},
        })

    out = []
    mismatches = []
    total_pairs = inseparable = 0
    for domain in DOMAINS:
        drows = sorted((r for r in rows if r["domain"] == domain), key=lambda r: -(r["ours"][1] or 0))
        if not drows:
            continue
        out.append(f"\n## {domain} ({len(drows)} text submissions with public results)\n")
        out.append("| rank | submission | tasks x trials | pass^1 (recomputed) | 95% CI | reported pass^1 | next model down: diff, 95% CI |")
        out.append("|---|---|---|---|---|---|---|")
        for i, r in enumerate(drows):
            lo, hi = boot_ci(r["per_task"], rng)
            nxt = ""
            if i + 1 < len(drows):
                d, dlo, dhi, n = paired_diff(r["per_task"], drows[i + 1]["per_task"], rng)
                sep = dlo > 0 or dhi < 0
                total_pairs += 1
                inseparable += not sep
                nxt = f"{d:+.1f} [{dlo:+.1f}, {dhi:+.1f}]" + ("" if sep else " overlaps 0")
            rep = r["reported"][1]
            out.append(
                f"| {i + 1} | {r['sub']} | {r['tasks']} x {r['trials']} | {r['ours'][1]:.2f} | {lo:.1f} to {hi:.1f} | "
                f"{rep if rep is not None else 'n/a'} | {nxt} |"
            )
            for k in (1, 2, 3, 4):
                o, p = r["ours"][k], r["reported"][k]
                if o is not None and p is not None and abs(o - p) > 0.5:
                    mismatches.append(f"| {r['sub']} | {domain} | pass^{k} | {p:.2f} | {o:.2f} | {r['agent']} | {r['infra']} |")

    head = [
        "# Results",
        "",
        f"Bootstrap: {BOOT} resamples over tasks, seed {SEED}. Success means reward == 1 and infrastructure errors are dropped, as in tau2-bench's metrics.",
        f"Adjacent leaderboard pairs whose pass^1 difference CI includes 0: {inseparable} of {total_pairs}.",
    ]
    tail = ["\n## Reported vs recomputed pass^k (differences over 0.5 points)\n",
            "| submission | domain | metric | reported | recomputed | agent model (reasoning) in results.json | infra errors dropped |",
            "|---|---|---|---|---|---|---|"]
    tail += mismatches or ["| none | | | | | | |"]
    text = "\n".join(head + out + tail) + "\n"
    Path("RESULTS.md").write_text(text)
    print(text)


if __name__ == "__main__":
    main()
