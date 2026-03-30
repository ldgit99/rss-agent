# Can MLLMs Read Students' Minds? Unpacking Multimodal Error Analysis in Handwritten Math

- Source: arxiv
- ID: http://arxiv.org/abs/2603.24961v1
- DOI: 명시되지 않음
- Published: 2026-03-26T02:57:20Z
- Authors: Dingjie Song, Tianlong Xu, Yi-Fan Zhang, Hang Li, Zhiling Yan, Xing Fan, Haoyang Li, Lichao Sun, Qingsong Wen
- Categories: cs.AI, cs.CL, cs.CV
- Link: https://arxiv.org/abs/2603.24961v1
- PDF: https://arxiv.org/pdf/2603.24961v1
- Keyword Score: 11

## Abstract
Assessing student handwritten scratchwork is crucial for personalized educational feedback but presents unique challenges due to diverse handwriting, complex layouts, and varied problem-solving approaches. Existing educational NLP primarily focuses on textual responses and neglects the complexity and multimodality inherent in authentic handwritten scratchwork. Current multimodal large language models (MLLMs) excel at visual reasoning but typically adopt an "examinee perspective", prioritizing generating correct answers rather than diagnosing student errors. To bridge these gaps, we introduce ScratchMath, a novel benchmark specifically designed for explaining and classifying errors in authentic handwritten mathematics scratchwork. Our dataset comprises 1,720 mathematics samples from Chinese primary and middle school students, supporting two key tasks: Error Cause Explanation (ECE) and Error Cause Classification (ECC), with seven defined error types. The dataset is meticulously annotated through rigorous human-machine collaborative approaches involving multiple stages of expert labeling, review, and verification. We systematically evaluate 16 leading MLLMs on ScratchMath, revealing significant performance gaps relative to human experts, especially in visual recognition and logical reasoning. Proprietary models notably outperform open-source models, with large reasoning models showing strong potential for error explanation. All evaluation data and frameworks are publicly available to facilitate further research.

## OpenAI Review
---
title: Can MLLMs Read Students' Minds? Unpacking Multimodal Error Analysis in Handwritten Math
authors: [Dingjie Song, Tianlong Xu, Yi-Fan Zhang, Hang Li, Zhiling Yan, Xing Fan, Haoyang Li, Lichao Sun, Qingsong Wen]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2603.24961v1
research_type: 실험적 연구
methodology: 데이터 세트 구축 및 평가
data_type: 수학 문제 풀이의 손으로 쓴 스크래치 작업
sample: 1,720개의 수학 샘플 (중국 초중학교 학생)
context: 중국 초중학교 교육 환경
theoretical_framework: 인지 이론 기반 분석
keywords: [multimodal large language models, mathematical reasoning, error diagnosis, multimodal systems, benchmarking, handwritten recognition]
---

# APA 7th style

# Summary
학생의 손으로 쓴 스크래치 작업을 평가하는 것은 개인화된 교육 피드백을 제공하는 데 필수적이지만, 다양한 필체와 복잡한 레이아웃으로 인해 독특한 도전 과제가 존재한다. 기존 교육 NLP는 주로 텍스트 응답에 초점을 맞추고 있으며, 실제 손으로 쓴 스크래치 작업의 복잡성과 다중 양식을 간과하고 있다. 본 연구에서는 ScratchMath라는 새로운 벤치마크를 도입하여 손으로 쓴 수학 스크래치 작업의 오류를 설명하고 분류하는 데 중점을 두었다. 데이터 세트는 중국의 초중학교 학생들로부터 수집된 1,720개의 수학 샘플로 구성되며, 오류 원인 설명(ECE)과 오류 원인 분류(ECC)라는 두 가지 주요 작업을 지원한다. 16개의 주요 MLLM을 평가한 결과, 인간 전문가에 비해 성능 차이가 뚜렷하게 나타났으며, 특히 시각 인식 및 논리적 추론에서의 격차가 두드러졌다.

# Research Logic
## Problem
학생의 손으로 쓴 스크래치 작업을 자동으로 분석하여 개인화된 피드백을 제공하는 데 어려움이 있다.
## Theory
인지 이론에 기반하여 오류 진단을 위한 다중 양식 모델의 필요성을 강조한다.
## Design
ScratchMath 벤치마크를 통해 오류 설명 및 분류 작업을 수행한다.
## Findings
MLLM은 인간 전문가에 비해 시각 인식 및 논리적 추론에서 성능 차이를 보인다.
## Conclusion
MLLM의 성능 향상을 위해서는 손으로 쓴 스크래치 작업의 복잡성을 이해하고 분석할 수 있는 모델 개발이 필요하다.

# Key Findings
- ScratchMath 데이터 세트는 1,720개의 손으로 쓴 수학 문제 샘플로 구성된다.
- MLLM의 성능은 인간 전문가에 비해 시각 인식 및 논리적 추론에서 유의미한 차이를 보인다.
- 비공식 모델이 오픈 소스 모델보다 성능이 우수하다.

# Contributions
## Theoretical
새로운 다중 양식 오류 탐지 및 설명 벤치마크 작업을 도입하였다.
## Methodological
고품질의 손으로 쓴 스크래치 작업 데이터 세트를 공개하였다.
## Practical
교육적 설정에서 MLLM의 적용 가능성을 평가하고 개선 방향을 제시하였다.

# Limitations
- 데이터 세트는 특정 지역(중국)에서 수집된 샘플로 제한된다.
- MLLM의 성능 평가가 특정 모델에 국한되어 있다.

# Transferable Insights
- 손으로 쓴 스크래치 작업의 오류 분석을 위한 새로운 접근 방식이 필요하다.
- MLLM의 교육적 활용을 위한 지속적인 연구와 개발이 요구된다.

# Idea Seeds
1. 다양한 교육 환경에서의 MLLM 성능 비교 연구.
2. 손으로 쓴 스크래치 작업의 자동 분석을 위한 새로운 알고리즘 개발.
3. MLLM을 활용한 개인화된 교육 피드백 시스템 구축.

# Citation Snippets
> Song, D., Xu, T., Zhang, Y.-F., Li, H., Yan, Z., Fan, X., Li, H., Sun, L., & Wen, Q. (2026). Can MLLMs Read Students' Minds? Unpacking Multimodal Error Analysis in Handwritten Math. arXiv. https://arxiv.org/abs/2603.24961v1

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy

---

학생의 손으로 쓴 스크래치 작업을 평가하는 것은 개인화된 피드백을 제공하는 데 필수적이나, 기존의 교육 NLP는 이 복잡성을 간과하고 있다. 본 연구는 ScratchMath라는 새로운 벤치마크를 통해 MLLM의 성능을 평가하고, 오류 분석의 필요성을 강조한다. 1,720개의 샘플을 통해 MLLM의 성능이 인간 전문가에 비해 유의미한 차이를 보임을 확인하였다.
