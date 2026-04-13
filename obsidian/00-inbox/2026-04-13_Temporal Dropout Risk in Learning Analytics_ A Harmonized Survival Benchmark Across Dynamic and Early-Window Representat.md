# Temporal Dropout Risk in Learning Analytics: A Harmonized Survival Benchmark Across Dynamic and Early-Window Representations

- Source: arxiv
- ID: http://arxiv.org/abs/2604.08870v1
- DOI: 명시되지 않음
- Published: 2026-04-10T02:10:12Z
- Authors: Rafael da Silva, Jeff Eicher, Gregory Longo
- Categories: cs.LG, cs.AI
- Link: https://arxiv.org/abs/2604.08870v1
- PDF: https://arxiv.org/pdf/2604.08870v1
- Keyword Score: 19

## Abstract
Student dropout is a persistent concern in Learning Analytics, yet comparative studies frequently evaluate predictive models under heterogeneous protocols, prioritizing discrimination over temporal interpretability and calibration. This study introduces a survival-oriented benchmark for temporal dropout risk modelling using the Open University Learning Analytics Dataset (OULAD). Two harmonized arms are compared: a dynamic weekly arm, with models in person-period representation, and a comparable continuous-time arm, with an expanded roster of families -- tree-based survival, parametric, and neural models. The evaluation protocol integrates four analytical layers: predictive performance, ablation, explainability, and calibration. Results are reported within each arm separately, as a single cross-arm ranking is not methodologically warranted. Within the comparable arm, Random Survival Forest leads in discrimination and horizon-specific Brier scores; within the dynamic arm, Poisson Piecewise-Exponential leads narrowly on integrated Brier score within a tight five-family cluster. No-refit bootstrap sampling variability qualifies these positions as directional signals rather than absolute superiority. Ablation and explainability analyses converged, across all families, on a shared finding: the dominant predictive signal was not primarily demographic or structural, but temporal and behavioral. Calibration corroborated this pattern in the better-discriminating models, with the exception of XGBoost AFT, which exhibited systematic bias. These results support the value of a harmonized, multi-dimensional benchmark in Learning Analytics and situate dropout risk as a temporal-behavioral process rather than a function of static background attributes.

## OpenAI Review
---
title: Temporal Dropout Risk in Learning Analytics: A Harmonized Survival Benchmark Across Dynamic and Early-Window Representations
authors: [Rafael da Silva, Jeff Eicher, Gregory Longo]
year: 2026
journal: 명시되지 않음
doi: https://arxiv.org/abs/2604.08870v1
research_type: 실증 연구
methodology: 서바이벌 분석
data_type: OULAD 데이터셋
sample: 32,593명의 등록
context: 학습 분석 및 교육 데이터 마이닝
theoretical_framework: 명시되지 않음
keywords: [Learning Analytics, dropout prediction, temporal risk modelling, survival analysis, time-to-event modelling, model benchmarking, explainability, calibration, early warning, OULAD]
---

# APA 7th style

# Summary
학생의 중퇴는 학습 분석에서 지속적인 문제로 여겨지며, 본 연구는 Open University Learning Analytics Dataset(OULAD)를 활용하여 시간적 중퇴 위험 모델링을 위한 서바이벌 지표를 제시한다. 연구는 동적 주간 모델과 비교 가능한 연속 시간 모델을 비교하며, 예측 성능, 제거 분석, 설명 가능성 및 보정의 네 가지 분석 레이어를 통합한다. 결과는 각 모델 군 내에서 별도로 보고되며, 주요 발견은 중퇴 위험의 주요 신호가 인구 통계적 또는 구조적 요인이 아닌 시간적 및 행동적 요인이라는 것이다. 이러한 결과는 학습 분석에서 중퇴 위험을 정적 배경 속성이 아닌 시간적-행동적 과정으로 자리매김하는 데 기여한다.

# Research Logic
## Problem
학생 중퇴는 고등 교육에서 지속적인 도전 과제로, 시간적 위험 패턴을 식별하는 데 어려움이 있다.
## Theory
중퇴 위험은 정적 조건이 아니라 시간에 따라 변화하는 과정으로 이해되어야 한다.
## Design
OULAD 데이터셋을 기반으로 한 서바이벌 분석을 통해 동적 및 연속 시간 모델을 비교하였다.
## Findings
Random Survival Forest가 비교 가능한 모델 군에서 우수한 성능을 보였으며, 시간적 및 행동적 신호가 주요 예측 요인으로 나타났다.
## Conclusion
중퇴 위험은 정적 속성이 아닌 시간적-행동적 과정으로 이해되어야 하며, 이를 위한 통합된 벤치마크의 필요성이 강조된다.

# Key Findings
- Random Survival Forest가 비교 가능한 모델 군에서 우수한 성능을 보였다.
- 시간적 및 행동적 신호가 중퇴 위험 예측에서 주요한 역할을 한다.
- 보정 분석에서 XGBoost AFT 모델이 체계적 편향을 보였다.

# Contributions
## Theoretical
중퇴 위험을 시간적-행동적 과정으로 재정의함.
## Methodological
서바이벌 분석을 위한 통합된 벤치마크를 제시함.
## Practical
학생 지원 및 개입 결정을 위한 예측 모델의 보정 필요성을 강조함.

# Limitations
- 연구는 특정 데이터셋에 국한되어 있어 일반화에 한계가 있다.
- 모델 비교가 단일한 평가 기준에 의존하고 있어 다각적인 해석이 필요하다.

# Transferable Insights
- 시간적 및 행동적 신호는 학생 중퇴 위험 예측에서 더 유용한 정보를 제공한다.
- 예측 모델의 보정 및 해석 가능성이 교육적 결정에 필수적이다.

# Idea Seeds
1. 다양한 교육 환경에서의 중퇴 위험 예측 모델 비교 연구.
2. 시간적 신호를 활용한 개입 전략 개발.
3. 학습 분석을 통한 학생 지원 시스템 개선 방안 연구.

# Citation Snippets
> da Silva, R., Eicher, J., & Longo, G. (2026). Temporal Dropout Risk in Learning Analytics: A Harmonized Survival Benchmark Across Dynamic and Early-Window Representations. 

tags: #학습분석, #중퇴예측, #서바이벌분석, #시간적위험모델링, #모델벤치마킹, #설명가능성, #보정

---

학생 중퇴는 학습 분석에서 중요한 문제로, 본 연구는 OULAD 데이터셋을 활용하여 시간적 중퇴 위험 모델링을 위한 서바이벌 벤치마크를 제시한다. 연구 결과, 중퇴 위험의 주요 신호는 시간적 및 행동적 요인으로 나타났으며, 이는 중퇴 위험을 정적 속성이 아닌 시간적-행동적 과정으로 이해해야 함을 시사한다.
