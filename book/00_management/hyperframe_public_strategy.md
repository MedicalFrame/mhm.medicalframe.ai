# HyperFrame Suite 공개 전략 요약

기준일: 2026-06-28

## 0. 한 줄 요약

HyperFrame은 기존 EMR을 대체하지 않고, 기존 EMR 위에 붙는 open-source AI clinical workflow layer입니다.

핵심 문장:

> EMR을 바꾸지 않고, EMR 위의 일을 바꾼다.
>
> 의료진은 환자에게, 반복 업무는 HyperClick에게.

## 1. 제품 구조

HyperFrame Suite는 병원과 센터의 반복 업무를 줄이기 위한 여섯 개의 계층으로 구성됩니다.

- **HyperClick**
  - 말, 텍스트, 버튼으로 EMR 업무를 지시하는 command layer
- **HyperEMR**
  - 기존 EMR 옆에 켜지는 AI clinical cockpit
- **HyperRAG**
  - 병원 문서, FAQ, 지침, 연구자료 기반 RAG
- **HyperIRB**
  - 연구 변수 추출, IRB 문서, CSV/JSONL/SQL export 지원
- **HyperText / CleanText**
  - 비식별화, 문서 정리, 텍스트 클리닝
- **HyperLink**
  - 기존 EMR, API, MCP, CLI, export를 연결하는 integration layer

## 2. 도입 원칙

HyperFrame은 병원의 공식 기록 원장을 대체하지 않습니다.

기존 EMR은 처방, 검사, 기록, 법적 책임의 원장으로 유지합니다. HyperFrame은 그 옆에서 문진, 요약, SOAP 초안, 환자 설명문, 연구 변수 추출, 비식별화, 문서 RAG를 보조합니다.

운영 원칙:

- AI는 draft only로 작동합니다.
- 의료진이 최종 확인하고 승인합니다.
- 초기 단계는 read-only 또는 export 기반 workflow로 시작합니다.
- 접근권한, 로그, 개인정보 처리 원칙을 명확히 둡니다.
- 병원별 EMR 연동은 계약과 승인 구조 안에서 진행합니다.

## 3. Open-source 전략

기본 원칙:

> Core는 공개하고, 병원 운영·보안·연동·지원은 유료로 둔다.

공개 가능한 범위:

- HyperFrame core
- HyperClick demo
- OpenEMR connector
- mock patient dataset
- RAG pipeline
- CleanText
- HyperIRB basic extractor
- prompt templates
- architecture docs
- demo video

계약 기반 운영 범위:

- 병원 EMR connector
- on-prem deployment
- private inference
- RBAC
- audit log
- 보안 검토 문서
- SLA / support
- 병원별 workflow customization
- 연구/IRB pipeline 구축
- 다기관 registry 운영

## 4. PoC 가격 구조

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

월 300만-500만 원.

- 특정 진료과/센터 PoC
- audit log
- 사용자 계정
- KIS/export/API 연동 검토
- 전산팀 협의
- 보안/개인정보 원칙 문서화

### Hospital Enterprise

월 1,000만 원 이상 또는 별도 계약.

- 정식 EMR connector
- on-prem/private inference
- RBAC
- 보안 검토
- SLA
- 병원별 workflow customization
- 다기관 연구 registry

핵심 카피:

> 1억짜리 EMR 교체가 아니라, 월 100만 원짜리 AI workflow PoC부터.

## 5. 30일 실행 계획

### Week 1. Demo / Repo

- HyperFrame GitHub repo
- HyperClick demo
- OpenEMR backend
- HyperRAG chatbot
- HyperIRB 변수 추출
- HyperText 비식별화
- HyperLink API/MCP/CLI 구조
- 3분 데모 영상

### Week 2. 병원용 PoC 패키지

- 병원장용 1-page proposal
- 전산팀용 architecture note
- 보안/개인정보 원칙
- 가격표
- 1개월 PoC 계획서
- Mac Studio local LLM 구성
- GPU partner 확장안

### Week 3. 1호 병원/센터 적용

적용 후보:

- 대학병원 진료과 또는 센터
- 공익 의료기관
- 연구팀 또는 다기관 registry 준비팀

기능 후보:

- 환자 문의 답장 초안
- 센터 문서 RAG
- 외래 요약
- SOAP 초안
- 연구 변수 추출
- IRB 변수표 초안

### Week 4. 시장 메시지 공개

공개 문장:

> HyperFrame은 기존 EMR을 대체하지 않습니다.
>
> 기존 EMR 위에 붙는 open-source AI clinical workflow layer입니다.
>
> 병원은 월 100만 원 수준의 starter PoC부터 진료·연구·환자응대 workflow를 검증할 수 있습니다.

## 6. 파트너 생태계

HyperFrame의 본체 매출은 병원 PoC와 병원 운영 계약에서 발생합니다.

동시에 MedicalFrame Partners는 웹사이트, AI 업무 자동화, 고객응대 시스템, 데이터베이스 정리, 브랜딩 자료 제작을 제공하고, 파트너사는 공간, 인쇄, 촬영, 서버, 홍보 채널 같은 현실 운영 자원을 지원하는 방식으로 확장할 수 있습니다.

슬로건:

> We build your digital system. You power our real-world operations.
>
> 우리는 파트너사의 디지털 시스템을 만들고, 파트너사는 우리의 현실 운영을 지원합니다.

## 7. 최종 구조

- 병원은 핵심 매출과 의료 레퍼런스를 만든다.
- 작은 기업은 현물, 공간, 네트워크, 실전 케이스를 만든다.
- 의대생과 연구자는 미래 사용자와 커뮤니티가 된다.
- 오픈소스는 신뢰와 검증 가능성을 만든다.
- 유료 운영은 보안, 설치, 유지보수, 책임을 가능하게 한다.

HyperFrame은 병원 EMR 위 AI workflow layer를 선점하고, open-source core로 신뢰를 만들며, 병원 PoC와 파트너 생태계로 지속 가능한 공익 인프라를 만든다.
