# Building Effective AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned

- Source: arxiv
- ID: http://arxiv.org/abs/2603.05344v3
- DOI: 명시되지 않음
- Published: 2026-03-05T16:21:08Z
- Authors: Nghi D. Q. Bui
- Categories: cs.AI
- Link: https://arxiv.org/abs/2603.05344v3
- PDF: https://arxiv.org/pdf/2603.05344v3
- Keyword Score: 13

## Abstract
The landscape of AI coding assistance is undergoing a fundamental shift from complex IDE plugins to versatile, terminal-native agents. Operating directly where developers manage source control, execute builds, and deploy environments, CLI-based agents offer unprecedented autonomy for long-horizon development tasks. In this paper, we present OPENDEV, an open-source, command-line coding agent written in Rust, engineered specifically for this new paradigm. Effective autonomous assistance requires strict safety controls and highly efficient context management to prevent context bloat and reasoning degradation. OPENDEV overcomes these challenges through a compound AI system architecture with workload-specialized model routing, a dual-agent architecture separating planning from execution, lazy tool discovery, and adaptive context compaction that progressively reduces older observations. Furthermore, it employs an automated memory system to accumulate project-specific knowledge across sessions and counteracts instruction fade-out through event-driven system reminders. By enforcing explicit reasoning phases and prioritizing context efficiency, OPENDEV provides a secure, extensible foundation for terminal-first AI assistance, offering a blueprint for robust autonomous software engineering.

## OpenAI Review
---
title: Building Effective AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned
authors: Nghi D. Q. Bui
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2603.05344v3
research_type: 기술 보고서
methodology: 시스템 아키텍처 설계
data_type: 명시되지 않음
sample: 명시되지 않음
context: AI 코딩 지원의 발전
theoretical_framework: 복합 AI 시스템 아키텍처
keywords: [AI 코딩 에이전트, OPENDEV, 명령줄 인터페이스, 안전성, 컨텍스트 관리, 자율 소프트웨어 공학]
---

# APA 7th style

# Summary
본 논문에서는 OPENDEV라는 오픈 소스 명령줄 코딩 에이전트를 제안한다. 이 에이전트는 복합 AI 시스템 아키텍처를 기반으로 하여 효율적인 컨텍스트 관리와 안전성을 보장하며, 개발자가 소스 제어, 빌드 실행 및 환경 배포를 관리하는 터미널에서 직접 작동한다. OPENDEV는 작업 부하에 특화된 모델 라우팅, 계획과 실행을 분리하는 이중 에이전트 아키텍처, 지연 도구 발견 및 적응형 컨텍스트 압축을 통해 기존의 문제를 해결한다. 또한, 프로젝트별 지식을 세션 간에 축적하는 자동화된 메모리 시스템을 채택하고, 명시적 추론 단계를 통해 안전하고 확장 가능한 터미널 중심 AI 지원의 기초를 제공한다.

# Research Logic
## Problem
AI 코딩 지원의 복잡한 IDE 플러그인에서 터미널 네이티브 에이전트로의 전환이 필요하다.
## Theory
복합 AI 시스템 아키텍처를 통해 다양한 모델과 도구를 조합하여 효율성을 극대화할 수 있다.
## Design
OPENDEV는 네 가지 주요 레이어로 구성된 아키텍처를 통해 에이전트의 추론, 도구 실행 및 컨텍스트 관리를 수행한다.
## Findings
OPENDEV는 안전성 및 컨텍스트 관리의 문제를 해결하며, 자율 소프트웨어 공학을 위한 견고한 기초를 제공한다.
## Conclusion
OPENDEV는 터미널 중심 AI 지원의 새로운 패러다임을 제시하며, 향후 연구 및 개발에 중요한 기초 자료가 될 것이다.

# Key Findings
- OPENDEV는 복합 AI 시스템 아키텍처를 통해 작업 부하에 특화된 모델 라우팅을 구현한다.
- 이중 에이전트 아키텍처를 통해 계획과 실행을 분리하여 효율성을 높인다.
- 자동화된 메모리 시스템을 통해 프로젝트별 지식을 축적하고, 명시적 추론 단계를 통해 안전성을 강화한다.

# Contributions
## Theoretical
복합 AI 시스템 아키텍처의 적용을 통해 AI 코딩 지원의 이론적 기초를 확립한다.
## Methodological
명령줄 인터페이스 기반의 자율 코딩 에이전트 설계 방법론을 제시한다.
## Practical
터미널 중심의 AI 지원 시스템을 통해 개발자 생산성을 향상시킬 수 있는 실용적인 솔루션을 제공한다.

# Limitations
- 기존 시스템과의 비교 분석이 부족하다.
- 실제 사용 사례에 대한 데이터가 명시되지 않았다.

# Transferable Insights
- 복합 AI 시스템 아키텍처는 다양한 도구와 모델의 조합을 통해 효율성을 극대화할 수 있다.
- 안전성과 컨텍스트 관리의 중요성을 강조하며, 이를 위한 설계 원칙이 필요하다.

# Idea Seeds
1. OPENDEV의 아키텍처를 기반으로 한 교육용 AI 도구 개발.
2. 다양한 프로그래밍 언어에 대한 지원을 포함한 확장 가능성 연구.
3. AI 코딩 에이전트의 사용자 경험 개선을 위한 인터페이스 디자인 연구.

# Citation Snippets
> Bui, N. D. Q. (2026). Building Effective AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned. arXiv. https://arxiv.org/abs/2603.05344v3

tags: #AI코딩에이전트, #OPENDEV, #명령줄인터페이스, #안전성, #컨텍스트관리, #자율소프트웨어공학, #복합AI시스템

---

압축 요약: 본 논문은 OPENDEV라는 오픈 소스 명령줄 코딩 에이전트를 제안하며, 복합 AI 시스템 아키텍처를 통해 효율적인 컨텍스트 관리와 안전성을 보장한다. 이 에이전트는 개발자가 소스 제어 및 환경 배포를 관리하는 터미널에서 직접 작동하며, 자율 소프트웨어 공학을 위한 견고한 기초를 제공한다.
