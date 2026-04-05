# Training data generation for context-dependent rubric-based short answer grading

- Source: arxiv
- ID: http://arxiv.org/abs/2603.28537v2
- DOI: 명시되지 않음
- Published: 2026-03-30T14:59:53Z
- Authors: Pavel Šindelář, Dávid Slivka, Christopher Bouma, Filip Prášil, Ondřej Bojar
- Categories: cs.CL
- Link: https://arxiv.org/abs/2603.28537v2
- PDF: https://arxiv.org/pdf/2603.28537v2
- Keyword Score: 10

## Abstract
Every four years, the PISA test is administered by the OECD to test the knowledge of teenage students worldwide and allow for comparisons of educational systems. However, having to avoid language differences and annotator bias makes the grading of student answers challenging. For these reasons, it would be interesting to consider methods of automatic student answer grading. To train some of these methods, which require machine learning, or to compute parameters or select hyperparameters for those that do not, a large amount of domain-specific data is needed. In this work, we explore a small number of methods for creating a large-scale training dataset using only a relatively small confidential dataset as a reference, leveraging a set of very simple derived text formats to preserve confidentiality. Using the proposed methods, we successfully created three surrogate datasets that are, at the very least, superficially more similar to the reference dataset than a straightforward result of prompt-based generation. Early experiments suggest one of these approaches might also lead to improved training of automatic answer grading models.

## OpenAI Review
---
title: Training data generation for context-dependent rubric-based short answer grading
authors: [Pavel Šindelář, Dávid Slivka, Christopher Bouma, Filip Prášil, Ondřej Bojar]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2603.28537v2
research_type: 실험적 연구
methodology: 데이터 생성 및 평가
data_type: 기계 학습 데이터셋
sample: 비공식 데이터셋
context: PISA 테스트의 학생 답변 평가
theoretical_framework: 기계 학습 및 데이터 생성 이론
keywords: [short answer grading, dataset generation, machine learning, PISA, educational assessment]
---

# APA 7th style

# Summary
본 연구는 PISA 테스트의 학생 답변을 평가하기 위한 자동화된 방법을 탐구하며, 기계 학습을 위한 대규모 훈련 데이터셋 생성을 목표로 한다. 연구자들은 비공식 데이터셋을 기반으로 간단한 파생 텍스트 형식을 활용하여 기밀성을 유지하면서도 유사한 데이터셋을 생성하는 방법을 제안하였다. 이 방법을 통해 세 가지 대체 데이터셋을 성공적으로 생성하였으며, 초기 실험 결과는 이 중 하나의 접근 방식이 자동 답변 평가 모델의 훈련 개선에 기여할 수 있음을 시사한다.

# Research Logic
## Problem
PISA 테스트의 학생 답변 평가에서 언어 차이와 주석자 편향을 피하는 것이 어려움.
## Theory
기계 학습 및 데이터 생성 이론을 바탕으로 한 자동화된 평가 방법.
## Design
기밀 데이터셋을 참조하여 파생 텍스트 형식을 활용한 대규모 데이터셋 생성.
## Findings
세 가지 대체 데이터셋이 생성되었으며, 초기 실험에서 하나의 접근 방식이 모델 훈련 개선에 기여할 가능성이 있음.
## Conclusion
제안된 방법은 기밀성을 유지하면서도 유사한 데이터셋을 생성할 수 있는 가능성을 보여준다.

# Key Findings
- PISA 테스트의 학생 답변 평가를 위한 자동화된 방법 탐구.
- 기밀 데이터셋을 기반으로 한 대규모 훈련 데이터셋 생성.
- 초기 실험에서 제안된 방법이 자동 답변 평가 모델의 훈련 개선에 기여할 가능성.

# Contributions
## Theoretical
기계 학습 및 데이터 생성 이론에 대한 새로운 통찰 제공.
## Methodological
기밀성을 유지하면서도 유사한 데이터셋을 생성하는 방법론 제안.
## Practical
PISA 테스트와 같은 교육 평가에서의 자동화된 답변 평가 가능성 제시.

# Limitations
- 기밀 데이터셋의 사용으로 인한 제한된 접근성.
- 생성된 데이터셋의 품질 및 유사성에 대한 추가 검증 필요.

# Transferable Insights
- 기밀성을 유지하면서도 데이터셋을 생성하는 방법은 다른 교육 평가 분야에 적용 가능.
- 자동화된 평가 시스템 개발에 있어 기계 학습의 활용 가능성.

# Idea Seeds
1. 다양한 교육 평가에서의 자동화된 답변 평가 시스템 개발.
2. 기밀 데이터셋을 활용한 다른 연구 분야에서의 데이터 생성 방법론 탐구.
3. 생성된 데이터셋의 품질 검증을 위한 추가 연구.

# Citation Snippets
> Šindelář, P., Slivka, D., Bouma, C., Prášil, F., & Bojar, O. (2026). Training data generation for context-dependent rubric-based short answer grading. arXiv. https://arxiv.org/abs/2603.28537v2

tags: #PISA, #기계학습, #데이터생성, #교육평가, #자동화된평가, #답변평가, #기밀성

---

요약: 본 연구는 PISA 테스트의 학생 답변 평가를 위한 자동화된 방법을 탐구하며, 기계 학습을 위한 대규모 훈련 데이터셋 생성을 목표로 한다. 기밀 데이터셋을 기반으로 간단한 파생 텍스트 형식을 활용하여 유사한 데이터셋을 생성하는 방법을 제안하였으며, 초기 실험 결과는 이 방법이 자동 답변 평가 모델의 훈련 개선에 기여할 수 있음을 시사한다.
