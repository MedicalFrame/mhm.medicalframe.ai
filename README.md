# mhm.medicalframe.ai

`나는 딴 돈의 절반만 가져가` 책과 HyperFrame Suite 전략을 함께 보여주는 정적 웹사이트입니다.

## 구성

- `index.html`: 공개 웹페이지
- `styles.css`: 스타일
- `assets/cover/book-cover.png`: 웹사이트 히어로와 PDF 표지 이미지
- `assets/cover/cover-art.png`: 표지 배경 원본
- `assets/hero-workflow.png`: 초기 HyperFrame 히어로 콘셉트 이미지
- `assets/illustrations/part-01.png`-`part-09.png`: 목차와 PDF 부 시작 페이지에 쓰는 부별 삽화
- `assets/site-concept.png`: 초기 디자인 콘셉트 참고 이미지
- `downloads/MHMbook.pdf`: 현재 책 PDF 초안
- `downloads/mhmbook-draft.md`: 현재 책 합본 초안 스냅샷
- `downloads/hyperframe-strategy.md`: 외부 공개용 HyperFrame Suite 전략 요약
- `book/`: MHMbook 원천 원고, 빌드 스크립트, 브런치 패키지, 출력물
- `LICENSE`: MIT License

## Book pipeline

```bash
cd book
python3 00_management/scripts/build_mhmbook.py
python3 00_management/scripts/build_mhmbook_pdf.py
```

`build_mhmbook_pdf.py`는 `reportlab`이 필요합니다. Codex 번들 Python을 쓸 때는 다음 경로를 사용할 수 있습니다.

```bash
/Users/jsbang/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 00_management/scripts/build_mhmbook_pdf.py
```

빌드 후 공개 파일을 갱신하려면 `book/output/mhmbook-draft.md`를 `downloads/mhmbook-draft.md`로, `book/output/pdf/MHMbook.pdf`를 `downloads/MHMbook.pdf`로 복사합니다.

## 운영 메모

- PDF는 1차 초안으로 연결하고, Markdown 초안은 검토용으로 함께 둔다.
- 원고가 갱신되면 `book/output/mhmbook-draft.md`를 `downloads/mhmbook-draft.md`로 다시 복사한다.
- PDF가 갱신되면 `book/output/pdf/MHMbook.pdf`를 `downloads/MHMbook.pdf`로 다시 복사한다.
- 표지가 갱신되면 `book/assets/cover/`를 `assets/cover/`와 동기화한다.
- 부별 삽화가 갱신되면 `book/assets/illustrations/`를 `assets/illustrations/`와 동기화한다.
- 공개 전략 문서가 갱신되면 `downloads/hyperframe-strategy.md`를 다시 복사한다.
- 첫 화면에서는 반드시 책 제목, 핵심 문장, HyperFrame 포지션이 함께 보여야 한다.
- 첫 화면 표지는 `assets/cover/book-cover.png`를 사용한다.
- 공개 표기는 `MedicalFrame Inc. company asset · Open Source MIT License`로 둔다.
- 목차 영역에서는 9부 카드와 부별 삽화 9장이 모두 보여야 한다.
