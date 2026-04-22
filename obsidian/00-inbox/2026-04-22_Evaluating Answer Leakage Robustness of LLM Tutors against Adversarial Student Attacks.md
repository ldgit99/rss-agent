# Evaluating Answer Leakage Robustness of LLM Tutors against Adversarial Student Attacks

- Source: arxiv
- ID: http://arxiv.org/abs/2604.18660v1
- DOI: 명시되지 않음
- Published: 2026-04-20T11:29:22Z
- Authors: Jin Zhao, Marta Knežević, Tanja Käser
- Categories: cs.CR, cs.AI
- Link: https://arxiv.org/abs/2604.18660v1
- PDF: https://arxiv.org/pdf/2604.18660v1
- Keyword Score: 14

## Abstract
Large Language Models (LLMs) are increasingly used in education, yet their default helpfulness often conflicts with pedagogical principles. Prior work evaluates pedagogical quality via answer leakage-the disclosure of complete solutions instead of scaffolding-but typically assumes well-intentioned learners, leaving tutor robustness under student misuse largely unexplored. In this paper, we study scenarios where students behave adversarially and aim to obtain the correct answer from the tutor. We evaluate a broad set of LLM-based tutor models, including different model families, pedagogically aligned models, and a multi-agent design, under a range of adversarial student attacks. We adapt six groups of adversarial and persuasive techniques to the educational setting and use them to probe how likely a tutor is to reveal the final answer. We evaluate answer leakage robustness using different types of in-context adversarial student agents, finding that they often fail to carry out effective attacks. We therefore introduce an adversarial student agent that we fine-tune to jailbreak LLM-based tutors, which we propose as the core of a standardized benchmark for evaluating tutor robustness. Finally, we present simple but effective defense strategies that reduce answer leakage and strengthen the robustness of LLM-based tutors in adversarial scenarios.

## OpenAI Review
---
title: LLM 튜터의 답변 유출 강건성 평가: 적대적 학생 공격에 대한 연구
authors: Jin Zhao, Marta Knežević, Tanja Käser
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.18660v1
research_type: 실험적 연구
methodology: 다중 턴 대화 시뮬레이션
data_type: 텍스트 데이터
sample: GSM8K 데이터셋
context: 교육적 맥락에서 LLM 기반 튜터의 강건성 평가
theoretical_framework: 교육 심리학, 인공지능
keywords: [human-ai collaboration, ai tutoring, instructional design, scaffolding, ai literacy, education, learning analytics, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 교육에서의 대형 언어 모델(LLM)의 사용이 증가함에 따라, 학생들이 적대적으로 행동할 때 LLM 튜터의 답변 유출 강건성을 평가한다. 기존 연구는 협력적인 학습자를 가정하고 답변 유출을 평가했으나, 본 연구는 적대적 학생 행동을 고려하여 다양한 공격 기법을 적용한다. 연구 결과, LLM 튜터는 다양한 공격에 대해 종종 효과적으로 방어하지 못하며, 이를 해결하기 위해 튜터의 강건성을 평가할 수 있는 새로운 기준을 제안한다. 또한, 간단하지만 효과적인 방어 전략을 통해 답변 유출을 줄이는 방법을 제시한다.

# Research Logic
## Problem
LLM 튜터가 학생의 적대적 행동에 대해 얼마나 강건한지를 평가하는 체계적인 방법이 부족하다.
## Theory
교육적 대화에서 LLM의 도움을 받는 과정에서 발생하는 답변 유출 문제를 다룬다.
## Design
다양한 적대적 공격 기법을 적용하여 LLM 튜터의 반응을 평가하는 다중 턴 대화 시뮬레이션을 설계하였다.
## Findings
LLM 튜터는 적대적 학생 공격에 대해 종종 효과적으로 방어하지 못하며, 새로운 적대적 학생 에이전트를 통해 강건성을 평가할 수 있는 기준을 제안하였다.
## Conclusion
LLM 기반 튜터의 강건성을 높이기 위한 방어 전략이 필요하며, 이를 통해 교육적 효과를 극대화할 수 있다.

# Key Findings
- LLM 튜터는 다양한 적대적 공격에 대해 종종 답변을 유출한다.
- 새로운 적대적 학생 에이전트를 통해 튜터의 강건성을 평가할 수 있는 기준이 제안되었다.
- 간단한 방어 전략이 답변 유출을 줄이는 데 효과적이다.

# Contributions
## Theoretical
LLM 튜터의 교육적 강건성에 대한 새로운 평가 기준을 제시하였다.
## Methodological
적대적 학생 행동을 고려한 다중 턴 대화 시뮬레이션 방법론을 개발하였다.
## Practical
교육적 맥락에서 LLM 튜터의 효과성을 높이기 위한 방어 전략을 제안하였다.

# Limitations
- 연구에서 사용된 데이터셋이 특정 문제 유형에 국한되어 있다.
- 적대적 공격 기법의 다양성이 제한적일 수 있다.

# Transferable Insights
- LLM 튜터의 강건성을 평가하기 위한 새로운 기준이 다른 교육적 도구에도 적용될 수 있다.
- 교육적 대화에서의 적대적 행동을 이해하는 것이 중요하다.

# Idea Seeds
1. 다양한 교육적 맥락에서 LLM 튜터의 강건성을 평가하는 연구.
2. 적대적 공격 기법의 확장을 통한 LLM 튜터의 방어 전략 개발.
3. LLM 튜터의 교육적 효과성을 높이기 위한 사용자 인터페이스 개선.

# Citation Snippets
> Zhao, J., Knežević, M., & Käser, T. (2026). Evaluating Answer Leakage Robustness of LLM Tutors against Adversarial Student Attacks. arXiv. https://arxiv.org/abs/2604.18660v1

tags: #human-ai collaboration, #ai tutoring, #instructional design, #scaffolding, #ai literacy, #education, #learning analytics, #ai pedagogy

---

요약: 본 연구는 LLM 튜터의 답변 유출 강건성을 적대적 학생 공격을 통해 평가하였다. 연구 결과, LLM 튜터는 다양한 공격에 대해 효과적으로 방어하지 못하며, 새로운 평가 기준과 방어 전략이 필요함을 제시하였다.
