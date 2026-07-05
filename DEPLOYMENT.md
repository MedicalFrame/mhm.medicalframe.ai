# mhm.medicalframe.ai 배포 메모

## GitHub Pages

- Repository: `https://github.com/MedicalFrame/mhm.medicalframe.ai`
- Pages source: `main` branch, repository root
- Custom domain: `mhm.medicalframe.ai`
- CNAME file: `CNAME`
- HTTPS: Cloudflare에서 제공
- Canonical book source: `book/`

## 현재 산출물

- `index.html`: 공개 웹사이트
- `styles.css`: 스타일
- `assets/cover/book-cover.png`: 책 표지 및 웹 히어로 이미지
- `assets/cover/cover-art.png`: 표지 배경 원본
- `assets/hero-workflow.png`: 초기 HyperFrame 히어로 콘셉트 이미지
- `assets/illustrations/part-01.png`-`part-09.png`: 부별 삽화 9장
- `downloads/MHMbook.pdf`: PDF 초안
- `downloads/mhmbook-draft.md`: Markdown 원고 초안
- `downloads/hyperframe-strategy.md`: 공개용 HyperFrame 전략 요약
- `book/`: MHMbook 원천 원고와 빌드 파이프라인
- `LICENSE`: MIT License
- `CNAME`: `mhm.medicalframe.ai`
- `.nojekyll`: GitHub Pages 정적 파일 보호용

## 배포 전 확인

배포 전에 다음을 확인한다.

- PDF 파일이 최신 합본에서 생성되었는가
- `downloads/MHMbook.pdf`와 `book/output/pdf/MHMbook.pdf`가 같은 파일인가
- `downloads/mhmbook-draft.md`와 `book/output/mhmbook-draft.md`가 같은 파일인가
- 표지 이미지가 로드되는가
- MIT License 파일이 공개 폴더에 있는가
- 목차가 9부 28장 구조로 보이는가
- 부별 삽화 9장이 모두 로드되는가
- HTML 링크 검사에서 누락이 0개인가
- 데스크톱/모바일 렌더링에서 가로 넘침이 없는가
- 외부 공개 문서에 내부 과격 표현이 남지 않았는가

## 현재 배포 확인

- `https://mhm.medicalframe.ai/`: 200 OK
- GitHub Pages status: `built`
- HTML 링크/이미지 검사: 참조 17개, 누락 0개
- 라이브 PDF: 129쪽, 제목 `나는 딴 돈의 절반만 가져가`
- 라이브 Markdown: `OpenFrame`, `Open Source MIT License` 표기 확인
- Cloudflare 이메일 보호 잡음 방지를 위해 footer 이메일은 텍스트로 표시한다.

## 갱신 순서

1. `cd book`
2. `python3 00_management/scripts/build_mhmbook.py`
3. `python3 00_management/scripts/build_mhmbook_pdf.py`
4. `cp output/mhmbook-draft.md ../downloads/mhmbook-draft.md`
5. `cp output/pdf/MHMbook.pdf ../downloads/MHMbook.pdf`
6. `assets/cover/` 변경분이 있으면 `../assets/cover/`와 동기화한다.
7. `assets/illustrations/` 변경분이 있으면 `../assets/illustrations/`와 동기화한다.
8. 웹사이트 링크, 표지/삽화 로딩, 데스크톱/모바일 렌더링을 확인한다.
