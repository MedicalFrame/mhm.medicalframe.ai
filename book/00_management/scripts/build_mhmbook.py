#!/usr/bin/env python3
from __future__ import annotations

from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANUSCRIPT_DIR = ROOT / "book_manuscript"
OUTPUT_DIR = ROOT / "output"

BOOK_MD = MANUSCRIPT_DIR / "book.md"
OUTPUT_MD = OUTPUT_DIR / "mhmbook-draft.md"

TITLE = "나는 딴 돈의 절반만 가져가"
SUBTITLE = "사회기업윤리와 공익 인프라의 원칙"


PARTS = [
    {
        "title": "1부. 기업은 사회 밖에서 살 수 없다",
        "dir": "01_기업은_사회_밖에서_살_수_없다",
        "image": "../assets/illustrations/part-01.png",
    },
    {
        "title": "2부. 나는 딴 돈의 절반만 가져가",
        "dir": "02_나는_딴돈의_절반만_가져가",
        "image": "../assets/illustrations/part-02.png",
    },
    {
        "title": "3부. 의료, 교육, 연구는 모두의 것이다",
        "dir": "03_의료_교육_연구는_모두의_것이다",
        "image": "../assets/illustrations/part-03.png",
    },
    {
        "title": "4부. Medical Frame과 OpenFrame 모델",
        "dir": "04_Medical_Frame과_OpenFrame_모델",
        "image": "../assets/illustrations/part-04.png",
    },
    {
        "title": "5부. AI EMR 선언",
        "dir": "05_AI_EMR_선언",
        "image": "../assets/illustrations/part-05.png",
    },
    {
        "title": "6부. 무료 배포는 마케팅이 아니라 실증이다",
        "dir": "06_무료_배포는_마케팅이_아니라_실증이다",
        "image": "../assets/illustrations/part-06.png",
    },
    {
        "title": "7부. 방해와 저항을 다루는 법",
        "dir": "07_방해와_저항을_다루는_법",
        "image": "../assets/illustrations/part-07.png",
    },
    {
        "title": "8부. 절반만 가져가는 회사의 운영 원칙",
        "dir": "08_절반만_가져가는_회사의_운영_원칙",
        "image": "../assets/illustrations/part-08.png",
    },
    {
        "title": "9부. 새로운 기업윤리 선언",
        "dir": "09_새로운_기업윤리_선언",
        "image": "../assets/illustrations/part-09.png",
    },
]


def normalize(text: str) -> str:
    return text.strip() + "\n"


def build() -> str:
    chunks = [
        f"# {TITLE}",
        "",
        f"부제: {SUBTITLE}",
        "",
        "프로젝트 코드: MHM",
        "",
        "자산/라이선스: MedicalFrame Inc. company asset · Open Source MIT License",
        "",
        f"생성일: {date.today().isoformat()}",
        "",
        "---",
        "",
    ]

    frontmatter = MANUSCRIPT_DIR / "00_frontmatter"
    for path in sorted(frontmatter.glob("00_*.md")):
        chunks.append(normalize(path.read_text(encoding="utf-8")))
        chunks.append("")
        chunks.append("---")
        chunks.append("")

    for part in PARTS:
        chunks.append(f"# {part['title']}")
        chunks.append("")
        chunks.append(f"![{part['title']} 삽화]({part['image']})")
        chunks.append("")
        chunks.append("---")
        chunks.append("")
        for path in sorted((MANUSCRIPT_DIR / part["dir"]).glob("*.md")):
            chunks.append(normalize(path.read_text(encoding="utf-8")))
            chunks.append("")
            chunks.append("---")
            chunks.append("")

    for path in sorted(frontmatter.glob("99_*.md")):
        chunks.append(normalize(path.read_text(encoding="utf-8")))
        chunks.append("")
        chunks.append("---")
        chunks.append("")

    return "\n".join(chunks).rstrip() + "\n"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    text = build()
    BOOK_MD.write_text(text, encoding="utf-8")
    OUTPUT_MD.write_text(text, encoding="utf-8")
    print(f"wrote {BOOK_MD}")
    print(f"wrote {OUTPUT_MD}")


if __name__ == "__main__":
    main()
