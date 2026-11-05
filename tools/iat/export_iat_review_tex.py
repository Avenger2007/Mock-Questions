"""Render authored IAT JSON as a printable question-and-solution PDF with XeLaTeX."""
import hashlib,json,re,subprocess,sys,shutil
import fitz
from pathlib import Path
root=Path(__file__).resolve().parents[2]
source=Path(sys.argv[1]).resolve()
data=json.loads(source.read_text())
t=data['test_number']; stem='IAT_TEST_1' if t==1 else f'IAT_NEW_TEST_{t}'
review=root/'IISER/review';review.mkdir(parents=True,exist_ok=True)
job=root/'tmp/pdfs'/stem;job.mkdir(parents=True,exist_ok=True)
math=re.compile(r'(\\\[.*?\\\]|\\\(.*?\\\))',re.S)
def escaped(s):
 return (s.replace('\\',r'\textbackslash{}').replace('&',r'\&').replace('%',r'\%').replace('#',r'\#').replace('$',r'\$').replace('_',r'\_').replace('{',r'\{').replace('}',r'\}').replace('~',r'\textasciitilde{}').replace('^',r'\textasciicircum{}'))
def rich(s):
 chunks=math.split(s)
 def compatible(c):
  # KaTeX mhchem permits comparisons inside ce; TeX mhchem requires separate species.
  return re.sub(r'\\ce\{([^{}]*\s[<>]\s[^{}]*)\}',
                lambda m:''.join(part if re.fullmatch(r'\s[<>]\s',part) else r'\ce{'+part+'}'
                                 for part in re.split(r'(\s[<>]\s)',m[1])),c)
 return ''.join(compatible(c) if c.startswith(('\\[','\\(')) else escaped(c) for c in chunks)
def explanation(s):
 out=[]
 for line in s.splitlines():
  m=re.match(r'^(Answer|Given|Formula/Principle|Step \d+|Worked derivation|Why|Why not the others|Key point):\s*(.*)',line)
  out.append(r'\textbf{'+escaped(m[1])+':} '+rich(m[2])+r'\par' if m else rich(line)+r'\par')
 return '\n'.join(out)
preamble=r'''\documentclass[10pt,a4paper]{article}
\usepackage[a4paper,margin=18mm,headheight=16pt,footskip=14mm]{geometry}
\usepackage{fontspec,amsmath,amssymb,graphicx,xcolor,fancyhdr,needspace}
\usepackage[version=4]{mhchem}
\setmainfont{DejaVu Sans}
\setsansfont{DejaVu Sans}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt}
\emergencystretch=4em
\linespread{1.10}
\definecolor{brand}{HTML}{276F72}
\pagestyle{fancy}\fancyhf{}\fancyhead[L]{\textcolor{brand}{OURMOCKS / IAT PREPARATION}}
\fancyhead[R]{REVIEW DRAFT}\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\begin{document}
'''
parts=[preamble,r'\begin{center}',r'{\Huge\bfseries '+escaped(data['title'])+r'}\\[8pt]',r'{\large Question paper, answer key and worked solutions}',r'\end{center}',r'\vspace{9mm}',r'\textbf{60 questions \quad 180 minutes \quad 240 marks}',r'\par Biology 1--15; Chemistry 16--30; Mathematics 31--45; Physics 46--60.',r'\par Correct +4; incorrect -1; unattempted 0. All 60 questions are available.',r'\par This is a provisional 2026-pattern authoring draft for 2027 preparation. Independent academic review is pending.',r'\vspace{8mm}\hrule\vspace{6mm}',r'\textbf{Instructions}\par Each item has exactly one correct option. Use the separate solution section for review after attempting the paper.',r'\vspace{8mm}\textcolor{brand}{\textbf{Figures and equations are part of the questions.}}',r'\newpage']
for sec,title in [('B','Biology'),('C','Chemistry'),('M','Mathematics'),('P','Physics')]:
 parts.append(r'\section*{'+title+'}')
 for q in [x for x in data['questions'] if x['section']==sec]:
  num=int(q['id'][-2:]);parts.append(r'\noindent\begin{minipage}{\linewidth}')
  parts.append(r'\textcolor{brand}{\textbf{Q'+str(num)+r'}}\quad '+rich(q['question'])+r'\par')
  if q.get('image_reference'):
   image=(root/data['image_base_path']/q['image_reference']).resolve();assert image.is_file()
   image_size=r'width=.82\linewidth,height=10.5cm' if t>=16 else r'width=.60\linewidth,height=7.8cm'
   parts.append(r'\begin{center}\includegraphics['+image_size+r',keepaspectratio]{\detokenize{'+str(image)+r'}}\end{center}')
  parts.extend(r'\textbf{'+a+r')} '+rich(v[3:])+r'\par' for a,v in zip('ABCD',q['options']))
  parts.append(r'\end{minipage}\par\vspace{3mm}\hrule\vspace{4mm}')
 parts.append(r'\newpage')
parts.append(r'\section*{Answer key and worked solutions}')
parts.append(r'\textit{Every solution explains the selected choice and the alternative errors.}\par')
for sec,title in [('B','Biology'),('C','Chemistry'),('M','Mathematics'),('P','Physics')]:
 parts.append(r'\subsection*{'+title+'}')
 for q in [x for x in data['questions'] if x['section']==sec]:
  num=int(q['id'][-2:])
  # Keep the last worked exercise together instead of stranding its key point.
  parts.append(r'\Needspace{28\baselineskip}' if t>=16 and num==60 else r'\Needspace{10\baselineskip}')
  parts.append(r'\textcolor{brand}{\textbf{Q'+str(num)+r' / '+q['correct_option']+r'}}\quad '+escaped(q['sub_topic'])+r'\par')
  parts.append(explanation(q['explanation']))
  parts.append(r'\vspace{2mm}\hrule\vspace{3mm}')
parts.append(r'\end{document}')
tex='\n'.join(parts);texpath=job/(stem+'.tex');texpath.write_text(tex)
result=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(job),str(texpath)],cwd=root,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
if result.returncode:
 print(result.stdout[-3500:]);raise SystemExit(result.returncode)
pdf=review/(stem+'.pdf');shutil.copy2(job/(stem+'.pdf'),pdf)
log=(job/(stem+'.log')).read_text()
assert 'Overfull' not in log and 'Missing character' not in log, 'PDF layout or glyph warning'
document=fitz.open(pdf)
pdf_text='\n'.join(page.get_text() for page in document)
question_text,solution_text=pdf_text.split('Answer key and worked solutions',1)
question_numbers=[int(m[1]) for m in re.finditer(r'(?m)^Q(\d{1,2})\b',question_text)]
solution_numbers=[int(m[1]) for m in re.finditer(r'(?m)^Q(\d{1,2})[ \t]*/[ \t]*[ABCD]\b',solution_text)]
question_count=len(question_numbers);solution_count=len(solution_numbers)
assert question_numbers==list(range(1,61)) and solution_numbers==list(range(1,61)), (question_numbers,solution_numbers)
assert all(page.get_text().strip() for page in document)
delivery=review/(stem+'.json');delivery.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
images={q['image_reference']:digest(root/data['image_base_path']/q['image_reference']) for q in data['questions'] if q.get('image_reference')}
check=dict(source_json=str(source.relative_to(root)),source_json_sha256=digest(source),delivery_json_sha256=digest(delivery),pdf_sha256=digest(pdf),image_sha256=images,math_expressions=tex.count(r'\[')+tex.count(r'\('),pdf_pages=len(document),questions=question_count,solutions=solution_count,empty_pages=0,layout_warnings=0,errors=[],renderer='XeLaTeX, independent of browser exporter')
(review/(stem+'_render_check.json')).write_text(json.dumps(check,indent=2)+'\n')
print(json.dumps({'pdf':str(pdf),'images':len(images),'math_expressions':check['math_expressions']}))
