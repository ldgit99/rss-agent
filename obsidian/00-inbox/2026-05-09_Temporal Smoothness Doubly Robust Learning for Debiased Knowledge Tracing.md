# Temporal Smoothness Doubly Robust Learning for Debiased Knowledge Tracing

- Source: arxiv
- ID: http://arxiv.org/abs/2605.05958v1
- DOI: 명시되지 않음
- Published: 2026-05-07T10:05:53Z
- Authors: Peilin Zhan, Wei Chen, Weilin Chen, Shuyi Pan, Ruichu Cai
- Categories: cs.AI
- Link: https://arxiv.org/abs/2605.05958v1
- PDF: https://arxiv.org/pdf/2605.05958v1
- Keyword Score: 13

## Abstract
Knowledge Tracing (KT) is fundamental to intelligent education systems, yet relies on educational logs that are selectively observed. The non-random nature of exercise recommendations and student choices inevitably induces severe selection bias. Most existing KT methods neglect this issue, training on observed logs using standard empirical risk, which yields biased mastery estimates and accumulates errors in subsequent recommendations. To address this, we introduce a doubly robust (DR) formulation for KT that integrates a propensity model with an error imputation model, theoretically guaranteeing unbiasedness if either model is accurate. Beyond unbiasedness, in the sequential setting of KT, we identify that the estimator's performance is compromised by variance-dependent stochastic deviations that accumulate over time, thereby causing training instability and limiting performance. To mitigate this, we derive a generalization bound that explicitly characterizes the impact of estimator variance and identifies temporal smoothness as a key factor in controlling it. Building on these theoretical insights, we propose the Temporal Smoothness Doubly Robust (TSDR) framework. TSDR jointly optimizes the KT predictor and the imputation model with a smoothness regularizer, effectively reducing variance while preserving the unbiasedness guarantee of DR. Experiments on multiple real-world benchmarks demonstrate that TSDR consistently enhances various state-of-the-art KT backbones, underscoring the vital role of principled bias correction in KT.

## OpenAI Review
(OpenAI review failed: 429 Client Error: Too Many Requests for url: https://api.openai.com/v1/chat/completions)
