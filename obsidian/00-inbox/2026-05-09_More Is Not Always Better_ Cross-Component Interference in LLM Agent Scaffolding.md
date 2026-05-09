# More Is Not Always Better: Cross-Component Interference in LLM Agent Scaffolding

- Source: arxiv
- ID: http://arxiv.org/abs/2605.05716v1
- DOI: 명시되지 않음
- Published: 2026-05-07T06:01:43Z
- Authors: Ming Liu
- Categories: cs.AI, cs.CL
- Link: https://arxiv.org/abs/2605.05716v1
- PDF: https://arxiv.org/pdf/2605.05716v1
- Keyword Score: 12

## Abstract
LLM agent systems are built by stacking scaffolding components (planning, tools, memory, self-reflection, retrieval) assuming more is better. We study cross-component interference (CCI): degradation when components interact destructively. We run a full factorial experiment over all 2^5=32 subsets of five components on HotpotQA and GSM8K with Llama-3.1-8B/70B (96 conditions, up to 10 seeds). The All-In system is consistently suboptimal: on HotpotQA, a single-tool agent surpasses All-In by 32% (F1 0.233 vs 0.177, p=0.023); on GSM8K, a 3-component subset beats All-In by 79% (0.43 vs 0.24, p=0.010). Optimal component count is task-dependent (k*=1-4) and scale-sensitive: at 70B, combinations that hurt at 8B provide gains, though All-In still trails the best subset. We fit a main-effects regression (R^2=0.916, adj-R^2=0.899, LOOCV=0.872), compute exact Shapley values, and find 183/325 submodularity violations (56.3%), showing greedy selection is unreliable. A three-body synergy among Tool Use, Self-Reflection, and Retrieval (INT_3=+0.175, 95% CI [+0.003,+0.351]) is reported as exploratory. CCI replicates across model families (Qwen2.5) and is robust to prompt paraphrasing. Our findings suggest maximally-equipped agent defaults should be replaced by task-specific subset selection via interaction-aware analysis.

## OpenAI Review
(OpenAI review failed: 429 Client Error: Too Many Requests for url: https://api.openai.com/v1/chat/completions)
