# SHAPE: Unifying Safety, Helpfulness and Pedagogy for Educational LLMs

- Source: arxiv
- ID: http://arxiv.org/abs/2604.22134v1
- DOI: 명시되지 않음
- Published: 2026-04-24T00:39:08Z
- Authors: Sihang, Zhao, Kangrui Yu, Youliang Yuan, Pinjia He, Hongyi Wen
- Categories: cs.CL
- Link: https://arxiv.org/abs/2604.22134v1
- PDF: https://arxiv.org/pdf/2604.22134v1
- Keyword Score: 23

## Abstract
Large Language Models (LLMs) have been widely explored in educational scenarios. We identify a critical vulnerability in current educational LLMs, pedagogical jailbreaks, where students use answer-inducing prompts to elicit solutions rather than scaffolded instructions. To enable systematic study, we unify and formalize safe, helpful, and pedagogical behaviors with a knowledge-mastery graph and introduce SHAPE, a benchmark of 9,087 student-question pairs for evaluating tutoring behavior under adversarial pressure. We propose a graph-augmented tutoring pipeline that infers prerequisite concepts from queries, identifies mastery gaps, and routes generation between instructing and problem-solving via explicit gating. Experiments across multiple LLMs show that our method yields significantly improved safety under two pedagogical jailbreak settings, while maintaining near-ceiling helpfulness under the same evaluation protocol. Our code and data are available at https://github.com/MAPS-research/SHaPE

## OpenAI Review
---
title: SHAPE: Unifying Safety, Helpfulness and Pedagogy for Educational LLMs
authors: [Sihang Zhao, Kangrui Yu, Youliang Yuan, Pinjia He, Hongyi Wen]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.22134v1
research_type: 실험적 연구
methodology: 그래프 기반 튜터링 파이프라인
data_type: 데이터셋
sample: 9,087 학생-질문 쌍
context: 교육적 LLM의 안전성 및 교육적 행동 평가
theoretical_framework: 지식-숙달 그래프
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 교육적 대형 언어 모델(LLM)의 안전성, 유용성 및 교육적 행동을 통합하는 SHAPE라는 벤치마크를 제안한다. 연구자들은 학생들이 답변 유도 프롬프트를 사용하여 해결책을 이끌어내는 '교육적 탈옥'이라는 취약점을 식별하였다. SHAPE는 9,087개의 학생-질문 쌍으로 구성되어 있으며, 교육적 LLM의 튜터링 행동을 평가하는 데 사용된다. 실험 결과, 제안된 방법은 두 가지 교육적 탈옥 설정에서 안전성을 크게 개선하면서도 유용성을 유지하는 것으로 나타났다. 연구 결과는 교육적 LLM의 안전성과 교육적 행동을 평가하는 데 기여할 수 있다.

# Research Logic
## Problem
교육적 LLM의 안전성과 유용성 간의 균형을 맞추는 것이 어렵다.
## Theory
지식-숙달 그래프를 기반으로 한 교육적 행동의 정의와 평가.
## Design
그래프 기반 튜터링 파이프라인을 설계하여 학생의 질문에 대한 적절한 반응을 생성.
## Findings
제안된 방법이 기존 모델보다 안전성과 유용성을 동시에 개선함을 발견.
## Conclusion
SHAPE 벤치마크는 교육적 LLM의 평가에 있어 중요한 도구가 될 수 있다.

# Key Findings
- 교육적 LLM의 안전성을 평가하기 위한 SHAPE 벤치마크를 개발.
- 기존 모델은 교육적 탈옥 공격에 취약함을 확인.
- 제안된 그래프 기반 튜터링 파이프라인이 안전성과 유용성을 동시에 개선함.

# Contributions
## Theoretical
교육적 LLM의 안전성 및 교육적 행동에 대한 통합된 정의 제공.
## Methodological
SHAPE 벤치마크를 통해 교육적 LLM의 평가 방법론 제안.
## Practical
교육적 LLM의 안전성과 유용성을 동시에 고려한 튜터링 시스템 설계 가능성 제시.

# Limitations
- 특정 교육적 맥락에서의 적용 가능성에 대한 제한.
- 데이터셋의 다양성이 부족할 수 있음.

# Transferable Insights
- 교육적 LLM의 안전성과 유용성을 동시에 고려해야 함.
- 지식-숙달 그래프를 활용한 개인화된 교육적 접근의 필요성.

# Idea Seeds
1. 다양한 교육적 맥락에서 SHAPE 벤치마크의 적용 가능성 탐색.
2. 다른 주제 영역에 대한 교육적 LLM의 튜터링 행동 평가.
3. 학생의 인지 상태에 따른 맞춤형 튜터링 시스템 개발.

# Citation Snippets
> Zhao, S., Yu, K., Yuan, Y., He, P., & Wen, H. (2026). SHAPE: Unifying Safety, Helpfulness and Pedagogy for Educational LLMs. arXiv. https://arxiv.org/abs/2604.22134v1

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy
