# Mitigating LLM biases toward spurious social contexts using direct preference optimization

- Source: arxiv
- ID: http://arxiv.org/abs/2604.02585v1
- DOI: 명시되지 않음
- Published: 2026-04-02T23:42:20Z
- Authors: Hyunji Nam, Dorottya Demszky
- Categories: cs.AI, cs.CL
- Link: https://arxiv.org/abs/2604.02585v1
- PDF: https://arxiv.org/pdf/2604.02585v1
- Keyword Score: 12

## Abstract
LLMs are increasingly used for high-stakes decision-making, yet their sensitivity to spurious contextual information can introduce harmful biases. This is a critical concern when models are deployed for tasks like evaluating teachers' instructional quality, where biased assessment can affect teachers' professional development and career trajectories. We investigate model robustness to spurious social contexts using the largest publicly available dataset of U.S. classroom transcripts (NCTE) paired with expert rubric scores. Evaluating seven frontier and open-weight models across seven categories of spurious contexts -- including teacher experience, education level, demographic identity, and sycophancy-inducing framings -- we find that irrelevant contextual information can shift model predictions by up to 1.48 points on a 7-point scale, with larger models sometimes exhibiting greater sensitivity despite higher predictive accuracy. Mitigations using prompts and standard direct preference optimization (DPO) prove largely insufficient. We propose **Debiasing-DPO**,, a self-supervised training method that pairs neutral reasoning generated from the query alone, with the model's biased reasoning generated with both the query and additional spurious context. We further combine this objective with supervised fine-tuning on ground-truth labels to prevent losses in predictive accuracy. Applied to Llama 3B \& 8B and Qwen 3B \& 7B Instruct models, Debiasing-DPO reduces bias by 84\% and improves predictive accuracy by 52\% on average. Our findings from the educational case study highlight that robustness to spurious context is not a natural byproduct of model scaling and that our proposed method can yield substantial gains in both accuracy and robustness for prompt-based prediction tasks.

## OpenAI Review
---
title: LLM의 잘못된 사회적 맥락에 대한 편향 완화: 직접 선호 최적화를 통한 접근
authors: [Hyunji Nam, Dorottya Demszky]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.02585v1
research_type: 실증 연구
methodology: 실험적 접근
data_type: 텍스트 데이터
sample: NCTE 데이터셋 (669개 샘플)
context: 교육 평가
theoretical_framework: 편향 완화 이론
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 대형 언어 모델(LLM)이 잘못된 사회적 맥락에 민감하게 반응하여 발생하는 편향을 완화하는 방법을 제안한다. 연구진은 미국 교실 전사 데이터셋(NCTE)과 전문가 평가 점수를 활용하여 7가지 범주의 잘못된 맥락에 대한 모델의 강건성을 평가하였다. 연구 결과, 관련 없는 맥락 정보가 모델 예측을 최대 1.48점까지 변화시킬 수 있으며, 대형 모델이 더 높은 예측 정확도를 보임에도 불구하고 더 큰 민감성을 나타내는 경향이 있음을 발견하였다. 기존의 편향 완화 방법은 효과적이지 않았으며, 연구진은 새로운 방법인 **Debiasing-DPO**를 제안하여 편향을 84% 줄이고 예측 정확도를 평균 52% 향상시켰다.

# Research Logic
## Problem
LLM의 잘못된 사회적 맥락에 대한 민감성이 교육 평가와 같은 고위험 결정에서 편향된 결과를 초래할 수 있다.

## Theory
편향 완화 이론을 바탕으로, 모델의 편향된 추론과 중립적인 추론을 결합하여 학습하는 방법을 제안한다.

## Design
NCTE 데이터셋을 사용하여 7가지 범주의 잘못된 맥락을 평가하고, 다양한 LLM 모델을 비교 분석하였다.

## Findings
모델의 예측은 관련 없는 맥락에 따라 최대 1.48점까지 변화하며, Debiasing-DPO 방법을 통해 편향을 84% 줄이고 예측 정확도를 52% 향상시킬 수 있었다.

## Conclusion
모델의 강건성은 자연스럽게 발생하지 않으며, 제안된 방법이 예측 정확도와 강건성을 동시에 향상시킬 수 있음을 보여준다.

# Key Findings
- 관련 없는 사회적 맥락이 모델 예측에 최대 1.48점의 변화를 초래할 수 있다.
- Debiasing-DPO 방법은 편향을 84% 줄이고 예측 정확도를 52% 향상시킨다.
- 대형 모델이 더 높은 예측 정확도를 보이지만, 잘못된 맥락에 대한 민감성이 더 크다.

# Contributions
## Theoretical
편향 완화 이론에 대한 새로운 통찰을 제공하며, LLM의 강건성에 대한 이해를 심화시킨다.

## Methodological
Debiasing-DPO라는 새로운 학습 방법론을 제안하여 기존의 편향 완화 방법의 한계를 극복한다.

## Practical
교육 평가에서 LLM의 활용을 개선하고, 교사 평가의 공정성을 높이는 데 기여할 수 있다.

# Limitations
- 연구는 특정 데이터셋(NCTE)에 국한되어 있으며, 일반화 가능성에 제한이 있다.
- 제안된 방법의 효과는 다른 유형의 LLM에 대해 추가적인 검증이 필요하다.

# Transferable Insights
- LLM의 편향 문제는 교육 외의 다른 분야에서도 유사하게 발생할 수 있다.
- 잘못된 맥락에 대한 민감성을 줄이는 방법론은 다양한 AI 응용 분야에 적용 가능하다.

# Idea Seeds
1. 다양한 교육 환경에서 Debiasing-DPO의 효과를 검증하는 연구.
2. 다른 유형의 LLM에 대한 편향 완화 방법의 적용 가능성 탐색.
3. AI 기반 교육 도구의 공정성을 높이기 위한 정책 제안.

# Citation Snippets
> Nam, H., & Demszky, D. (2026). Mitigating LLM biases toward spurious social contexts using direct preference optimization. arXiv. https://arxiv.org/abs/2604.02585v1

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy

---

### 압축 요약
본 연구는 대형 언어 모델(LLM)의 잘못된 사회적 맥락에 대한 민감성을 평가하고, 이를 완화하기 위한 새로운 방법인 Debiasing-DPO를 제안한다. 연구 결과, 이 방법은 편향을 84% 줄이고 예측 정확도를 52% 향상시키는 효과가 있음을 보여준다. LLM의 강건성은 자연스럽게 발생하지 않으며, 제안된 방법이 교육 평가에서의 공정성을 높이는 데 기여할 수 있다.
