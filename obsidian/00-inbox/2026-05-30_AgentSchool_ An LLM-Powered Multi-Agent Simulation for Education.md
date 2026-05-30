# AgentSchool: An LLM-Powered Multi-Agent Simulation for Education

- Source: arxiv
- ID: http://arxiv.org/abs/2605.30144v1
- DOI: 명시되지 않음
- Published: 2026-05-28T16:05:58Z
- Authors: Yulei Ye, Wenhao Li, Zhong Wen, Yunshu Huang, Yichen Hu, Zifan Wei, Yige Wang, Xinyu Xie, Haoxuan Yang, Yanjun Huang, Ruijia Li, Hong Qian, Yu Song, Bo Jiang, Bingdong Li, Lijun Li, Bo Zhang, Pinlong Cai, Xingcheng Xu, Shuangye Chen, Xia Hu, Liang He, Aimin Zhou, Jingjing Qu, Jing Shao, Xiangfeng Wang
- Categories: cs.AI, cs.MA
- Link: https://arxiv.org/abs/2605.30144v1
- PDF: https://arxiv.org/pdf/2605.30144v1
- Keyword Score: 22

## Abstract
Despite the rapid deployment of LLMs into classrooms, validating educational AI remains uniquely intractable: interventions act on developing learners whose cognitive and social trajectories are irreversibly shaped, while real-world trials are slow, ethically constrained, and institutionally locked. LLM-based educational simulators have emerged as a potential remedy, but many still collapse learning into persona-conditioned role-play and, when optimized only to reproduce existing classrooms, can structurally penalize the institutional novelty that pedagogical reform requires. In this work, we introduce AgentSchool, an LLM-driven multi-agent simulator that models learning as state transition rather than prompted behavior. AgentSchool couples cognitively growable student agents -- equipped with weighted subject knowledge graphs, thinking-workflow pools, and explicit misconceptions -- with adaptive teacher agents that plan, scaffold, and reflect along the Zone of Proximal Development, embedded in a configurable scenery generator that situates instruction within both formal and informal learning fields, and a multi-scale simulator that decouples interaction scale, temporal granularity, and simulation duration. Experiments show that structured student agents produce more differentiated mastery and misconception traces than a baseline simulator, while teacher-agent comparisons show backbone-dependent patterns consistent with ZPD-informed adaptation. Further, AgentSchool generates plausible traces of peripheral participation, clique formation, aggressor-induced cohesion, and opinion-leader emergence consistent with classroom social theories. Beyond its role as an educational research instrument, AgentSchool frames education as a socially meaningful testbed for long-horizon memory, multi-agent coordination, and future institutional reasoning under organizational pressure.

## OpenAI Review
---
title: AgentSchool: An LLM-Powered Multi-Agent Simulation for Education
authors: Yulei Ye, Wenhao Li, Zhong Wen, Yunshu Huang, Yichen Hu, Zifan Wei, Yige Wang, Xinyu Xie, Haoxuan Yang, Yanjun Huang, Ruijia Li, Hong Qian, Yu Song, Bo Jiang, Bingdong Li, Lijun Li, Bo Zhang, Pinlong Cai, Xingcheng Xu, Shuangye Chen, Xia Hu, Liang He, Aimin Zhou, Jingjing Qu, Jing Shao, Xiangfeng Wang
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2605.30144v1
research_type: 이론적 연구
methodology: 다중 에이전트 시뮬레이션
data_type: 시뮬레이션 데이터
sample: 5개의 LLM 백본을 사용한 2x3 통제 수업 연구
context: 교육 AI의 검증 및 시뮬레이션
theoretical_framework: 근접 발달 영역(ZPD) 이론
keywords: [human-ai collaboration, classroom ai, ai tutoring, instructional design, scaffolding, tpack, ai literacy, teacher ai, education, learning analytics, llm classroom, ai pedagogy]
---

# APA 7th style

# Summary
본 연구는 교육 현장에서 대규모 언어 모델(LLM)의 활용을 검증하기 위한 시뮬레이터인 AgentSchool을 소개한다. AgentSchool은 학습을 상태 전환으로 모델링하며, 인지적으로 성장 가능한 학생 에이전트와 적응형 교사 에이전트를 결합하여 근접 발달 영역(ZPD)을 기반으로 한 교수-학습 과정을 지원한다. 실험 결과, 구조화된 학생 에이전트가 기존 시뮬레이터보다 더 차별화된 숙련도와 오해의 흔적을 생성하며, 교사 에이전트 간 비교에서 ZPD에 기반한 적응 패턴이 나타났다. AgentSchool은 교육 연구 도구로서의 역할을 넘어, 교육을 사회적으로 의미 있는 테스트베드로 구성하여 장기 기억, 다중 에이전트 조정 및 조직적 압박 하의 미래적 추론을 탐구할 수 있는 환경을 제공한다.

# Research Logic
## Problem
교육 AI의 검증이 어려운 이유는 개입이 학습자의 인지 및 사회적 궤적에 영향을 미치기 때문이다.

## Theory
AgentSchool은 근접 발달 영역(ZPD) 이론을 기반으로 하여 학습 과정을 모델링한다.

## Design
다중 에이전트 시뮬레이션을 통해 학생과 교사 에이전트를 구성하고, 다양한 시나리오를 설정할 수 있다.

## Findings
구조화된 학생 에이전트가 기존 시뮬레이터보다 더 나은 학습 결과를 도출하며, 교사 에이전트의 적응 패턴이 ZPD와 일치한다.

## Conclusion
AgentSchool은 교육 AI의 효과를 사전 검증할 수 있는 안전한 시뮬레이션 환경을 제공한다.

# Key Findings
- 구조화된 학생 에이전트가 더 차별화된 숙련도와 오해의 흔적을 생성함.
- 교사 에이전트 간 비교에서 ZPD에 기반한 적응 패턴이 나타남.
- 교육 사회 이론과 일치하는 주변 참여 및 클리크 형성의 흔적을 생성함.

# Contributions
## Theoretical
AgentSchool은 근접 발달 영역(ZPD) 이론을 기반으로 한 새로운 교육 모델을 제시함.

## Methodological
다중 에이전트 시뮬레이션을 통한 교육 AI 검증 방법론을 개발함.

## Practical
교육 현장에서 AI의 효과를 사전 검증할 수 있는 도구를 제공함.

# Limitations
- 시뮬레이션의 결과가 실제 교육 현장과 다를 수 있음.
- 에이전트의 행동이 실제 학습자의 행동을 완벽히 반영하지 않을 수 있음.

# Transferable Insights
- 교육 AI의 검증을 위한 새로운 방법론 개발 가능성.
- 다중 에이전트 시뮬레이션을 통한 교육 혁신의 가능성 탐구.

# Idea Seeds
1. AgentSchool을 활용한 다양한 교육 시나리오 개발.
2. 교육 정책 결정에 대한 시뮬레이션 결과 활용.
3. AI 기반 교육 도구의 효과를 평가하기 위한 장기 연구 설계.

# Citation Snippets
> Ye, Y., Li, W., Wen, Z., Huang, Y., Hu, Y., Wei, Z., Wang, Y., Xie, X., Yang, H., Huang, Y., Li, R., Qian, H., Song, Y., Jiang, B., Li, B., Li, L., Zhang, B., Cai, P., Xu, X., Chen, S., Hu, X., He, L., Zhou, A., Qu, J., Shao, J., & Wang, X. (2026). AgentSchool: An LLM-Powered Multi-Agent Simulation for Education. arXiv. https://arxiv.org/abs/2605.30144v1

tags: #human-ai collaboration, #classroom ai, #ai tutoring, #instructional design, #scaffolding, #tpack, #ai literacy, #teacher ai, #education, #learning analytics, #llm classroom, #ai pedagogy

---

요약: 본 연구는 AgentSchool이라는 LLM 기반의 다중 에이전트 시뮬레이터를 통해 교육 AI의 검증을 시도한다. 이 시뮬레이터는 학생과 교사 에이전트를 결합하여 근접 발달 영역 이론에 기반한 학습 과정을 모델링하며, 실험 결과 기존 시뮬레이터보다 더 나은 학습 결과를 도출함을 보여준다. AgentSchool은 교육 연구 도구로서의 역할을 넘어 교육 혁신을 위한 안전한 테스트베드를 제공한다.
