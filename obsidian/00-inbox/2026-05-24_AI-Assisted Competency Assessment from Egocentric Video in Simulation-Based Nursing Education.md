# AI-Assisted Competency Assessment from Egocentric Video in Simulation-Based Nursing Education

- Source: arxiv
- ID: http://arxiv.org/abs/2605.20233v1
- DOI: 명시되지 않음
- Published: 2026-05-16T02:07:35Z
- Authors: Hanchen David Wang, Yilin Liu, Madison J. Lee, Surya Chand Rayala, Gautam Biswas, Daniel T. Levin, Meiyi Ma
- Categories: cs.CV, cs.AI
- Link: https://arxiv.org/abs/2605.20233v1
- PDF: https://arxiv.org/pdf/2605.20233v1
- Keyword Score: 16

## Abstract
Assessing learner competency in clinical simulation requires expert observation that is time-intensive, difficult to scale, and subject to inter-rater variability. Vision-language models have emerged as a promising tool for understanding complex visual behavior. In this work, we investigate whether visual observations can provide educationally meaningful signals for competency assessment through a three-stage framework that (1) extracts action timelines from egocentric nursing simulation video using frozen visual encoders and few-shot learning, (2) derives sequence-level features and per-session recognition metrics, and (3) relates these to instructor-rated competency. Across 22 densely annotated sessions (3.8 hours, 493 actions), a frozen DINOv2 backbone with HMM Viterbi decoding achieves 57.4% MOF in leave-one-out 1-shot recognition. Surprisingly, we observe a negative trend between recognition accuracy and competency (rho = -0.524, p = 0.012 for mIoU), robust to six confound controls: more competent students produce diverse, harder-to-classify workflows, while simple sequence features show no such relationship. Per-item analysis identifies patient safety protocols and team communication as the expected behaviors most reflected in this pattern, and process model comparisons reveal that higher-competency students exhibit more protocol-consistent action transitions. These findings suggest that recognition accuracy may complement predicted action timelines as a pedagogically informative signal in automated competency assessment.

## OpenAI Review
---
title: AI-Assisted Competency Assessment from Egocentric Video in Simulation-Based Nursing Education
authors: [Hanchen David Wang, Yilin Liu, Madison J. Lee, Surya Chand Rayala, Gautam Biswas, Daniel T. Levin, Meiyi Ma]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2605.20233v1
research_type: 실험적 연구
methodology: 세 단계 프레임워크
data_type: 비디오 데이터
sample: 22명의 간호 학생
context: 간호 교육 시뮬레이션
theoretical_framework: 행동 인식 및 평가
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 간호 교육에서의 학습자 역량 평가를 위해 시뮬레이션 비디오를 활용한 AI 기반 접근 방식을 제안한다. 세 단계의 프레임워크를 통해 행동 타임라인을 추출하고, 시퀀스 수준의 특징과 인스트럭터 평가 점수를 연관시킨다. 22개의 세션에서 DINOv2 모델을 사용하여 57.4%의 MOF를 달성하였으며, 인식 정확도와 역량 간의 부정적인 상관관계(ρ = -0.524, p = 0.012)를 발견하였다. 이 연구는 자동화된 역량 평가에서 인식 정확도가 교육적으로 유의미한 신호로 작용할 수 있음을 시사한다.

# Research Logic
## Problem
전문가 관찰이 필요한 임상 시뮬레이션에서 학습자 역량 평가의 비효율성과 신뢰성 문제.
## Theory
비디오 기반 행동 인식이 역량 평가에 기여할 수 있다는 이론적 배경.
## Design
세 단계의 프레임워크를 통해 행동 인식, 시퀀스 분석, 역량 분석을 수행.
## Findings
인식 정확도와 역량 간의 부정적 상관관계 발견, 높은 역량 학생들이 더 다양한 행동 패턴을 보임.
## Conclusion
AI 기반의 행동 인식이 역량 평가에 유용할 수 있으며, 인식 정확도가 교육적 신호로 작용할 수 있음을 제안.

# Key Findings
- DINOv2 모델을 통한 1-shot 행동 인식에서 57.4%의 MOF 달성.
- 인식 정확도와 인스트럭터 평가 점수 간의 부정적 상관관계 발견 (ρ = -0.524, p = 0.012).
- 높은 역량 학생들이 더 다양한 행동 전환을 보임.

# Contributions
## Theoretical
AI 기반 행동 인식의 교육적 활용 가능성 제시.
## Methodological
세 단계 프레임워크를 통한 역량 평가 방법론 개발.
## Practical
간호 교육에서의 자동화된 역량 평가 도구로서의 AI 활용 가능성 탐색.

# Limitations
- 샘플 크기가 작아 일반화에 한계가 있음.
- 특정 행동 패턴에 대한 분석이 제한적임.

# Transferable Insights
- AI 기반 행동 인식 기술이 다른 교육 분야에도 적용 가능할 수 있음.
- 역량 평가의 자동화가 교육의 효율성을 높일 수 있는 잠재력.

# Idea Seeds
1. 다양한 교육 분야에서 AI 기반 역량 평가 시스템 개발.
2. 행동 인식 기술을 활용한 실시간 피드백 시스템 구축.
3. 간호 교육 외 다른 전문 교육 분야에 대한 연구 확장.

# Citation Snippets
> Wang, H. D., Liu, Y., Lee, M. J., Rayala, S. C., Biswas, G., Levin, D. T., & Ma, M. (2026). AI-Assisted Competency Assessment from Egocentric Video in Simulation-Based Nursing Education. arXiv. https://arxiv.org/abs/2605.20233v1

tags: #human-ai collaboration, #ai tutoring, #instructional design, #education, #learning analytics, #ai pedagogy, #competency assessment

---

요약: 본 연구는 간호 교육에서 AI 기반의 행동 인식 기술을 활용하여 학습자 역량을 평가하는 방법을 제안한다. 세 단계의 프레임워크를 통해 행동 타임라인을 추출하고, 인식 정확도와 인스트럭터 평가 점수 간의 관계를 분석하였다. 연구 결과, 인식 정확도와 역량 간의 부정적 상관관계가 발견되었으며, 이는 자동화된 역량 평가에서 인식 정확도가 교육적 신호로 작용할 수 있음을 시사한다.
