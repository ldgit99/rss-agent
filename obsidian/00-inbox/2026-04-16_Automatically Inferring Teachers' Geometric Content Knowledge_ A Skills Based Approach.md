# Automatically Inferring Teachers' Geometric Content Knowledge: A Skills Based Approach

- Source: arxiv
- ID: http://arxiv.org/abs/2604.13666v1
- DOI: 명시되지 않음
- Published: 2026-04-15T09:34:46Z
- Authors: Ziv Fenigstein, Kobi Gal, Avi Segal, Osama Swidan, Inbal Israel, Hassan Ayoob
- Categories: cs.CY, cs.AI, cs.LG
- Link: https://arxiv.org/abs/2604.13666v1
- PDF: https://arxiv.org/pdf/2604.13666v1
- Keyword Score: 17

## Abstract
Assessing teachers' geometric content knowledge is essential for geometry instructional quality and student learning, but difficult to scale. The Van Hiele model characterizes geometric reasoning through five hierarchical levels. Traditional Van Hiele assessment relies on manual expert analysis of open-ended responses. This process is time-consuming, costly, and prevents large-scale evaluation. This study develops an automated approach for diagnosing teachers' Van Hiele reasoning levels using large language models grounded in educational theory. Our central hypothesis is that integrating explicit skills information significantly improves Van Hiele classification. In collaboration with mathematics education researchers, we built a structured skills dictionary decomposing the Van Hiele levels into 33 fine-grained reasoning skills. Through a custom web platform, 31 pre-service teachers solved geometry problems, yielding 226 responses. Expert researchers then annotated each response with its Van Hiele level and demonstrated skills from the dictionary. Using this annotated dataset, we implemented two classification approaches: (1) retrieval-augmented generation (RAG) and (2) multi-task learning (MTL). Each approach compared a skills-aware variant incorporating the skills dictionary against a baseline without skills information. Results showed that for both methods, skills-aware variants significantly outperformed baselines across multiple evaluation metrics. This work provides the first automated approach for Van Hiele level classification from open-ended responses. It offers a scalable, theory-grounded method for assessing teachers' geometric reasoning that can enable large-scale evaluation and support adaptive, personalized teacher learning systems.

## OpenAI Review
---
title: Automatically Inferring Teachers' Geometric Content Knowledge: A Skills Based Approach
authors: Ziv Fenigstein, Kobi Gal, Avi Segal, Osama Swidan, Inbal Israel, Hassan Ayoob
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.13666v1
research_type: 실험적 연구
methodology: 자동화된 분류 접근법
data_type: 응답 데이터
sample: 31명의 예비 교사
context: 기하학 교육
theoretical_framework: Van Hiele 모델
keywords: [기하학, 교육 기술, AI, 교사 교육, 자동화 평가]
---

# APA 7th style

# Summary
이 연구는 교사의 기하학적 내용 지식을 평가하기 위한 자동화된 접근법을 개발하였다. Van Hiele 모델을 기반으로 하여, 연구자들은 기하학적 추론 수준을 33개의 세부 기술로 분해한 구조화된 기술 사전을 구축하였다. 31명의 예비 교사가 기하학 문제를 해결한 226개의 응답을 수집하고, 전문가들이 각 응답을 Van Hiele 수준으로 주석 처리하였다. 연구 결과, 기술 정보를 포함한 분류 접근법이 기존의 기준선보다 유의미하게 성능이 향상되었음을 보여주었다. 이 연구는 기하학 교육의 대규모 평가를 가능하게 하는 이론 기반의 방법을 제공한다.

# Research Logic
## Problem
교사의 기하학적 내용 지식을 평가하는 것은 교육 품질을 높이는 데 필수적이나, 기존 방법은 시간과 비용이 많이 소요된다.
## Theory
Van Hiele 모델은 기하학적 사고를 다섯 개의 계층적 수준으로 설명하며, 각 수준은 특정한 사고 기술을 포함한다.
## Design
31명의 예비 교사가 기하학 문제에 대한 응답을 제공하고, 이를 기반으로 두 가지 분류 접근법(RAG, MTL)을 개발하였다.
## Findings
기술 정보를 포함한 분류 접근법이 기준선보다 모든 평가 지표에서 유의미하게 우수한 성과를 보였다.
## Conclusion
이 연구는 기하학적 추론 수준을 자동으로 분류하는 첫 번째 접근법을 제시하며, 대규모 평가와 개인화된 교사 학습 시스템을 지원할 수 있는 가능성을 보여준다.

# Key Findings
- 기술 정보를 포함한 분류 접근법이 기존 방법보다 성능이 향상됨.
- 226개의 응답 데이터셋이 구축되어 기하학적 사고 수준을 평가하는 데 사용됨.
- Van Hiele 모델을 기반으로 한 자동화된 평가 방법이 제안됨.

# Contributions
## Theoretical
기하학적 사고의 평가를 위한 새로운 이론적 기초 제공.
## Methodological
기술 기반 분류 접근법을 통한 자동화된 평가 방법 개발.
## Practical
교사의 기하학적 내용 지식을 대규모로 평가할 수 있는 실용적인 방법 제시.

# Limitations
- 연구 샘플이 제한적이며, 다양한 교육 환경에서의 일반화 가능성에 대한 검증이 필요함.
- 기하학적 사고 수준의 평가가 특정 문제 유형에 의존할 수 있음.

# Transferable Insights
- 기술 기반 접근법이 교육 평가의 효율성을 높일 수 있음.
- 대규모 데이터 수집 및 분석을 통한 교육 연구의 확장 가능성.

# Idea Seeds
1. 다양한 과목에 대한 유사한 자동화된 평가 방법 개발.
2. 기술 사전을 확장하여 다른 교육 분야에 적용 가능성 탐색.
3. 교사 교육 프로그램에 통합하여 실시간 피드백 제공.

# Citation Snippets
> Fenigstein, Z., Gal, K., Segal, A., Swidan, O., Israel, I., & Ayoob, H. (2026). Automatically Inferring Teachers' Geometric Content Knowledge: A Skills Based Approach. arXiv. https://arxiv.org/abs/2604.13666v1

tags: #기하학, #교육기술, #AI, #교사교육, #자동화평가, #기술사전, #VanHiele모델
