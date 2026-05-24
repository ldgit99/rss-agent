# Exploring the Effectiveness of Using LLMs for Automated Assessment of Student Self Explanations in Programming Education

- Source: arxiv
- ID: http://arxiv.org/abs/2605.21614v1
- DOI: 명시되지 않음
- Published: 2026-05-20T18:22:22Z
- Authors: Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky
- Categories: cs.HC, cs.LG
- Link: https://arxiv.org/abs/2605.21614v1
- PDF: https://arxiv.org/pdf/2605.21614v1
- Keyword Score: 16

## Abstract
Worked examples are step-by-step solutions to problems in a specific domain, offered to students to acquire domain-specific problem-solving skills. The effectiveness of worked examples could be enhanced by combining them with self-explanations, which ask students to explain rather than passively study each problem-solving step. The main challenge of this approach is assessing the correctness of the student's explanations. In the prevailing approach, student explanations are judged by their semantic similarity to an instructor's or domain expert's explanation. Given recent advances in LLM-based automated scoring, it remains unclear whether semantic similarity methods are still the most effective technique to automatically score textual student responses like essays or code explanations. Comparing these methods also requires quality datasets that offer distinctive features such as balanced class distributions and domain-specific labeled data for automated scoring tasks. In this paper, we present a rigorous comparison between LLMs and semantic similarity used for automated scoring, framed as a binary classification task.

## OpenAI Review
---
title: LLM을 활용한 프로그래밍 교육에서 학생 자기 설명의 자동 평가 효과 탐색
authors: [Arun-Balajiee Lekshmi-Narayanan, Mohammad Hassany, Peter Brusilovsky]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2605.21614v1
research_type: 실험 연구
methodology: 비교 연구
data_type: 텍스트 데이터
sample: 1854쌍의 학생 및 전문가 설명
context: 프로그래밍 교육
theoretical_framework: ICAP 프레임워크
keywords: [human-ai collaboration, ai tutoring, instructional design, scaffolding, ai literacy, education, learning analytics, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 LLM(대형 언어 모델)을 활용하여 프로그래밍 교육에서 학생의 자기 설명을 자동으로 평가하는 방법의 효과를 비교하였다. 연구는 학생의 설명이 전문가의 설명과 얼마나 유사한지를 평가하는 기존의 의미적 유사성 방법과 LLM 기반 방법을 비교하는 이진 분류 작업으로 구성되었다. 연구 결과, LLM 기반 평가 방법이 의미적 유사성 방법보다 높은 정확도(96%)와 F1 점수(0.98)를 기록하여 더 우수한 성능을 보였다. 이는 LLM이 학생의 설명을 평가하는 데 있어 더 효과적인 대안이 될 수 있음을 시사한다.

# Research Logic
## Problem
학생의 자기 설명을 평가하는 데 있어 기존의 의미적 유사성 방법의 한계.
## Theory
ICAP 프레임워크에 기반하여 능동적 학습의 중요성을 강조.
## Design
LLM과 의미적 유사성 방법을 비교하는 이진 분류 작업으로 설계.
## Findings
LLM 기반 방법이 의미적 유사성 방법보다 높은 성능을 보임.
## Conclusion
LLM이 학생의 설명 평가에 있어 더 효과적인 방법이 될 수 있음.

# Key Findings
- LLM 기반 평가의 F1 점수는 0.98, 정확도는 0.96으로 나타남.
- 의미적 유사성 방법의 F1 점수는 0.72, 정확도는 0.65로 낮음.
- LLM 방법이 학생의 설명을 더 정확하게 평가함.

# Contributions
## Theoretical
LLM의 교육적 활용 가능성을 제시.
## Methodological
자동 평가를 위한 새로운 데이터셋 생성 방법론 제안.
## Practical
학생의 자기 설명 평가에 있어 LLM의 적용 가능성을 보여줌.

# Limitations
- 기존 데이터셋의 전문가 평가 간 변동성 문제.
- LLM 기반 평가의 일반화 가능성에 대한 추가 연구 필요.

# Transferable Insights
- LLM을 활용한 자동 평가 시스템의 필요성.
- 교육 데이터셋의 품질 향상을 위한 합성 데이터 생성의 중요성.

# Idea Seeds
1. 다양한 프로그래밍 언어에 대한 LLM 평가 방법 확장.
2. LLM을 활용한 학생 피드백 생성 시스템 개발.
3. LLM의 평가 성능을 개선하기 위한 프롬프트 최적화 연구.

# Citation Snippets
> Lekshmi-Narayanan, A.-B., Hassany, M., & Brusilovsky, P. (2026). Exploring the Effectiveness of Using LLMs for Automated Assessment of Student Self Explanations in Programming Education. arXiv.

tags: #human-ai collaboration, #ai tutoring, #instructional design, #scaffolding, #ai literacy, #education, #learning analytics, #ai pedagogy
