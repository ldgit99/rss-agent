# Semantic Grading of Written Answers in Low-Resource Language Bangla Using a Fine-Tuned Lightweight Language Model

- Source: arxiv
- ID: http://arxiv.org/abs/2606.11931v1
- DOI: 명시되지 않음
- Published: 2026-06-10T11:03:59Z
- Authors: Meherun Farzana, Aniket Joarder, Mahmudul Hasan, Md. Mosaddek Khan
- Categories: cs.CL
- Link: https://arxiv.org/abs/2606.11931v1
- PDF: https://arxiv.org/pdf/2606.11931v1
- Keyword Score: 12

## Abstract
Bangla is among the world's most widely spoken languages, yet it remains underserved in educational NLP research. In many remote and rural regions, access to qualified subject teachers is limited, and written answers are consequently graded largely by hand, restricting timely and consistent feedback. Automatic assessment is challenging because semantically correct responses can vary substantially in surface form. We present a bilingual (Bangla-English) evaluation system designed for low-resource educational settings that prioritizes semantic correctness over lexical overlap. Our approach fine-tunes a lightweight language model to grade each response using the question, reference answer, and student answer, producing a numeric score and concise, context-grounded feedback suitable for classroom deployment. We also construct a synthetic bilingual dataset to enable controlled training and evaluation. Across proprietary and open-source LLMs evaluated under a unified protocol, our QLoRA-tuned Qwen3-8B confirms consistent improvement by producing the most leakage-resistant feedback (RoRa = 0.819) in synthetic evaluation and the strongest agreement with human scores (rho = 0.936, MAE = 0.725) in a dedicated human study.

## OpenAI Review
---
title: "Semantic Grading of Written Answers in Low-Resource Language Bangla Using a Fine-Tuned Lightweight Language Model"
authors: 
  - Meherun Farzana
  - Aniket Joarder
  - Mahmudul Hasan
  - Md. Mosaddek Khan
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2606.11931v1
research_type: 실험적 연구
methodology: QLoRA로 미세 조정된 경량 언어 모델을 사용한 자동 평가 시스템 개발
data_type: 합성 데이터셋
sample: 122,710개의 질문-참조 쌍
context: 방글라어 교육 환경
theoretical_framework: 의미적 정확성을 우선시하는 평가 시스템
keywords: [Bangla, 자동 평가, 의미적 정확성, 교육 NLP, 경량 언어 모델]
---

# APA 7th style

# Summary
본 연구는 방글라어의 저자원 교육 환경을 위한 이중 언어 평가 시스템을 제안한다. 이 시스템은 의미적 정확성을 우선시하며, 경량 언어 모델을 미세 조정하여 학생의 답변을 평가하고 점수와 피드백을 생성한다. 연구 결과, QLoRA로 미세 조정된 Qwen3-8B 모델이 인간 평가자와의 일치도에서 0.936의 상관계수를 기록하며, 가장 높은 피드백 신뢰도를 보였다(RoRa = 0.819). 이 시스템은 방글라어 교육에서의 자동 평가의 필요성을 충족시키고, 교사들이 더 나은 피드백을 제공할 수 있도록 지원한다.

# Research Logic
## Problem
방글라어는 교육 NLP 연구에서 소외되어 있으며, 많은 지역에서 자격을 갖춘 교사의 접근이 제한되어 있다. 이로 인해 수작업으로 채점하는 경우가 많아 피드백이 지연되고 일관성이 결여된다.

## Theory
기존의 자동 평가 시스템은 주로 표면적 일치에 의존하였으나, 본 연구는 의미적 정확성을 중심으로 한 평가 접근 방식을 채택하였다.

## Design
이 연구는 QLoRA로 미세 조정된 경량 언어 모델을 사용하여 질문, 참조 답변, 학생 답변을 기반으로 점수와 피드백을 생성하는 시스템을 설계하였다.

## Findings
QLoRA로 미세 조정된 Qwen3-8B 모델은 인간 평가자와의 상관관계에서 0.936을 기록하였으며, MAE는 0.725로 나타났다. 또한, 피드백의 신뢰도(RoRa)는 0.819로 확인되었다.

## Conclusion
본 연구는 방글라어 교육 환경에서의 자동 평가 시스템의 필요성을 강조하며, 교사들이 보다 효율적으로 학생의 답변을 평가할 수 있도록 지원하는 방법을 제시하였다.

# Key Findings
- QLoRA로 미세 조정된 Qwen3-8B 모델이 인간 평가자와의 높은 일치도를 보였다(상관계수 0.936).
- 피드백의 신뢰도는 0.819로, 의미적 정확성을 우선시하는 평가의 효과를 입증하였다.
- 합성 데이터셋을 통해 다양한 학생 답변 변형을 생성하고 평가하였다.

# Contributions
## Theoretical
의미적 정확성을 중심으로 한 새로운 평가 모델을 제안하여 교육 NLP 연구에 기여하였다.

## Methodological
QLoRA를 활용한 경량 언어 모델의 미세 조정 방법론을 개발하였다.

## Practical
방글라어 교육 환경에서의 자동 평가 시스템을 통해 교사들이 보다 효율적으로 학생의 답변을 평가할 수 있는 실용적인 도구를 제공하였다.

# Limitations
- 방글라어 교육 자료의 부족으로 인해 합성 데이터셋의 품질이 제한적일 수 있다.
- 시스템의 배포가 저자원 환경에서의 실제 적용에 대한 추가적인 검증이 필요하다.

# Transferable Insights
- 저자원 언어 환경에서도 효과적인 자동 평가 시스템을 구축할 수 있는 가능성을 보여준다.
- 의미적 정확성을 우선시하는 평가 접근 방식이 교육 현장에서의 피드백 품질을 향상시킬 수 있음을 시사한다.

# Idea Seeds
1. 다른 저자원 언어에 대한 유사한 평가 시스템 개발.
2. 학생의 답변에 대한 개인화된 피드백 생성 방법 연구.
3. 교사와 학생 간의 상호작용을 증진시키는 AI 기반 도구 개발.

# Citation Snippets
> Farzana, M., Joarder, A., Hasan, M., & Khan, M. M. (2026). Semantic Grading of Written Answers in Low-Resource Language Bangla Using a Fine-Tuned Lightweight Language Model. arXiv. https://arxiv.org/abs/2606.11931v1

tags: #Bangla, #자동_평가, #의미적_정확성, #교육_NLP, #경량_언어_모델, #합성_데이터셋, #QLoRA

---

요약: 본 연구는 방글라어 교육 환경을 위한 이중 언어 평가 시스템을 제안하며, QLoRA로 미세 조정된 경량 언어 모델을 사용하여 학생의 답변을 평가하고 피드백을 생성한다. 연구 결과, 이 시스템은 인간 평가자와의 높은 일치도를 보이며, 방글라어 교육에서의 자동 평가의 필요성을 충족시킨다.
