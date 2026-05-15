# Cognitive-Uncertainty Guided Knowledge Distillation for Accurate Classification of Student Misconceptions

- Source: arxiv
- ID: http://arxiv.org/abs/2605.14752v1
- DOI: 명시되지 않음
- Published: 2026-05-14T12:17:38Z
- Authors: Qirui Liu, Hao Chen, Weijie Shi, Jiajie Xu, Jia Zhu
- Categories: cs.LG, cs.AI
- Link: https://arxiv.org/abs/2605.14752v1
- PDF: https://arxiv.org/pdf/2605.14752v1
- Keyword Score: 13

## Abstract
Accurately identifying student misconceptions is crucial for personalized education but faces three challenges: (1) data scarcity with long-tail distribution, where authentic student reasoning is difficult to synthesize; (2) fuzzy boundaries between error categories with high annotation noise; (3) deployment parado-large models overlook unconventional approaches due to pretraining bias and cannot be deployed on edge, while small models overfit to noise. Unlike traditional methods that increase diversity through large-scale data synthesis, we propose a two-stage knowledge distillation framework that mines high-value samples from existing data. The first stage performs standard distillation to transfer task capabilities. The second stage introduces a dual-layer marginal selection mechanism based on cognitive uncertainty, identifying four types of critical samples based on teacher model uncertainty and confidence differences. For different data subsets, we design difficulty-adaptive mechanism to balance hard/soft label contributions, enabling student models to inherit inter-class relationships from teacher soft labels while distinguishing ambiguous error types. Experiments show that with augmented training on only 10.30% of filtered samples, we achieve MAP@3 of 0.9585 (+17.8%) on the MAP-Charting dataset, and using only a 4B parameter model, we attain 84.38% accuracy on cross-topic tests of middle school algebra misconception benchmarks, significantly outperforming sota LLM (67.73%) and standard fine-tuned 72B models (81.25%). Our code is available at https://github.com/RoschildRui/acl2026_map.

## OpenAI Review
---
title: Cognitive-Uncertainty Guided Knowledge Distillation for Accurate Classification of Student Misconceptions
authors: [Qirui Liu, Hao Chen, Weijie Shi, Jiajie Xu, Jia Zhu]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2605.14752v1
research_type: 실험적 연구
methodology: 두 단계 지식 증류 프레임워크
data_type: 학생 오해 데이터
sample: 10.30% 필터링된 샘플
context: 수학 교육에서 학생의 오해 분류
theoretical_framework: 인지 불확실성 이론
keywords: [학생 오해, 지식 증류, 인지 불확실성, 교육 기술, 머신러닝, 데이터 부족, 교육 평가]
---

# APA 7th style

# Summary
학생의 오해를 정확하게 식별하는 것은 개인화된 교육에 필수적이나, 데이터 부족, 오류 범주 간의 모호한 경계, 모델 배치의 패러독스와 같은 세 가지 주요 도전에 직면해 있다. 본 연구는 기존 데이터에서 고가치 샘플을 발굴하는 두 단계 지식 증류 프레임워크를 제안한다. 첫 번째 단계에서는 표준 증류를 통해 작업 능력을 전이하고, 두 번째 단계에서는 인지 불확실성을 기반으로 한 이중 레이어 마진 선택 메커니즘을 도입하여 교사 모델의 불확실성과 신뢰도 차이에 따라 네 가지 유형의 중요 샘플을 식별한다. 실험 결과, 필터링된 샘플의 10.30%로 훈련하여 MAP-Charting 데이터셋에서 MAP@3 0.9585를 달성하였으며, 4B 파라미터 모델을 사용하여 중학교 대수 오해 기준에서 84.38%의 정확도를 기록하였다.

# Research Logic
## Problem
학생의 오해를 정확하게 분류하는 데 있어 데이터 부족과 오류 범주 간의 모호한 경계, 모델 배치의 패러독스가 존재한다.
## Theory
인지 불확실성 이론을 기반으로 하여 학생의 오해를 효과적으로 식별할 수 있는 방법론을 제시한다.
## Design
두 단계 지식 증류 프레임워크를 설계하여 고가치 샘플을 선택하고, 인지 불확실성을 활용하여 학습을 최적화한다.
## Findings
10.30%의 필터링된 샘플로 훈련하여 MAP@3 0.9585를 달성하고, 4B 모델로 84.38%의 정확도를 기록하였다.
## Conclusion
제안된 방법론은 데이터 부족 문제를 해결하고, 학생의 다양한 사고 방식을 효과적으로 반영할 수 있는 가능성을 보여준다.

# Key Findings
- 두 단계 지식 증류 프레임워크가 효과적으로 학생 오해를 분류할 수 있음을 입증하였다.
- 인지 불확실성을 활용한 샘플 선택 메커니즘이 성능 향상에 기여하였다.
- 필터링된 샘플의 10.30%로도 높은 정확도를 달성하였다.

# Contributions
## Theoretical
인지 불확실성 이론을 기반으로 한 새로운 접근 방식을 제시하였다.
## Methodological
두 단계 지식 증류 프레임워크를 통해 데이터 부족 문제를 해결하는 방법론을 개발하였다.
## Practical
학생의 오해를 효과적으로 분류할 수 있는 실용적인 도구를 제공하였다.

# Limitations
- 데이터의 양이 제한적이며, 특정 오류 유형에 대한 분류 정확도가 낮을 수 있다.
- 모델의 일반화 능력이 특정 상황에 따라 제한될 수 있다.

# Transferable Insights
- 인지 불확실성을 활용한 샘플 선택이 다양한 교육적 맥락에서 적용 가능하다.
- 데이터 부족 문제를 해결하기 위한 새로운 방법론이 필요하다.

# Idea Seeds
1. 인지 불확실성을 활용한 다른 교육 분야에서의 적용 가능성 탐색.
2. 다양한 학생 집단에 대한 맞춤형 모델 개발.
3. 실시간 피드백 시스템과의 통합 가능성 연구.

# Citation Snippets
> Liu, Q., Chen, H., Shi, W., Xu, J., & Zhu, J. (2026). Cognitive-Uncertainty Guided Knowledge Distillation for Accurate Classification of Student Misconceptions. arXiv. https://arxiv.org/abs/2605.14752v1

tags: #학생오해, #지식증류, #인지불확실성, #교육기술, #머신러닝, #데이터부족, #교육평가
