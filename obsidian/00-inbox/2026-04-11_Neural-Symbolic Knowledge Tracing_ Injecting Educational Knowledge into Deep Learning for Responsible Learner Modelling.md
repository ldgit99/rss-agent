# Neural-Symbolic Knowledge Tracing: Injecting Educational Knowledge into Deep Learning for Responsible Learner Modelling

- Source: arxiv
- ID: http://arxiv.org/abs/2604.08263v1
- DOI: 명시되지 않음
- Published: 2026-04-09T13:49:07Z
- Authors: Danial Hooshyar, Gustav Šír, Yeongwook Yang, Tommi Kärkkäinen, Raija Hämäläinen, Ekaterina Krivich, Mutlu Cukurova, Dragan Gašević, Roger Azevedo
- Categories: cs.AI
- Link: https://arxiv.org/abs/2604.08263v1
- PDF: https://arxiv.org/pdf/2604.08263v1
- Keyword Score: 21

## Abstract
The growing use of artificial intelligence (AI) in education, particularly large language models (LLMs), has increased interest in intelligent tutoring systems. However, LLMs often show limited adaptivity and struggle to model learners' evolving knowledge over time, highlighting the need for dedicated learner modelling approaches. Although deep knowledge tracing methods achieve strong predictive performance, their opacity and susceptibility to bias can limit alignment with pedagogical principles. To address this, we propose Responsible-DKT, a neural-symbolic deep knowledge tracing approach that integrates symbolic educational knowledge (e.g., mastery and non-mastery rules) into sequential neural models for responsible learner modelling. Experiments on a real-world dataset of students' math interactions show that Responsible-DKT outperforms both a neural-symbolic baseline and a fully data-driven PyTorch DKT model across training settings. The model achieves over 0.80 AUC with only 10% of training data and up to 0.90 AUC, improving performance by up to 13%. It also demonstrates improved temporal reliability, producing lower early- and mid-sequence prediction errors and the lowest prediction inconsistency rates across sequence lengths, indicating that prediction updates remain directionally aligned with observed student responses over time. Furthermore, the neural-symbolic approach offers intrinsic interpretability via a grounded computation graph that exposes the logic behind each prediction, enabling both local and global explanations. It also allows empirical evaluation of pedagogical assumptions, revealing that repeated incorrect responses (non-mastery) strongly influence prediction updates. These results indicate that neural-symbolic approaches enhance both performance and interpretability, mitigate data limitations, and support more responsible, human-centered AI in education.

## OpenAI Review
---
title: Neural-Symbolic Knowledge Tracing: Injecting Educational Knowledge into Deep Learning for Responsible Learner Modelling
authors: [Danial Hooshyar, Gustav Šír, Yeongwook Yang, Tommi Kärkkäinen, Raija Hämäläinen, Ekaterina Krivich, Mutlu Cukurova, Dragan Gašević, Roger Azevedo]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.08263v1
research_type: 실험 연구
methodology: 신경-상징적 접근법
data_type: 실제 데이터셋
sample: 6학년 학생들의 수학 상호작용
context: 교육 AI
theoretical_framework: 책임 있는 AI
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 교육에서 인공지능(AI)의 사용 증가와 관련하여, 특히 대형 언어 모델(LLMs)의 한계를 지적하고, 책임 있는 학습자 모델링을 위한 신경-상징적 지식 추적 접근법인 Responsible-DKT를 제안한다. 이 모델은 상징적 교육 지식을 통합하여 학습자의 지식 변화를 추적하고, 예측 정확도를 향상시키며, 예측의 해석 가능성을 높인다. 실험 결과, Responsible-DKT는 기존의 신경-상징적 기준선 및 데이터 기반 DKT 모델보다 우수한 성능을 보였으며, 10%의 훈련 데이터로도 0.80 이상의 AUC를 달성하였다. 이 연구는 AI의 책임 있는 사용을 위한 설계 원칙을 강조하며, 교육적 지식과 기계 학습 방법의 융합을 통해 더 나은 AI 시스템을 개발할 수 있는 가능성을 제시한다.

# Research Logic
## Problem
LLMs는 학습자의 지식 변화를 신뢰성 있게 모델링하는 데 한계를 보인다.
## Theory
책임 있는 AI 원칙에 기반한 신경-상징적 접근법이 필요하다.
## Design
상징적 교육 지식을 통합한 신경 모델을 사용하여 학습자 모델링을 수행한다.
## Findings
Responsible-DKT는 예측 정확도에서 기존 모델을 초과하며, 예측의 일관성을 높인다.
## Conclusion
신경-상징적 접근법은 AI의 해석 가능성을 높이고, 교육적 원칙과의 정렬을 개선한다.

# Key Findings
- Responsible-DKT는 10%의 훈련 데이터로 0.80 이상의 AUC를 달성하였다.
- 예측의 일관성이 개선되어, 학생 반응과의 방향성이 유지되었다.
- 반복적인 잘못된 응답이 예측 업데이트에 강한 영향을 미친다.

# Contributions
## Theoretical
책임 있는 AI 설계 원칙을 교육 AI에 적용하는 새로운 이론적 틀을 제시한다.
## Methodological
신경-상징적 접근법을 통해 기존의 데이터 기반 모델의 한계를 극복한다.
## Practical
교육적 지식과 기계 학습의 통합을 통해 더 나은 학습자 지원 시스템을 개발할 수 있는 가능성을 제시한다.

# Limitations
- 연구는 특정 과목(수학)에 국한되어 있으며, 다른 과목에 대한 일반화가 필요하다.
- 데이터의 질과 양이 모델 성능에 영향을 미칠 수 있다.

# Transferable Insights
- 신경-상징적 모델링 접근법은 다양한 교육적 맥락에서 적용 가능하다.
- 책임 있는 AI 설계 원칙은 교육 외 다른 분야에서도 유용할 수 있다.

# Idea Seeds
1. 다른 과목에 대한 Responsible-DKT의 적용 가능성 연구.
2. 다양한 학습자 특성을 고려한 모델 개선 방안 탐색.
3. 교육적 피드백 시스템과의 통합 연구.

# Citation Snippets
> Hooshyar, D., Šír, G., Yang, Y., Kärkkäinen, T., Hämäläinen, R., Krivich, E., Cukurova, M., Gašević, D., & Azevedo, R. (2026). Neural-Symbolic Knowledge Tracing: Injecting Educational Knowledge into Deep Learning for Responsible Learner Modelling. arXiv. https://arxiv.org/abs/2604.08263v1

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy

---

요약: 본 연구는 AI의 교육적 활용에서 LLM의 한계를 극복하기 위한 신경-상징적 지식 추적 모델인 Responsible-DKT를 제안하며, 이 모델이 기존의 데이터 기반 모델보다 우수한 성능을 보임을 입증하였다. 연구 결과는 AI의 책임 있는 설계 원칙을 강조하며, 교육적 지식과 기계 학습의 융합을 통해 더 나은 학습자 지원 시스템 개발의 가능성을 제시한다.
