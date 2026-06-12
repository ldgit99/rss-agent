# Hey Chat, Can You Teach Me? Structuring Socratic Dialogue for Human Learning in the Wild

- Source: arxiv
- ID: http://arxiv.org/abs/2606.11744v1
- DOI: 명시되지 않음
- Published: 2026-06-10T07:20:59Z
- Authors: Sidney Tio, Arunesh Sinha, Pradeep Varakantham
- Categories: cs.CL, cs.AI
- Link: https://arxiv.org/abs/2606.11744v1
- PDF: https://arxiv.org/pdf/2606.11744v1
- Keyword Score: 15

## Abstract
Large language models are now widely used for everyday learning, but the underlying interactions are typically unstructured chats rather than following a curriculum. Unlike formal online learning systems, these interactions carry no prior record of the student, so any estimate of what the student already knows must be inferred from the dialogue itself. We show that this gap is not closed by scaling models alone. Frontier and education-tuned LLMs perform poorly when asked to tutor a student over an extended session, because doing so requires three things at once. The tutor must sequence a curriculum, conduct Socratic dialogue, and infer the student's knowledge state from that dialogue. We propose separating these responsibilities. Given a student query, our system constructs a prerequisite knowledge graph in which subtopics are nodes and dependencies are edges, and frames tutoring as deciding which node to teach next and how many dialogue turns to spend on it before moving on. A lightweight PPO policy handles this sequencing decision, while an LLM conducts the Socratic exchange at the chosen node and returns a signal of student progress. Across held-out STEM and non-STEM topics, our PPO-paired tutor outperforms heuristic baselines, frontier general-purpose models, and a model specialised for Socratic dialogue: on both the rate at which students reach full curriculum mastery and the number of turns required. Explicit curriculum structure delivers gains that scaling the underlying model does not.

## OpenAI Review
---
title: Hey Chat, Can You Teach Me? Structuring Socratic Dialogue for Human Learning in the Wild
authors: [Sidney Tio, Arunesh Sinha, Pradeep Varakantham]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2606.11744v1
research_type: 실험적 연구
methodology: 강화 학습 기반 시스템
data_type: 대화 데이터
sample: STEM 및 비-STEM 주제
context: 비구조적 학습 환경
theoretical_framework: 소크라틱 대화, 지식 그래프
keywords: [human-ai collaboration, ai tutoring, instructional design, scaffolding, ai literacy, education, learning analytics, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 대규모 언어 모델(LLM)이 비구조적 대화를 통해 학습을 지원하는 방식의 한계를 분석하고, 이를 해결하기 위한 새로운 튜터링 시스템을 제안한다. 기존의 LLM은 학생의 지식 상태를 추론하고 커리큘럼을 구성하는 데 어려움을 겪는다. 연구진은 학생의 질문을 기반으로 지식 그래프를 생성하고, 이를 통해 커리큘럼의 순서를 결정하는 경량화된 정책을 도입하였다. 이 시스템은 소크라틱 대화를 통해 학생의 이해도를 평가하고, STEM 및 비-STEM 주제에서 기존 모델보다 우수한 성과를 보였다. 명시된 커리큘럼 구조는 모델의 크기를 확장하는 것만으로는 얻을 수 없는 성과를 제공한다.

# Research Logic
## Problem
대규모 언어 모델이 비구조적 대화에서 학생의 지식 상태를 추론하고 커리큘럼을 효과적으로 구성하는 데 어려움이 있다.

## Theory
소크라틱 대화와 지식 그래프를 활용하여 학생의 이해도를 평가하고, 커리큘럼의 순서를 결정하는 새로운 접근 방식을 제안한다.

## Design
학생의 질문을 기반으로 지식 그래프를 생성하고, 강화 학습을 통해 커리큘럼 순서를 결정하는 경량화된 정책을 개발하였다.

## Findings
제안된 시스템은 기존의 휴리스틱 기준선 및 일반 목적 모델보다 학생의 커리큘럼 마스터리 속도와 대화 턴 수에서 우수한 성과를 보였다.

## Conclusion
명시된 커리큘럼 구조는 LLM의 성능을 향상시키며, 비구조적 학습 환경에서 효과적인 튜터링을 가능하게 한다.

# Key Findings
- 제안된 시스템은 학생의 질문을 기반으로 지식 그래프를 생성하여 커리큘럼을 구성한다.
- 소크라틱 대화를 통해 학생의 이해도를 평가하고, 이를 바탕으로 다음 학습 주제를 결정한다.
- 기존의 LLM보다 학생의 커리큘럼 마스터리 속도가 향상되었다.

# Contributions
## Theoretical
소크라틱 대화와 지식 그래프를 활용한 새로운 튜터링 모델을 제안하였다.

## Methodological
강화 학습 기반의 경량화된 정책을 통해 커리큘럼 순서를 결정하는 방법론을 개발하였다.

## Practical
비구조적 학습 환경에서 LLM을 활용한 효과적인 튜터링 시스템을 구현하였다.

# Limitations
- 연구는 특정 STEM 및 비-STEM 주제에 국한되어 있다.
- 시스템의 일반화 가능성에 대한 추가 연구가 필요하다.

# Transferable Insights
- 지식 그래프를 활용한 커리큘럼 구성 방식은 다양한 교육 환경에 적용 가능하다.
- 소크라틱 대화 방식은 학생의 이해도를 평가하는 데 효과적이다.

# Idea Seeds
1. 다양한 주제에 대한 지식 그래프를 확장하여 시스템의 적용 범위를 넓힐 수 있다.
2. 소크라틱 대화의 효과를 평가하기 위한 실험적 연구를 진행할 수 있다.
3. LLM의 성능을 향상시키기 위한 추가적인 커리큘럼 구조 연구를 수행할 수 있다.

# Citation Snippets
> Tio, S., Sinha, A., & Varakantham, P. (2026). Hey Chat, Can You Teach Me? Structuring Socratic Dialogue for Human Learning in the Wild. arXiv. https://arxiv.org/abs/2606.11744v1

tags: #human-ai collaboration, #ai tutoring, #instructional design, #scaffolding, #ai literacy, #education, #learning analytics, #ai pedagogy
