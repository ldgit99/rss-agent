# Rethinking Patient Education as Multi-turn Multi-modal Interaction

- Source: arxiv
- ID: http://arxiv.org/abs/2604.14656v1
- DOI: 명시되지 않음
- Published: 2026-04-16T06:06:50Z
- Authors: Zonghai Yao, Zhipeng Tang, Chengtao Lin, Xiong Luo, Benlu Wang, Juncheng Huang, Chin Siang Ong, Hong Yu
- Categories: cs.AI, cs.CL, cs.CV
- Link: https://arxiv.org/abs/2604.14656v1
- PDF: https://arxiv.org/pdf/2604.14656v1
- Keyword Score: 14

## Abstract
Most medical multimodal benchmarks focus on static tasks such as image question answering, report generation, and plain-language rewriting. Patient education is more demanding: systems must identify relevant evidence across images, show patients where to look, explain findings in accessible language, and handle confusion or distress. Yet most patient education work remains text-only, even though combined image-and-text explanations may better support understanding. We introduce MedImageEdu, a benchmark for multi-turn, evidence-grounded radiology patient education. Each case provides a radiology report with report text and case images. A DoctorAgent interacts with a PatientAgent, conditioned on a hidden profile that captures factors such as education level, health literacy, and personality. When a patient question would benefit from visual support, the DoctorAgent can issue drawing instructions grounded in the report, case images, and the current question to a benchmark-provided drawing tool. The tool returns image(s), after which the DoctorAgent produces a final multimodal response consisting of the image(s) and a grounded plain-language explanation. MedImageEdu contains 150 cases from three sources and evaluates both the consultation process and the final multimodal response along five dimensions: Consultation, Safety and Scope, Language Quality, Drawing Quality, and Image-Text Response Quality. Across representative open- and closed-source vision-language model agents, we find three consistent gaps: fluent language often outpaces faithful visual grounding, safety is the weakest dimension across disease categories, and emotionally tense interactions are harder than low education or low health literacy. MedImageEdu provides a controlled testbed for assessing whether multimodal agents can teach from evidence rather than merely answer from text.

## OpenAI Review
---
title: Rethinking Patient Education as Multi-turn Multi-modal Interaction
authors: [Zonghai Yao, Zhipeng Tang, Chengtao Lin, Xiong Luo, Benlu Wang, Juncheng Huang, Chin Siang Ong, Hong Yu]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.14656v1
research_type: 실험적 연구
methodology: 다중 턴 상호작용 기반 평가
data_type: 사례 연구
sample: 150개의 방사선학 사례
context: 방사선 환자 교육
theoretical_framework: 다중 모달 교육 이론
keywords: [patient education, multimodal interaction, radiology, evidence-based learning, AI in healthcare]
---

# APA 7th style

# Summary
본 연구는 방사선 환자 교육을 위한 MedImageEdu라는 새로운 벤치마크를 소개한다. 이 벤치마크는 환자가 이해할 수 있도록 다중 턴의 상호작용을 통해 방사선 보고서와 이미지를 기반으로 교육하는 시스템을 평가한다. 연구는 150개의 사례를 통해 DoctorAgent와 PatientAgent 간의 상호작용을 분석하며, 다섯 가지 평가 차원(상담, 안전 및 범위, 언어 품질, 그림 품질, 이미지-텍스트 응답 품질)을 통해 결과를 도출한다. 연구 결과, 언어의 유창성이 시각적 근거보다 우선하는 경향이 있으며, 안전성은 질병 범주에 따라 가장 약한 차원으로 나타났다. MedImageEdu는 다중 모달 에이전트가 단순히 텍스트에서 답변하는 것이 아니라 증거를 기반으로 교육할 수 있는지를 평가하는 통제된 테스트베드 역할을 한다.

# Research Logic
## Problem
기존의 환자 교육 시스템은 주로 텍스트 기반이며, 시각적 증거를 활용하지 못하는 한계가 있다.
## Theory
다중 모달 교육 이론을 바탕으로, 환자가 이해할 수 있도록 시각적 자료와 텍스트를 결합한 교육 방식이 필요하다.
## Design
DoctorAgent와 PatientAgent 간의 상호작용을 통해 환자 질문에 대한 시각적 지원을 제공하는 시스템을 설계하였다.
## Findings
언어의 유창성이 시각적 근거보다 우선하며, 안전성은 가장 약한 차원으로 나타났다. 감정적으로 긴장된 상호작용은 교육 수준이 낮거나 건강 문해력이 낮은 경우보다 더 어려운 것으로 평가되었다.
## Conclusion
MedImageEdu는 다중 모달 에이전트가 증거를 기반으로 교육할 수 있는지를 평가하는 유용한 도구로 기능한다.

# Key Findings
- MedImageEdu는 150개의 방사선학 사례를 포함한다.
- 상담 과정과 최종 다중 모달 응답을 다섯 가지 차원에서 평가한다.
- 언어의 유창성이 시각적 근거보다 우선하는 경향이 있다.

# Contributions
## Theoretical
다중 모달 교육 이론에 대한 새로운 통찰을 제공한다.
## Methodological
다중 턴 상호작용 기반의 평가 프레임워크를 제안한다.
## Practical
의료 교육에서 다중 모달 접근법의 필요성을 강조한다.

# Limitations
- 연구는 특정 방사선학 사례에 국한되어 있다.
- 감정적 상호작용의 복잡성을 충분히 반영하지 못할 수 있다.

# Transferable Insights
- 다중 모달 교육 접근법은 다양한 교육 환경에 적용 가능하다.
- 환자 맞춤형 교육의 중요성을 강조한다.

# Idea Seeds
1. 다른 의료 분야에 대한 다중 모달 교육 시스템 개발.
2. 환자 교육의 효과성을 높이기 위한 AI 기반 도구 설계.
3. 다양한 교육 수준을 가진 환자에 대한 맞춤형 교육 전략 연구.

# Citation Snippets
> Yao, Z., Tang, Z., Lin, C., Luo, X., Wang, B., Huang, J., Ong, C. S., & Yu, H. (2026). Rethinking Patient Education as Multi-turn Multi-modal Interaction. arXiv. https://arxiv.org/abs/2604.14656v1

tags: #환자교육, #다중모달상호작용, #방사선학, #증거기반학습, #AI의료, #교육기술, #의료교육
