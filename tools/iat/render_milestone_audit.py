"""Render the audit Markdown; no test content is changed."""
from pathlib import Path
import re,html
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,LongTable,TableStyle
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'IISER/audit/milestone_15'
pdfmetrics.registerFont(TTFont('DV','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('DV',normal='DV',bold='DVB',italic='DV',boldItalic='DVB')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Body',fontName='DV',fontSize=9,leading=13,spaceAfter=7))
styles.add(ParagraphStyle(name='Cell',fontName='DV',fontSize=7.7,leading=10.5,spaceAfter=0))
styles['Title'].fontName='DVB';styles['Title'].fontSize=21;styles['Title'].leading=26
styles['Heading2'].fontName='DVB';styles['Heading2'].textColor=colors.HexColor('#22646b')
styles['Heading2'].fontSize=13;styles['Heading2'].leading=17
def markup(s):
    s=html.escape(s)
    s=re.sub(r'\[([^]]+)\]\(([^)]+)\)',lambda m:f'<link href="{m[2]}">{m[1]}</link>',s)
    s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s)
    return s.replace('`','')
def para(s,style='Body'):return Paragraph(markup(s),styles[style])
lines=(OUT/'AUDIT_REPORT.md').read_text().splitlines();story=[];i=0
while i<len(lines):
    line=lines[i].strip()
    if not line:i+=1;continue
    if line.startswith('|'):
        table=[]
        while i<len(lines) and lines[i].strip().startswith('|'):
            cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch('[-: ]+',x) for x in cells):table.append([para(x,'Cell') for x in cells])
            i+=1
        n=len(table[0]);widths={3:[104,139,268],4:[40,110,150,211]}.get(n,[511/n]*n)
        t=LongTable(table,colWidths=widths,repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dcebed')),('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),.3,colors.HexColor('#b8cbcf')),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
        story.extend([t,Spacer(1,10)]);continue
    if line.startswith('# '):story.append(para(line[2:],'Title'))
    elif line.startswith('## '):story.append(para(line[3:],'Heading2'))
    else:story.append(para(line))
    i+=1
def page(canvas,doc):
    canvas.setFont('DV',8);canvas.setFillColor(colors.HexColor('#22646b'))
    canvas.drawString(42,814,'OURMOCKS / IAT MILESTONE AUDIT')
    canvas.drawRightString(553,25,str(doc.page))
doc=SimpleDocTemplate(str(OUT/'IAT_Tests_1_15_Audit.pdf'),pagesize=(595.28,841.89),leftMargin=42,rightMargin=42,topMargin=45,bottomMargin=40)
doc.build(story,onFirstPage=page,onLaterPages=page)
print(OUT/'IAT_Tests_1_15_Audit.pdf')
