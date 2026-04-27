# RFID-Based Non-Biometric Classroom Attendance System: Proxy Attendance Detection via Weight Sensor Integration

- Source: arxiv
- ID: http://arxiv.org/abs/2604.22697v1
- DOI: 명시되지 않음
- Published: 2026-04-24T16:30:32Z
- Authors: Furkan Ege, Muhsin Özdemir
- Categories: cs.CY, cs.HC
- Link: https://arxiv.org/abs/2604.22697v1
- PDF: https://arxiv.org/pdf/2604.22697v1
- Keyword Score: 15

## Abstract
Attendance tracking in educational institutions, when conducted through traditional methods, leads to structural problems that consume instruction time and threaten academic integrity. Attendance durations spanning several minutes in primary and secondary education and exceeding ten minutes in higher education, combined with the proxy attendance problem of signing on behalf of someone else, demonstrate the need for electronic systems. Most existing electronic solutions rely on biometric authentication, which raises legal and ethical risks under the European General Data Protection Regulation (GDPR), the Turkish Personal Data Protection Law (KVKK), and the United States Family Educational Rights and Privacy Act (FERPA). Systems using RFID alone provide no built-in safeguard against proxy attendance through card transfer.   This study proposes a biometric-free IoT attendance system addressing both deficiencies. The prototype consists of an RFID module, RFID cards, weight sensors, a Bluetooth module, and an Arduino UNO microcontroller. After the student presents their RFID card, the weight sensor measurement is compared against a statistical reference range of 350 individuals (aged 18-22) compiled from three Kaggle datasets; no personal biometric data is recorded. A Python-based GUI performs student management, course tracking, and CSV-based reporting via Bluetooth.   Qualitative tests in conditions close to a real classroom have shown that the RFID reading, weight verification, Bluetooth communication, and GUI modules operate in an integrated manner as expected. The proposed system offers a low-cost and reproducible solution that aims to reduce proxy attendance without storing biometric data.

## OpenAI Review
---
title: RFID 기반 비생체 인식 교실 출석 시스템: 중량 센서 통합을 통한 대리 출석 탐지
authors: Furkan Ege, Muhsin Özdemir
year: 2026
journal: arXiv
doi: https://arxiv.org/abs/2604.22697v1
research_type: 실험적 연구
methodology: 프로토타입 개발 및 질적 테스트
data_type: 양적 데이터
sample: 350명 (18-22세)
context: 교육 기관의 출석 관리
theoretical_framework: IoT 아키텍처, 비생체 인식 시스템
keywords: [RFID, 출석 시스템, 비생체 인식, 중량 센서, IoT, Arduino, 대리 출석 탐지]
---

# APA 7th style

# Summary
본 연구는 전통적인 출석 방법이 교육 기관에서 발생하는 구조적 문제를 해결하기 위해 비생체 인식 IoT 출석 시스템을 제안한다. 이 시스템은 RFID 모듈, RFID 카드, 중량 센서, 블루투스 모듈, Arduino UNO 마이크로컨트롤러로 구성된다. 학생이 RFID 카드를 제시하면 중량 센서의 측정값이 350명의 통계적 기준 범위와 비교되며, 개인 생체 데이터는 기록되지 않는다. 실제 교실과 유사한 조건에서의 질적 테스트 결과, 시스템의 통합 작동이 기대한 대로 이루어짐을 확인하였다. 제안된 시스템은 대리 출석 문제를 줄이기 위한 저비용의 재현 가능한 솔루션을 제공한다.

# Research Logic
## Problem
전통적인 출석 방법은 시간 소모와 대리 출석 문제를 초래하여 교육의 질을 저하시킨다.
## Theory
비생체 인식 기술을 활용한 IoT 기반 출석 시스템의 필요성이 대두된다.
## Design
RFID와 중량 센서를 통합한 시스템 아키텍처를 설계하였다.
## Findings
제안된 시스템은 대리 출석을 효과적으로 탐지하며, 생체 데이터를 저장하지 않는다.
## Conclusion
이 시스템은 출석 관리의 효율성을 높이고 법적 위험을 줄이는 데 기여할 수 있다.

# Key Findings
- RFID와 중량 센서를 통합하여 대리 출석 문제를 해결하였다.
- 생체 데이터 저장 없이 출석 확인이 가능하다.
- 저비용으로 재현 가능한 IoT 프로토타입을 개발하였다.

# Contributions
## Theoretical
비생체 인식 출석 시스템에 대한 새로운 이론적 기초를 제공한다.
## Methodological
질적 테스트를 통한 시스템의 통합 작동 검증 방법론을 제시한다.
## Practical
교육 기관에서의 출석 관리 효율성을 높이는 실용적인 솔루션을 제공한다.

# Limitations
- 시스템의 성능은 특정 환경에 국한될 수 있다.
- 대리 출석 탐지의 정확성은 중량 센서의 민감도에 의존한다.

# Transferable Insights
- 비생체 인식 기술의 활용 가능성을 보여준다.
- IoT 기반 시스템 설계의 유연성을 강조한다.

# Idea Seeds
1. 다양한 환경에서의 시스템 성능 평가 연구.
2. 다른 생체 인식 기술과의 통합 가능성 탐색.
3. 출석 관리 시스템의 사용자 경험 개선 방안 연구.

# Citation Snippets
> Ege, F., & Özdemir, M. (2026). RFID-Based Non-Biometric Classroom Attendance System: Proxy Attendance Detection via Weight Sensor Integration. arXiv. 

tags: #RFID, #출석시스템, #비생체인식, #중량센서, #IoT, #Arduino, #대리출석탐지

---

요약: 본 연구는 비생체 인식 IoT 출석 시스템을 제안하며, RFID와 중량 센서를 통합하여 대리 출석 문제를 해결하고자 한다. 이 시스템은 개인 생체 데이터를 저장하지 않으며, 저비용으로 재현 가능한 솔루션을 제공한다. 질적 테스트 결과, 시스템의 통합 작동이 기대한 대로 이루어짐을 확인하였다.
