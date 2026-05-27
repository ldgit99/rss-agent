# LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring

- Source: arxiv
- ID: http://arxiv.org/abs/2605.27088v1
- DOI: 명시되지 않음
- Published: 2026-05-26T14:35:57Z
- Authors: Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon
- Categories: cs.CL, cs.LG
- Link: https://arxiv.org/abs/2605.27088v1
- PDF: https://arxiv.org/pdf/2605.27088v1
- Keyword Score: 14

## Abstract
Aligning LLMs for math tutoring typically requires RL-based training with multi-GPU infrastructure. We investigate whether training-free prompt optimization-evolving only the system prompt via API calls-can serve as a practical alternative. We adapt 7 published methods and propose 5 education-specialized methods, evaluating these 12 methods under 5 conditions on 2 OOD benchmark suites. All 12 best-per-method configurations surpass the strongest RL-trained baseline (R_total = 0.633), and our ParetoGrad achieves the best Pareto balance across post-test solve rate, leak control, and helpfulness, rather than dominating any single component. Behavioral analysis with an 82-code educational codebook reveals that training-free methods rely on teaching-knowledge patterns at 2-3x the rate of RL-trained models, with a compensating ~10 percentage-point reduction in intent-level scaffolding. We also find a task-dependent reasoning mode effect consistent across training-free and RL-based paradigms. Our approach enables efficient development of pedagogically aligned LLM tutors with prompts alone and minimal compute.

## OpenAI Review
---
title: LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring
authors: [Unggi Lee, Minchul Shin, Yeil Jeong, Sookbun Lee, Jeongsu Moon, Kyungtae Joo, Eunjoo Lee, Hoilym Kwon]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2605.27088v1
research_type: 실험적 연구
methodology: 교육적 대화 시뮬레이션을 통한 프롬프트 최적화
data_type: 교육 데이터
sample: 792 평가 실행
context: 수학 튜터링을 위한 대형 언어 모델(LLM)의 최적화
theoretical_framework: 교육 심리학, 인공지능 교육
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 대형 언어 모델(LLM)을 수학 튜터로 활용하기 위한 훈련 없는 프롬프트 최적화 방법을 제안한다. 연구진은 7개의 기존 방법을 수정하고 5개의 교육 특화 방법을 제안하여 2개의 OOD 벤치마크에서 12개의 방법을 평가하였다. 모든 방법이 RL 훈련 모델을 초과하는 성과를 보였으며, 특히 ParetoGrad 방법이 최상의 균형을 달성하였다. 훈련 없는 방법은 RL 훈련 모델보다 2-3배 더 높은 교육 지식 패턴 의존성을 보였고, 의도 수준의 스캐폴딩은 약 10% 감소하였다. 이 접근법은 최소한의 컴퓨팅 자원으로 교육적으로 정렬된 LLM 튜터의 효율적인 개발을 가능하게 한다.

# Research Logic
## Problem
LLM을 수학 튜터로 활용하기 위한 기존의 RL 기반 접근법은 고비용의 다중 GPU 인프라를 필요로 한다.
## Theory
훈련 없는 프롬프트 최적화가 RL 기반 방법의 실용적인 대안이 될 수 있는지를 탐구한다.
## Design
7개의 기존 방법을 수정하고 5개의 교육 특화 방법을 제안하여 12개의 방법을 다양한 조건에서 평가하였다.
## Findings
모든 방법이 RL 훈련 모델을 초과하는 성과를 보였으며, ParetoGrad가 최상의 균형을 달성하였다.
## Conclusion
훈련 없는 프롬프트 최적화는 RL 기반 방법에 비해 접근성과 해석 가능성을 제공하며, 교육적 맥락에서 효과적이다.

# Key Findings
- 모든 훈련 없는 방법이 RL 훈련 모델을 초과하는 성과를 보였다.
- ParetoGrad가 세 가지 목표 간의 최상의 균형을 달성하였다 (R_total = 0.719).
- 교육 특화 방법이 일반 방법보다 특정 조건에서 우수한 성과를 보였다.

# Contributions
## Theoretical
훈련 없는 프롬프트 최적화의 가능성을 제시하며, 교육적 맥락에서의 LLM 활용에 대한 새로운 통찰을 제공한다.
## Methodological
다양한 교육적 대화 시뮬레이션을 통한 프롬프트 최적화 방법을 제안한다.
## Practical
교육자들이 LLM을 효과적으로 활용할 수 있는 실용적인 방법론을 제공한다.

# Limitations
- 연구에서 사용된 데이터셋의 범위가 제한적이다.
- 특정 교육적 맥락에서의 일반화 가능성에 대한 추가 연구가 필요하다.

# Transferable Insights
- 훈련 없는 방법이 RL 기반 방법에 비해 더 적은 자원으로 효과적인 튜터링을 가능하게 한다.
- 교육적 특화 방법이 특정 조건에서 성과를 향상시킬 수 있다.

# Idea Seeds
1. 다양한 교육적 맥락에서의 프롬프트 최적화 방법의 추가 연구.
2. LLM을 활용한 다른 과목에 대한 튜터링 방법 개발.
3. 교육적 효과성을 평가하기 위한 새로운 지표 개발.

# Citation Snippets
> Lee, U., Shin, M., Jeong, Y., Lee, S., Moon, J., Joo, K., Lee, E., & Kwon, H. (2026). LLMs Are Already Good Tutors: Training-Free Prompt Optimization for Pedagogical Math Tutoring. arXiv. https://arxiv.org/abs/2605.27088v1

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy
