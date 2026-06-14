# Fix the Mind, Not the Move: Interpretable AI Assistance via Knowledge-Gap Localization

- Source: arxiv
- ID: http://arxiv.org/abs/2606.05602v1
- DOI: 명시되지 않음
- Published: 2026-06-04T02:25:19Z
- Authors: Ayano Hiranaka, Ya-Chuan Hsu, Stefanos Nikolaidis, Erdem Bıyık, Daniel Seita
- Categories: cs.AI, cs.HC, cs.LG
- Link: https://arxiv.org/abs/2606.05602v1
- PDF: https://arxiv.org/pdf/2606.05602v1
- Keyword Score: 6

## Abstract
AI assistants in human-AI collaboration often correct suboptimal human actions through behavioral feedback (e.g., alerts or steering-wheel nudges in assistive driving). Such interventions can mitigate immediate errors, but long-term improvement requires addressing the underlying misconceptions that cause repeated mistakes. We introduce SENSEI, a framework that infers user misconceptions from interaction behavior and provides targeted, minimal yet sufficient suggestions to correct them. Our approach departs from action- or trajectory-level interventions by operating over a structured knowledge representation to localize and correct the sources of erroneous behavior. Across three long-horizon tasks with diverse misconceptions and corresponding behaviors, SENSEI demonstrates zero-shot compositional generalization, disentangling multiple overlapping misconceptions despite training only on single-misconception cases. A user study further shows that our method identifies real human misconceptions and provides effective guidance that improves long-horizon task performance, successfully correcting $90\%$ of student misconceptions. Code and project page are available at https://misoshiruseijin.github.io/SENSEI/.

## OpenAI Review
---
title: Fix the Mind, Not the Move: Interpretable AI Assistance via Knowledge-Gap Localization
authors: [Ayano Hiranaka, Ya-Chuan Hsu, Stefanos Nikolaidis, Erdem Bıyık, Daniel Seita]
year: 2026
journal: Proceedings of the 43rd International Conference on Machine Learning
doi: https://arxiv.org/abs/2606.05602v1
research_type: 실험적 연구
methodology: 사용자 연구 및 실험적 검증
data_type: 행동 데이터
sample: 20명 사용자
context: AI 보조 시스템의 인간-기계 협력
theoretical_framework: 지식 격차 이론
keywords: [human-ai collaboration, ai tutoring, instructional design, scaffolding, ai literacy, education, learning analytics, ai pedagogy]
---

# APA 7th style

# Summary
본 연구에서는 인간-기계 협력에서 AI 보조 시스템이 사용자의 오해를 진단하고 이를 교정하기 위한 SENSEI 프레임워크를 제안한다. SENSEI는 사용자의 상호작용 행동을 분석하여 지식 격차를 파악하고, 이를 바탕으로 최소한의 수정 제안을 제공한다. 연구 결과, SENSEI는 90%의 학생 오해를 성공적으로 교정하며, 장기적인 작업 성과를 향상시키는 데 기여함을 보여준다. 이 연구는 AI 보조 시스템의 지식 기반 지원의 필요성을 강조하며, 행동 수정이 아닌 지식 수정의 중요성을 부각시킨다.

# Research Logic
## Problem
AI 보조 시스템이 사용자의 오해를 해결하지 않고 단기적인 행동 수정에만 집중하는 문제.
## Theory
지식 격차 이론을 바탕으로, 사용자의 오해를 진단하고 교정하는 것이 장기적인 성과 향상에 필수적임을 주장.
## Design
SENSEI 프레임워크를 통해 사용자의 행동 데이터를 분석하고, 지식 격차를 파악하여 교정 제안을 생성.
## Findings
SENSEI는 90%의 오해를 교정하며, 사용자 연구를 통해 실제 인간 오해를 효과적으로 진단하고 교정할 수 있음을 입증.
## Conclusion
AI 보조 시스템은 행동 수정뿐만 아니라 지식 수정을 통해 사용자의 장기적인 성과를 향상시킬 수 있다.

# Key Findings
- SENSEI는 사용자의 행동 데이터를 기반으로 지식 격차를 효과적으로 진단함.
- 90%의 학생 오해를 성공적으로 교정함.
- 장기적인 작업 성과 향상에 기여함.

# Contributions
## Theoretical
지식 격차 이론을 기반으로 한 AI 보조 시스템의 필요성을 강조.
## Methodological
구조화된 지식 진단 및 교정 방법론을 제안.
## Practical
AI 보조 시스템의 실제 적용 가능성을 보여주며, 교육 현장에서의 활용 가능성을 제시.

# Limitations
- 연구 샘플이 20명으로 제한되어 일반화에 한계가 있음.
- 특정 작업에 국한된 결과로, 다양한 도메인에 대한 검증이 필요함.

# Transferable Insights
- AI 보조 시스템은 행동 수정뿐만 아니라 지식 교정의 중요성을 인식해야 함.
- 사용자 행동 데이터를 기반으로 한 지식 진단이 효과적임을 보여줌.

# Idea Seeds
1. 다양한 도메인에서 SENSEI 프레임워크의 적용 가능성 탐색.
2. AI 보조 시스템의 사용자 경험 개선을 위한 추가 연구.
3. 지식 격차 진단을 위한 새로운 알고리즘 개발.

# Citation Snippets
> Hiranaka, A., Hsu, Y.-C., Nikolaidis, S., Bıyık, E., & Seita, D. (2026). Fix the Mind, Not the Move: Interpretable AI Assistance via Knowledge-Gap Localization. Proceedings of the 43rd International Conference on Machine Learning.

tags: #human-ai collaboration, #ai tutoring, #instructional design, #scaffolding, #ai literacy, #education, #learning analytics, #ai pedagogy
