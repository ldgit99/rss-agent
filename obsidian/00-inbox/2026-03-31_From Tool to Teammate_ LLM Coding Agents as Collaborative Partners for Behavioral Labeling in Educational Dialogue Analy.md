# From Tool to Teammate: LLM Coding Agents as Collaborative Partners for Behavioral Labeling in Educational Dialogue Analysis

- Source: arxiv
- ID: http://arxiv.org/abs/2603.27440v1
- DOI: 명시되지 않음
- Published: 2026-03-28T23:04:36Z
- Authors: Eason Chen, Isabel Wang, Nina Yuan, Sophia Judicke, Kayla Beigh, Xinyi Tang
- Categories: cs.HC
- Link: https://arxiv.org/abs/2603.27440v1
- PDF: https://arxiv.org/pdf/2603.27440v1
- Keyword Score: 19

## Abstract
Behavioral analysis of tutoring dialogues is essential for understanding student learning, yet manual coding remains a bottleneck. We present a methodology where LLM coding agents autonomously improve the prompts used by LLM classifiers to label educational dialogues. In each iteration, a coding agent runs the classifier against human-labeled validation data, analyzes disagreements, and proposes theory-grounded prompt modifications for researcher review. Applying this approach to 659 AI tutoring sessions across four experiments with three agents and three classifiers, 4-fold cross-validation on held-out data confirmed genuine improvement: the best agent achieved test $κ=0.78$ (SD$=0.08$), matching human inter-rater reliability ($κ=0.78$), at a cost of approximately \$5--8 per agent. While development-set performance reached $κ=0.91$--$0.93$, the cross-validated results represent our primary generalization claim. The iterative process also surfaced an undocumented labeling pattern: human coders consistently treated expressions of confusion as engagement rather than disengagement. Continued iteration beyond the optimum led to regression, underscoring the need for held-out validation. We release all prompts, iteration logs, and data.

## OpenAI Review
---
title: From Tool to Teammate: LLM Coding Agents as Collaborative Partners for Behavioral Labeling in Educational Dialogue Analysis
authors: [Eason Chen, Isabel Wang, Nina Yuan, Sophia Judicke, Kayla Beigh, Xinyi Tang]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2603.27440v1
research_type: 실험적 연구
methodology: 반복적 개선 프로세스
data_type: 대화 데이터
sample: 659 AI 튜터링 세션
context: 대학교의 이산 수학 과정
theoretical_framework: 도움 요청 이론
keywords: [LLM labeling, behavioral analytics, prompt engineering, AI tutoring, educational data mining]
---

# APA 7th style

# Summary
본 연구는 교육 대화 분석에서 튜터링 대화의 행동 분석이 학생 학습 이해에 필수적임을 강조하며, LLM 코딩 에이전트가 교육 대화를 라벨링하는 데 있어 자율적으로 프롬프트를 개선하는 방법론을 제시한다. 659개의 AI 튜터링 세션을 대상으로 한 실험에서, 4배 교차 검증을 통해 최상의 에이전트가 테스트에서 $κ=0.78$ (SD$=0.08$)을 달성하여 인간 간의 일치도와 일치함을 확인하였다. 연구는 반복적 프로세스가 인간 코더가 혼란의 표현을 참여로 간주하는 패턴을 드러내는 등 중요한 통찰을 제공함을 보여준다. 최적 지점을 넘어서는 반복은 성능 저하를 초래할 수 있음을 강조하며, 모든 프롬프트와 반복 로그, 데이터를 공개하였다.

# Research Logic
## Problem
튜터링 대화의 행동 라벨링은 수작업으로 인한 병목 현상이 존재한다.
## Theory
도움 요청 이론을 기반으로 하여 학생의 행동을 분석한다.
## Design
LLM 코딩 에이전트가 자율적으로 프롬프트를 개선하는 반복적 프로세스를 설계하였다.
## Findings
최상의 에이전트는 $κ=0.78$을 달성하였으며, 인간 간의 일치도와 일치하였다.
## Conclusion
LLM 코딩 에이전트는 교육 대화의 라벨링을 개선할 수 있는 잠재력을 지니고 있으며, 반복적 개선이 성능 향상에 기여함을 보여준다.

# Key Findings
- LLM 코딩 에이전트는 자율적으로 프롬프트를 개선할 수 있다.
- 최상의 에이전트는 $κ=0.78$을 달성하여 인간 코더와의 일치도를 보였다.
- 반복적 프로세스에서 혼란의 표현이 참여로 간주되는 패턴이 드러났다.

# Contributions
## Theoretical
도움 요청 이론을 통해 행동 라벨링의 새로운 통찰을 제공하였다.
## Methodological
LLM 코딩 에이전트를 활용한 반복적 개선 프로세스를 제안하였다.
## Practical
교육 대화 분석의 효율성을 높이는 방법론을 제시하였다.

# Limitations
- 반복적 개선이 항상 성능 향상을 보장하지 않는다.
- 특정 에이전트의 성능 차이가 존재할 수 있다.

# Transferable Insights
- LLM 코딩 에이전트의 자율적 개선 가능성은 다양한 교육 환경에 적용될 수 있다.
- 반복적 오류 분석이 교육 데이터 라벨링의 품질을 향상시킬 수 있다.

# Idea Seeds
1. LLM 코딩 에이전트를 활용한 다양한 교육 대화 분석 연구.
2. 다른 교육 환경에서의 LLM 기반 라벨링 시스템 개발.
3. 반복적 개선 프로세스의 최적화 연구.

# Citation Snippets
> Chen, E., Wang, I., Yuan, N., Judicke, S., Beigh, K., & Tang, X. (2026). From Tool to Teammate: LLM Coding Agents as Collaborative Partners for Behavioral Labeling in Educational Dialogue Analysis. arXiv. https://arxiv.org/abs/2603.27440v1

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy
