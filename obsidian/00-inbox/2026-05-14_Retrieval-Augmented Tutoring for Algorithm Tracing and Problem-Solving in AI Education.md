# Retrieval-Augmented Tutoring for Algorithm Tracing and Problem-Solving in AI Education

- Source: arxiv
- ID: http://arxiv.org/abs/2605.12988v1
- DOI: 명시되지 않음
- Published: 2026-05-13T04:37:45Z
- Authors: Mragisha Jain, Tirth Bhatt, Griffin Pitts, Aum Pandya, Peter Brusilovsky, Narges Norouzi, Arto Hellas, Juho Leinonen, Bita Akram
- Categories: cs.AI, cs.CY, cs.IR
- Link: https://arxiv.org/abs/2605.12988v1
- PDF: https://arxiv.org/pdf/2605.12988v1
- Keyword Score: 25

## Abstract
Students learning algorithms often need support as they interpret traces, debug reasoning errors, and apply procedures across unfamiliar problem instances. In this paper, we present KITE (Knowledge-Informed Tutoring Engine), a Retrieval-Augmented Generation (RAG)-based intelligent tutoring system designed to serve as a classroom teaching assistant for algorithmic reasoning and problem-solving tasks. KITE uses an intent-aware Socratic response strategy to tailor support to different student needs, responding with targeted hints, guiding questions, and progressive scaffolding intended to strengthen students' algorithmic problem-solving ability. To keep responses aligned with course content, KITE uses a multimodal RAG pipeline that retrieves relevant information from course materials. We evaluate KITE using three forms of assessment: RAGAs-based metrics for response grounding and quality, expert evaluation of pedagogical quality, and a simulated student pipeline in which a weaker language model interacts with KITE across two-turn dialogues and produces revised answers after receiving feedback. Results indicate that KITE produces contextually grounded and pedagogically appropriate responses. Further, using simulated students, KITE's feedback helped the student models produce more accurate follow-up responses on procedural and tracing questions, suggesting that its scaffolding can support algorithmic problem-solving. This work contributes a tutoring architecture and an evaluation approach for assessing retrieval-grounded explanations and scaffolded problem-solving feedback.

## OpenAI Review
---
title: Retrieval-Augmented Tutoring for Algorithm Tracing and Problem-Solving in AI Education
authors: [Mragisha Jain, Tirth Bhatt, Griffin Pitts, Aum Pandya, Peter Brusilovsky, Narges Norouzi, Arto Hellas, Juho Leinonen, Bita Akram]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2605.12988v1
research_type: 실험적 연구
methodology: 혼합 방법론
data_type: 질적 및 양적 데이터
sample: 109개의 질문
context: 알고리즘 교육
theoretical_framework: 인지적 도제 이론, 소크라틱 교수법
keywords: [human-ai collaboration, ai tutoring, instructional design, scaffolding, ai literacy, education, learning analytics, ai pedagogy]
---

# APA 7th style

# Summary
이 연구에서는 알고리즘 교육을 위한 지식 기반 튜터링 시스템인 KITE(Knowledge-Informed Tutoring Engine)를 제안한다. KITE는 Retrieval-Augmented Generation(RAG) 방식을 활용하여 학생의 요구에 맞춘 지원을 제공하며, 알고리즘 문제 해결 능력을 강화하기 위한 목표로 소크라틱 응답 전략을 사용한다. 연구 결과, KITE는 맥락에 맞고 교육적으로 적절한 응답을 생성하며, 시뮬레이션된 학생 모델을 통해 피드백이 알고리즘 문제 해결에 긍정적인 영향을 미친다는 것을 보여준다. 이 연구는 튜터링 아키텍처와 평가 접근법을 제시하여 RAG 기반 설명 및 문제 해결 피드백을 평가하는 데 기여한다.

# Research Logic
## Problem
학생들이 알고리즘을 배우는 과정에서 추적 해석, 오류 디버깅 및 낯선 문제 인스턴스에 대한 절차 적용에 어려움을 겪는다.

## Theory
인지적 도제 이론과 소크라틱 교수법을 기반으로 하여 학생의 사고 과정을 지원하는 튜터링 시스템을 설계한다.

## Design
KITE는 다단계 다중 모드 검색 파이프라인과 의도 인식 응답 전략을 결합하여 학생의 질문에 맞는 적절한 피드백을 제공한다.

## Findings
KITE는 교육적 품질 평가에서 긍정적인 결과를 보였으며, 시뮬레이션된 학생 모델이 KITE의 피드백을 통해 더 정확한 후속 응답을 생성할 수 있었다.

## Conclusion
KITE는 알고리즘 문제 해결을 지원하는 효과적인 튜터링 시스템으로, 교육적 맥락에 적합한 피드백을 제공한다.

# Key Findings
- KITE는 맥락에 맞는 교육적 응답을 생성한다.
- KITE의 피드백은 학생 모델의 후속 응답 정확도를 향상시킨다.
- RAG 기반 메트릭을 통해 KITE의 응답 품질이 평가되었다.

# Contributions
## Theoretical
KITE는 인지적 도제 이론과 소크라틱 교수법을 통합하여 알고리즘 교육에 대한 새로운 접근 방식을 제시한다.

## Methodological
RAG 기반 메트릭을 활용한 새로운 평가 방법론을 제안한다.

## Practical
KITE는 교실에서 알고리즘 문제 해결을 지원하는 실용적인 도구로 활용될 수 있다.

# Limitations
- KITE의 성능은 특정 알고리즘 교육 맥락에 국한될 수 있다.
- 시뮬레이션된 학생 모델의 결과가 실제 학생의 행동을 완전히 반영하지 않을 수 있다.

# Transferable Insights
- 알고리즘 교육에서 AI 기반 튜터링 시스템의 필요성이 강조된다.
- 소크라틱 교수법을 활용한 피드백 제공의 중요성이 부각된다.

# Idea Seeds
1. KITE의 알고리즘을 다른 교육 분야에 적용할 수 있는 가능성 탐색.
2. KITE의 피드백 메커니즘을 개선하기 위한 사용자 경험 연구.
3. 다양한 학습 스타일에 맞춘 KITE의 응답 전략 개발.

# Citation Snippets
> Jain, M., Bhatt, T., Pitts, G., Pandya, A., Brusilovsky, P., Norouzi, N., Hellas, A., Leinonen, J., & Akram, B. (2026). Retrieval-Augmented Tutoring for Algorithm Tracing and Problem-Solving in AI Education. arXiv. https://arxiv.org/abs/2605.12988v1

tags: #human-ai collaboration, #ai tutoring, #instructional design, #scaffolding, #ai literacy, #education, #learning analytics, #ai pedagogy
