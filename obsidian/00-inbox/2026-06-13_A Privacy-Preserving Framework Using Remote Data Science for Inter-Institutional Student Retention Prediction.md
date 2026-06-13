# A Privacy-Preserving Framework Using Remote Data Science for Inter-Institutional Student Retention Prediction

- Source: arxiv
- ID: http://arxiv.org/abs/2606.12845v1
- DOI: 명시되지 않음
- Published: 2026-06-11T03:18:50Z
- Authors: John Fields, K M Sajjadul Islam, Ruchitha Thota, Victor Chen, Praveen Madiraju
- Categories: cs.CR, cs.LG
- Link: https://arxiv.org/abs/2606.12845v1
- PDF: https://arxiv.org/pdf/2606.12845v1
- Keyword Score: 13

## Abstract
This study explores privacy-preserving machine learning (PPML) techniques using the PySyft platform to enable collaborative prediction of student retention between institutions. We developed a remote data science (RDS) framework with a semi-air-gapped architecture consisting of high-side and low-side servers, allowing researchers from three universities to build predictive models on sensitive student data without direct data access. Using historical data from a small private university (N=720), we evaluated three synthetic data generation approaches and validated the framework through inter-institutional collaboration. The results demonstrate consistent classification performance across institutions (Macro F1: 0.690--0.695) while maintaining strict Family Educational Rights and Privacy Act (FERPA) compliance. We also propose Data-Type-Aware Templates, a novel synthetic data method that prioritizes privacy over distributional fidelity. Our findings confirm that RDS-based PPML is technically feasible for educational settings and offers a practical alternative to federated learning for small-scale inter-institutional collaborations. The code is available at https://github.com/jtfields/NAIRR240195-Privacy-Preserving-Machine-Learning.

## OpenAI Review
---
title: A Privacy-Preserving Framework Using Remote Data Science for Inter-Institutional Student Retention Prediction
authors: [John Fields, K M Sajjadul Islam, Ruchitha Thota, Victor Chen, Praveen Madiraju]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2606.12845v1
research_type: 실증 연구
methodology: 원격 데이터 과학(RDS) 프레임워크 개발 및 평가
data_type: 민감한 학생 데이터
sample: 720명의 학생 데이터
context: 고등 교육 기관 간의 협력 연구
theoretical_framework: 개인 정보 보호 기계 학습(PPML)
keywords: [privacy-preserving machine learning, student retention, remote data science, PySyft, higher education]
---

# APA 7th style

# Summary
본 연구는 PySyft 플랫폼을 활용한 개인 정보 보호 기계 학습(PPML) 기술을 탐구하여 교육 기관 간의 학생 유지 예측을 위한 협력적 접근 방식을 제안한다. 세 개의 대학에서 민감한 학생 데이터를 직접 접근하지 않고도 예측 모델을 구축할 수 있도록 하는 반공기형 아키텍처를 갖춘 원격 데이터 과학(RDS) 프레임워크를 개발하였다. 720명의 소규모 사립 대학의 역사적 데이터를 사용하여 세 가지 합성 데이터 생성 접근 방식을 평가하였으며, 기관 간 협력을 통해 프레임워크의 유효성을 검증하였다. 결과는 기관 간 일관된 분류 성능을 보여주었으며(매크로 F1: 0.690–0.695), FERPA 준수를 유지하였다. 또한, 개인 정보 보호를 우선시하는 새로운 합성 데이터 방법인 데이터 유형 인식 템플릿(Data-Type-Aware Templates)을 제안하였다. 연구 결과는 RDS 기반 PPML이 교육 환경에서 기술적으로 실행 가능하며, 소규모 기관 간 협력에 대한 실용적인 대안을 제공함을 확인하였다.

# Research Logic
## Problem
학생 유지율 예측의 필요성과 데이터 프라이버시 문제.
## Theory
개인 정보 보호 기계 학습(PPML) 및 원격 데이터 과학(RDS) 프레임워크.
## Design
세 개의 대학이 협력하여 민감한 데이터를 보호하면서 예측 모델을 개발하는 구조.
## Findings
기관 간 일관된 분류 성능을 보이며, FERPA 준수를 유지함.
## Conclusion
RDS 기반 PPML은 교육 환경에서 유용하며, 소규모 기관 간 협력에 적합한 대안임.

# Key Findings
- Macro F1 점수: 0.690–0.695로 기관 간 일관된 성능을 보임.
- 데이터 유형 인식 템플릿을 통한 합성 데이터 생성 방법 제안.
- FERPA 준수를 유지하면서 민감한 데이터 접근 없이 협력 가능.

# Contributions
## Theoretical
개인 정보 보호 기계 학습(PPML) 및 원격 데이터 과학(RDS) 분야의 이론적 기여.
## Methodological
합성 데이터 생성 및 기관 간 협력 연구를 위한 새로운 방법론 제시.
## Practical
소규모 기관 간 데이터 공유 및 협력 연구의 실용적 접근법 제공.

# Limitations
- 연구는 소규모 사립 대학에 국한됨.
- 데이터 유형 인식 템플릿의 유효성은 추가 연구가 필요함.

# Transferable Insights
- 교육 기관 간의 데이터 프라이버시 문제 해결을 위한 새로운 접근법.
- 합성 데이터 생성 방법의 다양성을 통한 연구 확장 가능성.

# Idea Seeds
1. 다양한 교육 기관에서의 PPML 적용 가능성 탐색.
2. 합성 데이터 생성 방법의 개선 및 확장 연구.
3. 다른 분야에서의 RDS 프레임워크 적용 가능성 검토.

# Citation Snippets
> Fields, J., Islam, K. M. S., Thota, R., Chen, V., & Madiraju, P. (2026). A Privacy-Preserving Framework Using Remote Data Science for Inter-Institutional Student Retention Prediction. arXiv. https://arxiv.org/abs/2606.12845v1

tags: #privacy-preserving, #student-retention, #remote-data-science, #PySyft, #higher-education, #machine-learning, #data-privacy

---

요약: 본 연구는 PySyft 플랫폼을 활용한 개인 정보 보호 기계 학습(PPML) 기술을 통해 교육 기관 간의 학생 유지 예측을 위한 협력적 접근 방식을 제안한다. 세 개의 대학에서 민감한 데이터를 직접 접근하지 않고도 예측 모델을 구축할 수 있도록 하는 원격 데이터 과학(RDS) 프레임워크를 개발하였으며, 결과적으로 FERPA 준수를 유지하면서도 일관된 성능을 보였다.
