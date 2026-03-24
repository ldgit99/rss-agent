# Abjad-Kids: An Arabic Speech Classification Dataset for Primary Education

- Source: arxiv
- ID: http://arxiv.org/abs/2603.20255v1
- DOI: 명시되지 않음
- Published: 2026-03-11T08:03:52Z
- Authors: Abdul Aziz Snoubara, Baraa Al_Maradni, Haya Al_Naal, Malek Al_Madrmani, Roaa Jdini, Seedra Zarzour, Khloud Al Jallad
- Categories: cs.CL, cs.HC, cs.LG, cs.SD, eess.AS
- Link: https://arxiv.org/abs/2603.20255v1
- PDF: https://arxiv.org/pdf/2603.20255v1
- Keyword Score: 14

## Abstract
Speech-based AI educational applications have gained significant interest in recent years, particularly for children. However, children speech research remains limited due to the lack of publicly available datasets, especially for low-resource languages such as Arabic.This paper presents Abjad-Kids, an Arabic speech dataset designed for kindergarten and primary education, focusing on fundamental learning of alphabets, numbers, and colors. The dataset consists of 46397 audio samples collected from children aged 3 - 12 years, covering 141 classes. All samples were recorded under controlled specifications to ensure consistency in duration, sampling rate, and format. To address high intra-class similarity among Arabic phonemes and the limited samples per class, we propose a hierarchical audio classification based on CNN-LSTM architectures. Our proposed methodology decomposes alphabet recognition into a two-stage process: an initial grouping classification model followed by specialized classifiers for each group. Both strategies: static linguistic-based grouping and dynamic clustering-based grouping, were evaluated. Experimental results demonstrate that static linguistic-based grouping achieves superior performance. Comparisons between traditional machine learning with deep learning approaches, highlight the effectiveness of CNN-LSTM models combined with data augmentation. Despite achieving promising results, most of our experiments indicate a challenge with overfitting, which is likely due to the limited number of samples, even after data augmentation and model regularization. Thus, future work may focus on collecting additional data to address this issue. Abjad-Kids will be publicly available. We hope that Abjad-Kids enrich children representation in speech dataset, and be a good resource for future research in Arabic speech classification for kids.

## OpenAI Review
---
title: Abjad-Kids: An Arabic Speech Classification Dataset for Primary Education
authors: [Abdul Aziz Snoubara, Baraa Al_Maradni, Haya Al_Naal, Malek Al_Madrmani, Roaa Jdini, Seedra Zarzour, Khloud Al Jallad]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2603.20255v1
research_type: 데이터셋 개발
methodology: 계층적 오디오 분류
data_type: 오디오 샘플
sample: 46,397
context: 아랍어 아동 교육
theoretical_framework: 언어학적 지식 기반 분류
keywords: [speech classification, child speech classification, Arabic Speech classification, low-resource language, numbers speech classification, alphabets speech classification]
---

# APA 7th style

# Summary
본 연구는 아동을 위한 아랍어 음성 분류 데이터셋인 Abjad-Kids를 제안한다. 이 데이터셋은 3세에서 12세 사이의 아동으로부터 수집된 46,397개의 오디오 샘플로 구성되어 있으며, 알파벳, 숫자 및 색상 학습에 중점을 두고 있다. 연구진은 CNN-LSTM 아키텍처를 기반으로 한 계층적 오디오 분류 방법론을 제안하며, 정적 언어학적 그룹화와 동적 클러스터링 기반 그룹화를 평가하였다. 실험 결과, 정적 언어학적 그룹화가 우수한 성능을 보였으며, 데이터 증강 기법을 통해 모델의 일반화 능력을 향상시켰다. 그러나 제한된 샘플 수로 인한 과적합 문제도 나타났다. Abjad-Kids는 공개될 예정이며, 아랍어 아동 음성 분류 연구에 기여할 것으로 기대된다.

# Research Logic
## Problem
아랍어 아동 음성 데이터셋의 부족으로 인해 아동 음성 연구가 제한적이다.
## Theory
언어학적 지식을 활용한 계층적 분류 방법론이 아랍어 음성 인식에 적합하다는 이론적 근거를 제시한다.
## Design
CNN-LSTM 아키텍처를 기반으로 한 두 단계의 계층적 분류 모델을 설계하였다.
## Findings
정적 언어학적 그룹화가 동적 클러스터링보다 우수한 성능을 보였으며, 데이터 증강이 모델의 일반화에 기여하였다.
## Conclusion
Abjad-Kids 데이터셋은 아랍어 아동 음성 연구의 중요한 자원이 될 것으로 기대된다.

# Key Findings
- Abjad-Kids 데이터셋은 3세에서 12세 아동의 46,397개의 오디오 샘플로 구성된다.
- 정적 언어학적 그룹화가 동적 클러스터링보다 우수한 성능을 보였다.
- 데이터 증강 기법이 모델의 일반화 능력을 향상시켰으나 과적합 문제가 발생하였다.

# Contributions
## Theoretical
아랍어 아동 음성 인식에 대한 새로운 이론적 접근을 제시하였다.
## Methodological
계층적 오디오 분류 방법론을 개발하여 아동 음성 인식의 효율성을 높였다.
## Practical
Abjad-Kids 데이터셋은 아랍어 아동 음성 연구에 실질적인 기여를 할 것이다.

# Limitations
- 샘플 수의 제한으로 인한 과적합 문제 발생.
- 데이터셋의 다양성이 부족하여 일반화에 한계가 있을 수 있다.

# Transferable Insights
- 아랍어와 같은 저자원 언어의 아동 음성 연구에 대한 필요성을 강조한다.
- 계층적 분류 방법론이 다양한 언어적 특성을 가진 데이터셋에 적용 가능함을 보여준다.

# Idea Seeds
1. Abjad-Kids 데이터셋을 기반으로 한 다양한 언어 모델 개발.
2. 아동 음성 인식의 정확성을 높이기 위한 추가 데이터 수집 방안 모색.
3. 다른 저자원 언어에 대한 유사한 데이터셋 구축 연구.

# Citation Snippets
> Snoubara, A. A., Al_Maradni, B., Al_Naal, H., Al_Madrmani, M., Jdini, R., Zarzour, S., & Al Jallad, K. (2026). Abjad-Kids: An Arabic Speech Classification Dataset for Primary Education. arXiv. https://arxiv.org/abs/2603.20255v1

tags: #아랍어, #음성인식, #아동교육, #데이터셋, #기계학습, #교육기술, #언어학
