# Three Roles, One Model: Role Orchestration at Inference Time to Close the Performance Gap Between Small and Large Agents

- Source: arxiv
- ID: http://arxiv.org/abs/2604.11465v2
- DOI: 명시되지 않음
- Published: 2026-04-13T13:40:33Z
- Authors: S. Aaron McClendon, Jorge Gallego-Feliciano, Stavros Zervoudakis, Antonios Saravanos
- Categories: cs.AI
- Link: https://arxiv.org/abs/2604.11465v2
- PDF: https://arxiv.org/pdf/2604.11465v2
- Keyword Score: 8

## Abstract
Large language model (LLM) agents show promise on realistic tool-use tasks, but deploying capable agents on modest hardware remains challenging. We study whether inference-time scaffolding alone, without any additional training compute, can improve the performance of a small model in complex multi-step environments. Operating on a single 24GB GPU, we evaluate Qwen3-8B on the AppWorld benchmark under both full-precision and 4-bit quantized configurations. Without any intervention, the raw model achieves just 5.4% (FP16) and 3.0% (AWQ) task goal completion. Guided by a systematic failure mode analysis, we introduce a three-tier inference scaffolding pipeline that deploys the same frozen model in three distinct roles: (1) a summarization model that preserves critical artifacts (tokens, credentials, API responses) while compressing dialogue history; (2) the main agent model that reasons over the compressed context; and (3) an isolated correction model that reviews and revises the agent's code output without access to conversation history, breaking repetitive failure loops. Applied to the same unmodified model, this scaffolding yields 8.9% (FP16) and 5.9% (AWQ) task goal completion, roughly doubling performance in both settings, with particularly strong gains on difficulty-1 tasks (15.8% to 26.3% FP16; 5.3% to 14.0% AWQ). On full-precision inference, our scaffolded 8B model surpasses DeepSeek-Coder 33B Instruct (7.1%) from the original AppWorld evaluation, demonstrating that structured inference-time interventions can make small models competitive with systems 4 times their size. We formalize the approach as a scaffolded policy over a frozen base model, three invocations of the same weights with different conditioning, drawing connections to test-time compute scaling and action-space shaping in reinforcement learning.

## OpenAI Review
---
title: Three Roles, One Model: Role Orchestration at Inference Time to Close the Performance Gap Between Small and Large Agents
authors: [S. Aaron McClendon, Jorge Gallego-Feliciano, Stavros Zervoudakis, Antonios Saravanos]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.11465v2
research_type: 실험적 연구
methodology: 세 가지 역할의 추론 시간 스캐폴딩 파이프라인 설계 및 평가
data_type: 성능 평가 데이터
sample: Qwen3-8B 모델
context: AppWorld 벤치마크
theoretical_framework: 추론 시간 구조의 효과
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
이 연구는 대형 언어 모델(LLM) 에이전트의 성능 격차를 줄이기 위해 작은 모델의 추론 시간 스캐폴딩을 평가한다. Qwen3-8B 모델을 AppWorld 벤치마크에서 평가한 결과, 기본 모델은 FP16에서 5.4%, AWQ에서 3.0%의 작업 목표 달성률을 보였다. 그러나 세 가지 역할을 가진 스캐폴딩 파이프라인을 적용한 후 FP16에서 8.9%, AWQ에서 5.9%로 성능이 향상되었다. 특히 난이도 1 작업에서 두 배 이상의 성능 향상이 나타났다. 이 연구는 작은 모델이 구조화된 추론 시간 개입을 통해 대형 모델과 경쟁할 수 있음을 보여준다.

# Research Logic
## Problem
작은 모델이 복잡한 다단계 환경에서 성능을 발휘하지 못하는 문제.
## Theory
추론 시간 스캐폴딩이 작은 모델의 성능을 향상시킬 수 있다는 이론.
## Design
세 가지 역할(요약 모델, 주 에이전트 모델, 수정 모델)을 가진 스캐폴딩 파이프라인 설계.
## Findings
스캐폴딩을 통해 성능이 FP16에서 5.4%에서 8.9%로, AWQ에서 3.0%에서 5.9%로 증가.
## Conclusion
구조화된 추론 시간 개입이 작은 모델을 대형 모델과 경쟁 가능하게 만든다는 결론.

# Key Findings
- 스캐폴딩을 통해 FP16에서 8.9%, AWQ에서 5.9%의 작업 목표 달성률을 기록.
- 난이도 1 작업에서 성능이 FP16에서 15.8%에서 26.3%로 증가.
- 스캐폴딩된 8B 모델이 DeepSeek-Coder 33B Instruct(7.1%)를 초과하는 성과를 보임.

# Contributions
## Theoretical
작은 모델의 실패 모드를 실증적으로 분석하고, 추론 시간 구조의 중요성을 강조.
## Methodological
추론 시간 스캐폴딩을 위한 진단 중심 설계 방법론 제시.
## Practical
소비자 등급 하드웨어에서 작은 모델의 성능을 실질적으로 향상시키는 방법 제공.

# Limitations
- 통계적으로 유의미한 차이가 발견되지 않음.
- 모델의 크기와 성능 간의 관계를 완전히 설명하지 못함.

# Transferable Insights
- 작은 모델의 성능 향상을 위한 추론 시간 개입의 가능성.
- 구조화된 추론 시간 접근 방식이 다양한 환경에 적용될 수 있음.

# Idea Seeds
1. 다양한 스캐폴딩 전략을 적용한 다른 모델의 성능 비교 연구.
2. 교육 환경에서 AI 모델의 역할을 확장하는 방법 탐색.
3. 추론 시간 스캐폴딩의 효과를 다른 벤치마크에 적용해 보는 연구.

# Citation Snippets
> McClendon, S. A., Gallego-Feliciano, J., Zervoudakis, S., & Saravanos, A. (2026). Three Roles, One Model: Role Orchestration at Inference Time to Close the Performance Gap Between Small and Large Agents. arXiv. https://arxiv.org/abs/2604.11465v2

tags: #human-ai collaboration, #ai tutoring, #instructional design, #scaffolding, #ai literacy, #education, #learning analytics

---

짧은 요약: 이 연구는 작은 모델의 성능을 향상시키기 위한 추론 시간 스캐폴딩을 평가하였다. Qwen3-8B 모델을 AppWorld 벤치마크에서 테스트한 결과, 스캐폴딩을 통해 FP16에서 8.9%, AWQ에서 5.9%의 작업 목표 달성률을 기록하며 성능이 두 배 이상 향상되었다. 이 연구는 작은 모델이 구조화된 개입을 통해 대형 모델과 경쟁할 수 있음을 보여준다.
