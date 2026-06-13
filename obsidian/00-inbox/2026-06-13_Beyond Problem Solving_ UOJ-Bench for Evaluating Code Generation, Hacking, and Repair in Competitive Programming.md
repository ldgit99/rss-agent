# Beyond Problem Solving: UOJ-Bench for Evaluating Code Generation, Hacking, and Repair in Competitive Programming

- Source: arxiv
- ID: http://arxiv.org/abs/2606.12864v1
- DOI: 명시되지 않음
- Published: 2026-06-11T03:48:18Z
- Authors: Tingqiang Xu, Hangrui Zhou, Tianle Cai, Alex Gu, Kaifeng Lyu
- Categories: cs.SE, cs.AI
- Link: https://arxiv.org/abs/2606.12864v1
- PDF: https://arxiv.org/pdf/2606.12864v1
- Keyword Score: 8

## Abstract
Despite strong performance in competitive programming, the role of Large Language Models (LLMs) in supporting human learning in the same setting remains largely unexplored. In this work, we introduce UOJ-Bench, a benchmark designed to evaluate not only the problem-solving ability of LLMs, but also their ability to identify errors in human-written code -- a crucial educational activity traditionally supported by running test cases over online judge systems. UOJ-Bench consists of three distinct tasks: code generation, code hacking, and code repair, all constructed from real-world code submissions on the Universal Online Judge (UOJ) and evaluated through UOJ's native judging infrastructure. Our results show that under one-shot evaluation, even the strongest models fail to identify errors in more than 50% of a set of submissions that have been found to be incorrect by UOJ users. While test-time scaling improves success rates to above 90%, the substantial computational costs incurred from model inference limit its practicality for large-scale deployment. Despite these limitations, we find that the best-performing models under test-time scaling can uncover errors in over 5% of full-score submissions across roughly 30 problems, suggesting that frontier LLMs can already provide complementary signals beyond standard judging systems.

## OpenAI Review
---
title: Beyond Problem Solving: UOJ-Bench for Evaluating Code Generation, Hacking, and Repair in Competitive Programming
authors: [Tingqiang Xu, Hangrui Zhou, Tianle Cai, Alex Gu, Kaifeng Lyu]
year: 2026
journal: Proceedings of the 43rd International Conference on Machine Learning
doi: https://arxiv.org/abs/2606.12864v1
research_type: 실험적 연구
methodology: 벤치마크 개발 및 평가
data_type: 코드 제출 데이터
sample: 500 쌍의 코드 제출
context: 경쟁 프로그래밍
theoretical_framework: 교육적 가치
keywords: [human-ai collaboration, ai tutoring, instructional design, scaffolding, ai literacy, education, learning analytics, ai pedagogy]
---

# APA 7th style

# Summary
이 연구에서는 경쟁 프로그래밍에서 대형 언어 모델(LLM)의 역할을 탐구하기 위해 UOJ-Bench라는 벤치마크를 소개한다. UOJ-Bench는 코드 생성, 해킹 및 수리의 세 가지 작업으로 구성되며, 실제 코드 제출을 기반으로 한다. 연구 결과, 가장 강력한 모델조차도 50% 이상의 오류를 식별하지 못하며, 테스트 시간 확장을 통해 성공률을 90% 이상으로 개선할 수 있지만, 모델 추론의 높은 계산 비용이 대규모 배포의 실용성을 제한한다. 그러나 최상의 성능을 보이는 모델은 전체 점수 제출의 5% 이상에서 오류를 발견할 수 있음을 보여준다.

# Research Logic
## Problem
대형 언어 모델이 경쟁 프로그래밍에서 인간 학습을 지원하는 역할이 충분히 탐구되지 않음.
## Theory
LLM의 오류 식별 능력이 학생들의 학습을 개선할 수 있는 잠재력을 지님.
## Design
UOJ-Bench는 코드 생성, 해킹, 수리의 세 가지 작업을 평가하기 위해 설계됨.
## Findings
모델들은 Easy 레벨에서 60% 미만, Hard 레벨에서 50% 미만의 성공률을 보임.
## Conclusion
현재 LLM은 교육적 목적을 위한 오류 식별 및 수정에서 개선의 여지가 큼.

# Key Findings
- LLM은 Easy 레벨에서 60% 미만, Hard 레벨에서 50% 미만의 성공률을 기록함.
- 테스트 시간 확장을 통해 성공률이 90% 이상으로 증가하지만, 계산 비용이 문제됨.
- GPT-OSS-120B 모델은 Zero-Day-Hacking-5K에서 10% 이상의 오류를 발견함.

# Contributions
## Theoretical
LLM의 교육적 활용 가능성을 제시함.
## Methodological
UOJ-Bench를 통해 LLM의 코드 해킹 및 수리 능력을 평가하는 새로운 방법론을 제안함.
## Practical
프로그래밍 교육에서 LLM을 활용한 피드백 제공 가능성을 탐구함.

# Limitations
- LLM의 오류 식별 능력은 여전히 제한적임.
- 대규모 배포를 위한 계산 비용이 높음.

# Transferable Insights
- LLM의 오류 식별 능력을 활용하여 프로그래밍 교육의 질을 향상시킬 수 있음.
- UOJ-Bench와 같은 벤치마크는 LLM의 성능을 평가하는 데 유용함.

# Idea Seeds
1. LLM을 활용한 자동화된 프로그래밍 교육 도구 개발.
2. UOJ-Bench를 기반으로 한 새로운 교육 커리큘럼 설계.
3. LLM의 성능을 개선하기 위한 추가 연구 필요성.

# Citation Snippets
> Xu, T., Zhou, H., Cai, T., Gu, A., & Lyu, K. (2026). Beyond Problem Solving: UOJ-Bench for Evaluating Code Generation, Hacking, and Repair in Competitive Programming. Proceedings of the 43rd International Conference on Machine Learning.

tags: #human-ai collaboration, #ai tutoring, #instructional design, #scaffolding, #ai literacy, #education, #learning analytics, #ai pedagogy

---

### 압축 요약
이 연구는 UOJ-Bench라는 벤치마크를 통해 대형 언어 모델(LLM)의 경쟁 프로그래밍에서의 오류 식별 능력을 평가한다. 연구 결과, LLM은 50% 이상의 오류를 식별하지 못하며, 테스트 시간 확장을 통해 성공률을 90% 이상으로 개선할 수 있지만, 높은 계산 비용이 문제로 지적된다. LLM의 교육적 활용 가능성을 제시하며, 프로그래밍 교육에서의 피드백 제공 가능성을 탐구한다.
