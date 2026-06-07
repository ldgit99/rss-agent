# Causal Scaffolding for Physical Reasoning: A Benchmark for Causally-Informed Physical World Understanding in VLMs

- Source: arxiv
- ID: http://arxiv.org/abs/2606.05966v1
- DOI: 명시되지 않음
- Published: 2026-06-04T10:07:05Z
- Authors: Tianyi Tang, Zhuoyi Lin, Zeyu Feng, Tianyi Ma, Yew-Soon Ong, Ivor Tsang, Haiyan Yin
- Categories: cs.DB, cs.AI
- Link: https://arxiv.org/abs/2606.05966v1
- PDF: https://arxiv.org/pdf/2606.05966v1
- Keyword Score: 13

## Abstract
Understanding and reasoning about the physical world is the foundation of intelligent behavior, yet state-of-the-art vision-language models (VLMs) still fail at causal physical reasoning, often producing plausible but incorrect answers. To address this gap, we introduce CausalPhys, a benchmark of over 3,000 carefully curated video- and image-based questions spanning four domains: Perception, Anticipation, Intervention, and Goal Orientation. Each question is paired with an expert-annotated causal graph capturing object-attribute-event dependencies, enabling interpretable and fine-grained evaluation of causal understanding. Building on this, we formulate a causal-graph-grounded metric that quantitatively measures how well a model's chain-of-thought reasoning aligns with the correct causal relations, moving beyond answer-only accuracy and enabling systematic diagnosis of VLMs' causal reasoning failures. Using this metric, we conduct a comprehensive analysis of leading VLMs, revealing systematic gaps in capturing causal dependencies and underscoring the need for causality-aware learning. To address these limitations, we further propose Causal Rationale-informed Fine-Tuning (CRFT), which explicitly aligns VLM reasoning with causal structures. Extensive experiments demonstrate that CRFT substantially enhances both reasoning accuracy and interpretability across multiple model backbones. By unifying dataset curation, causal evaluation, and causality-informed learning, CausalPhys establishes a strong foundation for advancing modern VLMs toward causally grounded physical reasoning.

## OpenAI Review
---
title: Causal Scaffolding for Physical Reasoning: A Benchmark for Causally-Informed Physical World Understanding in VLMs
authors: [Tianyi Tang, Zhuoyi Lin, Zeyu Feng, Tianyi Ma, Yew-Soon Ong, Ivor Tsang, Haiyan Yin]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2606.05966v1
research_type: 기초 연구
methodology: 실험적 연구
data_type: 비디오 및 이미지 기반 질문
sample: 3,000개 이상의 질문
context: 물리적 세계 이해를 위한 비전-언어 모델(VLMs)의 causal reasoning
theoretical_framework: Pearl의 인과적 사다리
keywords: [causal reasoning, physical reasoning, vision-language models, causal graphs, benchmark, AI, machine learning]
---

# APA 7th style

# Summary
이 연구는 물리적 세계에 대한 이해와 추론이 지능적 행동의 기초임을 강조하며, 현재의 비전-언어 모델(VLMs)이 인과적 물리적 추론에서 실패하는 문제를 다룬다. 이를 해결하기 위해 CausalPhys라는 벤치마크를 소개하며, 3,000개 이상의 비디오 및 이미지 기반 질문을 통해 인과적 이해를 평가할 수 있는 구조적 인과 그래프를 제공한다. 연구는 VLM의 인과적 추론 실패를 진단하고, Causal Rationale-informed Fine-Tuning (CRFT) 방법론을 통해 모델의 추론 정확성과 해석 가능성을 향상시키는 방법을 제안한다. 이 연구는 VLMs의 물리적 추론 능력을 향상시키기 위한 강력한 기초를 마련한다.

# Research Logic
## Problem
현재의 VLMs는 인과적 물리적 추론에서 신뢰할 수 없는 결과를 생성하며, 이는 물리적 상호작용에 대한 이해 부족에서 기인한다.

## Theory
Pearl의 인과적 사다리를 기반으로 한 인과적 이해의 수준을 정의하고, 이를 통해 VLM의 물리적 추론 능력을 평가한다.

## Design
CausalPhys 벤치마크는 3,000개 이상의 질문과 전문가가 주석을 단 인과 그래프를 포함하여, 물리적 세계의 다양한 시나리오를 포괄한다.

## Findings
VLMs는 인과적 의존성을 포착하는 데 시스템적인 격차가 있으며, CRFT 방법론을 통해 이러한 격차를 줄일 수 있음을 발견하였다.

## Conclusion
CausalPhys는 VLMs의 물리적 추론 능력을 향상시키기 위한 체계적이고 해석 가능한 평가 기준을 제공하며, 인과적 학습의 필요성을 강조한다.

# Key Findings
- CausalPhys는 3,000개 이상의 비디오 및 이미지 기반 질문을 포함한다.
- VLMs의 인과적 추론 실패를 진단할 수 있는 새로운 메트릭을 제안한다.
- CRFT 방법론은 VLM의 추론 정확성과 해석 가능성을 크게 향상시킨다.

# Contributions
## Theoretical
인과적 물리적 추론을 위한 새로운 평가 기준과 메트릭을 제시하였다.

## Methodological
CausalPhys 벤치마크와 CRFT 방법론을 통해 VLM의 인과적 이해를 체계적으로 평가할 수 있는 방법을 개발하였다.

## Practical
VLMs의 물리적 추론 능력을 향상시키기 위한 실용적인 접근 방식을 제공한다.

# Limitations
- 현재 벤치마크는 특정 물리적 시나리오에 국한되어 있다.
- 인과적 이해의 복잡성을 완전히 포착하지 못할 수 있다.

# Transferable Insights
- 인과적 추론을 위한 데이터셋 구축의 중요성을 강조한다.
- VLMs의 인과적 이해를 향상시키기 위한 체계적인 접근 방식이 필요하다.

# Idea Seeds
1. 다양한 물리적 시나리오를 포함하는 추가적인 벤치마크 개발.
2. 인과적 추론을 위한 교육 프로그램 개발.
3. VLMs의 인과적 이해를 평가하기 위한 새로운 메트릭 개발.

# Citation Snippets
> Tang, T., Lin, Z., Feng, Z., Ma, T., Ong, Y.-S., Tsang, I., & Yin, H. (2026). Causal scaffolding for physical reasoning: A benchmark for causally-informed physical world understanding in VLMs. arXiv. https://arxiv.org/abs/2606.05966v1

tags: #causal_reasoning, #physical_reasoning, #vision_language_models, #causal_graphs, #benchmark, #AI, #machine_learning
