# MHMbook 1차 빌드 검수 보고서

기준일: 2026-06-28

## 0. 결론

`나는 딴 돈의 절반만 가져가`는 9부 28장 책/웹사이트 패키지로 구성되었다.

- 책 원고: 9부 + 28장 + 프롤로그 + 에필로그 본문형 초안
- 합본 Markdown: `book_manuscript/book.md`
- 배포용 Markdown: `output/mhmbook-draft.md`
- 배포용 PDF: `output/pdf/MHMbook.pdf`
- 웹사이트: `mhm.medicalframe.ai/index.html`
- 삽화: 부별 삽화 9장 + 정식 표지 이미지
- 자산/라이선스: MedicalFrame Inc. company asset, Open Source MIT License

## 1. 원고 상태

- 전체 원고 단어 수: 18,513 words
- 메모형 섹션 잔여: 0개
- 본문형 구성:
  - 프롤로그 1개
  - 부 제목 9개
  - 본문 28장
  - 에필로그 1개
  - 부별 삽화 9장
  - MIT 라이선스 표기

검수 명령 결과 요약:

- `rg "^## 역할$|^## 핵심 논지$|^## 주요 내용$|^## 초안 메모$" ...`: 결과 없음
- `book_manuscript/book.md`, `output/mhmbook-draft.md`, `mhm.medicalframe.ai/downloads/mhmbook-draft.md`: 모두 18,513 words
- 9부 제목과 9개 삽화 링크가 합본 원고에 반영됨
- 예전 제목 표기, 예전 축약 표기, 예전 부제 표시 검색 결과 없음

## 2. PDF 상태

- PDF 파일: `output/pdf/MHMbook.pdf`
- 웹 배포 PDF: `mhm.medicalframe.ai/downloads/MHMbook.pdf`
- 페이지 수: 129쪽
- 판형: A5
- PDF 해시: 양쪽 파일 동일
- PDF 제목 메타데이터: `나는 딴 돈의 절반만 가져가`
- PDF 텍스트 레이어에서 `company asset`과 `MIT` 검색 확인
- PDF 이미지 리소스: 10개
  - 정식 표지 이미지 1개
  - 부별 삽화 9개
- 표지, 목차, 1부 삽화 페이지 샘플 렌더링 확인 완료
- 표지에 `MedicalFrame Inc. company asset` 및 `Open Source MIT License` 표기

PDF 내 부 시작 페이지:

- 1부: 9쪽
- 2부: 22쪽
- 3부: 35쪽
- 4부: 47쪽
- 5부: 60쪽
- 6부: 74쪽
- 7부: 86쪽
- 8부: 105쪽
- 9부: 117쪽

## 3. 웹사이트 상태

- 사이트 폴더: `mhm.medicalframe.ai/`
- 첫 화면 CTA:
  - PDF 다운로드
  - 책 원고 보기
  - HyperFrame 전략 보기
- 첫 화면 표지: `assets/cover/book-cover.png`
- 공개 표기: `MedicalFrame Inc. company asset · Open Source MIT License`
- 목차 카드:
  - 9부 카드
  - 부별 삽화 9장
- 외부 공개용 전략 문서 사용: `downloads/hyperframe-strategy.md`
- 내부 위험 표현 검색: 결과 없음
- HTML 링크/이미지 검사: 참조 24개, 누락 0개
- `LICENSE` 공개 파일 존재 확인
- 브라우저 검수:
  - 데스크톱/모바일 콘솔 오류 없음
  - 이미지 깨짐 없음: 표지 1장 + 부별 삽화 9장
  - 가로 넘침 0
  - PDF 링크 감지됨
  - 목차 앵커 이동 정상
  - 모바일 390px 폭에서 버튼과 목차 카드 폭 정상

## 4. 공개 범위

웹사이트에는 외부 공개용 문서만 연결한다.

- 공개:
  - PDF 초안
  - Markdown 원고 초안
  - 정제된 HyperFrame 공개 전략 요약
- 비공개/관리 문서:
  - 내부 표현이 포함된 원본 전략 메모
  - 사건 대응 상세 문서
  - 병원별 운영/연동/보안 세부

## 5. 후속 개선

다음 라운드에서 품질을 더 올릴 수 있는 작업:

- 문장 단위 카피에디팅
- PDF 서체 개선
- 표지 전용 이미지 또는 정식 표지 제작
- 병원장용 1-page proposal 추가
- 전산팀용 architecture note 추가
- DOCX/EPUB 출력 추가 여부 결정
