# Caliper: Probing Lexical Anchors versus Causal Structure in LLMs

- Source: arxiv
- ID: http://arxiv.org/abs/2606.04915v1
- DOI: 명시되지 않음
- Published: 2026-06-03T14:11:16Z
- Authors: Zhenyu Yu, Shuigeng Zhou
- Categories: cs.CL, cs.IR
- Link: https://arxiv.org/abs/2606.04915v1
- PDF: https://arxiv.org/pdf/2606.04915v1
- Keyword Score: 10

## Abstract
Large language models reach 50 to 70% accuracy on causal reasoning benchmarks such as CLadder, but it is unclear whether this reflects structural reasoning or lexical pattern matching. We introduce Caliper, a controlled perturbation that replaces semantic variable names with placeholder tokens while preserving the causal graph and probabilistic specification of each question. Across nine instruction-tuned LLMs from 3.8B to 671B and three causal reasoning benchmarks, lexical anonymization yields robust accuracy drops of +7.6, +27.0, and +11.1 pp on a local 3.8B-14B set, rising to +29.6 and +18.0 pp on CRASS and e-CARE across nine frontier models spanning the 2024-2026 generations. Of 40 engaged model-by-benchmark cells, 39 show a positive gap, and the gap collapses by 17x on CLadder's pseudoword subset. Structured scaffolding and few-shot in-context learning each narrow the gap, but mainly by lowering P0 accuracy on smaller models rather than recovering P1. Current instruction-tuned LLMs, evaluated zero-shot, show little evidence of structural causal reasoning once lexical anchors are removed.

## OpenAI Review
---
title: Caliper: Probing Lexical Anchors versus Causal Structure in LLMs
authors: [Zhenyu Yu, Shuigeng Zhou]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2606.04915v1
research_type: 실험적 연구
methodology: 제어된 교란 실험
data_type: LLMs 성능 데이터
sample: 14개의 instruction-tuned LLMs
context: 인과 추론 벤치마크 CLadder, CRASS, e-CARE
theoretical_framework: 구조적 인과 모델
keywords: [인과 추론, LLM, 교란 실험, 구조적 인과 모델, 성능 평가]
---

# APA 7th style

# Summary
본 연구는 대형 언어 모델(LLM)이 인과 추론 벤치마크에서 50%에서 70%의 정확도를 달성하는 이유가 구조적 추론인지 아니면 어휘적 패턴 매칭인지에 대한 논란을 다룬다. 연구팀은 Caliper라는 제어된 교란을 도입하여 의미 변수 이름을 자리 표시자 토큰으로 교체하면서 인과 그래프와 각 질문의 확률적 사양을 유지한다. 3.8B에서 671B까지의 아홉 개의 instruction-tuned LLM을 대상으로 한 실험 결과, 어휘적 익명화가 정확도를 7.6, 27.0, 11.1 pp 감소시키며, CRASS와 e-CARE에서는 각각 29.6 및 18.0 pp의 감소를 보였다. 구조적 스캐폴딩과 몇 샷 학습이 정확도 차이를 줄이는 데 기여했지만, 이는 주로 작은 모델의 P0 정확도를 낮추는 방식으로 나타났다.

# Research Logic
## Problem
대형 언어 모델의 인과 추론 능력이 구조적 추론인지 어휘적 패턴 매칭인지 명확하지 않음.
## Theory
구조적 인과 모델(SCM)을 기반으로 한 인과 추론의 정확도를 평가.
## Design
Caliper라는 제어된 교란을 통해 어휘적 요소를 제거하고 인과 구조를 유지하는 실험 설계.
## Findings
대부분의 모델에서 어휘적 익명화가 인과 추론 정확도를 감소시킴.
## Conclusion
현재의 instruction-tuned LLM은 어휘적 앵커가 제거되면 구조적 인과 추론의 증거가 부족함.

# Key Findings
- 어휘적 익명화가 LLM의 인과 추론 정확도를 7.6에서 29.6 pp까지 감소시킴.
- 구조적 스캐폴딩과 몇 샷 학습이 정확도 차이를 줄이지만, 주로 작은 모델에서 나타남.
- 40개의 모델-벤치마크 셀 중 39개에서 긍정적인 정확도 차이를 보임.

# Contributions
## Theoretical
구조적 인과 모델을 통한 인과 추론의 이해를 심화.
## Methodological
Caliper 교란을 통한 새로운 평가 방법론 제시.
## Practical
LLM의 인과 추론 능력에 대한 실질적인 통찰 제공.

# Limitations
- 실험에 사용된 모델의 범위가 제한적임.
- 어휘적 익명화의 효과가 모든 유형의 질문에 동일하게 적용되지 않을 수 있음.

# Transferable Insights
- LLM의 인과 추론 능력 평가에 있어 어휘적 요소의 중요성 강조.
- 교육 및 AI 시스템 설계에서 LLM의 한계를 이해하는 데 기여.

# Idea Seeds
1. Caliper 방법론을 다른 유형의 AI 모델에 적용하여 인과 추론 능력 평가.
2. LLM의 어휘적 패턴 매칭과 구조적 추론 간의 관계를 심층적으로 분석.
3. 교육적 맥락에서 LLM의 인과 추론 능력을 향상시키기 위한 스캐폴딩 전략 개발.

# Citation Snippets
> Yu, Z., & Zhou, S. (2026). Caliper: Probing Lexical Anchors versus Causal Structure in LLMs. arXiv. https://arxiv.org/abs/2606.04915v1

tags: #인과추론, #LLM, #교란실험, #구조적인과모델, #성능평가, #AI교육, #AI스캐폴딩

---

요약: 본 연구는 대형 언어 모델의 인과 추론 능력이 구조적 추론인지 어휘적 패턴 매칭인지에 대한 논란을 다루며, Caliper라는 제어된 교란을 통해 인과 추론의 정확도를 평가하였다. 연구 결과, 어휘적 익명화가 정확도를 유의미하게 감소시키며, 구조적 스캐폴딩과 몇 샷 학습이 일부 정확도 차이를 줄이는 데 기여함을 발견하였다.
