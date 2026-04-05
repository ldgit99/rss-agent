# Do Large Language Models Mentalize When They Teach?

- Source: arxiv
- ID: http://arxiv.org/abs/2604.01594v1
- DOI: 명시되지 않음
- Published: 2026-04-02T04:04:20Z
- Authors: Sevan K. Harootonian, Mark K. Ho, Thomas L. Griffiths, Yael Niv, Ilia Sucholutsky
- Categories: cs.AI
- Link: https://arxiv.org/abs/2604.01594v1
- PDF: https://arxiv.org/pdf/2604.01594v1
- Keyword Score: 10

## Abstract
How do LLMs decide what to teach next: by reasoning about a learner's knowledge, or by using simpler rules of thumb? We test this in a controlled task previously used to study human teaching strategies. On each trial, a teacher LLM sees a hypothetical learner's trajectory through a reward-annotated directed graph and must reveal a single edge so the learner would choose a better path if they replanned. We run a range of LLMs as simulated teachers and fit their trial-by-trial choices with the same cognitive models used for humans: a Bayes-Optimal teacher that infers which transitions the learner is missing (inverse planning), weaker Bayesian variants, heuristic baselines (e.g., reward based), and non-mentalizing utility models. In a baseline experiment matched to the stimuli presented to human subjects, most LLMs perform well, show little change in strategy over trials, and their graph-by-graph performance is similar to that of humans. Model comparison (BIC) shows that Bayes-Optimal teaching best explains most models' choices. When given a scaffolding intervention, models follow auxiliary inference- or reward-focused prompts, but these scaffolds do not reliably improve later teaching on heuristic-incongruent test graphs and can sometimes reduce performance. Overall, cognitive model fits provide insight into LLM tutoring policies and show that prompt compliance does not guarantee better teaching decisions.

## OpenAI Review
---
title: Do Large Language Models Mentalize When They Teach?
authors: [Sevan K. Harootonian, Mark K. Ho, Thomas L. Griffiths, Yael Niv, Ilia Sucholutsky]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.01594v1
research_type: 실험 연구
methodology: 인지 모델 적합 및 비교
data_type: 시뮬레이션 데이터
sample: 여러 LLM 모델
context: 교육에서 LLM의 교수 전략
theoretical_framework: Bayesian 모델, 비멘탈라이징 유틸리티 모델
keywords: [human-ai collaboration, ai tutoring, instructional design, scaffolding, ai literacy, education, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 대형 언어 모델(LLM)이 학습자의 지식을 추론하여 다음에 무엇을 가르칠지를 결정하는지, 아니면 단순한 규칙을 사용하는지를 조사한다. 연구에서는 LLM을 시뮬레이션한 교사로 사용하여, 보상 주석이 있는 방향 그래프를 통해 가르치는 전략을 평가하였다. 여러 LLM 모델의 선택을 인간의 인지 모델과 비교하여, Bayesian 최적 교사가 대부분의 모델 선택을 가장 잘 설명함을 발견하였다. 스캐폴딩 개입을 제공했을 때, 모델들은 보조 추론 또는 보상 중심의 프롬프트를 따르지만, 이러한 스캐폴딩이 항상 성과를 향상시키지는 않았다. 전반적으로, LLM의 교수 정책에 대한 통찰을 제공하며, 프롬프트 준수가 더 나은 교수 결정을 보장하지 않음을 보여준다.

# Research Logic
## Problem
LLM이 다음에 무엇을 가르칠지를 결정하는 전략이 명확하지 않음.
## Theory
인간의 교수 전략을 기반으로 한 Bayesian 모델과 비멘탈라이징 모델을 사용하여 LLM의 교수 전략을 분석.
## Design
그래프 교수 작업을 통해 LLM의 교수 성과를 평가하고, 인지 모델을 적합하여 비교.
## Findings
대부분의 LLM이 인간과 유사한 성과를 보였으며, Bayesian 최적 교사가 가장 잘 설명함.
## Conclusion
LLM의 교수 전략은 인간의 전략과 유사하지만, 스캐폴딩 개입이 항상 긍정적인 영향을 미치지 않음.

# Key Findings
- LLM은 인간과 유사한 교수 성과를 보임.
- Bayesian 최적 교사가 LLM의 선택을 가장 잘 설명함.
- 스캐폴딩 개입이 항상 성과를 향상시키지 않음.

# Contributions
## Theoretical
LLM의 교수 전략에 대한 새로운 통찰 제공.
## Methodological
인지 모델을 통한 LLM의 교수 전략 분석 방법론 제시.
## Practical
교육에서 LLM의 효과적인 활용 방안 제안.

# Limitations
- LLM의 교수 전략이 특정 상황에 국한될 수 있음.
- 스캐폴딩 개입의 효과가 일관되지 않음.

# Transferable Insights
- LLM의 교수 전략은 교육 설계에 중요한 고려사항이 될 수 있음.
- 스캐폴딩 개입의 설계가 LLM의 교수 성과에 미치는 영향을 이해하는 것이 필요함.

# Idea Seeds
1. LLM의 교수 전략을 개선하기 위한 다양한 스캐폴딩 기법 개발.
2. LLM의 교수 성과를 평가하기 위한 새로운 메트릭스 개발.
3. LLM과 인간 교사의 협업 모델 연구.

# Citation Snippets
> Harootonian, S. K., Ho, M. K., Griffiths, T. L., Niv, Y., & Sucholutsky, I. (2026). Do Large Language Models Mentalize When They Teach? arXiv. https://arxiv.org/abs/2604.01594v1

tags: #human-ai collaboration, #ai tutoring, #instructional design, #scaffolding, #ai literacy, #education, #ai pedagogy

---

요약: 본 연구는 LLM이 학습자의 지식을 추론하여 교수 전략을 결정하는 방식에 대해 조사하였다. Bayesian 최적 교사가 LLM의 선택을 가장 잘 설명하며, 스캐폴딩 개입이 항상 긍정적인 영향을 미치지 않음을 발견하였다. LLM의 교수 전략은 인간의 전략과 유사하지만, 특정 상황에서의 한계가 존재한다.
