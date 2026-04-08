# EduIllustrate: Towards Scalable Automated Generation Of Multimodal Educational Content

- Source: arxiv
- ID: http://arxiv.org/abs/2604.05005v1
- DOI: 명시되지 않음
- Published: 2026-04-06T08:58:31Z
- Authors: Shuzhen Bi, Mingzi Zhang, Zhuoxuan Li, Xiaolong Wang, keqian Li, Aimin Zhou
- Categories: cs.CY, cs.AI, cs.CL
- Link: https://arxiv.org/abs/2604.05005v1
- PDF: https://arxiv.org/pdf/2604.05005v1
- Keyword Score: 18

## Abstract
Large language models are increasingly used as educational assistants, yet evaluation of their educational capabilities remains concentrated on question-answering and tutoring tasks. A critical gap exists for multimedia instructional content generation -- the ability to produce coherent, diagram-rich explanations that combine geometrically accurate visuals with step-by-step reasoning. We present EduIllustrate, a benchmark for evaluating LLMs on interleaved text-diagram explanation generation for K-12 STEM problems. The benchmark comprises 230 problems spanning five subjects and three grade levels, a standardized generation protocol with sequential anchoring to enforce cross-diagram visual consistency, and an 8-dimension evaluation rubric grounded in multimedia learning theory covering both text and visual quality. Evaluation of ten LLMs reveals a wide performance spread: Gemini 3.0 Pro Preview leads at 87.8\%, while Kimi-K2.5 achieves the best cost-efficiency (80.8\% at \\$0.12/problem). Workflow ablation confirms sequential anchoring improves Visual Consistency by 13\% at 94\% lower cost. Human evaluation with 20 expert raters validates LLM-as-judge reliability for objective dimensions ($ρ\geq 0.83$) while revealing limitations on subjective visual assessment.

## OpenAI Review
---
title: EduIllustrate: Towards Scalable Automated Generation Of Multimodal Educational Content
authors: [Shuzhen Bi, Mingzi Zhang, Zhuoxuan Li, Xiaolong Wang, Keqian Li, Aimin Zhou]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.05005v1
research_type: 실험적 연구
methodology: 벤치마크 개발 및 평가
data_type: 문제 세트
sample: 230개의 K-12 STEM 문제
context: K-12 교육
theoretical_framework: 멀티미디어 학습 이론
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 EduIllustrate라는 벤치마크를 제안하여 K-12 STEM 문제에 대한 텍스트-다이어그램 설명 생성을 평가한다. 이 벤치마크는 230개의 문제로 구성되며, 다섯 개의 과목과 세 개의 학년을 포함한다. 연구 결과, Gemini 3.0 Pro Preview 모델이 87.8%의 성능을 기록하며 가장 높은 점수를 보였고, Kimi-K2.5는 비용 효율성에서 우수한 성과를 나타냈다. 연구는 또한 시각적 일관성을 개선하기 위한 순차적 앵커링의 효과를 확인하였다. 전문가 평가를 통해 LLM의 신뢰성을 검증하였으나, 주관적 시각 평가의 한계도 드러났다.

# Research Logic
## Problem
K-12 교육에서 멀티미디어 교육 콘텐츠 생성의 필요성이 존재하며, 기존 LLM의 평가가 주로 질문-응답 및 튜터링 작업에 집중되어 있음.
## Theory
Cognitive Load Theory, Dual Coding Theory, Multimedia Learning Principle에 기반하여 시각적 다이어그램과 텍스트적 추론의 조화가 인지 부담을 줄이고 개념 이해를 심화시킴.
## Design
230개의 문제를 포함한 벤치마크를 개발하고, 8차원 평가 루브릭을 통해 텍스트 및 시각적 품질을 평가함.
## Findings
Gemini 3.0 Pro Preview가 87.8%로 가장 높은 성능을 보였으며, Kimi-K2.5는 80.8%의 비용 효율성을 기록함. 순차적 앵커링이 시각적 일관성을 13% 개선함.
## Conclusion
EduIllustrate는 LLM의 멀티미디어 교육 콘텐츠 생성 능력을 평가하는 데 중요한 도구가 될 수 있으며, 교육적 가치가 높은 설명 생성을 위한 기준을 제공함.

# Key Findings
- Gemini 3.0 Pro Preview 모델이 87.8%의 성능을 기록함.
- Kimi-K2.5는 80.8%의 비용 효율성을 보임.
- 순차적 앵커링이 시각적 일관성을 13% 개선함.

# Contributions
## Theoretical
멀티미디어 학습 이론에 기반한 새로운 평가 기준을 제시함.
## Methodological
K-12 STEM 문제에 대한 텍스트-다이어그램 설명 생성을 위한 표준화된 생성 프로토콜을 개발함.
## Practical
교육 현장에서 LLM을 활용한 멀티미디어 콘텐츠 생성의 가능성을 제시함.

# Limitations
- 주관적 시각 평가의 한계가 드러남.
- 다양한 LLM의 성능 차이가 크며, 특정 모델에 대한 의존성이 존재함.

# Transferable Insights
- LLM의 멀티미디어 콘텐츠 생성 능력을 평가하기 위한 기준이 필요함.
- 교육적 맥락에서 LLM의 활용 가능성을 탐색할 수 있음.

# Idea Seeds
1. EduIllustrate를 기반으로 한 다양한 과목의 교육 콘텐츠 생성 시스템 개발.
2. LLM의 평가 기준을 확장하여 다른 교육 수준에 적용 가능성 탐색.
3. 주관적 평가의 한계를 극복하기 위한 새로운 평가 방법론 개발.

# Citation Snippets
> Bi, S., Zhang, M., Li, Z., Wang, X., Li, K., & Zhou, A. (2026). EduIllustrate: Towards Scalable Automated Generation Of Multimodal Educational Content. arXiv. https://arxiv.org/abs/2604.05005v1

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy
