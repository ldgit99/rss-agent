# Enhancing LLM Problem Solving via Tutor-Student Multi-Agent Interaction

- Source: arxiv
- ID: http://arxiv.org/abs/2604.08931v1
- DOI: 명시되지 않음
- Published: 2026-04-10T03:56:49Z
- Authors: Nurullah Eymen Özdemir, Erhan Oztop
- Categories: cs.AI, cs.MA
- Link: https://arxiv.org/abs/2604.08931v1
- PDF: https://arxiv.org/pdf/2604.08931v1
- Keyword Score: 13

## Abstract
Human cognitive development is shaped not only by individual effort but by structured social interaction, where role-based exchanges such as those between a tutor and a learner, enable solutions that neither could achieve alone. Inspired by these developmental principles, we ask the question whether a tutor-student multi-agent system can create a synergistic effect by pushing Large Language Model (LLM) beyond what it can do within existing frameworks. To test the idea, we adopt autonomous coding problem domain where two agents instantiated from the same LLM assigned asymmetric roles: a student agent generates and iteratively refines solutions, while a tutor agent provides structured evaluative feedback without access to ground-truth answers. In our proposed framework (PETITE), we aim to extract better problem-solving performance from one model by structuring its interaction through complementary roles, rather than relying on stronger supervisory models or heterogeneous ensembles. Our model is evaluated on the APPS coding benchmark against state-of-the-art approaches of Self-Consistency, Self-Refine, Multi-Agent Debate, and Multi-Agent Review. The results show that our model achieves similar or higher accuracy while consuming significantly fewer tokens. These results suggest that developmentally grounded role-differentiated interaction structures provide a principled and resource-efficient paradigm for enhancing LLM problem-solving through structured peer-like interactions. Index Terms- Peer Tutoring, Scaffolding, Large Language Models, Multi-Agent Systems, Code Generation

## OpenAI Review
---
title: LLM 문제 해결 향상을 위한 튜터-학생 다중 에이전트 상호작용
authors: Nurullah Eymen Özdemir, Erhan Oztop
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.08931v1
research_type: 실험적 연구
methodology: 다중 에이전트 시스템
data_type: 코드 생성 문제
sample: APPS 벤치마크의 100개 문제
context: 자율 코드 생성
theoretical_framework: 발달 이론, 동료 튜터링 이론
keywords: [peer tutoring, scaffolding, large language models, multi-agent systems, code generation]
---

# APA 7th style

# Summary
이 연구는 튜터-학생 다중 에이전트 시스템이 대형 언어 모델(LLM)의 문제 해결 능력을 향상시킬 수 있는지를 탐구한다. 연구진은 학생 에이전트가 솔루션을 생성하고 반복적으로 개선하는 역할을 맡고, 튜터 에이전트가 구조화된 피드백을 제공하는 비대칭 역할을 부여하였다. 제안된 PETITE 프레임워크는 APPS 코딩 벤치마크에서 기존의 방법들과 비교하여 유사하거나 더 높은 정확도를 달성하면서도 토큰 소비를 크게 줄이는 성과를 보였다. 이러한 결과는 발달 이론에 기반한 역할 차별화 상호작용 구조가 LLM 문제 해결을 향상시키는 데 효과적임을 시사한다.

# Research Logic
## Problem
LLM의 문제 해결 성능이 기존 방법론에 비해 낮은 문제를 해결하고자 함.
## Theory
발달 이론과 동료 튜터링 이론을 기반으로 한 비대칭 역할의 상호작용 구조가 효과적일 것이라는 가설.
## Design
학생 에이전트와 튜터 에이전트의 비대칭 역할을 가진 다중 에이전트 시스템을 설계.
## Findings
PETITE 프레임워크가 기존의 Self-Consistency, Self-Refine, Multi-Agent Debate, Multi-Agent Review 방법보다 유사하거나 더 높은 정확도를 보이며, 토큰 소비를 줄임.
## Conclusion
발달 이론에 기반한 역할 차별화 상호작용이 LLM의 문제 해결 성능을 향상시키는 유효한 방법임을 확인.

# Key Findings
- PETITE 프레임워크는 비대칭 역할을 통해 LLM의 문제 해결 성능을 향상시킴.
- 기존 방법들보다 유사하거나 더 높은 정확도를 달성하였음.
- 토큰 소비를 현저히 줄이는 성과를 보임.

# Contributions
## Theoretical
발달 이론과 동료 튜터링 이론을 LLM에 적용한 새로운 이론적 기여.
## Methodological
비대칭 역할을 통한 다중 에이전트 시스템의 설계 및 구현.
## Practical
효율적인 코드 생성 및 피드백 제공을 통한 교육적 활용 가능성 제시.

# Limitations
- 연구는 APPS 벤치마크에 국한되어 있어 일반화 가능성에 한계가 있음.
- 비대칭 역할의 효과를 다른 도메인에 적용한 연구가 필요함.

# Transferable Insights
- 비대칭 역할의 상호작용 구조가 다른 AI 시스템에도 적용 가능할 수 있음.
- 발달 이론을 기반으로 한 교육적 접근이 AI 튜터링 시스템에 유용할 수 있음.

# Idea Seeds
1. PETITE 프레임워크를 다른 문제 해결 도메인에 적용하여 효과를 검증.
2. 비대칭 역할의 상호작용을 통해 다양한 학습 환경에서의 효과 분석.
3. LLM의 피드백 메커니즘을 개선하기 위한 추가 연구.

# Citation Snippets
> Özdemir, N. E., & Oztop, E. (2026). Enhancing LLM Problem Solving via Tutor-Student Multi-Agent Interaction. arXiv. https://arxiv.org/abs/2604.08931v1

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy

---

이 연구는 LLM의 문제 해결 성능을 향상시키기 위한 튜터-학생 다중 에이전트 시스템의 효과를 탐구하며, 비대칭 역할의 상호작용이 성과를 높일 수 있음을 보여준다. APPS 벤치마크에서의 실험을 통해 기존 방법보다 높은 정확도와 낮은 토큰 소비를 달성하였다.
