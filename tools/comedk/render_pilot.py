"""Export COMEDK question and solution PDFs and combined HTML from canonical JSON."""
from argparse import ArgumentParser
from html import escape
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer

DIR = Path(__file__).resolve().parents[2] / "COMEDK"
OUT = DIR / "review"
PDF_FONT = Path("/usr/share/fonts/truetype/dejavu")
NAVY = colors.HexColor("#153049")
TEAL = colors.HexColor("#176568")


def pdf_style(name, size, leading, *, bold=False, color=NAVY, after=0):
    return ParagraphStyle(name, fontName="PilotBold" if bold else "PilotRegular",
                          fontSize=size, leading=leading, textColor=color,
                          alignment=TA_LEFT, spaceAfter=after, splitLongWords=True)


def number(question):
    return int(question["id"].rsplit("Q", 1)[1])


def render_pdf(data, solutions):
    test = data["test_number"]
    title = f"COMEDK UGET Test {test} · " + ("Worked solutions" if solutions else "Question paper")
    edition = "SOLUTIONS" if solutions else "QUESTIONS"
    name = f"COMEDK_TEST_{test:02}_{edition}.pdf"
    styles = {
        "title": pdf_style("title", 22, 26, bold=True, after=8),
        "section": pdf_style("section", 15, 19, bold=True, color=TEAL, after=11),
        "stem": pdf_style("stem", 10.35, 15, bold=True, after=5),
        "body": pdf_style("body", 10, 14.3, color=colors.HexColor("#233847"), after=3),
    }
    intro = ("Worked answers and reasons for each alternative. Based on the 2026 syllabus."
             if solutions else
             "180 minutes · 180 questions · 180 marks. Choose one answer per question. "
             "Award one mark for a correct answer and zero for an incorrect or unanswered question.")
    story = [Paragraph(escape(title), styles["title"]), Paragraph(escape(intro), styles["body"]), Spacer(1, 16)]
    section = None
    for q in data["questions"]:
        if q["section"] != section:
            if section is not None:
                story.append(PageBreak())
            section = q["section"]
            story.append(Paragraph(q["subject"], styles["section"]))
        block = [Paragraph(escape(f"Q{number(q):03}. {q['question']}"), styles["stem"])]
        if not solutions and "image_reference" in q:
            file = DIR / "images" / q["image_reference"]
            block.append(Image(str(file), width=310, height=145, kind="proportional"))
        lines = q["explanation"].splitlines() if solutions else q["options"]
        block.extend(Paragraph(escape(line), styles["body"]) for line in lines)
        block.append(Spacer(1, 9))
        story.append(KeepTogether(block))

    def footer(page, document):
        page.setStrokeColor(colors.HexColor("#C9D4DC"))
        page.line(42, 36, A4[0] - 42, 36)
        page.setFillColor(TEAL)
        page.setFont("PilotBold", 8)
        page.drawString(42, 23, f"OURMOCKS  /  COMEDK TEST {test}")
        page.drawRightString(A4[0] - 42, 23, f"{document.page}")

    doc = SimpleDocTemplate(str(OUT / name), pagesize=A4, title=title,
                            leftMargin=42, rightMargin=42, topMargin=39, bottomMargin=47)
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


def render_html(data):
    test = data["test_number"]
    content = [f'<!doctype html><html lang="en"><meta charset="utf-8"><title>COMEDK Test {test}</title>',
               '<style>body{font:16px/1.55 system-ui;max-width:52rem;margin:2rem auto;padding:0 1rem;color:#153049}'
               'article{border-bottom:1px solid #ccc;padding:1rem 0}img{width:min(100%,36rem)}'
               'summary{cursor:pointer;color:#176568}</style>',
               f'<h1>COMEDK UGET Test {test}</h1><p>180 minutes · 180 questions · +1 per correct answer · No negative marking</p>']
    section = None
    for q in data["questions"]:
        if q["section"] != section:
            section = q["section"]
            content.append(f"<h2>{q['subject']}</h2>")
        content.append(f'<article id="{q["id"]}"><h3>Q{number(q):03}. {escape(q["question"])}</h3>')
        if "image_reference" in q:
            content.append(f'<img src="../images/{q["image_reference"]}" alt="{escape(q["image_alt"])}">')
        content.extend(f"<div>{escape(option)}</div>" for option in q["options"])
        content.append("<details><summary>Worked solution</summary>")
        content.extend(f"<p>{escape(line)}</p>" for line in q["explanation"].splitlines())
        content.append("</details></article>")
    content.append("</html>")
    (OUT / f"COMEDK_TEST_{test:02}.html").write_text("\n".join(content) + "\n")


if __name__ == "__main__":
    pdfmetrics.registerFont(TTFont("PilotRegular", str(PDF_FONT / "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont("PilotBold", str(PDF_FONT / "DejaVuSans-Bold.ttf")))
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("test", nargs="?", type=int, default=1)
    test = parser.parse_args().test
    data = json.loads((DIR / f"COMEDK UGET TEST {test}.json").read_text())
    OUT.mkdir(exist_ok=True)
    render_pdf(data, solutions=False)
    render_pdf(data, solutions=True)
    render_html(data)
