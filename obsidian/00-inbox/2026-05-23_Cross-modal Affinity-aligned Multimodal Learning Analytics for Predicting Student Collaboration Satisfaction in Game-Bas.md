# Cross-modal Affinity-aligned Multimodal Learning Analytics for Predicting Student Collaboration Satisfaction in Game-Based Learning

- Source: arxiv
- ID: http://arxiv.org/abs/2605.16806v1
- DOI: 명시되지 않음
- Published: 2026-05-16T04:22:47Z
- Authors: Wen-Hsin Tsai, Chia-Ming Lee, Yuk-Ying Tung
- Categories: cs.LG, cs.AI, cs.CV
- Link: https://arxiv.org/abs/2605.16806v1
- PDF: https://arxiv.org/pdf/2605.16806v1
- Keyword Score: 25

## Abstract
Collaborative game-based learning environments offer rich opportunities for small-group knowledge construction, yet automatically predicting student collaboration satisfaction remains challenging. A critical barrier is modality degradation: in educational deployments, individual modalities such as eye gaze exhibit inconsistent informativeness across student cohorts, causing implicit attention-based fusion to produce brittle multimodal representations. We propose the Affinity-Aligned Multimodal Learning Analytics (AAMLA) framework, whose core contribution is the Cross-modal Affinity-guided Modality Alignment (CAMA) module, which explicitly models inter-modal relationships via affinity matrices and enforces cross-modal consistency through contrastive learning, enabling adaptive suppression of uninformative modalities without discarding them. AAMLA further applies modality-specific projection layers to map heterogeneous features, including facial action units, head pose, eye gaze, and interaction trace logs, into a unified semantic space prior to alignment. Experiments on 50 middle school students in the EcoJourneys collaborative learning environment demonstrate consistent improvements over unimodal baselines and prior cross-attention approaches under standard and modality degradation conditions, with SHAP and t-SNE analyses confirming that CAMA produces robust, interpretable cross-modal representations for student collaboration modeling.

## OpenAI Review
---
title: Cross-modal Affinity-aligned Multimodal Learning Analytics for Predicting Student Collaboration Satisfaction in Game-Based Learning
authors: [Wen-Hsin Tsai, Chia-Ming Lee, Yuk-Ying Tung]
year: 2026
journal: 명시되지 않음
doi: 명시되지 않음
research_type: 실험 연구
methodology: 실험적 접근법
data_type: 다중 모달 데이터
sample: 50명의 중학생
context: EcoJourneys 협력 학습 환경
theoretical_framework: 명시되지 않음
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 협력적 게임 기반 학습 환경에서 학생의 협력 만족도를 예측하기 위한 Affinity-Aligned Multimodal Learning Analytics (AAMLA) 프레임워크를 제안한다. AAMLA의 핵심 구성 요소인 Cross-modal Affinity-guided Modality Alignment (CAMA) 모듈은 모달리티 간의 관계를 명시적으로 모델링하고, 대조 학습을 통해 모달리티 일관성을 강화하여 비정보적 모달리티를 적응적으로 억제한다. 50명의 중학생을 대상으로 한 실험 결과, AAMLA는 단일 모달 기준선 및 이전의 교차 주의 접근법에 비해 일관된 성능 향상을 보였으며, SHAP 및 t-SNE 분석을 통해 CAMA가 학생 협력 모델링을 위한 강력하고 해석 가능한 교차 모달 표현을 생성함을 확인하였다.

# Research Logic
## Problem
학생의 협력 만족도를 자동으로 예측하는 것이 어렵고, 모달리티 저하가 주요 장애물로 작용한다.
## Theory
모달리티 간의 관계를 명시적으로 모델링하고, 대조 학습을 통해 모달리티 일관성을 유지하는 것이 중요하다.
## Design
AAMLA 프레임워크는 다양한 모달리티의 데이터를 통합하여 협력 만족도를 예측한다.
## Findings
AAMLA는 단일 모달 접근법 및 이전의 교차 주의 접근법에 비해 성능이 우수하며, 모달리티 저하 조건에서도 안정적인 예측을 제공한다.
## Conclusion
CAMA 모듈은 비정보적 모달리티를 효과적으로 억제하면서도 유용한 정보를 유지하여, 협력 만족도 예측의 신뢰성을 높인다.

# Key Findings
- AAMLA는 단일 모달 기준선보다 우수한 성능을 보였다.
- CAMA 모듈은 모달리티 저하 조건에서도 안정적인 예측을 가능하게 한다.
- SHAP 및 t-SNE 분석을 통해 CAMA의 해석 가능성이 입증되었다.

# Contributions
## Theoretical
모달리티 간의 관계를 명시적으로 모델링하는 새로운 접근법을 제안하였다.
## Methodological
대조 학습을 활용한 모달리티 일관성 유지 방법론을 개발하였다.
## Practical
학생의 협력 만족도를 자동으로 예측할 수 있는 실용적인 도구를 제공하였다.

# Limitations
- 연구 샘플이 중학생으로 제한되어 있어 일반화에 한계가 있다.
- 모달리티 저하 조건에서의 성능 향상에 대한 추가 연구가 필요하다.

# Transferable Insights
- 다양한 모달리티를 통합하여 협력적 학습 환경에서의 학생 행동을 분석할 수 있다.
- 모달리티 간의 관계를 명시적으로 모델링하는 것이 예측 성능을 향상시킬 수 있다.

# Idea Seeds
1. AAMLA 프레임워크를 다른 교육 환경에 적용하여 효과를 검증할 수 있다.
2. 다양한 연령대의 학생을 대상으로 한 연구를 통해 일반화 가능성을 높일 수 있다.
3. 모달리티 저하에 대한 대처 방안을 추가적으로 연구할 수 있다.

# Citation Snippets
> Tsai, W.-H., Lee, C.-M., & Tung, Y.-Y. (2026). Cross-modal Affinity-aligned Multimodal Learning Analytics for Predicting Student Collaboration Satisfaction in Game-Based Learning.

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy

---

### 압축 요약
본 연구는 협력적 게임 기반 학습 환경에서 학생의 협력 만족도를 예측하기 위한 AAMLA 프레임워크를 제안하며, CAMA 모듈을 통해 모달리티 간의 관계를 명시적으로 모델링하고 비정보적 모달리티를 억제하는 방법을 제시한다. 50명의 중학생을 대상으로 한 실험에서 AAMLA는 기존 방법들보다 우수한 성능을 보였으며, 해석 가능성 또한 입증되었다.
