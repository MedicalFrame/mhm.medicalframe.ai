#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)
from reportlab.lib.styles import ParagraphStyle


ROOT = Path(__file__).resolve().parents[2]
BOOK_MD = ROOT / "book_manuscript" / "book.md"
OUTPUT_DIR = ROOT / "output" / "pdf"
OUTPUT_PDF = OUTPUT_DIR / "MHMbook.pdf"
COVER_IMAGE = ROOT / "assets" / "cover" / "book-cover.png"

KOREAN_FONT = Path("/System/Library/Fonts/Supplemental/AppleGothic.ttf")

TITLE = "나는 딴 돈의 절반만 가져가"
SUBTITLE = "사회기업윤리와 공익 인프라의 원칙"
PUBLISHER = "MedicalFrame Inc."


def register_fonts() -> None:
    fonts = {
        "MHMRegular": KOREAN_FONT,
        "MHMBold": KOREAN_FONT,
        "MHMExtraBold": KOREAN_FONT,
    }
    for name, path in fonts.items():
        if not path.exists():
            raise FileNotFoundError(f"Missing font: {path}")
        pdfmetrics.registerFont(TTFont(name, str(path)))


def styles() -> dict[str, ParagraphStyle]:
    return {
        "cover_kicker": ParagraphStyle(
            "cover_kicker",
            fontName="MHMBold",
            fontSize=9,
            leading=12,
            textColor=colors.HexColor("#B8872E"),
            alignment=TA_CENTER,
            spaceAfter=8,
            wordWrap="CJK",
        ),
        "cover_title": ParagraphStyle(
            "cover_title",
            fontName="MHMExtraBold",
            fontSize=25,
            leading=30,
            textColor=colors.HexColor("#132036"),
            alignment=TA_CENTER,
            spaceAfter=2,
            wordWrap="CJK",
        ),
        "cover_title_last": ParagraphStyle(
            "cover_title_last",
            fontName="MHMExtraBold",
            fontSize=25,
            leading=30,
            textColor=colors.HexColor("#132036"),
            alignment=TA_CENTER,
            spaceAfter=12,
            wordWrap="CJK",
        ),
        "cover_subtitle": ParagraphStyle(
            "cover_subtitle",
            fontName="MHMBold",
            fontSize=12,
            leading=17,
            textColor=colors.HexColor("#145F9F"),
            alignment=TA_CENTER,
            spaceAfter=20,
            wordWrap="CJK",
        ),
        "cover_meta": ParagraphStyle(
            "cover_meta",
            fontName="MHMRegular",
            fontSize=8.5,
            leading=13,
            textColor=colors.HexColor("#58667A"),
            alignment=TA_CENTER,
            wordWrap="CJK",
        ),
        "toc_title": ParagraphStyle(
            "toc_title",
            fontName="MHMExtraBold",
            fontSize=20,
            leading=26,
            textColor=colors.HexColor("#132036"),
            spaceAfter=16,
            wordWrap="CJK",
        ),
        "license_note": ParagraphStyle(
            "license_note",
            fontName="MHMRegular",
            fontSize=8.2,
            leading=12,
            textColor=colors.HexColor("#58667A"),
            spaceAfter=12,
            wordWrap="CJK",
        ),
        "toc_item": ParagraphStyle(
            "toc_item",
            fontName="MHMRegular",
            fontSize=9.2,
            leading=14,
            leftIndent=3 * mm,
            firstLineIndent=-3 * mm,
            textColor=colors.HexColor("#253449"),
            wordWrap="CJK",
        ),
        "toc_part": ParagraphStyle(
            "toc_part",
            fontName="MHMBold",
            fontSize=10,
            leading=15,
            textColor=colors.HexColor("#145F9F"),
            spaceBefore=7,
            spaceAfter=2,
            wordWrap="CJK",
        ),
        "part_title": ParagraphStyle(
            "part_title",
            fontName="MHMExtraBold",
            fontSize=23,
            leading=30,
            textColor=colors.HexColor("#132036"),
            alignment=TA_CENTER,
            spaceAfter=12,
            wordWrap="CJK",
        ),
        "chapter": ParagraphStyle(
            "chapter",
            fontName="MHMExtraBold",
            fontSize=18,
            leading=24,
            textColor=colors.HexColor("#132036"),
            spaceAfter=10,
            wordWrap="CJK",
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="MHMRegular",
            fontSize=9.6,
            leading=16.2,
            textColor=colors.HexColor("#1E2A3D"),
            spaceAfter=7,
            alignment=TA_LEFT,
            wordWrap="CJK",
        ),
        "short": ParagraphStyle(
            "short",
            fontName="MHMBold",
            fontSize=10.5,
            leading=16.5,
            textColor=colors.HexColor("#132036"),
            spaceAfter=7,
            wordWrap="CJK",
        ),
        "quote": ParagraphStyle(
            "quote",
            fontName="MHMBold",
            fontSize=10.2,
            leading=16,
            leftIndent=5 * mm,
            rightIndent=3 * mm,
            textColor=colors.HexColor("#145F9F"),
            borderColor=colors.HexColor("#D6E4F2"),
            borderWidth=0.6,
            borderPadding=5,
            spaceBefore=4,
            spaceAfter=9,
            wordWrap="CJK",
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName="MHMRegular",
            fontSize=9.4,
            leading=15.6,
            leftIndent=6 * mm,
            firstLineIndent=-3 * mm,
            textColor=colors.HexColor("#1E2A3D"),
            spaceAfter=4,
            wordWrap="CJK",
        ),
    }


def split_sections(markdown: str) -> list[dict[str, object]]:
    chunks = re.split(r"(?m)^---\s*$", markdown)
    sections: list[dict[str, object]] = []

    for chunk in chunks[1:]:
        lines = [line.rstrip() for line in chunk.strip().splitlines()]
        if not lines:
            continue
        title = None
        body_start = 0
        for index, line in enumerate(lines):
            if line.startswith("# "):
                title = line[2:].strip()
                body_start = index + 1
                break
        if title:
            kind = "part" if re.match(r"^\d+부\.", title) else "chapter"
            sections.append({"kind": kind, "title": title, "body": lines[body_start:]})
    return sections


def inline_markup(text: str) -> str:
    escaped = html.escape(text.strip())
    escaped = re.sub(
        r"`([^`]+)`",
        lambda match: f'<font name="MHMBold" color="#145F9F">{match.group(1)}</font>',
        escaped,
    )
    return escaped


def image_for(src: str, max_width: float, max_height: float) -> Image | None:
    path = (BOOK_MD.parent / src).resolve()
    if not path.exists():
        return None
    image = Image(str(path))
    image._restrictSize(max_width, max_height)
    return image


def paragraph_for(line: str, st: dict[str, ParagraphStyle]) -> Paragraph | Spacer | Image | None:
    stripped = line.strip()
    if not stripped:
        return Spacer(1, 3.5)
    image_match = re.match(r"^!\[[^\]]*\]\(([^)]+)\)", stripped)
    if image_match:
        return image_for(image_match.group(1), 90 * mm, 90 * mm)
    if stripped.startswith(">"):
        return Paragraph(inline_markup(stripped.lstrip("> ")), st["quote"])
    if stripped.startswith("- "):
        return Paragraph(f"- {inline_markup(stripped[2:])}", st["bullet"])
    if len(stripped) <= 28 and not stripped.endswith("."):
        return Paragraph(inline_markup(stripped), st["short"])
    return Paragraph(inline_markup(stripped), st["body"])


def draw_footer(canvas, doc) -> None:
    page = canvas.getPageNumber()
    if page <= 1:
        return
    canvas.saveState()
    canvas.setFont("MHMRegular", 7)
    canvas.setFillColor(colors.HexColor("#7A8798"))
    footer = f"{TITLE}  |  {page}"
    canvas.drawCentredString(A5[0] / 2, 10 * mm, footer)
    canvas.restoreState()


def build_story() -> list:
    st = styles()
    markdown = BOOK_MD.read_text(encoding="utf-8")
    sections = split_sections(markdown)
    story: list = []

    if COVER_IMAGE.exists():
        cover = Image(str(COVER_IMAGE))
        cover._restrictSize(108 * mm, 162 * mm)
        story.append(cover)
    else:
        story.append(Spacer(1, 8 * mm))
        story.append(Paragraph("MedicalFrame Open Book", st["cover_kicker"]))
        story.append(Paragraph("나는 딴 돈의", st["cover_title"]))
        story.append(Paragraph("절반만 가져가", st["cover_title_last"]))
        story.append(Paragraph(SUBTITLE, st["cover_subtitle"]))
        story.append(Paragraph("방지송 지음", st["cover_meta"]))
        story.append(Paragraph(f"{PUBLISHER} · {date.today().isoformat()} draft", st["cover_meta"]))
    story.append(PageBreak())

    story.append(Paragraph("목차", st["toc_title"]))
    story.append(
        Paragraph(
            "자산/라이선스: MedicalFrame Inc. company asset · Open Source MIT License",
            st["license_note"],
        )
    )
    for section in sections:
        title = str(section["title"])
        if section["kind"] == "part":
            story.append(Paragraph(inline_markup(title), st["toc_part"]))
        else:
            story.append(Paragraph(inline_markup(title), st["toc_item"]))
    story.append(PageBreak())

    for section_index, section in enumerate(sections):
        title = str(section["title"])
        body_lines = list(section["body"])
        if section_index:
            story.append(PageBreak())
        if section["kind"] == "part":
            story.append(Spacer(1, 20 * mm))
            story.append(Paragraph(inline_markup(title), st["part_title"]))
            for line in body_lines:
                flowable = paragraph_for(line, st)
                if flowable is not None:
                    story.append(flowable)
            continue
        story.append(Paragraph(inline_markup(title), st["chapter"]))
        story.append(Spacer(1, 2 * mm))
        for line in body_lines:
            flowable = paragraph_for(line, st)
            if flowable is not None:
                story.append(flowable)

    return story


def main() -> None:
    register_fonts()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT_PDF),
        pagesize=A5,
        rightMargin=17 * mm,
        leftMargin=17 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title=TITLE,
        author="방지송",
        subject=SUBTITLE,
    )
    doc.build(build_story(), onFirstPage=draw_footer, onLaterPages=draw_footer)
    print(f"wrote {OUTPUT_PDF}")


if __name__ == "__main__":
    main()
