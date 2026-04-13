# A Mathematical Framework for Temporal Modeling and Counterfactual Policy Simulation of Student Dropout

- Source: arxiv
- ID: http://arxiv.org/abs/2604.08874v1
- DOI: 명시되지 않음
- Published: 2026-04-10T02:26:23Z
- Authors: Rafael da Silva, Jeff Eicher, Gregory Longo
- Categories: cs.LG, cs.AI
- Link: https://arxiv.org/abs/2604.08874v1
- PDF: https://arxiv.org/pdf/2604.08874v1
- Keyword Score: 11

## Abstract
This study proposes a temporal modeling framework with a counterfactual policy-simulation layer for student dropout in higher education, using LMS engagement data and administrative withdrawal records. Dropout is operationalized as a time-to-event outcome at the enrollment level; weekly risk is modeled in discrete time via penalized, class-balanced logistic regression over person--period rows. Under a late-event temporal holdout, the model attains row-level AUCs of 0.8350 (train) and 0.8405 (test), with aggregate calibration acceptable but sparsely supported in the highest-risk bins. Ablation analyses indicate performance is sensitive to feature set composition, underscoring the role of temporal engagement signals. A scenario-indexed policy layer produces survival contrasts $ΔS(T)$ under an explicit trigger/schedule contract: positive contrasts are confined to the shock branch ($T_{\rm policy}=18$: 0.0102, 0.0260, 0.0819), while the mechanism-aware branch is negative ($ΔS_{\rm mech}(18)=-0.0078$, $ΔS_{\rm mech}(38)=-0.0134$). A subgroup analysis by gender quantifies scenario-induced survival gaps via bootstrap; contrasts are directionally stable but small. Results are not causally identified; they demonstrate the framework's capacity for internal structural scenario comparison under observational data constraints.

## OpenAI Review
---
title: A Mathematical Framework for Temporal Modeling and Counterfactual Policy Simulation of Student Dropout
authors: [Rafael da Silva, Jeff Eicher, Gregory Longo]
year: 2026
journal: arXiv
doi: https://doi.org/10.48550/arXiv.2604.08874
research_type: 이론적 연구
methodology: 패널 데이터 분석, 로지스틱 회귀
data_type: LMS 참여 데이터, 행정적 철회 기록
sample: 고등 교육 기관의 학생
context: 고등 교육에서의 학생 이탈
theoretical_framework: 시간적 모델링, 정책 시뮬레이션
keywords: [학생 이탈, 학습 분석, 생존 분석, 시간적 모델링, 정책 시뮬레이션]
---

# APA 7th style

# Summary
본 연구는 고등 교육에서 학생 이탈을 분석하기 위한 시간적 모델링 프레임워크와 반사실적 정책 시뮬레이션 레이어를 제안한다. LMS 참여 데이터와 행정적 철회 기록을 사용하여 이탈을 시간-사건 결과로 운영화하고, 주간 위험을 패널 데이터의 로지스틱 회귀를 통해 모델링하였다. 모델은 훈련 데이터에서 0.8350, 테스트 데이터에서 0.8405의 AUC를 달성하였으며, 정책 시뮬레이션을 통해 다양한 시나리오에 따른 생존 차이를 분석하였다. 성별에 따른 하위 그룹 분석을 통해 시나리오에 따른 생존 격차를 정량화하였으나, 결과는 인과적 식별이 이루어지지 않았다.

# Research Logic
## Problem
고등 교육에서 학생 이탈 문제는 개인, 가족, 기관 및 사회에 상당한 비용을 초래한다. 기존 연구는 정적 위험 추정에 초점을 맞추어 이탈 시점을 명확히 하지 못하였다.

## Theory
이 연구는 시간적 위험 모델링과 정책 시뮬레이션을 통해 이탈 예측의 한계를 극복하고자 하였다.

## Design
패널 데이터 분석을 통해 주간 위험을 로지스틱 회귀로 모델링하고, 반사실적 시뮬레이션을 통해 정책 효과를 비교하였다.

## Findings
모델은 주간 위험을 효과적으로 예측하였으며, 성별에 따른 생존 격차를 분석하였다. 그러나 인과적 효과는 식별되지 않았다.

## Conclusion
제안된 프레임워크는 관찰 데이터의 제약 속에서도 내부 구조적 시나리오 비교를 지원할 수 있음을 보여준다.

# Key Findings
- 모델은 훈련 데이터에서 AUC 0.8350, 테스트 데이터에서 AUC 0.8405를 달성하였다.
- 정책 시뮬레이션을 통해 생존 차이를 분석하였으며, 성별에 따른 격차를 정량화하였다.
- 결과는 인과적 식별이 이루어지지 않았으며, 시나리오 비교의 가능성을 보여주었다.

# Contributions
## Theoretical
시간적 모델링과 정책 시뮬레이션의 통합을 통해 학생 이탈 연구의 새로운 방향을 제시하였다.

## Methodological
패널 데이터 분석과 로지스틱 회귀를 활용한 새로운 분석 방법론을 개발하였다.

## Practical
고등 교육 기관에서의 이탈 예측 및 개입 정책 수립에 기여할 수 있는 실용적인 프레임워크를 제공하였다.

# Limitations
- 인과적 효과를 식별할 수 있는 데이터가 부족하다.
- 특정 시나리오에 대한 결과가 제한적이다.

# Transferable Insights
- 시간적 모델링은 다양한 교육 환경에서 학생 이탈 예측에 적용 가능하다.
- 정책 시뮬레이션은 교육 개입의 효과를 평가하는 데 유용할 수 있다.

# Idea Seeds
1. 다른 교육 환경에서의 시간적 모델링 적용 연구.
2. 다양한 인구 집단에 대한 정책 시뮬레이션의 효과 분석.
3. LMS 데이터의 활용을 통한 학생 참여 증진 방안 연구.

# Citation Snippets
> da Silva, R., Eicher, J., & Longo, G. (2026). A Mathematical Framework for Temporal Modeling and Counterfactual Policy Simulation of Student Dropout. arXiv. https://doi.org/10.48550/arXiv.2604.08874

tags: #학생이탈, #학습분석, #생존분석, #시간적모델링, #정책시뮬레이션

---

요약: 본 연구는 고등 교육에서 학생 이탈을 분석하기 위한 시간적 모델링 프레임워크를 제안하며, LMS 데이터를 활용하여 주간 위험을 모델링하고 정책 시뮬레이션을 통해 생존 차이를 분석하였다. 결과는 인과적 식별이 이루어지지 않았으나, 제안된 프레임워크는 내부 구조적 시나리오 비교를 지원할 수 있음을 보여준다.
