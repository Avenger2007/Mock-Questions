#!/usr/bin/env python3
"""
Export CUET test JSON files to review PDFs (question paper + answer key +
explanations). Mechanical formatting only — no content is generated.

Renders HTML and prints it with headless Google Chrome, so Unicode (₹,
Devanagari) and KaTeX/mhchem formulas display as students will see them.

Usage:
  python3 export_test_pdf.py "CUET/Accountancy/CUET ACCOUNTANCY TEST 1.json" [more files] [--out review/Accountancy]
"""
import html, json, os, subprocess, sys, tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
KATEX = "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist"

CSS = """
@page { size: A4; margin: 16mm 14mm; }
body { font-family: -apple-system, 'Helvetica Neue', Arial, 'Kohinoor Devanagari', sans-serif;
       font-size: 10.5pt; color: #111; line-height: 1.45; }
h1 { font-size: 17pt; margin: 0 0 4px; }
h2 { font-size: 13pt; margin: 18px 0 8px; padding: 4px 8px; background: #eef2f7; border-left: 4px solid #2f5d8a; }
.meta { color: #444; font-size: 9.5pt; margin-bottom: 10px; }
.instr { border: 1px solid #ccd; border-radius: 6px; padding: 8px 12px; margin: 10px 0 14px; font-size: 9.5pt; }
.q { break-inside: avoid; margin: 0 0 12px; padding-bottom: 8px; border-bottom: 1px solid #e3e3e3; }
.qh { font-size: 8.5pt; color: #666; margin-bottom: 2px; }
.stem { white-space: pre-line; }
.opts { margin: 6px 0 0 14px; padding: 0; list-style: none; }
.opts li { margin: 2px 0; }
.key { width: 100%; border-collapse: collapse; font-size: 9.5pt; margin-bottom: 8px; }
.key td, .key th { border: 1px solid #ccc; padding: 3px 6px; text-align: center; }
.sol { break-inside: avoid; margin: 0 0 12px; padding: 8px 10px; border: 1px solid #e0e6ee; border-radius: 6px; }
.sol .exp { white-space: pre-line; margin-top: 4px; }
.tag { display: inline-block; font-size: 8pt; padding: 0 6px; border-radius: 8px; background: #eef; margin-left: 4px; }
.pb { break-before: page; }
"""


def esc(s):
    return html.escape(s or "")


def render(data):
    qs = data["questions"]
    sections = {s["id"]: s for s in data.get("sections", [])} or {None: {"title": "Questions"}}
    out = [f"<h1>{esc(data.get('title', data.get('test_id')))}</h1>",
           f"<div class='meta'>{esc(data.get('exam', ''))} · {esc(data.get('subject', ''))}"
           f"{' (' + esc(data.get('subject_code')) + ')' if data.get('subject_code') else ''} · "
           f"Duration {data.get('duration_minutes', 60)} min · "
           f"{data.get('questions_to_attempt', data.get('total_questions', len(qs)))} questions to attempt"
           f" (of {len(qs)})</div>"]
    if data.get("instructions"):
        out.append("<div class='instr'><b>Instructions</b><ul>" +
                   "".join(f"<li>{esc(i)}</li>" for i in data["instructions"]) + "</ul></div>")

    current = object()
    for n, q in enumerate(qs, 1):
        sec = q.get("section")
        if sec != current:
            current = sec
            out.append(f"<h2>{esc(sections.get(sec, {}).get('title', sec or 'Questions'))}</h2>")
        opts = "".join(f"<li>{esc(o)}</li>" for o in q["options"])
        out.append(f"<div class='q'><div class='qh'>Q{n} · {esc(q.get('topic', ''))}</div>"
                   f"<div class='stem'><b>{n}.</b> {esc(q['question'])}</div><ul class='opts'>{opts}</ul></div>")

    # Answer key grid
    out.append("<h2 class='pb'>Answer key</h2><table class='key'>")
    for r in range(0, len(qs), 10):
        row = qs[r:r + 10]
        out.append("<tr>" + "".join(f"<th>Q{r + i + 1}</th>" for i in range(len(row))) + "</tr>")
        out.append("<tr>" + "".join(f"<td>{esc(q['correct_option'])}</td>" for q in row) + "</tr>")
    out.append("</table>")

    out.append("<h2>Solutions and explanations</h2>")
    for n, q in enumerate(qs, 1):
        tags = "".join(f"<span class='tag'>{esc(t)}</span>" for t in
                       (q.get("difficulty"), q.get("format"), q.get("sub_topic")) if t)
        out.append(f"<div class='sol'><b>Q{n}</b>{tags}<div class='exp'>{esc(q.get('explanation', ''))}</div></div>")

    katex = (f"<link rel='stylesheet' href='{KATEX}/katex.min.css'>"
             f"<script src='{KATEX}/katex.min.js'></script>"
             f"<script src='{KATEX}/contrib/mhchem.min.js'></script>"
             f"<script src='{KATEX}/contrib/auto-render.min.js'></script>"
             "<script>document.addEventListener('DOMContentLoaded',()=>{try{renderMathInElement(document.body,"
             "{delimiters:[{left:'\\\\(',right:'\\\\)',display:false},{left:'\\\\[',right:'\\\\]',display:true}]})}catch(e){}});</script>")
    return (f"<!doctype html><html><head><meta charset='utf-8'><title>{esc(data.get('title'))}</title>"
            f"<style>{CSS}</style>{katex}</head><body>{''.join(out)}</body></html>")


def main():
    args = sys.argv[1:]
    out_dir = "review"
    if "--out" in args:
        i = args.index("--out")
        out_dir = args[i + 1]
        args = args[:i] + args[i + 2:]
    os.makedirs(out_dir, exist_ok=True)
    for path in args:
        data = json.load(open(path, encoding="utf-8"))
        name = os.path.splitext(os.path.basename(path))[0]
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
            f.write(render(data))
            tmp = f.name
        pdf = os.path.abspath(os.path.join(out_dir, name + ".pdf"))
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=8000", f"--print-to-pdf={pdf}", "file://" + tmp],
                       check=True, capture_output=True)
        os.unlink(tmp)
        print(pdf)


if __name__ == "__main__":
    main()
