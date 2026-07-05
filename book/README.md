# MHMbook

`MHMbook`은 새 책 **「나는 딴 돈의 절반만 가져가」**를 관리하는 원고 프로젝트입니다.

프로젝트 코드명은 **MHM**입니다. 현재 단계에서는 확장명을 고정하지 않고, 책의 작업 코드로만 사용합니다.

## 책 개요

- **작업 제목:** 나는 딴 돈의 절반만 가져가
- **원문 seed 제목:** 나는 딴 돈의 절반만 가져가
- **부제:** 사회기업윤리와 공익 인프라의 원칙
- **핵심 구조:** 도발적인 입구 -> 사회기업윤리 -> Medical Frame/OpenFrame 모델 -> AI EMR 사례 -> 방해/저항 대응 -> 실행 선언
- **원고 형식:** Markdown
- **현재 산출물:** 합본 Markdown, PDF 초안, 웹 공개 페이지
- **자산/라이선스:** MedicalFrame Inc. company asset, Open Source MIT License

## 핵심 선언

- 기업은 사회 밖에서 돈을 벌지 않는다.
- 의료, 교육, 연구는 인간의 기반이므로 무상 접근을 원칙으로 해야 한다.
- 돈 있는 곳에서 정당하게 벌고, 돈 없는 곳에는 인프라를 나눈다.
- Medical Frame은 만들고 벌며, OpenFrame은 공개하고 나눈다.
- 공익은 선언이 아니라 설치, 교육, 문서화, 유지보수로 증명된다.

## 폴더 구조

- `book_manuscript/`: 실제 원고와 장별 초안
- `assets/cover/`: 표지 배경과 최종 표지 PNG
- `assets/illustrations/`: 부별 삽화 9장
- `00_management/`: 기획, 목차, 운영 기준
- `output/`: 합본 Markdown과 PDF 산출물
- `tasks/`: 작업 TODO와 교훈
- `LICENSE`: MIT License

## 현재 운영 기준

현재는 원고, PDF, 웹사이트를 함께 갱신합니다.

빌드 기준은 다음과 같습니다.

- 책 제목: `나는 딴 돈의 절반만 가져가`
- 부제: `사회기업윤리와 공익 인프라의 원칙`
- 구조: 9부 28장 + 프롤로그 + 에필로그
- 삽화: 부별 삽화 9장
- 표지: `assets/cover/book-cover.png`
- 라이선스: MIT License, copyright MedicalFrame Inc.
- 공개 산출물: Markdown 초안, PDF 초안, `mhm.medicalframe.ai` 정적 웹사이트

합본은 `00_management/scripts/build_mhmbook.py`, PDF는 `00_management/scripts/build_mhmbook_pdf.py`로 생성합니다.

## 참고 문서

- 책 기획 요약: `00_management/book_brief.md`
- 장별 지도: `00_management/chapter_map.md`
- 외부 대응 패키지: `00_management/external_response_pack.md`
- 의료정보학회 사건 대응 전략: `00_management/medical_informatics_incident_response.md`
- HyperFrame Suite 사업 전략: `00_management/hyperframe_suite_strategy.md`
- HospitalFrame PoC 전략: `00_management/hospitalframe_poc_strategy.md`
- 원고 목차: `book_manuscript/README.md`
- 합본 초안: `book_manuscript/book.md`
- 작업 TODO: `tasks/todo.md`
- 작업 교훈: `tasks/lessons.md`
