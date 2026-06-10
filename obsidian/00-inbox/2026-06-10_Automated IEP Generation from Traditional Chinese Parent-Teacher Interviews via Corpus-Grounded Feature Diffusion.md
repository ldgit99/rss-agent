# Automated IEP Generation from Traditional Chinese Parent-Teacher Interviews via Corpus-Grounded Feature Diffusion

- Source: arxiv
- ID: http://arxiv.org/abs/2606.09603v1
- DOI: 명시되지 않음
- Published: 2026-06-08T15:13:45Z
- Authors: Kuanlin Chen, Cheng-En Ou
- Categories: cs.CL
- Link: https://arxiv.org/abs/2606.09603v1
- PDF: https://arxiv.org/pdf/2606.09603v1
- Keyword Score: 11

## Abstract
Writing Individualized Education Programs (IEPs) is a high-labor, knowledge-intensive document burden; English-language research has demonstrated that generative AI can significantly reduce drafting time, yet automated IEP generation in Traditional Chinese remains virtually unexplored due to domain data scarcity, strict privacy regulations, and the absence of local evaluation benchmarks. We propose a low-resource fine-tuning pipeline centered on Corpus-Grounded Feature Diffusion (CGFD): (1) 25 dual-expert high-score seed transcripts are selected via a tau threshold with flag-aware score caps; (2) a FeatureProfile (sentence length, structure, quantification templates) is extracted from seeds and injected into LLM prompts alongside Verbalized-Sampling-style diversity control to drive diffusion; (3) 15 expert gold seeds are used as diffusion anchors, targeting 585 samples; 567 valid diffusion samples are obtained, yielding a 582-sample training set used to fine-tune Breeze-7B with QLoRA; (4) schema-constrained inference via Grammar-Constrained Decoding (GCD) enforces a hierarchical SMART Goal Ladder schema at inference time. Ablation results on a 55-sample schema stress set reveal an unexpected finding: GCD is counterproductive under Traditional Chinese token budgets -- the no-GCD path achieves 100% schema pass rate at 34% lower median latency, outperforming GCD on both reliability and speed. On the n=10 formal hold-out, the no-GCD inference path achieves BERTScore F1 = 0.779, exceeding GPT-5.4 (0.726), DeepSeek-V3.2 (0.703), Gemini-3-Flash-Preview (0.703), and Llama-4-Maverick (0.700) zero-shot baselines while maintaining fully local, air-gapped inference. This system addresses a gap in Traditional Chinese special-education NLP and offers a scalable, privacy-preserving local inference solution under an industrial engineering paradigm.

## OpenAI Review
---
title: Automated IEP Generation from Traditional Chinese Parent-Teacher Interviews via Corpus-Grounded Feature Diffusion
authors: [Kuanlin Chen, Cheng-En Ou]
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2606.09603v1
research_type: 실험적 연구
methodology: 저자 제안의 저자 중심 파이프라인
data_type: 텍스트 데이터
sample: 582개 샘플
context: 대만의 전통 중국어 특수 교육
theoretical_framework: 산업 공학 관점
keywords: [IEP, 전통 중국어 NLP, 합성 데이터 생성, 특징 확산, LLM-판사, 문법 제약 디코딩, QLoRA, 산업 공학]
---

# APA 7th style

# Summary
본 연구는 전통 중국어의 개별화 교육 프로그램(IEP) 생성을 위한 자동화 시스템을 제안한다. 연구는 데이터 부족, 엄격한 개인정보 보호 규정, 지역 평가 기준의 부재로 인해 전통 중국어에서의 자동화된 IEP 생성이 거의 탐구되지 않았음을 지적한다. 저자들은 Corpus-Grounded Feature Diffusion(CGFD) 기반의 저자원 미세 조정 파이프라인을 제안하며, 이를 통해 582개의 샘플을 생성하고, 문법 제약 디코딩(GCD)을 통한 추론을 수행하였다. 연구 결과, GCD가 전통 중국어의 토큰 예산 하에서 비생산적임을 발견하였고, GCD를 사용하지 않은 경로가 더 높은 신뢰성과 속도를 보였다. 이 시스템은 전통 중국어 특수 교육 NLP의 격차를 해소하고, 산업 공학 패러다임 하에서 확장 가능하고 개인정보를 보호하는 로컬 추론 솔루션을 제공한다.

# Research Logic
## Problem
전통 중국어에서의 IEP 작성은 데이터 부족과 개인정보 보호 문제로 인해 자동화가 거의 이루어지지 않음.
## Theory
산업 공학 관점에서 IEP 작성의 비효율성을 해결하기 위한 자동화 필요성.
## Design
Corpus-Grounded Feature Diffusion(CGFD) 기반의 저자원 미세 조정 파이프라인 설계.
## Findings
GCD가 전통 중국어의 토큰 예산 하에서 비생산적이며, GCD를 사용하지 않은 경로가 더 높은 성능을 보임.
## Conclusion
제안된 시스템은 전통 중국어 특수 교육 분야의 NLP 격차를 해소하고, 개인정보 보호를 유지하는 로컬 추론 솔루션을 제공함.

# Key Findings
- GCD를 사용하지 않은 경로가 100%의 스키마 통과율을 달성하며, GCD 경로보다 34% 낮은 중간 지연 시간을 기록함.
- BERTScore F1 = 0.779로, 여러 모델의 제로샷 기준을 초과함.
- 제안된 시스템은 전통 중국어 특수 교육 NLP의 격차를 해소함.

# Contributions
## Theoretical
전통 중국어 특수 교육 NLP 분야의 연구 기여.
## Methodological
저자원 환경에서의 합성 데이터 생성 방법론 확장.
## Practical
개인정보 보호를 유지하는 로컬 IEP 생성 솔루션 제공.

# Limitations
- 전통 중국어의 특정 문법적 제약으로 인해 GCD의 비효율성 발견.
- 데이터 부족으로 인한 일반화 가능성의 제한.

# Transferable Insights
- 저자원 환경에서의 데이터 생성 및 처리 방법론의 적용 가능성.
- 특수 교육 분야에서의 AI 활용 방안 제시.

# Idea Seeds
1. 전통 중국어 외 다른 언어로의 IEP 자동화 시스템 개발.
2. GCD의 효율성을 높이기 위한 새로운 접근법 연구.
3. AI 기반 교육 도구의 사용자 경험 개선 방안 탐색.

# Citation Snippets
> Chen, K., & Ou, C.-E. (2026). Automated IEP Generation from Traditional Chinese Parent-Teacher Interviews via Corpus-Grounded Feature Diffusion. arXiv. https://arxiv.org/abs/2606.09603v1

tags: #IEP, #전통중국어, #NLP, #합성데이터, #AI, #교육기술, #산업공학

---

요약: 본 연구는 전통 중국어에서의 개별화 교육 프로그램(IEP) 자동화를 위한 시스템을 제안하며, 데이터 부족과 개인정보 보호 문제를 해결하고자 한다. 연구 결과, 문법 제약 디코딩(GCD)이 비생산적임을 발견하고, GCD를 사용하지 않은 경로가 더 높은 성능을 보였다. 이 시스템은 전통 중국어 특수 교육 NLP의 격차를 해소하고 개인정보를 보호하는 로컬 추론 솔루션을 제공한다.
