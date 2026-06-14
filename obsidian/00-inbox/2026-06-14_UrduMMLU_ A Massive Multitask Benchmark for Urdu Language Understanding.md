# UrduMMLU: A Massive Multitask Benchmark for Urdu Language Understanding

- Source: arxiv
- ID: http://arxiv.org/abs/2606.07167v1
- DOI: 명시되지 않음
- Published: 2026-06-05T11:35:27Z
- Authors: Ahmer Tabassum, Sarfraz Ahmad, Hasan Iqbal, Owais Aijaz, Momina Ahsan, Preslav Nakov
- Categories: cs.CL, cs.AI
- Link: https://arxiv.org/abs/2606.07167v1
- PDF: https://arxiv.org/pdf/2606.07167v1
- Keyword Score: 6

## Abstract
Meaningful multilingual evaluation must test models in the target language and educational context. Urdu, spoken by more than 230 million people, lacks a broad MMLU-style benchmark built from native educational sources. We introduce UrduMMLU, a benchmark of 26,431 Urdu MCQs across 26 subjects and five domains, collected from native Urdu MCQ banks and public examination PDFs. Unlike translation-based resources, UrduMMLU covers both standard academic subjects and Urdu- and region-specific content. We label the exam-derived portion through dual human annotation with strict consensus filtering. We evaluate 30 LLMs under English and Urdu prompts, yielding 60 zero-shot evaluations, and further evaluate four open-source LLMs under multiple few-shot settings across both prompt languages. Gemini-3.5-Flash performs best, reaching 90.20% and 90.34% accuracy, while no other model exceeds 85%. The strongest open-source model trails by 7.79 and 8.92 points, and many models lose 25 to 40 points on Urdu-centered Humanities subjects compared with STEM. Few-shot prompting yields only modest gains. UrduMMLU shows that Urdu knowledge remains uneven in current LLMs, especially for regionally grounded content.

## OpenAI Review
---
title: UrduMMLU: A Massive Multitask Benchmark for Urdu Language Understanding
authors: [Ahmer Tabassum, Sarfraz Ahmad, Hasan Iqbal, Owais Aijaz, Momina Ahsan, Preslav Nakov]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2606.07167v1
research_type: 실험적 연구
methodology: 대규모 데이터 수집 및 평가
data_type: 객관식 질문 (MCQ)
sample: 26,431개의 질문
context: 우르두어 교육 및 평가
theoretical_framework: MMLU 스타일 벤치마크
keywords: [우르두어, MMLU, 대규모 언어 모델, 교육 평가, 객관식 질문]
---

# APA 7th style

# Summary
본 연구는 2억 3천만 명 이상이 사용하는 우르두어를 위한 대규모 다중 작업 벤치마크인 UrduMMLU를 소개한다. UrduMMLU는 26개 과목과 5개 도메인에서 수집된 26,431개의 우르두어 객관식 질문(MCQ)으로 구성되어 있으며, 원주율 교육 자료에서 직접 수집되었다. 연구진은 30개의 대규모 언어 모델(LLM)을 평가하여, Gemini-3.5-Flash 모델이 90.20%와 90.34%의 정확도로 가장 높은 성능을 보였음을 확인하였다. 연구 결과, 우르두어 중심의 인문학 과목에서 많은 모델이 STEM 과목에 비해 25에서 40점의 성능 저하를 보였으며, 이는 현재 LLM이 지역적 지식에 대한 불균형을 나타낸다.

# Research Logic
## Problem
우르두어 교육 및 문화적 맥락에서의 모델 성능 평가 부족.
## Theory
MMLU 스타일 벤치마크의 필요성 및 지역적 교육 자료의 중요성.
## Design
26,431개의 MCQ를 포함하는 UrduMMLU 벤치마크 설계.
## Findings
우르두어 중심의 인문학 과목에서 LLM의 성능 저하 확인.
## Conclusion
우르두어 지식의 불균형을 해결하기 위한 보다 나은 벤치마크 필요.

# Key Findings
- UrduMMLU는 26,431개의 MCQ로 구성되어 있으며, 이는 우르두어 교육 자료에서 직접 수집됨.
- Gemini-3.5-Flash 모델이 90.20%와 90.34%의 정확도로 가장 높은 성능을 기록.
- 인문학 과목에서 LLM의 성능이 STEM 과목에 비해 25에서 40점 낮음.

# Contributions
## Theoretical
우르두어 교육 평가를 위한 새로운 벤치마크 개발.
## Methodological
이중 인간 주석을 통한 고품질 질문 및 답변 생성.
## Practical
우르두어 LLM 개발을 위한 데이터셋 및 평가 코드 공개.

# Limitations
- 기존의 영어 중심 벤치마크와의 비교 한계.
- 지역적 지식의 불균형 문제.

# Transferable Insights
- 다국어 교육 평가의 필요성.
- 지역적 교육 자료의 중요성 강조.

# Idea Seeds
1. 우르두어 외 다른 언어를 위한 유사한 벤치마크 개발.
2. LLM의 지역적 지식 향상을 위한 추가 연구.
3. 교육 현장에서의 LLM 활용 방안 탐색.

# Citation Snippets
> Tabassum, A., Ahmad, S., Iqbal, H., Aijaz, O., Ahsan, M., & Nakov, P. (2026). UrduMMLU: A Massive Multitask Benchmark for Urdu Language Understanding. arXiv. https://arxiv.org/abs/2606.07167v1

tags: #우르두어, #MMLU, #대규모언어모델, #교육평가, #객관식질문, #언어이해, #인문학

---

요약: 본 연구는 우르두어를 위한 대규모 다중 작업 벤치마크인 UrduMMLU를 소개하며, 26,431개의 객관식 질문을 포함한다. 연구 결과, Gemini-3.5-Flash 모델이 가장 높은 성능을 보였고, 인문학 과목에서 LLM의 성능 저하가 관찰되었다. 이는 우르두어 지식의 불균형을 나타내며, 보다 나은 벤치마크의 필요성을 강조한다.
