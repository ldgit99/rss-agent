# Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation

- Source: arxiv
- ID: http://arxiv.org/abs/2603.15547v1
- DOI: 명시되지 않음
- Published: 2026-03-16T17:09:41Z
- Authors: Yanick Zengaffinen, Andreas Opedal, Donya Rooein, Kv Aditya Srivatsa, Shashank Sonkar, Mrinmaya Sachan
- Categories: cs.CL, cs.AI, cs.HC
- Link: https://arxiv.org/abs/2603.15547v1
- PDF: https://arxiv.org/pdf/2603.15547v1
- Keyword Score: 13

## Abstract
Modeling plausible student misconceptions is critical for AI in education. In this work, we examine how large language models (LLMs) reason about misconceptions when generating multiple-choice distractors, a task that requires modeling incorrect yet plausible answers by coordinating solution knowledge, simulating student misconceptions, and evaluating plausibility. We introduce a taxonomy for analyzing the strategies used by state-of-the-art LLMs, examining their reasoning procedures and comparing them to established best practices in the learning sciences. Our structured analysis reveals a surprising alignment between their processes and best practices: the models typically solve the problem correctly first, then articulate and simulate multiple potential misconceptions, and finally select a set of distractors. An analysis of failure modes reveals that errors arise primarily from failures in recovering the correct solution and selecting among response candidates, rather than simulating errors or structuring the process. Consistent with these results, we find that providing the correct solution in the prompt improves alignment with human-authored distractors by 8%, highlighting the critical role of anchoring to the correct solution when generating plausible incorrect student reasoning. Overall, our analysis offers a structured and interpretable lens into LLMs' ability to model incorrect student reasoning and produce high-quality distractors.

## OpenAI Review
---
title: "Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation"
authors: 
  - "Yanick Zengaffinen"
  - "Andreas Opedal"
  - "Donya Rooein"
  - "Kv Aditya Srivatsa"
  - "Shashank Sonkar"
  - "Mrinmaya Sachan"
year: 2026
journal: "arXiv"
doi: "https://arxiv.org/abs/2603.15547v1"
research_type: "실증 연구"
methodology: "정량적 분석 및 질적 분석"
data_type: "대량 언어 모델의 추론 추적"
sample: "240개의 선택형 질문에 대한 오답 생성 추적"
context: "교육에서의 AI 활용 및 학생 모델링"
theoretical_framework: "학습 과학 이론 및 오류 시뮬레이션 이론"
keywords: ["human-ai collaboration", "classroom ai", "ai tutoring", "instructional design", "scaffolding", "tpack", "ai literacy", "teacher ai", "education", "learning analytics", "llm classroom", "ai pedagogy"]
---

# APA 7th style

# Summary
이 연구는 대량 언어 모델(LLM)이 학생의 오해를 모델링할 수 있는지를 조사한다. 연구진은 LLM이 다중 선택 질문의 오답 생성 과정에서 오해를 어떻게 추론하는지를 분석하고, 이를 통해 LLM의 추론 절차와 학습 과학의 모범 사례 간의 정렬을 비교한다. 분석 결과, LLM은 문제를 올바르게 해결한 후 여러 잠재적 오해를 시뮬레이션하고, 최종적으로 오답을 선택하는 과정을 거친다. 연구는 LLM이 올바른 해답을 제공할 때 오답의 품질이 8% 향상된다는 점을 강조하며, 이는 오답 생성 과정에서 올바른 해답에 대한 고정이 중요함을 시사한다.

# Research Logic
## Problem
학생의 오해를 모델링하는 것이 교육 AI에서 중요한 문제임.
## Theory
LLM의 추론 과정이 학습 과학의 모범 사례와 어떻게 정렬되는지를 분석.
## Design
240개의 오답 생성 추적을 분석하여 LLM의 전략을 분류하는 세분화된 체계 개발.
## Findings
LLM은 문제를 올바르게 해결한 후 오해를 시뮬레이션하고, 오답을 선택하는 과정에서 오류가 발생하는 경향이 있음.
## Conclusion
LLM은 올바른 해답에 고정될 때 오답 생성에서 효과적으로 학생의 오해를 모델링할 수 있음.

# Key Findings
- LLM은 문제를 올바르게 해결한 후 여러 오해를 시뮬레이션함.
- 오답 생성에서의 오류는 주로 올바른 해답 복구 실패에서 발생함.
- 올바른 해답을 제공할 때 오답의 품질이 8% 향상됨.

# Contributions
## Theoretical
학생 모델링 및 오답 생성에 대한 새로운 통찰 제공.
## Methodological
LLM의 추론 과정을 분석하기 위한 체계적 접근법 제안.
## Practical
교육 AI 도구의 신뢰성을 높이기 위한 실용적인 지침 제공.

# Limitations
- LLM의 성능 향상에 대한 추가적인 연구 필요.
- 특정 문제 유형에 대한 일반화의 한계 존재.

# Transferable Insights
- LLM의 오답 생성 과정에서 올바른 해답의 중요성 강조.
- 교육 AI 도구의 신뢰성을 높이기 위한 명확한 지침 필요.

# Idea Seeds
1. LLM의 오답 생성 전략을 개선하기 위한 추가적인 연구.
2. 교육 현장에서 LLM을 활용한 학생 모델링의 실제 적용 사례 연구.
3. LLM의 추론 과정을 기반으로 한 교육 콘텐츠 개발.

# Citation Snippets
> Zengaffinen, Y., Opedal, A., Rooein, D., Srivatsa, K. A., Sonkar, S., & Sachan, M. (2026). Can LLMs Model Incorrect Student Reasoning? A Case Study on Distractor Generation. arXiv. https://arxiv.org/abs/2603.15547v1

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy
