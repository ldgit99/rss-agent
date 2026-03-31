# Evaluating LLMs for Answering Student Questions in Introductory Programming Courses

- Source: arxiv
- ID: http://arxiv.org/abs/2603.28295v1
- DOI: 명시되지 않음
- Published: 2026-03-30T11:22:58Z
- Authors: Thomas Van Mullem, Bart Mesuere, Peter Dawyndt
- Categories: cs.AI
- Link: https://arxiv.org/abs/2603.28295v1
- PDF: https://arxiv.org/pdf/2603.28295v1
- Keyword Score: 15

## Abstract
The rapid emergence of Large Language Models (LLMs) presents both opportunities and challenges for programming education. While students increasingly use generative AI tools, direct access often hinders the learning process by providing complete solutions rather than pedagogical hints. Concurrently, educators face significant workload and scalability challenges when providing timely, personalized feedback. This study investigates the capabilities of LLMs to safely and effectively assist educators in answering student questions within a CS1 programming course. To achieve this, we established a rigorous, reproducible evaluation process by curating a benchmark dataset of 170 authentic student questions from a learning management system, paired with ground-truth responses authored by subject matter experts. Because traditional text-matching metrics are insufficient for evaluating open-ended educational responses, we developed and validated a custom LLM-as-a-Judge metric optimized for assessing pedagogical accuracy. Our findings demonstrate that models, such as Gemini 3 flash, can surpass the quality baseline of typical educator responses, achieving high alignment with expert pedagogical standards. To mitigate persistent risks like hallucination and ensure alignment with course-specific context, we advocate for a "teacher-in-the-loop" implementation. Finally, we abstract our methodology into a task-agnostic evaluation framework, advocating for a shift in the development of educational LLM tools from ad-hoc, post-deployment testing to a quantifiable, pre-deployment validation process.

## OpenAI Review
---
title: LLM을 활용한 프로그래밍 수업에서 학생 질문 응답 평가
authors: [Thomas Van Mullem, Bart Mesuere, Peter Dawyndt]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2603.28295v1
research_type: 실험적 연구
methodology: 데이터 수집 및 평가 프레임워크 개발
data_type: 질적 데이터
sample: 170개의 학생 질문
context: CS1 프로그래밍 수업
theoretical_framework: LLM-as-a-Judge
keywords: [human-ai collaboration, ai tutoring, instructional design, ai literacy, education, learning analytics, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 대규모 언어 모델(LLM)이 프로그래밍 교육에서 학생 질문에 대한 응답을 제공하는 능력을 평가한다. 170개의 실제 학생 질문을 기반으로 한 평가 프레임워크를 개발하였으며, LLM이 제공하는 응답의 교육적 정확성을 평가하기 위해 LLM-as-a-Judge 메트릭을 도입하였다. 연구 결과, Gemini 3 flash 모델이 일반 교육자의 응답 품질 기준을 초과하는 성과를 보였으며, 교육적 맥락에 맞춘 "teacher-in-the-loop" 구현을 제안하였다. 이 연구는 교육적 LLM 도구 개발에서 사전 검증 프로세스의 필요성을 강조한다.

# Research Logic
## Problem
학생들이 LLM을 사용하여 프로그래밍 문제를 해결할 때, 완전한 솔루션을 제공받아 학습 과정이 저해되는 문제를 다룬다.

## Theory
LLM의 교육적 활용 가능성을 탐구하며, LLM-as-a-Judge 메트릭을 통해 응답의 교육적 정확성을 평가한다.

## Design
170개의 학생 질문을 포함한 데이터셋을 수집하고, 전문가의 응답을 기준으로 하여 LLM의 성능을 평가하는 프레임워크를 설계하였다.

## Findings
Gemini 3 flash 모델이 교육자의 응답 품질 기준을 초과하며, LLM의 응답이 교육적 맥락에 잘 맞는다는 것을 발견하였다.

## Conclusion
LLM의 안전하고 효과적인 활용을 위해 교육자의 검증을 포함한 시스템 구현이 필요하며, 사전 검증 프로세스의 중요성을 강조한다.

# Key Findings
- LLM은 교육자의 응답 품질 기준을 초과하는 성과를 보였다.
- LLM-as-a-Judge 메트릭이 교육적 정확성을 평가하는 데 효과적이었다.
- "teacher-in-the-loop" 접근 방식이 LLM의 위험을 완화하는 데 기여할 수 있다.

# Contributions
## Theoretical
LLM의 교육적 활용 가능성과 평가 방법론에 대한 새로운 통찰을 제공한다.

## Methodological
LLM-as-a-Judge 메트릭을 통한 교육적 응답 평가의 새로운 접근 방식을 제시한다.

## Practical
교육자가 LLM을 안전하게 활용할 수 있는 방법론을 제안한다.

# Limitations
- 연구에 사용된 데이터셋이 특정 프로그래밍 수업에 국한되어 있다.
- LLM의 응답 품질이 모든 교육적 맥락에 적용될 수 있는지는 명시되지 않음.

# Transferable Insights
- LLM의 교육적 활용을 위한 사전 검증 프로세스의 필요성.
- LLM과 교육자 간의 협력 모델의 중요성.

# Idea Seeds
1. 다양한 교육적 맥락에서 LLM의 응답 품질을 평가하는 연구.
2. LLM의 응답을 개선하기 위한 교육자의 피드백 시스템 개발.
3. LLM의 교육적 활용을 위한 윤리적 가이드라인 수립.

# Citation Snippets
> Van Mullem, T., Mesuere, B., & Dawyndt, P. (2026). Evaluating LLMs for Answering Student Questions in Introductory Programming Courses. arXiv. https://arxiv.org/abs/2603.28295v1

tags: #human-ai collaboration, #ai tutoring, #instructional design, #ai literacy, #education, #learning analytics, #ai pedagogy

---

요약: 본 연구는 LLM이 프로그래밍 교육에서 학생 질문에 대한 응답을 제공하는 능력을 평가하며, Gemini 3 flash 모델이 교육자의 응답 품질 기준을 초과하는 성과를 보였음을 발견하였다. LLM-as-a-Judge 메트릭을 통해 교육적 정확성을 평가하고, 교육자의 검증을 포함한 시스템 구현의 필요성을 강조한다.
