# RAG-KT: Cross-platform Explainable Knowledge Tracing with Multi-view Fusion Retrieval Generation

- Source: arxiv
- ID: http://arxiv.org/abs/2604.10960v2
- DOI: 명시되지 않음
- Published: 2026-04-13T03:56:17Z
- Authors: Zhiyi Duan, Hongyu Yuan, Rui Liu
- Categories: cs.AI
- Link: https://arxiv.org/abs/2604.10960v2
- PDF: https://arxiv.org/pdf/2604.10960v2
- Keyword Score: 10

## Abstract
Knowledge Tracing (KT) infers a student's knowledge state from past interactions to predict future performance. Conventional Deep Learning (DL)-based KT models are typically tied to platform-specific identifiers and latent representations, making them hard to transfer and interpret. Large Language Model (LLM)-based methods can be either ungrounded under prompting or overly domain-dependent under fine-tuning. In addition, most existing KT methods are developed and evaluated under a same-distribution assumption. In real deployments, educational data often arise from heterogeneous platforms with substantial distribution shift, which often degrades generalization. To this end, we propose RAG-KT, a retrieval-augmented paradigm that frames cross-platform KT as reliable context constrained inference with LLMs. It builds a unified multi-source structured context with cross-source alignment via Question Group abstractions and retrieves complementary rich and reliable context for each prediction, enabling grounded prediction and interpretable diagnosis. Experiments on three public KT benchmarks demonstrate consistent gains in accuracy and robustness, including strong performance under cross-platform conditions.

## OpenAI Review
---
title: RAG-KT: Cross-platform Explainable Knowledge Tracing with Multi-view Fusion Retrieval Generation
authors: [Zhiyi Duan, Hongyu Yuan, Rui Liu]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.10960v2
research_type: 이론적 연구
methodology: 실험적 연구
data_type: 공공 데이터셋
sample: 세 가지 공공 KT 벤치마크
context: 교육 데이터 마이닝
theoretical_framework: 지식 추적(KT)
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구에서는 RAG-KT라는 새로운 지식 추적(KT) 패러다임을 제안한다. 기존의 딥러닝 기반 KT 모델은 플랫폼 특정 식별자와 잠재 표현에 의존하여 일반화 및 해석이 어려운 문제를 가지고 있다. RAG-KT는 다양한 플랫폼에서 수집된 교육 데이터를 통합하여 신뢰할 수 있는 맥락 제약 추론을 가능하게 하며, 다중 소스 구조적 맥락을 구축하여 각 예측에 대해 보완적인 정보를 검색한다. 실험 결과, RAG-KT는 정확성과 강건성에서 일관된 향상을 보여주며, 특히 크로스 플랫폼 조건에서 강력한 성능을 발휘한다.

# Research Logic
## Problem
기존 KT 모델은 플랫폼 특정 식별자에 의존하여 일반화가 어렵고 해석 가능성이 낮다.
## Theory
RAG-KT는 다중 소스 지식 그래프와 구조적 검색을 통해 KT의 해석 가능성과 크로스 플랫폼 일반화를 개선한다.
## Design
RAG-KT는 다중 소스 지식 기반을 구축하고, 다중 뷰 검색 메커니즘을 통해 관련 맥락 정보를 검색한다.
## Findings
RAG-KT는 세 가지 공공 KT 벤치마크에서 정확성과 강건성을 일관되게 향상시켰다.
## Conclusion
RAG-KT는 기존 KT 방법의 한계를 극복하고, 해석 가능성과 크로스 플랫폼 일반화를 제공한다.

# Key Findings
- RAG-KT는 기존 KT 모델보다 높은 정확성을 보였다.
- 다중 소스 구조적 맥락을 통해 해석 가능한 분석 보고서를 생성한다.
- 크로스 플랫폼 조건에서도 강력한 성능을 유지한다.

# Contributions
## Theoretical
KT의 해석 가능성과 크로스 플랫폼 일반화 문제를 해결하는 새로운 패러다임을 제안하였다.
## Methodological
다중 소스 지식 그래프와 다중 뷰 검색 메커니즘을 통해 KT의 성능을 향상시켰다.
## Practical
교육 데이터의 이질성을 고려한 KT 모델을 통해 실제 교육 환경에서의 적용 가능성을 높였다.

# Limitations
- 특정 플랫폼에 대한 의존성이 여전히 존재할 수 있다.
- 데이터의 이질성으로 인해 예측 정확도가 제한될 수 있다.

# Transferable Insights
- 다양한 플랫폼에서의 교육 데이터를 통합하는 방법론은 다른 교육 기술 연구에 적용 가능하다.
- KT의 해석 가능성을 높이는 접근법은 교육자에게 유용한 정보를 제공할 수 있다.

# Idea Seeds
1. RAG-KT의 구조적 검색 메커니즘을 다른 교육 기술 분야에 적용하기.
2. 다양한 교육 플랫폼에서의 데이터 통합 방법론 개발.
3. KT의 해석 가능성을 높이기 위한 추가적인 분석 도구 개발.

# Citation Snippets
> Duan, Z., Yuan, H., & Liu, R. (2026). RAG-KT: Cross-platform Explainable Knowledge Tracing with Multi-view Fusion Retrieval Generation. arXiv. https://arxiv.org/abs/2604.10960v2

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy

---

요약: 본 연구에서는 RAG-KT라는 새로운 지식 추적 패러다임을 제안하며, 기존 KT 모델의 한계를 극복하고 해석 가능성과 크로스 플랫폼 일반화를 제공한다. RAG-KT는 다중 소스 구조적 맥락을 통해 예측의 정확성과 강건성을 향상시키며, 교육 데이터의 이질성을 고려한 접근법을 통해 실제 교육 환경에서의 적용 가능성을 높인다.
