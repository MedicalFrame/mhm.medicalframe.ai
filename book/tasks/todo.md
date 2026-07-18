# MHMbook 작업 TODO

기준일: 2026-06-28

## 현재 상태 요약

- 새 책 프로젝트 코드명을 `MHM`으로 두었다.
- 정식 작업 제목은 `나는 딴 돈의 절반만 가져가`로 시작한다.
- 붙여준 원문 seed와 새 7부 구성을 기준으로 9부 28장 구조를 세웠다.
- 오늘 외부 대응 원칙을 `00_management/external_response_pack.md`로 정리했다.
- HospitalFrame/KUH 3개월 PoC 전략을 `00_management/hospitalframe_poc_strategy.md`로 정리했다.
- 의료정보학회 사건 대응 전략을 `00_management/medical_informatics_incident_response.md`로 정리했다.
- HyperFrame Suite 사업 전략을 `00_management/hyperframe_suite_strategy.md`로 정리했다.
- 책과 웹사이트를 함께 제작하는 계획을 `00_management/book_website_production_plan.md`로 정리했다.
- `mhm.medicalframe.ai/` 정적 웹사이트 1차 구현을 완료했다.
- 정식 표지 `assets/cover/book-cover.png`를 생성했다.
- 회사 자산 공개 기준을 `Open Source MIT License`로 정리했다.
- 9부 체계와 부별 삽화 9장을 원고, PDF, 웹사이트에 반영했다.
- 현재 단계에서는 Markdown/PDF/웹 배포 산출물을 함께 갱신한다.
- 2026-07-05 기준 원본 소스는 `mhm.medicalframe.ai/book/` 아래로 흡수했고, 공개 다운로드는 `downloads/`에서 관리한다.
- PDF 생성은 `reportlab`이 포함된 번들 파이썬 런타임으로 검증했다.
- 2026-07-12 기준 브런치 삽화 정본은 비공개 저장소 `jsbang01357/MHMbook-assets`이며, 전체 90장을 동기화했다.

## 1) 프로젝트 세팅

- [x] `MHMbook/` 폴더 생성
- [x] `README.md` 작성
- [x] `tasks/todo.md` 작성
- [x] `tasks/lessons.md` 작성
- [x] `00_management/book_brief.md` 작성
- [x] `00_management/chapter_map.md` 작성
- [x] `00_management/external_response_pack.md` 작성
- [x] `00_management/hospitalframe_poc_strategy.md` 작성
- [x] `00_management/medical_informatics_incident_response.md` 작성
- [x] `00_management/hyperframe_suite_strategy.md` 작성
- [x] `00_management/hyperframe_public_strategy.md` 작성
- [x] `00_management/book_website_production_plan.md` 작성
- [x] `book_manuscript/README.md` 작성
- [x] `book_manuscript/book.md` 작성
- [x] 장별 초안 파일 생성

## 2) 제목 / 포지셔닝

- [x] 제목 표기 확정: `나는 딴 돈의 절반만 가져가`
- [x] MHM은 확장명 없이 책 프로젝트 코드명으로 유지
- [x] 부제 확정: `사회기업윤리와 공익 인프라의 원칙`
- [x] 자산/라이선스 표기 확정: `MedicalFrame Inc. company asset · Open Source MIT License`
- [x] 프롤로그의 도발 수위 1차 확정

## 3) 원고 작성

- [x] 프롤로그 1차 초안 작성
- [x] 1부: 기업은 사회 밖에서 살 수 없다
- [x] 2부: 나는 딴 돈의 절반만 가져가
- [x] 3부: 의료, 교육, 연구는 모두의 것이다
- [x] 4부: Medical Frame과 OpenFrame 모델
  - [x] 10장에 HyperFrame open-source / 유료 운영 분리 원칙을 본문형 원고로 확장
- [x] 5부: AI EMR 선언
  - [x] 14-15장에 HospitalFrame/KUH PoC 전략을 본문형 원고로 확장
  - [x] 14장에 HyperFrame Suite 제품 구조를 본문형 원고로 확장
- [x] 6부: 무료 배포는 마케팅이 아니라 실증이다
  - [x] 18장에 3개월 PoC 성과지표를 본문형 원고로 확장
- [x] 7부: 방해와 저항을 다루는 법
  - [x] 20장에 외부 대응 원칙을 본문형 원고로 확장
  - [x] 의료정보학회 사건은 실명 없이 구조화 사례로 재구성
- [x] 8부: 절반만 가져가는 회사의 운영 원칙
  - [x] 23장에 HyperFrame 가격 전략을 본문형 원고로 확장
- [x] 9부: 새로운 기업윤리 선언
- [x] 에필로그 1차 초안 작성

## 4) 검토 포인트

- [x] 개인 밈이 사회기업윤리로 자연스럽게 승격되는지 확인
- [x] Medical Frame / OpenFrame / 지송재단 역할이 혼동되지 않는지 확인
- [x] 무료 제공 원칙이 지속 가능한 수익 구조와 연결되는지 확인
- [x] AI EMR 공개 주장이 개인정보, 안전, 의료진 최종 판단 원칙과 함께 설명되는지 확인
- [x] `절반만 가져가`가 단순 기부론이 아니라 운영 원칙으로 서는지 확인

## 5) 이후 자동화

- [x] 원고가 3장 이상 작성되면 합본 스크립트 추가 여부 판단
- [x] `00_management/scripts/build_mhmbook.py` 합본 스크립트 추가
- [x] PDF 출력 파이프라인 추가
- [x] `00_management/scripts/build_mhmbook_pdf.py` PDF 초안 생성 스크립트 추가
- [x] PDF 표지에 정식 표지 PNG 연결
- [ ] DOCX / EPUB 출력 파이프라인 필요 여부 결정
- [x] 웹 공개용 README와 배포 메모 작성

## 6) 웹사이트 / 공개 페이지

- [x] `mhm.medicalframe.ai/` 폴더 생성
- [x] 웹사이트 히어로 이미지 생성 및 `assets/hero-workflow.png` 배치
- [x] 책 표지 생성 및 `assets/cover/book-cover.png` 배치
- [x] 부별 삽화 9장 생성 및 `assets/illustrations/part-01.png`-`part-09.png` 배치
- [x] 책 원고 초안 스냅샷을 `downloads/mhmbook-draft.md`로 배치
- [x] HyperFrame 전략 스냅샷을 `downloads/hyperframe-strategy.md`로 배치
- [x] 외부 공개용 HyperFrame 전략 문서로 다운로드 파일 정제
- [x] `index.html` 1차 구현
- [x] `styles.css` 1차 구현
- [x] `README.md`와 `CNAME` 작성
- [x] 로컬 브라우저 렌더링 확인
- [x] 모바일 폭에서 텍스트 겹침 확인
- [x] PDF 초안 생성 후 다운로드 링크 연결
- [x] 웹 목차 카드에 부별 삽화 연결
- [x] `LICENSE` 파일 추가
- [x] 웹 첫 화면에 회사 자산/MIT 표기 추가
- [x] 원본 소스를 `mhm.medicalframe.ai/book/` 아래로 흡수
- [x] `book/output/pdf/MHMbook.pdf`와 `downloads/MHMbook.pdf` 해시 일치 확인
- [x] `book/output/mhmbook-draft.md`와 `downloads/mhmbook-draft.md` 해시 일치 확인

## 7) 브런치 연재화

- [x] 브런치 연재 목표 확정: 책의 장별 원고를 책 순서대로 브런치 글로 전환
- [x] 1차 발행 묶음 확정: 1장부터 5장까지 회사 철학 글 5편
- [x] 1차 발행용 삽화 5장 생성 및 `brunch/assets/illustrations/`에 복사
- [x] 발행 순서, 삽화 매핑, 변환 규칙을 `brunch/README.md`에 정리
- [x] 전체 책 30개 브런치 원고를 `brunch/posts/`에 생성
- [x] 전체 글에 삽화 3장 슬롯과 생성 프롬프트 큐 생성
- [x] 삽화 기준 갱신: 중심 인물은 여성 주인공으로 통일하고 주변 인물은 다양하게 구성
- [x] 삽화 기준 갱신: 2:1 가로형으로 통일
- [x] 프롤로그 원고 기반 맞춤 삽화 3장 생성 및 기존 정사각형 이미지 교체
- [x] 1장 원고 기반 맞춤 삽화 3장 생성 및 기존 정사각형 이미지 교체
- [x] 2장 원고 기반 맞춤 삽화 3장 생성 및 기존 정사각형 이미지 교체
- [x] 3장 원고 기반 맞춤 삽화 3장 생성 및 기존 정사각형 이미지 교체
- [x] 4장 원고 기반 맞춤 삽화 3장 생성 및 기존 정사각형 이미지 교체
- [x] 5장 원고 기반 맞춤 삽화 3장 생성 및 기존 정사각형 이미지 교체
- [x] 프롤로그-5장 삽화 18장 2:1 비율 검수
- [x] `jsbang01357/MHMbook-assets`에서 전체 삽화 90장을 동기화
- [x] `brunch/manifest.md` 기준으로 전체 이미지 누락 여부 최종 확인 (`90/90`, 누락 0)
- [x] 15장 `작은 병원부터 좋은 시스템을 쓴다`에 커버 1장과 본문 삽화 3장을 배치하고 브런치 초안 저장
- [ ] 1장 `기업은 혼자 돈을 벌지 않는다` 브런치 발행용 본문 최종 점검
- [ ] 2장 `사회기업윤리란 무엇인가` 브런치 발행용 본문 최종 점검
- [ ] 3장 `탐욕은 성장 전략이 아니다` 브런치 발행용 본문 최종 점검
- [ ] 4장 `절반만 가져간다는 것` 브런치 발행용 본문 최종 점검
- [ ] 5장 `돈 있는 곳에서 벌고, 돈 없는 곳에는 나눈다` 브런치 발행용 본문 최종 점검
