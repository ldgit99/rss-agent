# EvoMD-LLM: Learning the Language of Species Evolution in Reactive Molecular Dynamics

- Source: arxiv
- ID: http://arxiv.org/abs/2605.29394v1
- DOI: 명시되지 않음
- Published: 2026-05-28T05:44:40Z
- Authors: Zhichen Tang, Zhengzheng Dang, Yulin Chen, Jixin Wu, Haiwen Li, Yanming Wang
- Categories: cs.AI
- Link: https://arxiv.org/abs/2605.29394v1
- PDF: https://arxiv.org/pdf/2605.29394v1
- Keyword Score: 11

## Abstract
While large language models (LLMs) excel at static scientific reasoning, they struggle to model the temporal structure of dynamic physical processes. We present EvoMD-LLM (Evolutionary Molecular Dynamics Large Language Model), a framework that reformulates species-level molecular dynamics as a symbolic temporal language modeling problem. Reactive MD trajectories are discretized into sequences of molecular events, where each token represents a chemical species augmented with its persistence duration, enabling standard autoregressive LLMs to learn compositional evolution over time through efficient fine-tuning. A key component of EvoMD-LLM is temporal scaffolding, which treats event duration as an explicit linguistic token and serves as a structured inductive bias, significantly reducing invalid or hallucinated molecular outputs compared to conventional sequence modeling approaches. We evaluate EvoMD-LLM on multiple temporal prediction tasks, achieving up to 66.14% accuracy and consistently outperforming sequential neural networks and language-based baselines. Beyond quantitative improvements, we qualitatively observe that the model is capable of generating interpretations for its own predictions by incorporating relevant chemical knowledge, even though it was not explicitly supervised with paired trajectory-explanation data. These results demonstrate that symbolic temporal language modeling provides an effective framework for grounding LLMs in dynamic physical simulations.

## OpenAI Review
---
title: EvoMD-LLM: Learning the Language of Species Evolution in Reactive Molecular Dynamics
authors: [Zhichen Tang, Zhengzheng Dang, Yulin Chen, Jixin Wu, Haiwen Li, Yanming Wang]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2605.29394v1
research_type: 이론적 연구
methodology: 실험적 연구
data_type: 분자 동역학 데이터
sample: 명시되지 않음
context: 분자 동역학 시뮬레이션
theoretical_framework: 상징적 시간 언어 모델링
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 EvoMD-LLM(Evolutionary Molecular Dynamics Large Language Model)이라는 프레임워크를 제안하여, 분자 동역학을 상징적 시간 언어 모델링 문제로 재구성한다. 이 모델은 분자 사건의 시퀀스를 생성하고, 각 토큰은 화학 종과 그 지속 시간을 나타내며, 이를 통해 LLM이 시간에 따른 조합적 진화를 학습할 수 있도록 한다. EvoMD-LLM은 시간적 스캐폴딩을 통해 이벤트 지속 시간을 명시적 언어 토큰으로 처리하며, 이는 전통적인 시퀀스 모델링 접근법에 비해 무효 또는 환각된 분자 출력을 크게 줄인다. 여러 시간 예측 작업에서 최대 66.14%의 정확도를 달성하며, 순차 신경망 및 언어 기반 기준을 지속적으로 초과하는 성능을 보인다. 이 연구는 상징적 시간 언어 모델링이 동적 물리 시뮬레이션에서 LLM을 기반으로 하는 효과적인 프레임워크임을 입증한다.

# Research Logic
## Problem
대규모 언어 모델(LLMs)은 정적 과학적 추론에서는 뛰어나지만, 동적 물리 과정의 시간 구조를 모델링하는 데 어려움을 겪는다.

## Theory
EvoMD-LLM은 분자 동역학을 상징적 사건 시퀀스로 재구성하여 LLM이 시간적 진화를 모델링할 수 있도록 한다.

## Design
모델은 분자 사건을 지속 시간과 함께 토큰화하여, 시간적 스캐폴딩을 통해 물리적 일관성을 유지한다.

## Findings
EvoMD-LLM은 여러 시간 예측 작업에서 최대 66.14%의 정확도를 달성하며, 기존의 신경망 및 언어 기반 모델보다 우수한 성능을 보인다.

## Conclusion
상징적 시간 언어 모델링은 LLM이 동적 물리 시뮬레이션에 효과적으로 적용될 수 있는 프레임워크임을 입증하였다.

# Key Findings
- EvoMD-LLM은 최대 66.14%의 정확도를 달성하였다.
- 시간적 스캐폴딩이 무효 또는 환각된 분자 출력을 크게 줄였다.
- 모델은 화학 지식을 통합하여 자신의 예측에 대한 해석을 생성할 수 있다.

# Contributions
## Theoretical
상징적 시간 언어 모델링의 새로운 접근법을 제안하였다.

## Methodological
EvoMD-LLM의 구조적 설계와 시간적 스캐폴딩 기법을 통해 예측 정확도를 높였다.

## Practical
동적 물리 시뮬레이션에서 LLM의 적용 가능성을 확장하였다.

# Limitations
- 샘플 크기 및 데이터의 다양성이 명시되지 않았다.
- 특정 화학 반응에 대한 일반화 가능성에 대한 추가 연구가 필요하다.

# Transferable Insights
- 상징적 시간 언어 모델링은 다른 동적 시스템에도 적용 가능할 수 있다.
- 시간적 스캐폴딩 기법은 다양한 AI 모델에 통합될 수 있다.

# Idea Seeds
1. EvoMD-LLM의 구조를 다른 과학적 시뮬레이션에 적용하기.
2. 시간적 스캐폴딩을 활용한 교육적 AI 도구 개발.
3. 다양한 화학 반응에 대한 예측 정확도 향상 연구.

# Citation Snippets
> Tang, Z., Dang, Z., Chen, Y., Wu, J., Li, H., & Wang, Y. (2026). EvoMD-LLM: Learning the Language of Species Evolution in Reactive Molecular Dynamics. arXiv. https://arxiv.org/abs/2605.29394v1

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy

---

### 압축 요약
EvoMD-LLM은 분자 동역학을 상징적 시간 언어 모델링 문제로 재구성하여, LLM이 시간에 따른 조합적 진화를 학습할 수 있도록 하는 프레임워크이다. 이 모델은 최대 66.14%의 정확도를 달성하며, 시간적 스캐폴딩을 통해 무효 또는 환각된 분자 출력을 줄인다. 연구 결과는 LLM이 동적 물리 시뮬레이션에 효과적으로 적용될 수 있음을 보여준다.
