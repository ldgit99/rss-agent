# Learning Developmental Scaffoldings to Guide Self-Organisation

- Source: arxiv
- ID: http://arxiv.org/abs/2605.14998v1
- DOI: 명시되지 않음
- Published: 2026-05-14T16:01:25Z
- Authors: Milton L. Montero, Elias Najarro, Jakob Schauser, Sebastian Risi
- Categories: cs.AI, eess.SY, q-bio.QM
- Link: https://arxiv.org/abs/2605.14998v1
- PDF: https://arxiv.org/pdf/2605.14998v1
- Keyword Score: 16

## Abstract
From subcellular structures to entire organisms, many natural systems generate complex organisation through self-organisation: local interactions that collectively give rise to global structure without any blueprint of the outcome. Yet a significant portion of the information driving such processes is not produced by self-organisation itself, instead, it is often offloaded to initial conditions of the system. Biological development is a prime example, where maternal pre-patterns encode positional and symmetry-breaking information that scaffolds the self-organising process. From maternal morphogen gradients in early embryogenesis to tissue-level morphogenetic pre-patterns guiding organ formation, this transfer of information to initial conditions, analogous to a memory-compute trade-off in computational systems, is a fundamental part of developmental processes. In this work, we study this offloading phenomenon by introducing a model that jointly learns both the self-organisation rules and the pre-patterns, allowing their interplay to be varied and measured under controlled conditions: a Neural Cellular Automaton (NCA) paired with a learned coordinate-based pattern generator (SIREN), both trained simultaneously to generate a set of patterns. We provide information-theoretic analyses of how information is distributed between pre-patterns and the self-organising process, and show that jointly learning both components yields improvements in robustness, encoding capacity, and symmetry breaking over purely self-organising alternatives. Our analysis further suggests that effective pre-patterns do not simply approximate their targets; rather, they bias the developmental dynamics in ways that facilitate convergence, pointing to a non-trivial relationship between the structure of initial conditions and the dynamics of self-organisation.

## OpenAI Review
---
title: Learning Developmental Scaffoldings to Guide Self-Organisation
authors: [Milton L. Montero, Elias Najarro, Jakob Schauser, Sebastian Risi]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2605.14998v1
research_type: 이론적 연구
methodology: 신경 세포 자동화(NCA)와 학습된 패턴 생성기(SIREN)를 결합한 모델
data_type: 실험적 데이터
sample: 20개의 수작업 이모지
context: 생물학적 발달 과정의 정보 오프로드 현상 연구
theoretical_framework: 정보 이론
keywords: [self-organisation, pre-patterns, Neural Cellular Automata, SIREN, 정보 이론, 생물학적 발달]
---

# APA 7th style

# Summary
이 연구는 생물학적 발달 과정에서 초기 조건으로의 정보 오프로드 현상을 탐구한다. 연구자들은 신경 세포 자동화(NCA)와 학습된 패턴 생성기(SIREN)를 결합한 모델을 제안하여, 두 구성 요소의 상호작용을 조절 가능한 조건 하에서 측정하였다. 정보 이론적 분석을 통해 초기 패턴과 자가 조직화 과정 간의 정보 분배를 평가하였으며, 두 구성 요소를 동시에 학습하는 것이 자가 조직화 대안에 비해 강건성, 인코딩 용량 및 대칭 파괴에서 개선을 가져온다는 것을 보여주었다. 연구 결과는 초기 조건의 구조와 자가 조직화의 역학 간의 비선형 관계를 강조한다.

# Research Logic
## Problem
생물학적 시스템에서 자가 조직화 과정의 정보 출처와 초기 조건의 역할에 대한 이해 부족.
## Theory
정보 이론을 기반으로 한 자가 조직화와 초기 패턴 간의 관계 분석.
## Design
NCA와 SIREN을 결합한 모델을 통해 실험적 데이터 수집 및 분석.
## Findings
초기 패턴이 자가 조직화의 역학을 편향시켜 수렴을 촉진하며, 정보 오프로드가 강건성 및 인코딩 용량을 향상시킴.
## Conclusion
효과적인 초기 패턴은 단순히 목표를 근사하는 것이 아니라, 발달 역학에 영향을 미치는 중요한 역할을 한다.

# Key Findings
- 초기 패턴과 자가 조직화 과정 간의 정보 분배가 개선됨.
- 초기 조건의 구조가 자가 조직화의 역학에 비선형적인 영향을 미침.
- 자가 조직화 대안에 비해 강건성 및 인코딩 용량이 향상됨.

# Contributions
## Theoretical
자가 조직화와 초기 조건 간의 관계에 대한 새로운 통찰 제공.
## Methodological
NCA와 SIREN의 결합을 통한 실험적 접근법 제안.
## Practical
생물학적 발달 과정의 모델링 및 이해에 기여.

# Limitations
- 실험 데이터가 제한적이며, 다양한 생물학적 시스템에 대한 일반화가 필요함.
- 모델의 복잡성으로 인해 해석이 어려울 수 있음.

# Transferable Insights
- 초기 조건의 설계가 자가 조직화 시스템의 성능에 미치는 영향.
- 정보 이론적 접근이 복잡한 시스템의 이해에 기여할 수 있음.

# Idea Seeds
1. 다양한 생물학적 시스템에 대한 초기 패턴의 역할 연구.
2. 자가 조직화 모델의 강건성을 평가하기 위한 새로운 실험 설계.
3. 정보 이론을 활용한 복잡한 시스템의 동적 분석.

# Citation Snippets
> Montero, M. L., Najarro, E., Schauser, J., & Risi, S. (2026). Learning Developmental Scaffoldings to Guide Self-Organisation. arXiv. https://arxiv.org/abs/2605.14998v1

tags: #자가조직화, #정보이론, #신경세포자동화, #SIREN, #생물학적발달, #패턴생성, #모델링
