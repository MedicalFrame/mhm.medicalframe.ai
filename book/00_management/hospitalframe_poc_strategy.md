# HospitalFrame / MedicalFrame PoC 전략

기준일: 2026-06-28

## 한 줄 결론

HospitalFrame은 기존 EMR을 교체하지 않고, 병원 진료·연구·행정 workflow 위에 AI layer를 얹어 업무 시간을 줄이고, 기록 품질을 높이며, 연구 데이터 구조화를 자동화하는 AI-native clinical workflow platform이다.

초기에는 특정 센터/진료과 3개월 PoC로 검증하고, 이후 KUH reference, 충주병원 multi-site deployment, 신규 smart hospital/greenfield package로 확장한다.

상위 제품군, 브랜드, 가격, 오픈소스, 현물 파트너십, 30일 실행계획은 `00_management/hyperframe_suite_strategy.md`를 기준으로 한다.

내부 구호:

> 센터 PoC로 들어가서, KUH reference 만들고, 충주까지 확장하고, 나중엔 HospitalFrame을 병원 OS로 박는다.

## 1. 제품 포지션

MedicalFrame/HospitalFrame은 EMR을 대체하는 회사가 아니라, 기존 EMR 위에 얹히는 AI clinical workflow layer다.

핵심 문장:

> 기존 EMR을 교체하는 것이 아니라, 병원 EMR 위에 AI workflow layer를 얹어 진료·연구·행정 업무를 자동화한다.

기능 후보:

- 진료 음성/텍스트 -> SOAP note 자동화
- 외래 기록 구조화
- 협진/검사/수술 workflow 자동화
- 환자 안내/문진/예약 응대
- 연구용 EMR 데이터 추출
- IRB/논문 pipeline 보조
- 병상/외래/수술 운영 dashboard
- 국제진료/외국인 환자 이메일 응대
- 정신과 narrative note/risk assessment 구조화
- GAHT/성소수자 의료 follow-up 관리

## 2. 현재 협상 구도

### EMR 업체

확인한 요구사항:

- EMR 초기 도입 비용
- 월 사용/유지 비용
- 연구용 EMR 또는 실증용 EMR 제공 가능성
- AI 모듈 API 연동 가능성
- EMR 화면 내 버튼/UI 추가 가능성
- 3개월 PoC 가능성
- 강동성심병원 또는 건대병원 단위 확장 가능성

구두상 나온 가능성:

- 일부 시스템 무상 제공 가능성
- 연구용 EMR 제공 가능성
- 5억 원 규모 용역/공동개발 과제 가능성
- 교수님-대표이사 미팅 가능성
- 대표이사/실무진 후속 논의 가능성

전략적 의미:

- 실무 영업 라인을 우회하고 영업이사/대표 라인으로 escalation한 상태
- 이후 커뮤니케이션은 영업이사/대표 라인으로 고정하는 것이 유리
- 가격보다 중요한 것은 AI 연동 가능성, 연구용 환경, PoC 지원 범위

### 서버/인프라 업체

협상 기준선:

> 고가 장비를 일시 구매하는 방식보다, 월 과금형 임대 또는 managed service 형태로 검토하고 싶습니다.

확인해야 할 조건:

| 항목 | 확인할 내용 |
| --- | --- |
| 계약 형태 | 임대, 리스, 구독형, managed service, rent-to-own |
| 계약 기간 | 3개월 PoC, 1년 약정, 3년 약정 |
| 유지보수 | 장애 대응, 부품 교체, 원격/현장 지원 포함 여부 |
| SLA | 장애 발생 시 대응 시간 |
| 설치비 | 초기 설치/세팅 비용 별도 여부 |
| 병원 내부망 | 내부망 설치 가능성, 외부 접속 조건 |
| 소유권 | 반납인지, 인수 옵션인지 |
| 증설 | GPU/RAM/storage 추가 비용 |
| 데이터 | 병원 데이터가 외부로 나가지 않는 구조인지 |

### PoC implementation partner 후보

좋은 후보의 조건:

- 대표 라인에서 가격, 조건, PoC, 계약 구조를 결정할 수 있음
- 개발자 라인에서 API, 서버, EMR 연동, 배포 구조를 논의할 수 있음
- 의료기관 workflow와 보안/운영 맥락을 이해함
- 너무 느리지 않고, 너무 불안정하지 않은 조직 규모
- 기술 언어가 잘 통함

확인할 것:

- 회사명
- 법인명
- 견적서 상호
- 계약 주체
- 대표/실무자 연락 라인

## 3. 3개월 PoC 전략

핵심 실행 계획:

> 특정 센터/진료과에서 3개월 PoC를 진행하고, 성과지표를 확보한 뒤 병원 내 확장 가능성을 만든다.

PoC 성공 기준은 반드시 숫자로 잡는다.

| 영역 | 성과지표 예시 |
| --- | --- |
| 진료기록 | SOAP note 작성 시간 30% 감소 |
| 행정 | 수술 예약/협진 요청 누락 감소 |
| 연구 | EMR 변수 추출 시간 감소 |
| 사용자 만족도 | 교수/코디/전공의 만족도 설문 |
| 안정성 | 개인정보 유출 0건, 장애 대응 기록 |
| 확장성 | 타과 적용 가능한 workflow template 확보 |

핵심 질문:

- 시간을 줄였는가?
- 누락을 줄였는가?
- 연구 데이터를 쉽게 만들었는가?
- 병원 업무를 덜 귀찮게 만들었는가?

## 4. LGBTQ+센터 / 강동성심병원 PoC 구조

초기 구조:

| 주체 | 얻는 것 |
| --- | --- |
| LGBTQ+센터/교수님 | EMR, 연구용 EMR, AI workflow, 서버/인프라를 무상 또는 저비용으로 실증 |
| EMR 회사 | 병원 레퍼런스, AI 연동 사례, 병원 확장 가능성 |
| 서버/AI 업체 | 의료기관 PoC, 병원 고객 진입, 공동개발/용역 기회 |
| MedicalFrame | 병원 workflow, PoC 실적, 교수진 레퍼런스, AI 플랫폼 검증 |

핵심:

센터에는 무상/저비용 실증 인프라를 가져다주고, MedicalFrame은 AI 플랫폼을 실제 병원 workflow에서 검증하고 사업화한다.

이 구조는 `교수님께 좋은 걸 공짜로 드리는 구조`이면서 동시에 `MedicalFrame의 첫 clinical validation site`다.

## 5. KUH reference site 전략

처음에는 LGBTQ+센터 PoC였지만, 전략은 더 크게 잡는다.

현실 언어:

> 건국대병원 내 소규모 PoC에서 시작해, 성과가 확인되면 병원 단위 확장 가능한 AI clinical workflow model로 키운다.

로드맵:

1. 센터/특정 진료과 3개월 PoC
2. 건대병원 내부 확장
3. KUH reference site 확보
4. 건대충주병원 적용
5. multi-site hospital deployment 검증
6. 신규 병원/스마트병원 package로 확장

즉, 센터 하나를 자동화하는 것이 아니라 KUH를 HospitalFrame의 첫 reference hospital로 만드는 전략이다.

## 6. Multi-site hospital AI operating layer

건국대병원 및 건국대충주병원을 초기 reference site로 삼아, 향후 권역별 신규 병원 또는 제휴 병원에 확장 가능한 AI clinical workflow platform을 구축한다.

| 사이트 | 역할 |
| --- | --- |
| 건대서울병원 | flagship tertiary reference, 고난도 진료/연구 |
| 건대충주병원 | regional hospital reference, 운영 효율화 모델 |
| 건대송도병원 | 국제진료/바이오/글로벌 임상시험 허브 |
| 건대청주병원 | greenfield smart hospital, AI-native 설계 |
| 건대전병원 | 충청권 연구·교육·산학협력 거점 |
| 건대구병원 | 영남권 확장/권역 네트워크 모델 |

이것은 `병원 많이 만들자`가 아니라 multi-site hospital AI operating layer 전략이다.

## 7. Greenfield hospital 비전

기존 병원 시스템 전환의 한계를 고려하면, 장기적으로는 신규 병원 또는 신규 센터 설립 단계에서 AI-native clinical workflow를 기본 인프라로 설계하는 greenfield model을 검토한다.

핵심은 건물을 짓는 것이 아니라 AI-native hospital operating model을 설계하는 것이다.

처음부터 들어가야 할 것:

- EMR이 AI 연동 가능
- 진료기록 자동 구조화
- 연구 데이터 자동 축적
- 문진/예약/검사/협진 workflow 자동화
- 병원 운영 dashboard 실시간 작동
- 교수/전공의/간호사/코디가 같은 cockpit 사용

## 8. 대형 수주의 현실적 의미

건대병원/충주병원/신규 병원/의과대학 구조를 묶으면 대형 digital transformation program이 될 수 있다.

다만 이것은 단일 AI 소프트웨어 계약이 아니라 multi-year hospital digital transformation program이다.

포함 범위:

| 범위 | 내용 |
| --- | --- |
| 병원 IT/인프라 | 서버, 네트워크, 보안, storage, 백업, 관제 |
| EMR/OCS/PACS 연동 | 기존 EMR wrapper, 신규 EMR, API, 데이터 이관 |
| AI clinical workflow | 진료기록, 문진, 환자응대, 협진, 검사/처방 보조 |
| Research/IRB platform | cohort search, chart review, 변수 추출, 비식별화 |
| 운영 command center | 병상, 외래, 수술, 검사, 인력 flow dashboard |
| 교육 플랫폼 | 의대/전공의/학생 clinical learning system |
| 유지보수/운영 | multi-year managed service, SLA, 교육, 고도화 |

MedicalFrame의 핵심 capture 영역:

- AI workflow layer
- orchestration
- data/research platform
- clinical workflow consulting
- 일부 PM/architecture
- long-term maintenance/software subscription

## 9. 전략적 파트너 판단 원칙

비플러스 또는 유사 파트너가 없어도 MedicalFrame PoC가 돌아간다면 운영권이나 주도권을 줄 이유는 없다.

다만 병원 채널, 납품, 운영, 인프라, 개발 리소스를 실제로 열어줄 수 있다면 제한적 전략 옵션은 검토 가능하다.

권장 구조:

1. MOU
2. 3개월 PoC
3. 실제 기여 확인
4. 성공 시 지분교환 또는 전략 제휴 옵션 검토

절대 넘기면 안 되는 것:

- 공동 IP
- 독점 영업권
- 병원 PoC 주도권
- 코드 접근권
- 무조건적 지분
- 공동대표/공동사업 명의

줄 수 있는 것:

- PoC 참여권
- 실제 기여 시 레퍼런스 공동 표기
- 특정 영역/기간 제한 공동영업
- 매출쉐어
- 지분교환 옵션
- 제한적 우선협상권

## 10. 트랜스젠더 의료 service line 구상

현실 언어:

> 트랜스젠더 의료를 비싸고, 흩어져 있고, 담당자마다 다른 의료에서 표준화·저비용·연속관리 가능한 service line으로 바꾼다.

### GAHT 모델

목표:

> 환자 본인부담을 최소화하는 합법적 저비용 GAHT pathway

구성:

| 구성 | 방향 |
| --- | --- |
| 진료 | 초진/재진 protocol 표준화 |
| 약제 | 저가 generic/standard regimen 정리 |
| 검사 | E2/T/liver/lipid/prolactin 등 follow-up panel 최적화 |
| 모니터링 | EstroFrame 기반 dose/lab interval 관리 |
| 문서 | 동의서, 안내문, 부작용 설명 자동화 |
| 비용지원 | 사회사업팀, 연구비, 기부금, 재단지원 |
| 보험 | 합법적 급여 가능 영역과 비급여 영역 분리 |

주의:

- 허위상병, 허위청구, 목적과 다른 급여처리는 절대 하지 않는다.
- 급여/비급여 판단은 병원 원무·심사·법무 검토를 거친다.

### 수술 service line

현실 구조:

> gender-affirming surgery service line을 위한 session-based surgeon 계약 또는 clinical advisor 계약

구성:

- 파트타임 수술 세션
- 특정 요일 gender-affirming surgery clinic
- 병원 간 협력/초빙 수술
- 수술 전후관리 pathway
- case volume 확보 후 전담 service line 확장

## 11. 역할 분리와 리스크

가장 중요한 리스크는 역할과 이해관계가 섞이는 것이다.

동시에 수행할 수 있는 역할:

1. 의대생/실습생
2. 교수님을 돕는 사람
3. 센터에 리소스를 가져오는 사람
4. AI 플랫폼 개발자
5. 회사/창업자
6. 업체와 협상하는 사람
7. 병원 PoC 설계자

반드시 분리해야 할 항목:

| 항목 | 정리 방식 |
| --- | --- |
| 병원/센터 | PoC site, clinical validation |
| 교수님 | clinical advisor 또는 PI |
| MedicalFrame | AI platform/IP owner |
| EMR/서버 업체 | 기술지원/인프라/연동 파트너 |
| 데이터 | 병원 소유, 승인/비식별 범위 내 사용 |
| 성과물 | PoC report와 제품 IP 분리 |
| 비용 | 무상지원, 연구비, 병원 구매, 용역 구분 |
| 보험/청구 | 합법적 급여/비급여 구조 분리 |
| 계약 | MOU, NDA, PoC agreement, 본계약 구분 |

특히 중요한 것:

- 병원 자원으로 개인 회사를 키우는 것처럼 보이지 않게 하기
- 교수님/병원/회사/업체의 역할을 문서화하기
- IP와 데이터 소유권을 명확히 하기
- 무상 PoC와 향후 유료 전환 조건을 분리하기
- 병원 전체 확장은 `약속`이 아니라 `성과 기반 검토`로 표현하기

## 12. KUH / HospitalFrame 3-month PoC 1-page proposal

### 문제

병원 EMR/기록/연구/행정 workflow에는 반복 입력, 비정형 기록, 연구 변수 추출, 환자 응대, 협진/검사/수술 flow 관리 병목이 존재한다.

### 해결

기존 EMR을 교체하지 않고, 그 위에 AI clinical workflow layer를 구축한다.

### PoC 범위

특정 센터 또는 진료과에서 3개월간 실증한다.

우선 후보:

- SOAP note 작성 보조
- 외래 기록 구조화
- 연구 변수 추출
- chart review workflow
- 문진/안내/예약 응대
- GAHT follow-up 관리

### 성과지표

- SOAP note 작성 시간 감소
- 수술 예약/협진 요청 누락 감소
- EMR 변수 추출 시간 감소
- 교수/코디/전공의 만족도
- 개인정보 유출 0건
- 장애 대응 기록
- 타과 적용 가능한 workflow template 확보

### 확장 가능성

PoC 결과가 확인되면 KUH 내 타과, 건대충주병원, multi-site hospital deployment로 확장 가능성을 검토한다.

## 13. 업체 비교표

| 업체 | 초기비 | 월비 | 무상 제공 | 연구용 EMR | API 연동 | UI 버튼 | 3개월 PoC | 연구용역 | 리스크 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 업체 A |  |  |  |  |  |  |  |  |  |
| 업체 B |  |  |  |  |  |  |  |  |  |
| 업체 C |  |  |  |  |  |  |  |  |  |

## 14. 역할분담표

| 주체 | 역할 | 제공 | 얻는 것 | 주의점 |
| --- | --- | --- | --- | --- |
| 병원/센터 | PoC site | workflow/data access | 업무개선/성과 | 데이터/보안 |
| 교수님 | clinical champion | 임상 검증 | 업적/센터 강화 | 이해상충 |
| MedicalFrame | AI platform | 제품/IP | validation/사업화 | IP 보호 |
| EMR 업체 | 시스템/연동 | EMR/API | 레퍼런스/납품 | lock-in |
| 서버 업체 | 인프라 | server/SLA | 의료기관 고객 | 보안/SLA |

## 15. NDA/MOU/PoC agreement 체크리스트

최소 포함:

- 비밀유지
- 각자 IP 보유
- 데이터 접근 범위
- 비식별화
- PoC 기간
- 비용/무상지원 범위
- 결과물 사용 가능 범위
- 레퍼런스 표기 조건
- 본계약 전 독점 없음
- 종료 후 자료/접근권 처리

주의:

- 실제 계약 문안은 법률 검토 전 초안으로만 다룬다.
- 병원 데이터와 환자정보가 포함되는 순간 IRB, 병원 승인, 보안 검토가 선행되어야 한다.
