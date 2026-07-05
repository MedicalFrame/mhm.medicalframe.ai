# HyperFrame Suite 사업 전략

기준일: 2026-06-28

## 0. 전체 한 줄 요약

HyperFrame은 기존 EMR을 갈아엎는 제품이 아니라, 기존 EMR 위에 붙는 open-source AI clinical workflow layer다.

병원 PoC를 본체 매출로 삼고, 주변 소기업·협력사는 AI 전환 패키지와 현물 자원을 교환하는 파트너 생태계로 키운다.

핵심 구호:

> 기존 EMR은 그대로, 옆에 AI workflow layer를 붙인다.
>
> EMR을 바꾸지 않고, EMR 위의 일을 바꾼다.
>
> 의료진은 환자에게, 반복 업무는 슈퍼딸깍에게.

## 1. 제품 구조

공식 제품군:

### HyperFrame Suite

- **HyperClick / 슈퍼딸깍**
  - 말·텍스트·버튼으로 EMR 업무를 지시하는 command layer
- **HyperEMR**
  - 기존 EMR 옆에 붙는 AI clinical cockpit
- **HyperRAG**
  - 병원/센터 문서, FAQ, 지침, 연구자료 기반 RAG
- **HyperIRB**
  - 연구 변수 추출, IRB 문서, CSV/JSONL/SQL export
- **HyperText / CleanText**
  - 비식별화, 문서 정리, 텍스트 클리닝
- **HyperLink**
  - 기존 EMR, API, MCP, CLI, export 연결 layer

## 2. 브랜드 / 밈 구조

공식명:

- HyperClick

한국어 제품명/데모명:

- 슈퍼딸깍

내부 밈:

- 으응딸깍

내부 예시:

- 으응 딸깍하면 그만이야.
- 으응 딸깍하면 논문 나와.
- 따알까악~ 외래 잡무가 사라지는 소리.

외부 공식 표현:

- HyperClick is a one-click clinical workflow assistant for existing EMRs.
- 슈퍼딸깍은 기존 EMR 옆에서 작동하는 AI clinical workflow assistant입니다.

주의:

- 내부 밈은 기억 장치로 사용한다.
- 병원장, 교수, 전산팀, 법무, IRB 문서에서는 공식명과 정제 문장을 사용한다.

## 3. PPT / 덱 구조 v2

초기 PPT는 에너지는 좋지만 병원장/교수/전산팀용으로 정제가 필요하다.

추천 목차:

1. Title
   - 슈퍼딸깍 / HyperClick
   - One-Click Clinical Workflow Assistant
2. Problem
   - 의료진은 환자를 봐야 하는데, EMR 업무가 시간을 먹는다.
3. Why Now
   - LLM, RAG, MCP, local inference로 EMR 옆 AI layer가 가능해졌다.
4. Core Idea
   - 기존 EMR은 그대로, 옆에 AI workflow layer.
5. HyperFrame Suite
   - HyperClick / HyperEMR / HyperRAG / HyperIRB / HyperText / HyperLink.
6. HyperClick
   - 말·텍스트·버튼으로 EMR 업무를 지시한다.
7. Clinical Workflow Demo
   - 환자 요약 -> SOAP 초안 -> 처방/예약/설명 초안 -> 의료진 승인.
8. Research Workflow Demo
   - 연구 변수 -> IRB -> CSV/JSONL/SQL -> Python 분석 -> 연구자 승인.
9. Hospital Setup
   - KIS 왼쪽, HyperEMR 오른쪽.
   - API / MCP / CLI / export 기반 modular integration.
10. Infrastructure
    - Mac Studio local LLM + H200 partner inference.
11. Safety & Governance
    - Draft only, human-in-the-loop, read-only first, audit log.
12. Open Source Strategy
    - Core open-source, 병원 운영/연동/보안/지원은 유료.
13. PoC Plan
    - 2일 demo -> 7일 public release -> 30일 hospital PoC.
14. Expected Impact
    - 의료진 시간 절감, 누락 감소, 연구 데이터 생성 시간 단축.
15. Closing
    - EMR을 바꾸지 않고, EMR 위의 일을 바꿉니다.

## 4. 내부 표현과 외부 표현

| 내부 표현 | 외부 표현 |
| --- | --- |
| 이지케어넥스트 좆됐다 | 고가 폐쇄형 구축형 솔루션에 대한 open-source 대안 |
| 내가 다 먹었다 | 의제를 선점했다 |
| 의료정보학회 내 거 | 의료정보학회 내 다음 agenda를 선점했다 |
| EMR 회사 잡아먹는다 | EMR 위 workflow layer 포지션을 선점한다 |
| 공짜로 받아낸다 | 현물 파트너십을 유치한다 |
| 돈 뜯어낸다 | 서비스 교환 구조를 만든다 |
| 가차 없이 자른다 | 수습 평가 후 계약 연장 여부를 결정한다 |
| 말단 직원 부린다 | 초기 운영보조 / 현장 오퍼레이터로 테스트한다 |

## 5. 시장 전략

### 국내

국내는 beachhead market이다.

목표:

> 한국에서 기존 EMR 위 AI workflow layer라는 포지션을 먼저 선점한다.

국내 전략 자산:

- 건국대병원 PoC
- 서울대 라인 학술 credibility
- 가톨릭/CMC 가치 alignment
- 부민병원 등 빠른 reference
- 의료정보학회/중계학술대회 agenda
- HyperFrame open-source repo
- 슈퍼딸깍 demo
- 병원장용 1-page proposal

### 미국

미국은 open-source + research credibility로 진입한다.

키워드:

- open-source
- EHR-agnostic
- vendor-neutral
- clinical workflow automation
- RAG for hospital knowledge
- de-identification
- human-in-the-loop
- local/private deployment

미국용 문장:

> HyperFrame is an open-source, EHR-agnostic AI workflow layer that helps clinicians generate chart summaries, drafts, patient replies, research variables, and de-identified text without replacing the existing EHR.

### 일본

일본은 보수적이므로 `혁명`보다 `기존 시스템 존중` 프레임으로 접근한다.

일본용 문장:

> 既存電子カルテを置き換えず、業務を支援するAIワークフローレイヤー

## 6. 경쟁 / 협력 지도

### 이지케어넥스트

포지션:

- 비교 대상
- 가격 파괴 대상
- 폐쇄형 구축형 AI EMR의 상징

전략:

- 직접 공격하지 않는다.
- 코드를 베끼지 않는다.
- 고가 구축형 모델과 비교한다.
- open-source core + 저비용 PoC + 빠른 demo로 우회한다.

핵심:

> 이지케어넥스트를 먹는 게 아니라, 이지케어넥스트가 비싸게 팔던 미래 서사를 무너뜨린다.

### BIT / B10

포지션:

- 협력사
- connector partner

이유:

- HyperFrame은 모든 EMR 위에 붙어야 한다.
- 특정 EMR 업체를 전부 적으로 만들면 안 된다.

공식 문장:

> 귀사의 기존 EMR 고객에게 HyperFrame AI workflow layer를 붙이면, EMR 교체 없이 AI 요약·SOAP 초안·문서 RAG·연구 변수 추출 기능을 빠르게 제공할 수 있습니다.

### 의사랑

포지션:

1. 연동 후보
2. 협력 후보
3. 후속 인수 후보

접근:

- 처음부터 인수가 아니라 HyperLink connector로 접근한다.

### 가톨릭 / CMC

접근:

- 종교적 소속을 노골적인 거래 명분으로 쓰지 않는다.
- 공동선, 의료 접근성, 환자 중심 가치로 접근한다.

공식 문장:

> 의료 AI가 특정 회사의 폐쇄형 자산이 아니라, 환자와 의료진을 위한 공공적 인프라가 되어야 한다고 봅니다. 가톨릭 의료기관의 환자 중심 가치와도 잘 맞는 방향이라고 생각합니다.

## 7. Open-source 전략

기본 원칙:

> Core는 무료 공개, 병원 운영·보안·연동·지원은 유료.

공개할 것:

- HyperFrame core
- HyperClick demo
- OpenEMR connector
- MCP server
- mock patient dataset
- RAG pipeline
- CleanText
- HyperIRB basic extractor
- prompt templates
- architecture docs
- demo video

유료화할 것:

- 병원 EMR connector
- on-prem deployment
- private inference
- RBAC
- audit log
- 보안 검토 문서
- SLA/support
- 병원별 workflow customization
- 연구/IRB pipeline 구축
- 다기관 registry 운영

## 8. 가격 전략

### Community

무료.

- GitHub 공개
- OpenEMR demo
- synthetic data
- local install

### Clinic / Center Starter

월 100만 원부터.

- 문서 RAG
- 환자 답장 초안
- SOAP 초안
- 연구 변수 추출
- 비식별화
- export 기반 workflow

### Department PoC

월 300만~500만 원.

- 특정 진료과/센터 PoC
- audit log
- 사용자 계정
- KIS/export/API 연동 검토

### Hospital Enterprise

월 1,000만 원 이상.

- 정식 EMR connector
- on-prem/private inference
- RBAC
- 보안 검토
- SLA
- 병원별 workflow customization

핵심 카피:

> 1억짜리 EMR 교체가 아니라, 월 100만 원짜리 AI workflow PoC부터.
>
> Open-source core. Free integration pilot. Starter PoC from KRW 1M/month.

## 9. 인프라 전략

### Mac Studio

센터/진료과 PoC용.

- local LLM
- 문서 RAG
- SOAP 초안
- 환자 답장 초안
- 연구 변수 추출
- 비식별화
- 외부망 차단 데모

### H200 / GPU 파트너

병원 확장/다기관 연구/대량 batch용.

- H200급 인프라 협찬 가능성
- 현물 지원 대가로 acknowledgement, technical partner 표기, 데모/논문/학회 노출
- 단순 인프라 제공은 공동저자보다 acknowledgement가 적절
- 실질 연구 설계·분석 기여 시 공동저자 검토

핵심 문장:

> Mac Studio로 진료실 딸깍, H200으로 병원/연구 확장 딸깍.

## 10. MedicalFrame Partners / 현물 파트너십

핵심:

> 디지털 부가가치를 거의 0에 가까운 한계비용으로 생산해서, 상대가 가진 물리 자원·유통망·레퍼런스·공간·차량·인쇄·촬영·고객망과 교환한다.

제공할 수 있는 것:

- 회사 홈페이지
- 랜딩페이지
- 예약/문의 폼
- AI 전화/문의응대
- 고객 DB
- 견적서 자동화
- 브로셔/PPT
- 블로그/SEO
- Notion/CRM/Google Workspace 세팅
- AI 업무 자동화 컨설팅
- 출판/인쇄 workflow
- 의료 공부 플랫폼

받을 수 있는 것:

- 차량
- 사무실/회의실
- 인쇄
- 사진/영상
- 서버/GPU
- 법무/세무/노무
- 홍보 채널
- 병원/기업 소개
- 물건/서비스

외부용 표현:

> 저희는 초기 파트너사에 웹사이트, AI 업무 자동화, 고객응대 시스템, 데이터베이스 정리, 브랜딩 자료 제작 등을 제공합니다.
>
> 대신 파트너사는 차량, 공간, 인쇄, 촬영, 서버, 홍보 채널 등 필요한 자원을 현물로 지원합니다.
>
> 단순 협찬이 아니라, AI 시대에 서로의 자산을 교환하는 파트너십 구조입니다.

슬로건:

> We build your digital system. You power our real-world operations.
>
> 우리는 파트너사의 디지털 시스템을 만들고, 파트너사는 우리의 현실 운영을 지원합니다.

## 11. 작은 기업 AI 전환 전략

작은 기업은 당장 현금 매출원이 아니라 다음을 얻는 채널이다.

- 현물 자원
- 레퍼런스
- 네트워크
- 유통망
- 실전 케이스

### Small Business AI Starter Pack

제공 범위:

- 랜딩페이지 1개
- 최대 5개 섹션
- 문의폼 1개
- 카카오톡/이메일 연결
- Google Sheet 또는 Notion DB
- AI 문의응대 초안
- 기본 소개문/서비스 문구 정리
- 1회 수정

제외 범위:

- 쇼핑몰
- 결제
- 회원가입
- 복잡한 예약 시스템
- 커스텀 관리자 페이지
- 무제한 유지보수
- 무제한 수정

핵심 원칙:

> 무료로 해주는 건 맞춤 외주가 아니라 템플릿 상품만.

## 12. 출판 / 인쇄 / 교육 플랫폼

### 출판사 / 인쇄소

연결 대상:

- 브런치북
- 의료 공부 자료
- HyperFrame 백서
- 학회 포스터
- 브로셔
- 소량 인쇄/POD

이름 후보:

- MedicalFrame Press
- Jisong Press

### 의대생 무료 플랫폼

제공:

- KMLE/CPX 자료
- Anki 카드
- 임상 요약
- AI 공부 도구
- 논문 읽기 도구
- 연구 자동화 템플릿

목적:

> 무료 의료 공부 플랫폼 = 미래 의사 사용자 확보 + 브랜드 신뢰 + 병원 내부 챔피언 양성.

## 13. AI-assisted Counseling Workflow

위험한 표현:

- AI가 상담한다
- AI가 치료한다
- AI가 진단한다

안전한 표현:

> 상담자/임상심리사가 상담을 더 잘 운영하도록 돕는 AI-assisted counseling workflow.

가능 기능:

- 사전 문진
- 상담 목표 정리
- 세션 요약 초안
- 다음 회기 계획 초안
- 숙제/워크시트 생성
- 감정 기록 정리
- 위험 신호 체크리스트
- 상담자용 기록 보조
- 내담자용 psychoeducation 자료 초안

필수 안전장치:

- AI는 상담자를 대체하지 않음
- 진단/치료 결정은 전문가가 수행
- 자살/자해/폭력 위험은 즉시 사람에게 escalation
- 민감정보 저장 최소화
- 동의서/개인정보 처리방침 필요
- 기록은 전문가 검토 후 확정

## 14. 초기 운영보조 / 현장 오퍼레이터 후보

해석:

- 개발자/기획자가 아니라 초기 운영보조 / 현장 오퍼레이터 후보

바로 하면 안 되는 것:

- 바로 서울로 부르기
- 바로 차 제공
- 바로 숙소 제공
- 바로 회사 카드 제공
- 병원/교수/협력사 연락처 전체 공유
- 외부에서 MedicalFrame 대표처럼 말하게 하기

### 1단계: 1주 유급 테스트

볼 것:

- 연락이 되는가
- 약속을 지키는가
- 보고를 남기는가
- 거짓말을 안 하는가
- 단순 지시를 끝까지 하는가

### 2단계: 1개월 운영보조

직무명:

- MedicalFrame Operations Assistant

역할:

- 인쇄물 수령/배송
- 명함/브로셔/포스터 픽업
- 협력업체 방문/사진 기록
- 미팅 장소 세팅
- 장비 구매/수령/반납
- 병원/학회/업체 미팅 준비물 운반
- 파트너 업체 리스트 정리
- 카톡방 지시사항 수행 후 완료 보고

### 3단계: 운영 매니저 후보

역할:

- 일정 관리
- 협력업체 연락
- 견적/영수증 정리
- 외주 인력 1명 관리

### 4단계: Logistics Lead

역할:

- 물류/현장 운영 총괄
- 신규 보조 인력 교육
- 파트너사 일정 조율
- 행사/학회/병원 미팅 세팅

### KPI

- 시간 약속 지키기
- 연락 10분 내 확인
- 지시사항 누락 없이 완료
- 영수증/사진/위치/완료보고 남기기
- 거짓말 안 하기
- 사고 안 치기

### 카톡 지시 양식

```text
[업무 지시]
1. 업무:
2. 장소:
3. 마감시간:
4. 준비물:
5. 비용 한도:
6. 완료보고 방식:
   - 사진
   - 영수증
   - 위치
   - 완료 메시지
7. 특이사항:
```

## 15. 노동 / 계약 리스크

필수:

- 고용 형태 명확화
- 월 보수의 의미 명확화
- 근무시간/휴무/업무범위 명시
- 근로계약서 또는 업무계약서 작성
- 보안/비밀유지 조항
- 산출물 귀속 조항
- 차량/숙소 제공 시 책임범위 명시

금지 표현:

- 가차 없이 자른다

대체 표현:

> 1개월 계약으로 먼저 시작하고, 기간 종료 시 산출물과 근무태도 평가 후 연장 여부를 결정한다.

## 16. 공간 / 차량 현물 지원

### 차량

가능하지만 리스크가 크다.

반드시 문서화:

- 보험
- 사고 책임
- 유류비
- 과태료
- 개인 사용 금지
- 운전자 범위
- 운행기록
- 반납 조건

### 오피스텔 / 사무실

핵심은 `집`이 아니라 MedicalFrame 초기 개발·PoC 거점 공간이다.

공식 문장:

> 초기 병원 PoC와 파트너 미팅을 위한 개발 거점/회의 공간이 필요합니다.
>
> 귀사가 3~6개월 공간을 현물 지원해주시면, 저희는 귀사에 AI 전환 패키지와 업무 자동화 컨설팅을 제공하겠습니다.

우선순위:

1. 공유오피스 / 코워킹 스페이스
2. 빌딩 내 빈 사무실/회의실
3. 오피스텔 사무용 사용
4. 개인 주거 형태 아파트/오피스텔은 비추천

## 17. 30일 실행계획

### Week 1: Demo / Repo

- HyperFrame GitHub repo
- HyperClick demo
- OpenEMR backend
- HyperRAG chatbot
- HyperIRB 변수 추출
- HyperText 비식별화
- HyperLink API/MCP/CLI 구조
- 3분 데모 영상

### Week 2: 병원용 PoC 패키지

- 병원장용 1-page proposal
- 전산팀용 architecture
- 보안/개인정보 원칙
- 가격표
- 1개월 PoC 계획서
- Mac Studio local LLM 구성
- H200 partner 확장안

### Week 3: 1호 병원/센터 적용

후보:

- 건국대병원 AI Clinical Workflow TF
- 강동성심 LGBTQ+센터
- 부민병원
- 서울대병원 연구팀/교수 라인

기능:

- 환자 문의 답장 초안
- 센터 문서 RAG
- 외래 요약
- SOAP 초안
- 연구 변수 추출
- IRB 변수표 초안

### Week 4: 시장 메시지 공개

공개 문장:

> HyperFrame은 기존 EMR을 대체하지 않습니다.
>
> 기존 EMR 위에 붙는 open-source AI clinical workflow layer입니다.
>
> 병원은 월 100만 원 수준의 starter PoC부터 진료·연구·환자응대 workflow를 검증할 수 있습니다.

## 18. 최종 사업 구조

가장 깔끔한 정리:

- 병원은 돈.
- 작은 기업은 자원.
- 의대생은 미래 사용자.
- 상담센터는 확장 시장.
- 오픈소스는 신뢰와 확산.

전체 구조:

- Hospital / MedicalFrame
  - 핵심 매출, 병원 PoC, 의료 레퍼런스
- Small Business AI Transformation
  - 현물, 공간, 차량, 인쇄, 촬영, 네트워크
- Medical Student Platform
  - 무료 배포, 브랜드 확산, 미래 의료진 사용자 확보
- AI-assisted Counseling Workflow
  - 병원 밖 확장 제품, 상담자/센터용 운영 자동화
- Open Source HyperFrame
  - 신뢰, 개발자 커뮤니티, 글로벌 확장

## 19. 가장 중요한 운영 원칙

### 말보다 산출물

상대를 흔드는 건 욕이 아니라:

- GitHub repo
- demo video
- 병원장용 1-page
- PPT v2
- PoC 가격표
- 파트너 제안서
- 실제 돌아가는 화면

### 무료는 템플릿만

무료/현물 교환은 가능하지만 반드시 scope를 잘라야 한다.

> 무료로 해주는 건 맞춤 외주가 아니라 템플릿 상품만.

### 사람은 단계적으로

1주 유급 테스트 -> 1개월 수습 -> 정식 합류.

### 외부 언어는 정제

내부 에너지는 유지하되, 외부에는 항상 다음 언어로 말한다.

- vendor-neutral
- open-source
- workflow layer
- human-in-the-loop
- draft only
- hospital PoC
- partner ecosystem
- 현물 파트너십
- AI 전환 패키지

## 20. 최종 한 줄

HyperFrame으로 병원 EMR 위 AI workflow layer를 선점하고, 슈퍼딸깍으로 데모와 기억을 먹고, 오픈소스로 신뢰를 만들고, 작은 기업 AI 전환으로 현물 파트너 생태계를 만들고, 그 자원으로 병원 PoC와 해외 확장을 밀어붙인다.
