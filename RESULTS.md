# Results

Bootstrap: 5000 resamples over tasks, seed 0. Success means reward == 1 and infrastructure errors are dropped, as in tau2-bench's metrics.
Adjacent leaderboard pairs whose pass^1 difference CI includes 0: 43 of 46.

## airline (8 text submissions with public results)

| rank | submission | tasks x trials | pass^1 (recomputed) | 95% CI | reported pass^1 | next model down: diff, 95% CI |
|---|---|---|---|---|---|---|
| 1 | claude-opus-4-5_sierra_2026-02-26 | 50 x 4 | 84.00 | 76.0 to 91.5 | 84.0 | +1.0 [-4.0, +6.5] overlaps 0 |
| 2 | gpt-5-2_sierra_2026-02-26 | 50 x 4 | 83.00 | 73.5 to 91.5 | 83.0 | +0.5 [-6.0, +7.0] overlaps 0 |
| 3 | glm-5-think_sierra_2026-03-02 | 50 x 4 | 82.50 | 74.0 to 90.5 | 82.5 | +1.0 [-4.5, +7.0] overlaps 0 |
| 4 | gemini-3-pro_sierra_2026-03-02 | 50 x 4 | 81.50 | 71.5 to 90.5 | 80.5 | +0.0 [-10.0, +10.0] overlaps 0 |
| 5 | qwen3.5-397b-a17b-think_sierra_2026-03-02 | 50 x 4 | 81.50 | 72.0 to 90.0 | 81.5 | +1.0 [-7.0, +9.5] overlaps 0 |
| 6 | gpt-5-2-none_sierra_2026-02-26 | 50 x 4 | 80.50 | 72.0 to 88.5 | 52.5 | +8.5 [+1.5, +15.5] |
| 7 | claude-sonnet-4-5_sierra_2026-02-26 | 50 x 4 | 72.00 | 62.0 to 81.5 | 72.0 | +5.0 [-7.0, +17.5] overlaps 0 |
| 8 | gemini-3-flash_sierra_2026-03-02 | 50 x 4 | 67.00 | 54.5 to 79.0 | 82.5 |  |

## retail (8 text submissions with public results)

| rank | submission | tasks x trials | pass^1 (recomputed) | 95% CI | reported pass^1 | next model down: diff, 95% CI |
|---|---|---|---|---|---|---|
| 1 | qwen3.5-397b-a17b-think_sierra_2026-03-02 | 114 x 4 | 84.43 | 80.0 to 88.8 | 84.43 | +2.9 [-1.8, +7.5] overlaps 0 |
| 2 | gpt-5-2_sierra_2026-02-26 | 114 x 4 | 81.58 | 76.8 to 86.0 | 81.58 | +2.0 [-2.9, +6.8] overlaps 0 |
| 3 | claude-opus-4-5_sierra_2026-02-26 | 114 x 4 | 79.61 | 74.6 to 84.2 | 79.61 | +0.4 [-4.4, +5.4] overlaps 0 |
| 4 | gemini-3-pro_sierra_2026-03-02 | 114 x 4 | 79.24 | 73.8 to 84.6 | 75.88 | +2.5 [-2.2, +7.2] overlaps 0 |
| 5 | gemini-3-flash_sierra_2026-03-02 | 114 x 4 | 76.75 | 70.8 to 82.2 | 76.75 | +0.6 [-5.0, +6.1] overlaps 0 |
| 6 | gpt-5-2-none_sierra_2026-02-26 | 114 x 4 | 76.17 | 70.6 to 81.6 | 75.0 | +1.8 [-4.2, +7.9] overlaps 0 |
| 7 | glm-5-think_sierra_2026-03-02 | 114 x 4 | 74.42 | 68.5 to 80.0 | 73.68 | +2.0 [-3.3, +7.5] overlaps 0 |
| 8 | claude-sonnet-4-5_sierra_2026-02-26 | 114 x 4 | 72.37 | 66.9 to 77.6 | 72.37 |  |

## telecom (8 text submissions with public results)

| rank | submission | tasks x trials | pass^1 (recomputed) | 95% CI | reported pass^1 | next model down: diff, 95% CI |
|---|---|---|---|---|---|---|
| 1 | glm-5-think_sierra_2026-03-02 | 114 x 4 | 97.88 | 96.3 to 99.3 | 86.84 | +0.1 [-1.5, +1.6] overlaps 0 |
| 2 | qwen3.5-397b-a17b-think_sierra_2026-03-02 | 114 x 4 | 97.81 | 96.3 to 99.1 | 97.81 | +5.5 [+2.4, +8.6] |
| 3 | claude-opus-4-5_sierra_2026-02-26 | 114 x 4 | 92.32 | 89.3 to 95.2 | 92.32 | +1.0 [-2.3, +4.4] overlaps 0 |
| 4 | gemini-3-pro_sierra_2026-03-02 | 114 x 4 | 91.37 | 87.9 to 94.4 | 91.01 | +0.1 [-4.0, +4.2] overlaps 0 |
| 5 | gemini-3-flash_sierra_2026-03-02 | 114 x 4 | 91.23 | 88.4 to 93.9 | 91.23 | +1.5 [-2.2, +5.3] overlaps 0 |
| 6 | gpt-5-2_sierra_2026-02-26 | 114 x 4 | 89.69 | 86.0 to 93.2 | 89.69 | +4.8 [-0.7, +10.1] overlaps 0 |
| 7 | claude-sonnet-4-5_sierra_2026-02-26 | 114 x 4 | 84.87 | 80.5 to 89.0 | 84.87 | +23.2 [+17.5, +28.9] |
| 8 | gpt-5-2-none_sierra_2026-02-26 | 114 x 4 | 61.62 | 54.8 to 68.2 | 57.23684210526315 |  |

## banking_knowledge (26 text submissions with public results)

| rank | submission | tasks x trials | pass^1 (recomputed) | 95% CI | reported pass^1 | next model down: diff, 95% CI |
|---|---|---|---|---|---|---|
| 1 | qwen3-8-max_sierra_2026-08-04 | 97 x 4 | 55.15 | 46.6 to 63.7 | 55.154639175257735 | +6.4 [-0.3, +13.7] overlaps 0 |
| 2 | claude-opus-5_sierra_2026-08-04 | 97 x 4 | 48.71 | 40.2 to 57.5 | 48.71134020618557 | +0.8 [-5.9, +7.5] overlaps 0 |
| 3 | grok-4-5_sierra_2026-08-04 | 97 x 4 | 47.94 | 39.4 to 56.4 | 47.93814432989691 | +1.4 [-4.7, +7.6] overlaps 0 |
| 4 | gpt-5-6-sol_sierra_2026-08-04 | 96 x 4 | 47.05 | 38.7 to 55.4 | 46.90721649484536 | +2.3 [-5.3, +10.3] overlaps 0 |
| 5 | claude-fable-5_sierra_2026-08-04 | 88 x 4 | 44.89 | 35.5 to 54.5 | 39.69072164948454 | -1.0 [-9.1, +6.9] overlaps 0 |
| 6 | gpt-5-5_sierra_2026-05-05 | 97 x 4 | 44.50 | 35.8 to 53.2 | 44.58762886597938 | +4.3 [-2.1, +10.7] overlaps 0 |
| 7 | claude-opus-4-7_sierra_2026-05-05 | 97 x 4 | 40.21 | 32.0 to 48.7 | 40.20618556701031 | +0.5 [-3.6, +4.6] overlaps 0 |
| 8 | claude-opus-4-8_sierra_2026-08-04 | 97 x 4 | 39.69 | 31.7 to 48.2 | 39.69072164948454 | +2.6 [-2.8, +7.7] overlaps 0 |
| 9 | glm-5-2_sierra_2026-08-04 | 97 x 4 | 37.11 | 29.6 to 44.6 | 37.11340206185567 | +0.0 [-6.7, +6.7] overlaps 0 |
| 10 | kimi-k3_sierra_2026-08-04 | 97 x 4 | 37.11 | 29.4 to 44.6 | 37.11340206185567 | +6.4 [-0.3, +13.1] overlaps 0 |
| 11 | gpt-5-4_sierra_2026-03-25 | 97 x 4 | 30.67 | 23.2 to 38.7 | 39.43 | +5.7 [-1.8, +13.4] overlaps 0 |
| 12 | inkling_sierra_2026-08-04 | 97 x 4 | 25.00 | 18.0 to 32.2 | 25.0 | +0.3 [-6.2, +6.7] overlaps 0 |
| 13 | gpt-5-2_sierra_2026-02-26 | 97 x 4 | 24.74 | 17.8 to 32.0 | 32.22 | +0.3 [-6.4, +7.0] overlaps 0 |
| 14 | claude-opus-4-6_sierra_2026-05-05 | 97 x 4 | 24.48 | 17.5 to 31.7 | 27.32 | +2.1 [-4.6, +8.5] overlaps 0 |
| 15 | claude-sonnet-4-5_sierra_2026-02-26 | 97 x 4 | 22.42 | 16.2 to 29.1 | 25.26 | +0.0 [-6.7, +7.0] overlaps 0 |
| 16 | gemini-3-1-pro-preview_sierra_2026-05-05 | 97 x 4 | 22.42 | 16.5 to 28.9 | 26.03 | +1.0 [-6.2, +8.0] overlaps 0 |
| 17 | claude-opus-4-5_sierra_2026-02-26 | 97 x 4 | 21.39 | 15.2 to 28.1 | 24.74 | +0.8 [-5.4, +7.5] overlaps 0 |
| 18 | gemini-3-flash_sierra_2026-03-02 | 97 x 4 | 20.62 | 14.9 to 26.8 | 27.32 | +3.1 [-2.6, +8.8] overlaps 0 |
| 19 | grok-4-2_sierra_2026-05-05 | 97 x 4 | 17.53 | 11.6 to 24.2 | 18.04 | +1.8 [-3.4, +7.2] overlaps 0 |
| 20 | gemini-3-pro_sierra_2026-03-02 | 97 x 4 | 15.72 | 10.3 to 21.1 | 18.04 | +1.5 [-3.9, +7.0] overlaps 0 |
| 21 | grok-4-fast_sierra_2026-05-05 | 97 x 4 | 14.18 | 9.0 to 19.8 | 15.72 | +1.4 [-2.5, +5.1] overlaps 0 |
| 22 | gemini-2-5-pro_sierra_2026-05-05 | 97 x 4 | 12.80 | 8.2 to 18.0 | 13.66 | +0.4 [-4.1, +5.1] overlaps 0 |
| 23 | gpt-5-2-none_sierra_2026-02-26 | 97 x 4 | 12.37 | 7.2 to 18.0 | 12.63 | +0.0 [-4.4, +4.4] overlaps 0 |
| 24 | grok-4-1-fast_sierra_2026-05-05 | 97 x 4 | 12.37 | 7.5 to 17.8 | 13.14 | +2.5 [-2.6, +7.6] overlaps 0 |
| 25 | qwen3.5-397b-a17b-think_sierra_2026-03-02 | 97 x 4 | 9.88 | 5.2 to 15.2 | 9.79 | +0.1 [-2.5, +2.5] overlaps 0 |
| 26 | glm-5-think_sierra_2026-03-02 | 97 x 4 | 9.79 | 4.9 to 15.2 | 9.79 |  |

## Reported vs recomputed pass^k (differences over 0.5 points)

| submission | domain | metric | reported | recomputed | agent model (reasoning) in results.json | infra errors dropped |
|---|---|---|---|---|---|---|
| gemini-3-pro_sierra_2026-03-02 | airline | pass^1 | 80.50 | 81.50 | vertex_ai/gemini-3-pro-preview (high) | 3 |
| gemini-3-pro_sierra_2026-03-02 | airline | pass^2 | 74.67 | 76.67 | vertex_ai/gemini-3-pro-preview (high) | 3 |
| gemini-3-pro_sierra_2026-03-02 | airline | pass^3 | 70.00 | 73.00 | vertex_ai/gemini-3-pro-preview (high) | 3 |
| gpt-5-2-none_sierra_2026-02-26 | airline | pass^1 | 52.50 | 80.50 | gpt-5.2 (medium) | 0 |
| gpt-5-2-none_sierra_2026-02-26 | airline | pass^2 | 35.67 | 71.00 | gpt-5.2 (medium) | 0 |
| gpt-5-2-none_sierra_2026-02-26 | airline | pass^3 | 27.00 | 64.50 | gpt-5.2 (medium) | 0 |
| gpt-5-2-none_sierra_2026-02-26 | airline | pass^4 | 22.00 | 60.00 | gpt-5.2 (medium) | 0 |
| gemini-3-flash_sierra_2026-03-02 | airline | pass^1 | 82.50 | 67.00 | vertex_ai/gemini-3-flash-preview (high) | 0 |
| gemini-3-flash_sierra_2026-03-02 | airline | pass^2 | 76.33 | 64.33 | vertex_ai/gemini-3-flash-preview (high) | 0 |
| gemini-3-flash_sierra_2026-03-02 | airline | pass^3 | 72.00 | 63.00 | vertex_ai/gemini-3-flash-preview (high) | 0 |
| gemini-3-flash_sierra_2026-03-02 | airline | pass^4 | 68.00 | 62.00 | vertex_ai/gemini-3-flash-preview (high) | 0 |
| gemini-3-pro_sierra_2026-03-02 | retail | pass^1 | 75.88 | 79.24 | vertex_ai/gemini-3-pro-preview (high) | 20 |
| gemini-3-pro_sierra_2026-03-02 | retail | pass^2 | 63.45 | 69.15 | vertex_ai/gemini-3-pro-preview (high) | 20 |
| gemini-3-pro_sierra_2026-03-02 | retail | pass^3 | 54.39 | 61.62 | vertex_ai/gemini-3-pro-preview (high) | 20 |
| gpt-5-2-none_sierra_2026-02-26 | retail | pass^1 | 75.00 | 76.17 | gpt-5.2 (medium) | 51 |
| gpt-5-2-none_sierra_2026-02-26 | retail | pass^2 | 62.13 | 63.45 | gpt-5.2 (medium) | 51 |
| glm-5-think_sierra_2026-03-02 | retail | pass^1 | 73.68 | 74.42 | openai/glm-5-fp8 (None) | 4 |
| glm-5-think_sierra_2026-03-02 | retail | pass^2 | 60.38 | 61.55 | openai/glm-5-fp8 (None) | 4 |
| glm-5-think_sierra_2026-03-02 | retail | pass^3 | 51.10 | 52.41 | openai/glm-5-fp8 (None) | 4 |
| glm-5-think_sierra_2026-03-02 | telecom | pass^1 | 86.84 | 97.88 | openai/glm-5-fp8 (None) | 52 |
| glm-5-think_sierra_2026-03-02 | telecom | pass^2 | 76.32 | 95.76 | openai/glm-5-fp8 (None) | 52 |
| gemini-3-pro_sierra_2026-03-02 | telecom | pass^2 | 84.50 | 85.09 | vertex_ai/gemini-3-pro-preview (high) | 2 |
| gemini-3-pro_sierra_2026-03-02 | telecom | pass^3 | 79.17 | 79.82 | vertex_ai/gemini-3-pro-preview (high) | 2 |
| gpt-5-2-none_sierra_2026-02-26 | telecom | pass^1 | 57.24 | 61.62 | gpt-5.2 (none) | 0 |
| gpt-5-2-none_sierra_2026-02-26 | telecom | pass^2 | 42.84 | 47.95 | gpt-5.2 (none) | 0 |
| gpt-5-2-none_sierra_2026-02-26 | telecom | pass^3 | 35.53 | 39.91 | gpt-5.2 (none) | 0 |
| gpt-5-2-none_sierra_2026-02-26 | telecom | pass^4 | 30.70 | 34.21 | gpt-5.2 (none) | 0 |
| claude-fable-5_sierra_2026-08-04 | banking_knowledge | pass^1 | 39.69 | 44.89 | anthropic/claude-fable-5 (max) | 53 |
| gpt-5-4_sierra_2026-03-25 | banking_knowledge | pass^1 | 39.43 | 30.67 | openai/responses/gpt-5.4 (None) | 0 |
| gpt-5-4_sierra_2026-03-25 | banking_knowledge | pass^2 | 29.55 | 22.51 | openai/responses/gpt-5.4 (None) | 0 |
| gpt-5-4_sierra_2026-03-25 | banking_knowledge | pass^3 | 24.48 | 18.56 | openai/responses/gpt-5.4 (None) | 0 |
| gpt-5-4_sierra_2026-03-25 | banking_knowledge | pass^4 | 21.65 | 16.49 | openai/responses/gpt-5.4 (None) | 0 |
| gpt-5-2_sierra_2026-02-26 | banking_knowledge | pass^1 | 32.22 | 24.74 | gpt-5.2 (high) | 0 |
| gpt-5-2_sierra_2026-02-26 | banking_knowledge | pass^2 | 23.88 | 16.84 | gpt-5.2 (high) | 0 |
| gpt-5-2_sierra_2026-02-26 | banking_knowledge | pass^3 | 20.62 | 13.66 | gpt-5.2 (high) | 0 |
| gpt-5-2_sierra_2026-02-26 | banking_knowledge | pass^4 | 18.56 | 11.34 | gpt-5.2 (high) | 0 |
| claude-opus-4-6_sierra_2026-05-05 | banking_knowledge | pass^1 | 27.32 | 24.48 | claude-opus-4-6 (None) | 0 |
| claude-opus-4-6_sierra_2026-05-05 | banking_knowledge | pass^2 | 18.73 | 16.67 | claude-opus-4-6 (None) | 0 |
| claude-opus-4-6_sierra_2026-05-05 | banking_knowledge | pass^3 | 14.18 | 12.89 | claude-opus-4-6 (None) | 0 |
| claude-opus-4-6_sierra_2026-05-05 | banking_knowledge | pass^4 | 11.34 | 10.31 | claude-opus-4-6 (None) | 0 |
| claude-sonnet-4-5_sierra_2026-02-26 | banking_knowledge | pass^1 | 25.26 | 22.42 | claude-sonnet-4-5-20250929 (high) | 0 |
| claude-sonnet-4-5_sierra_2026-02-26 | banking_knowledge | pass^2 | 15.81 | 14.09 | claude-sonnet-4-5-20250929 (high) | 0 |
| claude-sonnet-4-5_sierra_2026-02-26 | banking_knowledge | pass^3 | 12.63 | 11.86 | claude-sonnet-4-5-20250929 (high) | 0 |
| gemini-3-1-pro-preview_sierra_2026-05-05 | banking_knowledge | pass^1 | 26.03 | 22.42 | vertex_ai/gemini-3.1-pro-preview (high) | 2 |
| gemini-3-1-pro-preview_sierra_2026-05-05 | banking_knowledge | pass^2 | 15.12 | 12.71 | vertex_ai/gemini-3.1-pro-preview (high) | 2 |
| gemini-3-1-pro-preview_sierra_2026-05-05 | banking_knowledge | pass^3 | 11.08 | 9.28 | vertex_ai/gemini-3.1-pro-preview (high) | 2 |
| claude-opus-4-5_sierra_2026-02-26 | banking_knowledge | pass^1 | 24.74 | 21.39 | claude-opus-4-5 (None) | 0 |
| claude-opus-4-5_sierra_2026-02-26 | banking_knowledge | pass^2 | 17.18 | 13.75 | claude-opus-4-5 (None) | 0 |
| claude-opus-4-5_sierra_2026-02-26 | banking_knowledge | pass^3 | 13.66 | 10.57 | claude-opus-4-5 (None) | 0 |
| claude-opus-4-5_sierra_2026-02-26 | banking_knowledge | pass^4 | 11.34 | 8.25 | claude-opus-4-5 (None) | 0 |
| gemini-3-flash_sierra_2026-03-02 | banking_knowledge | pass^1 | 27.32 | 20.62 | vertex_ai/gemini-3-flash-preview (high) | 0 |
| gemini-3-flash_sierra_2026-03-02 | banking_knowledge | pass^2 | 15.46 | 10.31 | vertex_ai/gemini-3-flash-preview (high) | 0 |
| gemini-3-flash_sierra_2026-03-02 | banking_knowledge | pass^3 | 10.31 | 6.44 | vertex_ai/gemini-3-flash-preview (high) | 0 |
| gemini-3-flash_sierra_2026-03-02 | banking_knowledge | pass^4 | 7.22 | 4.12 | vertex_ai/gemini-3-flash-preview (high) | 0 |
| grok-4-2_sierra_2026-05-05 | banking_knowledge | pass^1 | 18.04 | 17.53 | xai/grok-4.20-0309-reasoning (None) | 1 |
| grok-4-2_sierra_2026-05-05 | banking_knowledge | pass^2 | 12.37 | 11.86 | xai/grok-4.20-0309-reasoning (None) | 1 |
| grok-4-2_sierra_2026-05-05 | banking_knowledge | pass^3 | 10.05 | 9.28 | xai/grok-4.20-0309-reasoning (None) | 1 |
| gemini-3-pro_sierra_2026-03-02 | banking_knowledge | pass^1 | 18.04 | 15.72 | vertex_ai/gemini-3-pro-preview (high) | 0 |
| gemini-3-pro_sierra_2026-03-02 | banking_knowledge | pass^2 | 9.28 | 8.08 | vertex_ai/gemini-3-pro-preview (high) | 0 |
| grok-4-fast_sierra_2026-05-05 | banking_knowledge | pass^1 | 15.72 | 14.18 | xai/grok-4-fast-reasoning (high) | 0 |
| grok-4-fast_sierra_2026-05-05 | banking_knowledge | pass^2 | 8.42 | 7.90 | xai/grok-4-fast-reasoning (high) | 0 |
| gemini-2-5-pro_sierra_2026-05-05 | banking_knowledge | pass^1 | 13.66 | 12.80 | vertex_ai/gemini-2.5-pro (high) | 4 |
| grok-4-1-fast_sierra_2026-05-05 | banking_knowledge | pass^1 | 13.14 | 12.37 | xai/grok-4-1-fast-reasoning (None) | 1 |
