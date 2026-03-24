# Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks

- Source: arxiv
- ID: http://arxiv.org/abs/2603.21636v1
- DOI: 명시되지 않음
- Published: 2026-03-23T07:03:07Z
- Authors: Yiliang Song, Hongjun An, Jiangan Chen, Xuanchen Yan, Huan Song, Jiawei Shao, Xuelong Li
- Categories: cs.AI, cs.CL
- Link: https://arxiv.org/abs/2603.21636v1
- PDF: https://arxiv.org/pdf/2603.21636v1
- Keyword Score: 12

## Abstract
Public benchmarks increasingly govern how large language models (LLMs) are ranked, selected, and deployed. We frame this benchmark-centered regime as Silicon Bureaucracy and AI Test-Oriented Education, and argue that it rests on a fragile assumption: that benchmark scores directly reflect genuine generalization. In practice, however, such scores may conflate exam-oriented competence with principled capability, especially when contamination and semantic leakage are difficult to exclude from modern training pipelines. We therefore propose an audit framework for analyzing contamination sensitivity and score confidence in LLM benchmarks. Using a router-worker setup, we compare a clean-control condition with noisy conditions in which benchmark problems are systematically deleted, rewritten, and perturbed before being passed downstream. For a genuinely clean benchmark, noisy conditions should not consistently outperform the clean-control baseline. Yet across multiple models, we find widespread but heterogeneous above-baseline gains under noisy conditions, indicating that benchmark-related cues may be reassembled and can reactivate contamination-related memory. These results suggest that similar benchmark scores may carry substantially different levels of confidence. Rather than rejecting benchmarks altogether, we argue that benchmark-based evaluation should be supplemented with explicit audits of contamination sensitivity and score confidence.

## OpenAI Review
---
title: Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks
authors: [Yiliang Song, Hongjun An, Jiangan Chen, Xuanchen Yan, Huan Song, Jiawei Shao, Xuelong Li]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2603.21636v1
research_type: 이론적 연구
methodology: 감사 프레임워크 제안, 라우터-작업자 설정 비교
data_type: 대규모 언어 모델 벤치마크 데이터
sample: 여러 모델
context: LLM 벤치마크의 신뢰성 및 오염 민감도 분석
theoretical_framework: 실리콘 관료제 및 AI 시험 지향 교육
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 대규모 언어 모델(LLM)의 벤치마크가 어떻게 평가되고 선택되는지를 분석하며, 이를 '실리콘 관료제'와 'AI 시험 지향 교육'으로 프레이밍한다. 연구자들은 벤치마크 점수가 진정한 일반화 능력을 반영한다는 가정이 불안정하다고 주장하며, 오염 민감도와 점수 신뢰성을 분석하기 위한 감사 프레임워크를 제안한다. 라우터-작업자 설정을 통해 청정 조건과 노이즈 조건을 비교한 결과, 노이즈 조건에서의 성능 향상이 청정 조건을 지속적으로 초과하는 경우가 많음을 발견하였다. 이는 벤치마크 점수가 신뢰성을 다르게 가질 수 있음을 시사하며, 벤치마크 평가에 대한 명시적인 감사가 필요하다고 결론짓는다.

# Research Logic
## Problem
LLM 벤치마크 점수가 진정한 일반화 능력을 반영하지 않는다는 문제.
## Theory
벤치마크 점수는 시험 지향적 능력과 원칙적 능력을 혼합하여 측정한다는 이론.
## Design
라우터-작업자 설정을 통해 청정 조건과 노이즈 조건을 비교하는 실험 설계.
## Findings
노이즈 조건에서의 성능이 청정 조건을 초과하는 경우가 발견됨.
## Conclusion
벤치마크 점수는 신뢰성이 다를 수 있으며, 감사가 필요하다는 결론.

# Key Findings
- 벤치마크 점수는 시험 지향적 능력과 원칙적 능력을 혼합하여 측정한다.
- 노이즈 조건에서의 성능 향상이 청정 조건을 지속적으로 초과하는 경우가 많음.
- 벤치마크 점수의 신뢰성을 평가하기 위한 감사가 필요함.

# Contributions
## Theoretical
LLM 벤치마크의 신뢰성에 대한 새로운 이론적 프레임워크 제안.
## Methodological
라우터-작업자 기반의 감사 방법론 개발.
## Practical
벤치마크 평가의 신뢰성을 높이기 위한 실용적인 접근법 제안.

# Limitations
- 연구에서 사용된 모델의 다양성이 제한적일 수 있음.
- 벤치마크의 오염 민감도 분석이 모든 상황에 적용되지 않을 수 있음.

# Transferable Insights
- LLM 벤치마크의 신뢰성을 높이기 위한 감사 프레임워크는 다른 분야에도 적용 가능.
- 벤치마크 점수의 해석 방식이 교육 및 AI 평가에 중요한 영향을 미칠 수 있음.

# Idea Seeds
1. 다양한 모델에 대한 오염 민감도 분석을 위한 추가 연구.
2. 교육 현장에서 AI 벤치마크의 신뢰성을 높이기 위한 실용적 가이드라인 개발.
3. AI 평가에서 벤치마크 점수의 해석을 위한 새로운 기준 설정.

# Citation Snippets
> Song, Y., An, H., Chen, J., Yan, X., Song, H., Shao, J., & Li, X. (2026). Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks. arXiv. https://arxiv.org/abs/2603.21636v1

tags: #human-ai collaboration, #ai tutoring, #instructional design, #ai literacy, #education, #learning analytics, #ai pedagogy
