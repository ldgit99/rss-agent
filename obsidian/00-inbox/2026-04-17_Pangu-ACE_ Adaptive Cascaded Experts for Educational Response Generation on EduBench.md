# Pangu-ACE: Adaptive Cascaded Experts for Educational Response Generation on EduBench

- Source: arxiv
- ID: http://arxiv.org/abs/2604.14828v1
- DOI: 명시되지 않음
- Published: 2026-04-16T10:02:48Z
- Authors: Dinghao Li, Wenlong Zhou, Zhimin Chen, Yuehan Peng, Hong Ni, Chengfu Zou, Guoyu Shi, Yaochen Li
- Categories: cs.CL
- Link: https://arxiv.org/abs/2604.14828v1
- PDF: https://arxiv.org/pdf/2604.14828v1
- Keyword Score: 12

## Abstract
Educational assistants should spend more computation only when the task needs it. This paper rewrites our earlier draft around the system that was actually implemented and archived in the repository: a sample-level 1B to 7B cascade for the shared-8 EduBench benchmark. The final system, Pangu-ACE, uses a 1B tutor-router to produce a draft answer plus routing signals, then either accepts the draft or escalates the sample to a 7B specialist prompt. We also correct a major offline evaluation bug: earlier summaries over-credited some open-form outputs that only satisfied superficial format checks. After CPU-side rescoring from saved prediction JSONL, the full Chinese test archive (7013 samples) shows that cascade_final improves deterministic quality from 0.457 to 0.538 and format validity from 0.707 to 0.866 over the legacy rule_v2 system while accepting 19.7% of requests directly at 1B. Routing is strongly task dependent: IP is accepted by 1B 78.0% of the time, while QG and EC still escalate almost always. The current archived deployment does not yet show latency gains, so the defensible efficiency story is routing selectivity rather than wall-clock speedup. We also package a reproducible artifact-first paper workflow and clarify the remaining external-baseline gap: GPT-5.4 re-judging is implemented locally, but the configured provider endpoint and key are invalid, so final sampled-baseline alignment with GPT-5.4 remains pending infrastructure repair.

## OpenAI Review
---
title: Pangu-ACE: Adaptive Cascaded Experts for Educational Response Generation on EduBench
authors: [Dinghao Li, Wenlong Zhou, Zhimin Chen, Yuehan Peng, Hong Ni, Chengfu Zou, Guoyu Shi, Yaochen Li]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.14828v1
research_type: 실험적 연구
methodology: 샘플 수준의 적응형 캐스케이드 시스템
data_type: 정량적 데이터
sample: 7013개의 샘플
context: 교육적 응답 생성
theoretical_framework: 이중 과정 추론, 비용 인식 라우팅
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 교육적 응답 생성을 위한 Pangu-ACE 시스템을 제안하며, 샘플 수준에서의 1B에서 7B로의 캐스케이드 구조를 통해 효율적인 라우팅을 구현하였다. 실험 결과, Pangu-ACE는 기존 시스템에 비해 품질과 형식 유효성을 각각 0.081과 0.159 향상시켰으며, 19.7%의 요청을 1B 단계에서 직접 수용하였다. 그러나 현재 배포된 시스템은 지연 시간 개선을 보이지 않으며, 라우팅 선택성에 기반한 효율성 이야기가 필요하다. 이 연구는 교육적 응답 생성의 질을 높이기 위한 새로운 접근 방식을 제시하며, 향후 GPT-5.4와의 정렬 문제 해결이 필요하다.

# Research Logic
## Problem
교육적 응답 생성에서의 효율성과 품질 간의 균형 문제.
## Theory
이중 과정 추론 및 비용 인식 라우팅 이론을 기반으로 함.
## Design
1B 튜터-라우터와 7B 전문 프롬프트를 사용하는 샘플 수준의 캐스케이드 시스템 설계.
## Findings
Pangu-ACE는 품질을 0.538로 향상시키고, 형식 유효성을 0.866으로 개선함.
## Conclusion
효율적인 라우팅을 통해 교육적 응답의 질을 높일 수 있으며, 향후 연구는 GPT-5.4와의 정렬 문제를 해결해야 함.

# Key Findings
- Pangu-ACE는 품질을 0.538로 향상시킴.
- 형식 유효성이 0.866으로 개선됨.
- 19.7%의 요청이 1B 단계에서 직접 수용됨.

# Contributions
## Theoretical
이중 과정 추론 및 비용 인식 라우팅에 대한 새로운 통찰 제공.
## Methodological
샘플 수준의 적응형 캐스케이드 시스템 설계 및 구현.
## Practical
교육적 응답 생성의 질 향상 및 효율성 증대.

# Limitations
- 현재 시스템은 지연 시간 개선을 보이지 않음.
- GPT-5.4와의 정렬 문제 해결이 필요함.

# Transferable Insights
- 교육적 응답 생성에서의 라우팅 선택성이 중요함.
- 비용 인식 라우팅이 교육적 품질 향상에 기여할 수 있음.

# Idea Seeds
1. 다양한 교육적 시나리오에 대한 추가 연구.
2. GPT-5.4와의 정렬 문제 해결을 위한 인프라 개선 연구.
3. 다른 교육적 모델과의 비교 연구.

# Citation Snippets
> Li, D., Zhou, W., Chen, Z., Peng, Y., Ni, H., Zou, C., Shi, G., & Li, Y. (2026). Pangu-ACE: Adaptive Cascaded Experts for Educational Response Generation on EduBench. arXiv. https://arxiv.org/abs/2604.14828v1

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy
