# Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents

- Source: arxiv
- ID: http://arxiv.org/abs/2606.01584v1
- DOI: 명시되지 않음
- Published: 2026-06-01T02:28:27Z
- Authors: Aitor Arronte Alvarez, Naiyi Xie Fincham
- Categories: cs.CL, cs.AI
- Link: https://arxiv.org/abs/2606.01584v1
- PDF: https://arxiv.org/pdf/2606.01584v1
- Keyword Score: 17

## Abstract
Conversational tutoring agents have been shown to improve learning engagement and student outcomes, and large language models (LLMs) are increasingly used in these systems to provide scalable, personalized feedback. However, LLMs may perpetuate or amplify stereotypical social biases, posing particular risks in educational settings.   In this study, we evaluate LLMs in conversational tutoring scenarios to identify high-confidence social biases, instances where models are unable to identify biased judgments in tutoring conversations while maintaining strong confidence in their assessments, potentially affecting their reasoning and the feedback they provide to learners. We present a new dataset generation method that enables bias evaluation under naturalistic instructional conditions by regenerating student-AI tutor interactions and introducing turns with controlled bias derived from a benchmark dataset.   Using this data, we assess multiple LLMs' ability to detect stereotypical biases and analyze the confidence and reasoning underlying their responses through computational and human evaluations. We find that bias detection is substantially more challenging in conversational tutoring contexts than in benchmark-based evaluations, and that state-of-the-art LLMs are overconfident in their incorrect assessments of stereotypical bias statements. Moreover, model confidence strongly influences reasoning and feedback, highlighting the risks of overconfident, biased behavior in LLM-based tutoring agents. We conclude by discussing implications, mitigation considerations, and directions for future research.

## OpenAI Review
---
title: Identifying High-Confidence Social Biases in LLMs for Trustworthy Conversational Tutoring Agents
authors: [Aitor Arronte Alvarez, Naiyi Xie Fincham]
year: 2026
journal: AIED
doi: https://arxiv.org/abs/2606.01584v1
research_type: 실험적 연구
methodology: 데이터셋 생성 및 실험
data_type: 대화 데이터
sample: 1,727개의 학생-튜터 대화
context: 제2외국어 학습
theoretical_framework: 사회적 편견, 신뢰할 수 있는 AI
keywords: [social biases, stereotypes, overconfidence, conversational tutoring agents, trustworthy AI]
---

# APA 7th style

# Summary
본 연구는 대화형 튜터링 에이전트에서 대규모 언어 모델(LLMs)의 사회적 편견을 식별하는 데 중점을 두고 있다. LLMs는 학습자의 피드백을 제공하는 데 사용되지만, 이들이 편견을 강화할 위험이 있다. 연구진은 새로운 데이터셋 생성 방법을 제안하고, 여러 LLM의 편견 탐지 능력을 평가하였다. 결과적으로, 대화형 튜터링 맥락에서 편견 탐지가 일반적인 벤치마크 평가보다 더 어려운 것으로 나타났으며, LLM이 잘못된 판단에 대해 과도한 자신감을 보이는 경향이 있음을 발견하였다. 이러한 결과는 교육적 맥락에서 LLM의 사용에 대한 위험성을 강조하며, 향후 연구 방향에 대한 논의도 포함되어 있다.

# Research Logic
## Problem
LLMs가 교육적 맥락에서 사회적 편견을 강화할 위험이 있음.
## Theory
사회적 편견과 과도한 자신감이 교육적 피드백에 미치는 영향.
## Design
학생-튜터 대화 데이터셋을 생성하고, 여러 LLM의 편견 탐지 능력을 평가.
## Findings
대화형 튜터링에서 편견 탐지가 더 어렵고, LLM이 잘못된 판단에 대해 과도한 자신감을 보임.
## Conclusion
LLM 기반 튜터링 에이전트의 신뢰성을 높이기 위한 추가 연구 필요.

# Key Findings
- 대화형 튜터링에서 편견 탐지가 벤치마크 평가보다 더 어려움.
- LLM이 잘못된 판단에 대해 과도한 자신감을 보임.
- 모델의 자신감이 피드백의 질에 영향을 미침.

# Contributions
## Theoretical
사회적 편견과 AI의 신뢰성에 대한 새로운 통찰 제공.
## Methodological
자연스러운 교육 환경에서의 편견 평가를 위한 데이터셋 생성 방법 제안.
## Practical
LLM 기반 튜터링 시스템의 신뢰성을 높이기 위한 실용적 고려사항 제시.

# Limitations
- 연구에서 사용된 데이터셋의 범위가 제한적임.
- LLM의 성능 평가가 특정 맥락에 국한됨.

# Transferable Insights
- 교육적 맥락에서 LLM의 신뢰성을 높이기 위한 방법론적 접근 필요.
- 과도한 자신감이 교육적 피드백에 미치는 영향에 대한 이해 증진.

# Idea Seeds
1. LLM의 편견 탐지 능력을 향상시키기 위한 알고리즘 개발.
2. 다양한 교육적 맥락에서 LLM의 신뢰성 평가 연구.
3. LLM의 피드백 품질을 개선하기 위한 사용자 피드백 시스템 구축.

# Citation Snippets
> Arronte Alvarez, A., & Fincham, N. X. (2026). Identifying high-confidence social biases in LLMs for trustworthy conversational tutoring agents. AIED.

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy
