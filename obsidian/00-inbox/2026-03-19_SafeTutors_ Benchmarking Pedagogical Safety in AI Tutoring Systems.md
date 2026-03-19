# SafeTutors: Benchmarking Pedagogical Safety in AI Tutoring Systems

- Source: arxiv
- ID: http://arxiv.org/abs/2603.17373v1
- DOI: 명시되지 않음
- Published: 2026-03-18T05:33:50Z
- Authors: Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy
- Categories: cs.CL
- Link: https://arxiv.org/abs/2603.17373v1
- PDF: https://arxiv.org/pdf/2603.17373v1
- Keyword Score: 20

## Abstract
Large language models are rapidly being deployed as AI tutors, yet current evaluation paradigms assess problem-solving accuracy and generic safety in isolation, failing to capture whether a model is simultaneously pedagogically effective and safe across student-tutor interaction. We argue that tutoring safety is fundamentally different from conventional LLM safety: the primary risk is not toxic content but the quiet erosion of learning through answer over-disclosure, misconception reinforcement, and the abdication of scaffolding. To systematically study this failure mode, we introduce SafeTutors, a benchmark that jointly evaluates safety and pedagogy across mathematics, physics, and chemistry. SafeTutors is organized around a theoretically grounded risk taxonomy comprising 11 harm dimensions and 48 sub-risks drawn from learning-science literature. We uncover that all models show broad harm; scale doesn't reliably help; and multi-turn dialogue worsens behavior, with pedagogical failures rising from 17.7% to 77.8%. Harms also vary by subject, so mitigations must be discipline-aware, and single-turn "safe/helpful" results can mask systematic tutor failure over extended interaction.

## OpenAI Review
---
title: SafeTutors: Benchmarking Pedagogical Safety in AI Tutoring Systems
authors: [Rima Hazra, Bikram Ghuku, Ilona Marchenko, Yaroslava Tokarieva, Sayan Layek, Somnath Banerjee, Julia Stoyanovich, Mykola Pechenizkiy]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2603.17373v1
research_type: 실험적 연구
methodology: 벤치마크 개발 및 평가
data_type: 정량적 데이터
sample: 10개의 오픈 웨이트 LLMs (3.8B–72B) 및 1개의 블랙박스 LLM
context: 수학, 물리학, 화학 교육
theoretical_framework: 학습 과학 이론에 기반한 위험 분류 체계
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 AI 튜터 시스템의 교육적 안전성을 평가하기 위한 벤치마크인 SafeTutors를 소개한다. 기존의 평가 방식은 문제 해결 정확도와 일반적인 안전성을 개별적으로 평가하여, 모델이 학생-튜터 상호작용에서 교육적으로 효과적이고 안전한지를 포착하지 못하고 있다. 연구진은 안전한 튜터링이 전통적인 LLM 안전성과 근본적으로 다르며, 주된 위험은 유해한 내용이 아니라 학습의 침식이라고 주장한다. SafeTutors는 수학, 물리학, 화학을 포함한 교육적 맥락에서 안전성과 교육 효과성을 동시에 평가하는 체계를 제공하며, 11개의 위험 차원과 48개의 하위 위험으로 구성된 이론적으로 기반한 위험 분류 체계를 통해 이를 실현한다. 연구 결과, 모든 모델이 광범위한 해를 보이며, 다중 턴 대화에서 교육적 실패율이 17.7%에서 77.8%로 증가함을 발견하였다.

# Research Logic
## Problem
AI 튜터의 안전성과 교육적 효과성을 동시에 평가할 수 있는 체계의 부재.
## Theory
안전한 튜터링은 유해한 내용의 회피뿐만 아니라 교육적 효과성을 포함해야 한다는 이론적 주장.
## Design
SafeTutors 벤치마크는 11개의 위험 차원과 48개의 하위 위험을 포함하여 설계됨.
## Findings
모든 모델이 60% 이상의 해를 보이며, 다중 턴 대화에서 교육적 실패율이 급증함.
## Conclusion
AI 튜터의 평가에서 교육 지원과 해의 회피를 동시에 측정할 필요성이 강조됨.

# Key Findings
- 모든 모델이 최소 60%의 해를 보이며, 다중 턴 대화에서 교육적 실패율이 77.8%로 증가함.
- 모델의 규모가 안전성을 일관되게 개선하지 않음.
- 수학, 물리학, 화학 과목에 따라 해의 유형이 다르게 나타남.

# Contributions
## Theoretical
AI 튜터의 안전성과 교육적 효과성을 동시에 평가하는 새로운 이론적 틀 제공.
## Methodological
다중 턴 대화에서의 안전성과 교육적 효과성을 평가하는 벤치마크 개발.
## Practical
AI 튜터의 설계 및 평가에 있어 교육적 안전성을 고려해야 함을 강조.

# Limitations
- 연구는 특정 과목(수학, 물리학, 화학)에 국한됨.
- 다중 턴 대화의 복잡성을 완전히 반영하지 못할 수 있음.

# Transferable Insights
- AI 튜터의 설계 시 교육적 안전성을 고려해야 함.
- 다중 턴 대화에서의 상호작용이 교육적 결과에 미치는 영향을 분석할 필요가 있음.

# Idea Seeds
1. AI 튜터의 교육적 안전성을 평가하기 위한 추가적인 위험 차원 개발.
2. 다양한 학습 환경에서의 AI 튜터의 효과성 연구.
3. AI 튜터와 학생 간의 상호작용을 개선하기 위한 설계 원칙 제안.

# Citation Snippets
> Hazra, R., Ghuku, B., Marchenko, I., Tokarieva, Y., Layek, S., Banerjee, S., Stoyanovich, J., & Pechenizkiy, M. (2026). SafeTutors: Benchmarking Pedagogical Safety in AI Tutoring Systems. arXiv. https://arxiv.org/abs/2603.17373v1

tags: #human-ai collaboration, #ai tutoring, #instructional design, #scaffolding, #ai literacy, #education, #learning analytics
