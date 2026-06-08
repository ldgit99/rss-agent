# Uncertainty-Aware Transfer Learning for Cross-Building Energy Forecasting: Toward Robust and Scalable District-Level Energy Management

- Source: arxiv
- ID: http://arxiv.org/abs/2605.29733v1
- DOI: 명시되지 않음
- Published: 2026-05-28T10:28:05Z
- Authors: Shadmehr Zaregarizi, Khashayar Yavari
- Categories: cs.AI
- Link: https://arxiv.org/abs/2605.29733v1
- PDF: https://arxiv.org/pdf/2605.29733v1
- Keyword Score: 11

## Abstract
Scaling data-driven energy forecasting to district level requires models that can be re-used across buildings with minimal target-domain data and honest uncertainty estimates. We present an uncertainty-aware transfer learning (TL) framework for cross-building energy forecasting based on the Temporal Fusion Transformer (TFT), evaluated on a newly released high-resolution real sub-meter dataset: an educational building at Aalborg University, Denmark (source) and the multi-typology NEST building at EMPA, Switzerland (target). We introduce the Transfer Robustness Index (TRI), an architecture-agnostic metric for quantifying generalization quality across domain gaps. A four-strategy layer-freezing ablation shows that Probe-Only fine-tuning, updating only 455 output-layer parameters out of 806K, achieves the best transfer quality (TRI = 3,097), outperforming full fine-tuning and suggesting that TFT encoders learn transferable temporal representations. Monte Carlo Dropout yields a prediction interval coverage probability of 93.2%, close to the nominal 95% target. A data-scarcity analysis further shows monotonic improvement with increasing target-domain data, providing practical guidance for district energy deployment.

## OpenAI Review
---
title: Uncertainty-Aware Transfer Learning for Cross-Building Energy Forecasting: Toward Robust and Scalable District-Level Energy Management
authors: [Shadmehr Zaregarizi, Khashayar Yavari]
year: 2026
journal: Proceedings of 6th ACM International Workshop on Big Data and Machine Learning for Smart Buildings and Cities (BALANCES’26)
doi: https://doi.org/10.1145/nnnnnnn.nnnnnnn
research_type: 실험적 연구
methodology: 전이 학습 프레임워크, 몬테카를로 드롭아웃
data_type: 고해상도 실측 데이터
sample: Aalborg University의 교육 건물 및 EMPA의 NEST 건물
context: 덴마크 및 스위스의 다중 건물 에너지 관리
theoretical_framework: 전이 학습, 불확실성 정량화
keywords: [전이 학습, 건물 에너지 예측, Temporal Fusion Transformer, Transfer Robustness Index, 지역 에너지 관리, 불확실성 정량화, 데이터 부족, 스마트 빌딩]
---

# APA 7th style

# Summary
본 연구는 지역 수준의 에너지 관리를 위한 전이 학습 프레임워크를 제안하며, Temporal Fusion Transformer(TFT)를 기반으로 한다. 연구는 덴마크 Aalborg University와 스위스 EMPA의 NEST 건물에서 수집된 고해상도 실측 데이터를 사용하여 평가되었다. Transfer Robustness Index(TRI)를 도입하여 도메인 간 일반화 품질을 정량화하며, Probe-Only 미세 조정 전략이 가장 우수한 성능을 보였다(TRI = 3,097). 몬테카를로 드롭아웃을 통해 예측 구간의 커버리지 확률이 93.2%로 나타났으며, 데이터 부족 분석을 통해 목표 도메인 데이터가 증가함에 따라 성능이 향상됨을 확인하였다.

# Research Logic
## Problem
지역 수준의 에너지 예측을 위한 모델 재사용의 어려움과 불확실성 추정의 필요성.
## Theory
전이 학습과 불확실성 정량화 이론을 기반으로 한 접근.
## Design
Temporal Fusion Transformer(TFT) 기반의 전이 학습 프레임워크 설계.
## Findings
Probe-Only 미세 조정 전략이 가장 높은 TRI 값을 기록하며, 몬테카를로 드롭아웃을 통한 예측 구간의 신뢰성 확보.
## Conclusion
TFT 기반의 전이 학습 프레임워크가 지역 에너지 관리에 효과적임을 입증.

# Key Findings
- Probe-Only 미세 조정 전략이 TRI = 3,097로 가장 높은 성능을 기록.
- 몬테카를로 드롭아웃을 통한 예측 구간 커버리지 확률이 93.2%.
- 데이터 부족 분석 결과, 목표 도메인 데이터가 증가할수록 성능이 향상됨.

# Contributions
## Theoretical
전이 학습과 불확실성 정량화의 새로운 통합 모델 제안.
## Methodological
Transfer Robustness Index(TRI)라는 새로운 평가 지표 도입.
## Practical
지역 에너지 관리에 대한 실용적인 가이드라인 제공.

# Limitations
- 연구는 단일 목표 사례 연구로 한정됨.
- 고주파 스파이크로 인한 부정적인 R² 값 발생.

# Transferable Insights
- 전이 학습 전략의 효과적인 적용 가능성.
- 데이터 부족 상황에서의 성능 향상 가능성.

# Idea Seeds
1. 다양한 건물 유형에 대한 전이 학습 전략 확장.
2. 불확실성 정량화를 위한 새로운 메트릭 개발.
3. 다중 목표 예측을 위한 모델 확장.

# Citation Snippets
> Zaregarizi, S., & Yavari, K. (2026). Uncertainty-Aware Transfer Learning for Cross-Building Energy Forecasting: Toward Robust and Scalable District-Level Energy Management. In Proceedings of 6th ACM International Workshop on Big Data and Machine Learning for Smart Buildings and Cities (BALANCES’26). https://doi.org/10.1145/nnnnnnn.nnnnnnn

tags: #전이학습, #건물에너지예측, #TemporalFusionTransformer, #TransferRobustnessIndex, #지역에너지관리, #불확실성정량화, #스마트빌딩

---

요약: 본 연구는 지역 수준의 에너지 관리를 위한 전이 학습 프레임워크를 제안하며, Temporal Fusion Transformer(TFT)를 기반으로 하여 덴마크와 스위스의 데이터를 분석하였다. Probe-Only 미세 조정 전략이 가장 높은 성능을 보였으며, 몬테카를로 드롭아웃을 통한 예측 구간의 신뢰성도 확보되었다. 데이터 부족 분석을 통해 목표 도메인 데이터의 중요성을 강조하였다.
