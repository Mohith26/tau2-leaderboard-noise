# tau2-leaderboard-noise

How many neighbors on the τ²-bench text leaderboard are actually distinguishable?

Sierra publishes the per-simulation results behind the τ²-bench leaderboard in a public S3 bucket (`sierra-tau-bench-public`, the same `results.json` files the trajectory visualizer loads). `analyze.py` downloads every standard text submission's `results.json` for airline, retail, telecom and banking_knowledge, recomputes pass^k with the same rules as tau2-bench's `metrics/agent_metrics.py` (success means reward == 1, infrastructure errors dropped, pass^k = mean over tasks of C(successes, k) / C(trials, k)), and then bootstraps over tasks:

- a 95% interval for each submission's pass^1, and
- a paired bootstrap of the pass^1 difference between each submission and the one ranked just below it, on the tasks they share.

```
python3 analyze.py   # standard library only; caches downloads in ./cache
```

Full output is in [RESULTS.md](RESULTS.md).

## What I found

**43 of 46 adjacent pairs are within noise.** Across the four domains (8, 8, 8 and 26 submissions with public results), the 95% interval on the pass^1 gap between neighbors includes zero for 43 of the 46 neighboring pairs. With 50 to 114 tasks per domain and 4 trials each, the median 95% interval on a single submission's pass^1 is about 13 points wide, while most neighbors are less than 3 points apart. On banking_knowledge, where 26 submissions sit between about 10% and 55%, no two neighbors separate.

The three pairs that do separate:
- telecom: qwen3.5-397b-a17b-think over claude-opus-4-5 (+5.5, [+2.4, +8.6])
- airline: gpt-5-2-none (as recomputed from its published file) over claude-sonnet-4-5 (+8.5, [+1.5, +15.5])
- telecom: claude-sonnet-4-5 over gpt-5-2-none (+23.2, [+17.5, +28.9])

So the order within a cluster mostly reflects which tasks happened to go which way, not a measured difference. Comparisons across clusters (for example, the top of banking_knowledge against the bottom) do separate.

**Some published trajectory files do not reproduce the reported score.** Most submissions match to two decimals. The ones that don't, and what I could tell about why:

- `gpt-5-2-none_sierra_2026-02-26`, airline and retail: the `results.json` files record the agent as `gpt-5.2` with `reasoning_effort: medium`, not `none`. Airline recomputes to 80.5 pass^1 against a reported 52.5. It looks like the medium-effort run's files were linked to the no-reasoning submission. The telecom and banking files for the same submission do say `none`.
- `gemini-3-flash_sierra_2026-03-02`, airline: reported 82.5, the published file gives 67.0. I could not find an explanation in the file.
- banking_knowledge, several submissions from February to May: reported scores are 1 to 9 points above what their files give. The submission notes say banking_knowledge was re-graded under v1.0.1 grading fixes on 2026-07-15, and the larger gaps are all in files timestamped February to May. Apart from claude-fable-5 (whose gap comes from 53 infrastructure-error simulations), every banking file timestamped July or August matches. So this is most likely files from before the re-grade, not a scoring error.
- `glm-5-think_sierra_2026-03-02`, telecom: 52 simulations are infrastructure errors. Dropping them (as tau2-bench's metrics do) gives 97.9; the reported 86.8 matches counting them as failures, which the submission notes describe.

## Limits

- Bootstrapping over tasks treats the task set as a sample from a larger population of tasks. If you care only about these exact tasks, the right interval is narrower (trial noise only).
- I compared neighbors only, using my recomputed scores for the ranking. Rankings by reported score differ where the files do not match.
- I did not rerun any model. Everything comes from the published files, so if a file is stale, my numbers for that submission are too.
- Voice, multilingual and custom submissions are left out.
