# Unveiling Deepfakes: A Frequency-Aware Triple Branch Network for Deepfake Detection

- Source: arxiv
- ID: http://arxiv.org/abs/2604.17477v1
- DOI: 명시되지 않음
- Published: 2026-04-19T15:08:05Z
- Authors: Qihao Shen, Jiaxing Xuan, Zhenguang Liu, Sifan Wu, Yutong Xie, Zhaoyan Ming, Yingying Jiao, kui Ren
- Categories: cs.CV, cs.LG
- Link: https://arxiv.org/abs/2604.17477v1
- PDF: https://arxiv.org/pdf/2604.17477v1
- Keyword Score: 8

## Abstract
Advanced deepfake technologies are blurring the lines between real and fake, presenting both revolutionary opportunities and alarming threats. While it unlocks novel applications in fields like entertainment and education, its malicious use has sparked urgent ethical and societal concerns ranging from identity theft to the dissemination of misinformation. To tackle these challenges, feature analysis using frequency features has emergedas a promising direction for deepfake detection. However, oneaspect that has been overlooked so far is that existing methodstend to concentrate on one or a few specific frequency domains,which risks overfitting to particular artifacts and significantlyundermines their robustness when facing diverse forgery patterns. Another underexplored aspect we observe is that different features often attend to the same forged region, resulting in redundant feature representations and limiting the diversity of the extracted clues. This may undermine the ability of a model to capture complementary information across different facets, thereby compromising its generalization capability to diverse manipulations. In this paper, we seek to tackle these challenges from two aspects: (1) we propose a triple-branch network that jointly captures spatial and frequency features by learning from both original image and image reconstructed by different frequency channels, and (2) we mathematically derive feature decoupling and fusion losses grounded in the mutual information theory, which enhances the model to focus on task-relevant features across the original image and the image reconstructed by different frequency channels. Extensive experiments on six large-scale benchmark datasets demonstrate that our method consistently achieves state-of-the-art performance. Our code is released at https://github.com/injooker/Unveiling Deepfake.

## OpenAI Review
---
title: Unveiling Deepfakes: A Frequency-Aware Triple Branch Network for Deepfake Detection
authors: [Qihao Shen, Jiaxing Xuan, Zhenguang Liu, Sifan Wu, Yutong Xie, Zhaoyan Ming, Yingying Jiao, kui Ren]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.17477v1
research_type: 실험적 연구
methodology: 실험적 방법론
data_type: 대규모 벤치마크 데이터셋
sample: 6개의 대규모 데이터셋
context: 딥페이크 탐지
theoretical_framework: 상호 정보 이론
keywords: [deepfake detection, multimedia security, image forensics, trustworthy AI]
---

# APA 7th style

# Summary
본 연구는 딥페이크 탐지를 위한 새로운 접근법으로, 주파수 인식 삼중 분기 네트워크를 제안한다. 기존의 방법들이 특정 주파수 영역에 집중함으로써 발생하는 과적합 문제를 해결하기 위해, 원본 이미지와 다양한 주파수 채널로 재구성된 이미지를 동시에 학습하여 공간적 및 주파수적 특징을 포착한다. 연구 결과, 제안된 방법이 6개의 대규모 벤치마크 데이터셋에서 기존 방법들보다 우수한 성능을 보임을 확인하였다. 이 연구는 딥페이크 탐지의 복잡성을 해결하기 위한 새로운 방향을 제시한다.

# Research Logic
## Problem
딥페이크 기술의 발전으로 인해 진짜와 가짜의 경계가 모호해지고 있으며, 이는 신원 도용 및 잘못된 정보 유포와 같은 심각한 사회적 문제를 야기하고 있다.

## Theory
본 연구는 상호 정보 이론에 기반하여 특징 분리 및 융합 손실을 수학적으로 도출하여, 원본 이미지와 주파수 채널에서 학습된 특징들이 서로 보완적이도록 유도한다.

## Design
삼중 분기 네트워크를 설계하여 공간적 및 주파수적 특징을 동시에 캡처하고, 동적 주파수 채널 선택 모듈을 통해 중요한 주파수 채널을 선택한다.

## Findings
제안된 방법은 6개의 대규모 데이터셋에서 기존의 방법들보다 일관되게 우수한 성능을 달성하였다.

## Conclusion
본 연구는 딥페이크 탐지의 효과성을 높이기 위한 새로운 방법론을 제시하며, 향후 연구에 기여할 수 있는 기초 자료를 제공한다.

# Key Findings
- 제안된 삼중 분기 네트워크는 공간적 및 주파수적 특징을 동시에 학습하여 딥페이크 탐지의 정확성을 향상시킨다.
- 동적 주파수 채널 선택 모듈을 통해 중요한 주파수 정보를 효과적으로 활용한다.
- 6개의 대규모 데이터셋에서 기존 방법들보다 우수한 성능을 기록하였다.

# Contributions
## Theoretical
상호 정보 이론을 기반으로 한 특징 분리 및 융합 손실의 수학적 도출.

## Methodological
삼중 분기 네트워크 설계를 통해 공간적 및 주파수적 특징을 통합적으로 학습하는 방법론 제시.

## Practical
딥페이크 탐지의 정확성을 높이는 실용적인 접근법 제공.

# Limitations
- 특정 데이터셋에 대한 성능 평가에 국한되어 있어, 일반화 가능성에 대한 추가 연구가 필요하다.
- 다양한 딥페이크 생성 기술에 대한 포괄적인 대응이 필요하다.

# Transferable Insights
- 주파수 도메인 분석의 중요성을 강조하며, 다양한 주파수 채널을 활용한 탐지 방법론의 필요성을 제시한다.
- 딥페이크 탐지의 복잡성을 해결하기 위한 다각적인 접근법의 필요성을 강조한다.

# Idea Seeds
1. 다양한 주파수 채널을 활용한 딥페이크 탐지 기술의 발전 방향.
2. 상호 정보 이론을 활용한 다른 이미지 처리 분야의 응용 가능성.
3. 딥페이크 탐지 기술의 실시간 적용 가능성에 대한 연구.

# Citation Snippets
> Shen, Q., Xuan, J., Liu, Z., Wu, S., Xie, Y., Ming, Z., Jiao, Y., & Ren, K. (2026). Unveiling Deepfakes: A Frequency-Aware Triple Branch Network for Deepfake Detection. arXiv. https://arxiv.org/abs/2604.17477v1

tags: #deepfake, #detection, #multimedia_security, #image_forensics, #trustworthy_AI, #frequency_analysis, #machine_learning
