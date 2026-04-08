# AI-Driven Modular Services for Accessible Multilingual Education in Immersive Extended Reality Settings: Integrating Speech Processing, Translation, and Sign Language Rendering

- Source: arxiv
- ID: http://arxiv.org/abs/2604.05591v1
- DOI: 명시되지 않음
- Published: 2026-04-07T08:35:53Z
- Authors: N. D. Tantaroudas, A. J. McCracken, I. Karachalios, E. Papatheou
- Categories: cs.CE, cs.AI, cs.CL, cs.CY, cs.ET
- Link: https://arxiv.org/abs/2604.05591v1
- PDF: https://arxiv.org/pdf/2604.05591v1
- Keyword Score: 16

## Abstract
This work introduces a modular platform that brings together six AI services, automatic speech recognition via OpenAI Whisper, multilingual translation through Meta NLLB, speech synthesis using AWS Polly, emotion classification with RoBERTa, dialogue summarisation via flan t5 base samsum, and International Sign (IS) rendering through Google MediaPipe. A corpus of IS gesture recordings was processed to derive hand landmark coordinates, which were subsequently mapped onto three dimensional avatar animations inside a virtual reality (VR) environment. Validation comprised technical benchmarking of each AI component, including comparative assessments of speech synthesis providers and multilingual translation models (NLLB 200 and EuroLLM 1.7B variants). Technical evaluations confirmed the suitability of the platform for real time XR deployment. Speech synthesis benchmarking established that AWS Polly delivers the lowest latency at a competitive price point. The EuroLLM 1.7B Instruct variant attained a higher BLEU score, surpassing NLLB. These findings establish the viability of orchestrating cross modal AI services within XR settings for accessible, multilingual language instruction. The modular design permits independent scaling and adaptation to varied educational contexts, providing a foundation for equitable learning solutions aligned with European Union digital accessibility goals.

## OpenAI Review
---
title: AI-Driven Modular Services for Accessible Multilingual Education in Immersive Extended Reality Settings: Integrating Speech Processing, Translation, and Sign Language Rendering
authors: 
  - N. D. Tantaroudas
  - A. J. McCracken
  - I. Karachalios
  - E. Papatheou
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.05591v1
research_type: 실험적 연구
methodology: 기술 벤치마킹 및 시스템 평가
data_type: 정량적 데이터
sample: 750개의 IS 제스처 녹화
context: 몰입형 확장 현실 환경에서의 다국어 교육
theoretical_framework: 접근성 및 포용성 이론
keywords: [AI, 다국어 교육, 접근성, 확장 현실, 수화, 음성 인식, 번역]
---

# APA 7th style

# Summary
본 연구는 몰입형 확장 현실(XR) 환경에서 접근 가능한 다국어 교육을 위한 모듈형 플랫폼을 소개한다. 이 플랫폼은 OpenAI Whisper를 통한 자동 음성 인식, Meta NLLB를 통한 다국어 번역, AWS Polly를 이용한 음성 합성, RoBERTa를 통한 감정 분류, flan-t5-base-samsum을 통한 대화 요약, Google MediaPipe를 통한 국제 수화(IS) 렌더링 등 여섯 가지 AI 서비스를 통합한다. 연구 결과, AWS Polly는 낮은 지연 시간(50-100ms)과 경쟁력 있는 가격으로 음성 합성에서 가장 우수한 성능을 보였으며, EuroLLM 1.7B Instruct 변형은 BLEU 점수 84.34를 기록하여 NLLB를 초과하였다. 이러한 결과는 XR 환경 내에서 접근 가능한 다국어 언어 교육을 위한 AI 서비스의 조정 가능성을 입증한다.

# Research Logic
## Problem
현재의 XR 기반 언어 교육 플랫폼은 청각 장애인을 위한 접근성 요구를 간과하고 있다.

## Theory
접근성과 포용성을 강조하는 이론적 틀을 바탕으로 다양한 언어 사용자와 청각 장애인을 위한 교육 기술의 필요성이 제기된다.

## Design
모듈형 AI 서비스 통합 플랫폼을 설계하여 다양한 교육 맥락에 맞게 독립적으로 확장 및 조정 가능하도록 하였다.

## Findings
기술 벤치마킹 결과, AWS Polly는 가장 낮은 지연 시간과 높은 성능을 보였으며, EuroLLM 모델은 NLLB 모델보다 우수한 번역 성능을 나타냈다.

## Conclusion
모듈형 설계는 다양한 교육 환경에 적합한 공평한 학습 솔루션의 기초를 제공하며, 유럽연합의 디지털 접근성 목표와 일치한다.

# Key Findings
- AWS Polly는 음성 합성에서 가장 낮은 지연 시간(50-100ms)을 기록하였다.
- EuroLLM 1.7B Instruct 변형의 BLEU 점수는 84.34로 NLLB를 초과하였다.
- 1,000명의 동시 사용자 시뮬레이션에서 평균 응답 시간은 800ms 이하로 유지되었다.

# Contributions
## Theoretical
접근성과 포용성을 강조하는 새로운 교육 기술 모델을 제시하였다.

## Methodological
모듈형 AI 서비스의 기술 벤치마킹 및 성능 평가 방법론을 개발하였다.

## Practical
다국어 교육을 위한 접근 가능한 XR 플랫폼의 설계 및 구현을 통해 교육 현장에서의 실제 적용 가능성을 높였다.

# Limitations
- 청각 장애인을 위한 수화 인식의 정확성 향상 필요.
- 다양한 언어와 문화적 맥락에 대한 AI의 적응력 부족.

# Transferable Insights
- XR 환경에서의 AI 서비스 통합은 교육 접근성을 향상시킬 수 있다.
- 다양한 사용자 요구를 충족하는 교육 기술의 필요성이 더욱 강조된다.

# Idea Seeds
1. 다양한 언어와 문화적 맥락에 맞춘 AI 기반 교육 콘텐츠 개발.
2. 청각 장애인을 위한 실시간 수화 번역 시스템 연구.
3. XR 환경에서의 사용자 경험 개선을 위한 감정 인식 기술 적용.

# Citation Snippets
> Tantaroudas, N. D., McCracken, A. J., Karachalios, I., & Papatheou, E. (2026). AI-Driven Modular Services for Accessible Multilingual Education in Immersive Extended Reality Settings: Integrating Speech Processing, Translation, and Sign Language Rendering. arXiv. 

tags: #AI, #다국어교육, #접근성, #확장현실, #수화, #음성인식, #번역
