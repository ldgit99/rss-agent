# Fatigue-Aware Learning to Defer via Constrained Optimisation

- Source: arxiv
- ID: http://arxiv.org/abs/2604.00904v1
- DOI: 명시되지 않음
- Published: 2026-04-01T13:48:24Z
- Authors: Zheng Zhang, Cuong C. Nguyen, David Rosewarne, Kevin Wells, Gustavo Carneiro
- Categories: cs.LG
- Link: https://arxiv.org/abs/2604.00904v1
- PDF: https://arxiv.org/pdf/2604.00904v1
- Keyword Score: 9

## Abstract
Learning to defer (L2D) enables human-AI cooperation by deciding when an AI system should act autonomously or defer to a human expert. Existing L2D methods, however, assume static human performance, contradicting well-established findings on fatigue-induced degradation. We propose Fatigue-Aware Learning to Defer via Constrained Optimisation (FALCON), which explicitly models workload-varying human performance using psychologically grounded fatigue curves. FALCON formulates L2D as a Constrained Markov Decision Process (CMDP) whose state includes both task features and cumulative human workload, and optimises accuracy under human-AI cooperation budgets via PPO-Lagrangian training. We further introduce FA-L2D, a benchmark that systematically varies fatigue dynamics from near-static to rapidly degrading regimes. Experiments across multiple datasets show that FALCON consistently outperforms state-of-the-art L2D methods across coverage levels, generalises zero-shot to unseen experts with different fatigue patterns, and demonstrates the advantage of adaptive human-AI collaboration over AI-only or human-only decision-making when coverage lies strictly between 0 and 1.

## OpenAI Review
---
title: Fatigue-Aware Learning to Defer via Constrained Optimisation
authors: [Zheng Zhang, Cuong C. Nguyen, David Rosewarne, Kevin Wells, Gustavo Carneiro]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.00904v1
research_type: 이론적 연구
methodology: 제약 마르코프 결정 과정(CMDP)
data_type: 실험 데이터
sample: 여러 데이터셋
context: 인간-인공지능 협력
theoretical_framework: 심리학적 피로 곡선
keywords: [human-ai collaboration, fatigue, learning to defer, constrained optimisation, decision-making]
---

# APA 7th style

# Summary
본 연구는 인간-인공지능 협력을 위한 'Learning to defer (L2D)' 방법론을 제안하며, 기존 L2D 방법들이 정적 인간 성능을 가정하는 것에 대한 문제를 지적한다. 연구진은 피로를 고려한 L2D 방법인 FALCON을 개발하였으며, 이는 작업 부하에 따라 변동하는 인간 성능을 모델링한다. FALCON은 L2D를 제약 마르코프 결정 과정(CMDP)으로 공식화하고, PPO-Lagrangian 훈련을 통해 인간-인공지능 협력 예산 하에서 정확도를 최적화한다. 실험 결과, FALCON은 기존 L2D 방법들보다 일관되게 우수한 성능을 보였으며, 적응형 인간-인공지능 협력이 AI 전용 또는 인간 전용 의사결정보다 우수함을 입증하였다.

# Research Logic
## Problem
기존 L2D 방법들이 인간 성능을 정적으로 가정하여 피로에 따른 성능 저하를 반영하지 못하는 문제.
## Theory
인간 성능은 작업 부하에 따라 변동하며, 이는 심리학적 피로 곡선으로 모델링할 수 있다.
## Design
FALCON은 CMDP로 L2D를 공식화하고, 작업 부하에 따라 변동하는 인간 성능을 고려하여 의사결정을 내린다.
## Findings
FALCON은 다양한 데이터셋에서 기존 L2D 방법들보다 높은 정확도를 기록하며, 적응형 협력이 효과적임을 보여준다.
## Conclusion
피로를 고려한 L2D 접근법이 인간-인공지능 협력의 효율성을 향상시킬 수 있음을 제시한다.

# Key Findings
- FALCON은 작업 부하에 따라 변동하는 인간 성능을 모델링하여 L2D를 개선하였다.
- 실험 결과, FALCON은 기존 L2D 방법들보다 높은 정확도를 달성하였다.
- 적응형 인간-인공지능 협력이 AI 전용 또는 인간 전용 의사결정보다 우수함을 입증하였다.

# Contributions
## Theoretical
피로를 고려한 인간 성능 모델링을 통해 L2D 이론에 기여.
## Methodological
제약 마르코프 결정 과정(CMDP) 기반의 새로운 L2D 접근법 제안.
## Practical
실제 환경에서의 인간-인공지능 협력 최적화를 위한 실용적인 방법론 제공.

# Limitations
- 특정 데이터셋에 대한 실험 결과에 국한되어 일반화의 한계가 있을 수 있다.
- 피로 모델링의 정확성이 실제 환경에서의 적용에 영향을 미칠 수 있다.

# Transferable Insights
- 인간 성능의 변동성을 고려한 의사결정 시스템의 필요성.
- 피로 관리가 인간-인공지능 협력의 효율성을 높일 수 있는 방법임을 시사.

# Idea Seeds
1. 피로를 고려한 다양한 인간-인공지능 협력 모델 개발.
2. 실시간 피로 모니터링 시스템과의 통합 연구.
3. 교육 분야에서의 L2D 적용 가능성 탐색.

# Citation Snippets
> Zhang, Z., Nguyen, C. C., Rosewarne, D., Wells, K., & Carneiro, G. (2026). Fatigue-Aware Learning to Defer via Constrained Optimisation. arXiv. https://arxiv.org/abs/2604.00904v1

tags: #human-ai collaboration, #fatigue, #learning to defer, #constrained optimisation, #decision-making, #education, #ai pedagogy
