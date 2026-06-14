# An Infectious Disease Spread Simulation Based on Large Language Model Decision Making

- Source: arxiv
- ID: http://arxiv.org/abs/2606.06360v2
- DOI: 명시되지 않음
- Published: 2026-06-04T16:30:13Z
- Authors: Yonchanok Khaokaew, Ruochen Kong, Andreas Zufle, Hao Xue, Taylor Anderson, Chandini Raina MacIntyre, Matthew Scotch, Flora D. Salim, David J Heslop
- Categories: cs.AI
- Link: https://arxiv.org/abs/2606.06360v2
- PDF: https://arxiv.org/pdf/2606.06360v2
- Keyword Score: 6

## Abstract
Modelling individual decision-making during infectious disease outbreaks is crucial for understanding behavioural dynamics and informing effective public health interventions. Prior work has shown that large language models can simulate realistic human behaviour by generating agent decisions based on demographic prompts and situational context. We build on this foundation with a spatially grounded, agent-based simulation framework that integrates LLM-generated decisions about self-reported influenza-like illness into a census-based synthetic population of agents. Location is treated as a central feature: agents are assigned to spatial units within cities, capturing the spatial distributions of different demographic groups using real-world census data and enabling geographically diverse behavioural modelling. We implement and compare three decision scenarios, independent reasoning, household influence, and message framing, and simulate self-reporting outcomes in San Francisco and Atlanta. Results reveal that income and education are the dominant drivers of reporting rate variation, with smaller but consistent effects from geography, LLM model choice, and message framing. Our framework generates synthetic data that captures both social and geographic heterogeneity, supporting spatial epidemiological modelling and bias-aware behavioural analysis.

## OpenAI Review
---
title: 전염병 확산 시뮬레이션: 대형 언어 모델 의사결정 기반
authors: [Yonchanok Khaokaew, Ruochen Kong, Andreas Zufle, Hao Xue, Taylor Anderson, Chandini Raina MacIntyre, Matthew Scotch, Flora D. Salim, David J Heslop]
year: 2026
journal: Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining
doi: https://doi.org/10.1145/3770855.3818983
research_type: 실험적 연구
methodology: 에이전트 기반 시뮬레이션
data_type: 합성 인구 데이터
sample: 샌프란시스코 및 애틀랜타 지역의 인구
context: 전염병 확산 및 공공 보건 개입
theoretical_framework: 계획된 행동 이론
keywords: [전염병, 시뮬레이션, 건강 행동, 대형 언어 모델, 생성적 AI]
---

# APA 7th style

# Summary
이 연구는 전염병 발생 시 개인의 의사결정을 모델링하여 행동 역학을 이해하고 효과적인 공공 보건 개입을 지원하는 것을 목표로 한다. 대형 언어 모델(LLM)을 활용하여 에이전트의 의사결정을 생성하고, 이를 기반으로 한 공간적 에이전트 기반 시뮬레이션 프레임워크를 개발하였다. 연구 결과, 소득과 교육 수준이 보고율 변동의 주요 요인으로 나타났으며, 지리적 요인, LLM 모델 선택, 메시지 프레이밍도 일정한 영향을 미쳤다. 이 프레임워크는 사회적 및 지리적 이질성을 포착하여 공간 역학 모델링과 편향 인식 행동 분석을 지원한다.

# Research Logic
## Problem
전염병 발생 시 개인의 의사결정이 전염병 확산에 미치는 영향을 이해하는 것이 중요하다.

## Theory
계획된 행동 이론을 기반으로 하여 개인의 행동 결정이 사회적 요인과 정보에 의해 어떻게 영향을 받는지를 탐구한다.

## Design
대형 언어 모델을 활용한 에이전트 기반 시뮬레이션을 통해 다양한 인구 통계적 특성을 가진 에이전트를 생성하고, 이들의 의사결정을 모델링하였다.

## Findings
소득과 교육 수준이 보고율 변동에 가장 큰 영향을 미치며, 지리적 요인과 메시지 프레이밍도 영향을 미친다.

## Conclusion
LLM 기반 의사결정 프레임워크는 전염병 모델링에서 개인의 행동 이질성을 포착하고, 공공 보건 연구에 유용한 도구가 될 수 있다.

# Key Findings
- 소득과 교육 수준이 보고율 변동의 주요 요인으로 작용한다.
- 지리적 요인과 LLM 모델 선택이 보고율에 미치는 영향이 존재한다.
- LLM을 통한 의사결정이 실제 인구의 행동 패턴을 반영한다.

# Contributions
## Theoretical
LLM 기반 의사결정 모델이 전염병 확산 연구에 기여할 수 있는 새로운 이론적 틀을 제공한다.

## Methodological
에이전트 기반 시뮬레이션에 LLM을 통합하여 보다 정교한 행동 모델링을 가능하게 한다.

## Practical
공공 보건 개입을 위한 데이터 기반 의사결정 지원 도구로 활용될 수 있다.

# Limitations
- 특정 지역(샌프란시스코 및 애틀랜타)에서만 연구가 수행되어 일반화에 한계가 있다.
- LLM의 결정이 실제 행동과 일치하지 않을 수 있는 가능성이 존재한다.

# Transferable Insights
- LLM을 활용한 의사결정 모델링은 다양한 분야에 적용 가능하다.
- 인구 통계적 특성이 행동 결정에 미치는 영향을 분석하는 데 유용하다.

# Idea Seeds
1. LLM을 활용한 다른 전염병 모델링 연구 확장.
2. 다양한 지역에서의 데이터 수집을 통한 일반화 가능성 검토.
3. LLM의 의사결정 정확성을 높이기 위한 추가 연구.

# Citation Snippets
> Khaokaew, Y., Kong, R., Zufle, A., Xue, H., Anderson, T., MacIntyre, C. R., Scotch, M., Salim, F. D., & Heslop, D. J. (2026). An Infectious Disease Spread Simulation Based on Large Language Model Decision Making. In Proceedings of the 32nd ACM SIGKDD Conference on Knowledge Discovery and Data Mining.

tags: #전염병, #시뮬레이션, #건강행동, #대형언어모델, #생성적AI, #공공보건, #에이전트기반모델
