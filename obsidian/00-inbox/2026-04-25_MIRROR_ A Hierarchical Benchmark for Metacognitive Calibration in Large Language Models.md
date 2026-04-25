# MIRROR: A Hierarchical Benchmark for Metacognitive Calibration in Large Language Models

- Source: arxiv
- ID: http://arxiv.org/abs/2604.19809v1
- DOI: 명시되지 않음
- Published: 2026-04-15T08:41:12Z
- Authors: Jason Z Wang
- Categories: cs.AI, cs.LG
- Link: https://arxiv.org/abs/2604.19809v1
- PDF: https://arxiv.org/pdf/2604.19809v1
- Keyword Score: 6

## Abstract
We introduce MIRROR, a benchmark comprising eight experiments across four metacognitive levels that evaluates whether large language models can use self-knowledge to make better decisions. We evaluate 16 models from 8 labs across approximately 250,000 evaluation instances using five independent behavioral measurement channels. Core experiments are run across the full model roster; experiments with specialized infrastructure requirements report explicitly marked model subsets. We find two phenomena with direct implications for agentic deployment: (1) compositional self-prediction fails universally -- the Compositional Calibration Error ranges from 0.500 to 0.943 on the original 15-model Exp3-v1 set (and 0.434 to 0.758 on the balanced 16-model Exp3-v2 expansion), indicating that models cannot predict their own performance on multi-domain tasks, and (2) models exhibit above-chance but imperfect domain-specific self-knowledge yet systematically fail to translate even this partial awareness into appropriate agentic action-selection -- external metacognitive control reduces the Confident Failure Rate from 0.600 to 0.143 (76% reduction at temperature 0; mean 70% at temperature 0.7 across 5 models from 4 labs). Providing models with their own calibration scores produces no significant improvement (p > 0.05); only architectural constraint is effective. This suggests that external metacognitive scaffolding -- not improved self-knowledge -- is the path to safer autonomous AI systems. Code, data, and Croissant metadata will be released publicly with the benchmark.

## OpenAI Review
---
title: MIRROR: A Hierarchical Benchmark for Metacognitive Calibration in Large Language Models
authors: Jason Z Wang
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.19809v1
research_type: 실험적 연구
methodology: 계층적 벤치마크 실험
data_type: 모델 평가 데이터
sample: 16개 모델, 8개 연구소, 약 250,000 평가 인스턴스
context: 대규모 언어 모델의 메타인지 능력 평가
theoretical_framework: 메타인지 이론
keywords: [metacognition, large language models, calibration, agentic action, external scaffolding]
---

# APA 7th style

# Summary
본 연구에서는 대규모 언어 모델이 자기 지식을 활용하여 더 나은 결정을 내릴 수 있는지를 평가하는 MIRROR라는 벤치마크를 소개한다. 8개 연구소에서 16개 모델을 평가하였으며, 약 250,000개의 평가 인스턴스를 사용하여 5개의 독립적인 행동 측정 채널을 통해 실험을 진행하였다. 주요 발견으로는 조합적 자기 예측 실패와 도메인 특정 자기 지식의 불완전함이 있으며, 외부 메타인지 제어가 신뢰 실패율을 76% 감소시킨다는 점이 강조되었다. 연구 결과는 안전한 자율 AI 시스템을 위한 외부 메타인지 스캐폴딩의 필요성을 시사한다.

# Research Logic
## Problem
대규모 언어 모델이 자기 지식을 기반으로 적절한 행동을 선택할 수 있는지에 대한 검증 부족.
## Theory
메타인지 이론에 기반하여 모델의 자기 인식과 행동 선택 간의 간극을 분석.
## Design
4개의 메타인지 수준을 포함하는 8개의 실험을 설계하여 모델의 성능을 평가.
## Findings
모델은 자기 예측에서 조합적 실패를 보였으며, 외부 제어가 신뢰 실패율을 크게 감소시킴.
## Conclusion
자기 지식 향상보다 외부 메타인지 스캐폴딩이 자율 AI 시스템의 안전성을 높이는 경로임을 제안.

# Key Findings
- 조합적 자기 예측 실패율이 0.500에서 0.943로 나타남.
- 외부 메타인지 제어가 신뢰 실패율을 0.600에서 0.143로 감소시킴 (76% 감소).
- 자기 지식은 도메인 별로 제한적이며, 도메인 간 전이가 이루어지지 않음.

# Contributions
## Theoretical
메타인지와 자율 에이전트의 관계에 대한 새로운 통찰 제공.
## Methodological
MIRROR 벤치마크를 통해 메타인지 평가의 체계적 접근법 제시.
## Practical
AI 시스템의 안전성을 높이기 위한 외부 메타인지 스캐폴딩의 필요성을 강조.

# Limitations
- 모델의 성능이 특정 도메인에 국한됨.
- 외부 제어의 효과가 모든 상황에 일반화될 수 없음.

# Transferable Insights
- 메타인지 능력이 자율 AI 시스템의 안전성에 미치는 영향.
- 외부 스캐폴딩이 AI의 행동 선택에 긍정적인 영향을 미칠 수 있음.

# Idea Seeds
1. 메타인지 기반 AI 교육 프로그램 개발.
2. 다양한 도메인에서의 AI 성능 평가를 위한 새로운 벤치마크 설계.
3. AI의 자기 지식 향상을 위한 훈련 방법론 연구.

# Citation Snippets
> Wang, J. Z. (2026). MIRROR: A Hierarchical Benchmark for Metacognitive Calibration in Large Language Models. arXiv. https://arxiv.org/abs/2604.19809v1

tags: #metacognition, #large_language_models, #AI_safety, #self_knowledge, #agentic_action, #external_scaffolding, #benchmark

---

요약: 본 연구는 대규모 언어 모델의 메타인지 능력을 평가하는 MIRROR 벤치마크를 소개하며, 모델들이 자기 지식을 활용하여 적절한 행동을 선택하는 데 실패한다는 점을 강조한다. 외부 메타인지 제어가 신뢰 실패율을 크게 감소시킨다는 결과는 자율 AI 시스템의 안전성을 높이기 위한 새로운 방향성을 제시한다.
