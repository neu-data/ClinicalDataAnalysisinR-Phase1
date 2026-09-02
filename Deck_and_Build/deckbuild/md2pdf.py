# -*- coding: utf-8 -*-
"""
Lightweight Markdown -> PDF converter (reportlab), Neudata-branded.
Handles: # ## ### headings, paragraphs, - / * bullets, 1. ordered lists,
pipe tables, ``` fenced code blocks, **bold**, *italic*, `inline code`,
--- horizontal rules. Good enough for the course documents.

Usage: python md2pdf.py input.md output.pdf "Document Title"
"""
import sys, re, html
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, Preformatted, HRFlowable,
                                ListFlowable, ListItem)

TEAL = colors.HexColor("#0D7377")
TEALD = colors.HexColor("#0A5557")
STEEL = colors.HexColor("#2E7E96")
GREY = colors.HexColor("#595959")
CODEBG = colors.HexColor("#EDF1F2")
LIGHT = colors.HexColor("#E8F4F4")

styles = getSampleStyleSheet()
def S(name, **kw):
    kw.setdefault("parent", styles["Normal"])
    return ParagraphStyle(name, **kw)

BODY = S("body", fontName="Helvetica", fontSize=10.5, leading=15, spaceAfter=6,
         textColor=colors.HexColor("#1A1A1A"))
H1 = S("h1", fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=TEAL,
       spaceBefore=14, spaceAfter=8)
H2 = S("h2", fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=TEALD,
       spaceBefore=12, spaceAfter=5)
H3 = S("h3", fontName="Helvetica-Bold", fontSize=12, leading=16, textColor=STEEL,
       spaceBefore=9, spaceAfter=3)
BUL = S("bul", parent=BODY, leftIndent=14, spaceAfter=3)
CELL = S("cell", fontName="Helvetica", fontSize=8.8, leading=11.5,
         textColor=colors.HexColor("#1A1A1A"))
CELLH = S("cellh", fontName="Helvetica-Bold", fontSize=8.8, leading=11.5,
          textColor=colors.white)


def inline(t):
    t = html.escape(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"`(.+?)`", r'<font name="Courier" size="9.5">\1</font>', t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    return t


def make_pdf(md_path, pdf_path, title):
    lines = open(md_path, encoding="utf-8").read().split("\n")
    story = []
    i = 0
    bullets = []

    def flush_bullets():
        nonlocal bullets
        if bullets:
            items = [ListItem(Paragraph(inline(b), BUL), leftIndent=10,
                              value=None) for b in bullets]
            story.append(ListFlowable(items, bulletType="bullet", start="•",
                                      bulletColor=TEAL, leftIndent=12))
            story.append(Spacer(1, 4))
            bullets = []

    while i < len(lines):
        ln = lines[i].rstrip()
        # fenced code
        if ln.strip().startswith("```"):
            flush_bullets()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            code = "\n".join(buf) if buf else " "
            pre = Preformatted(code, S("code", fontName="Courier", fontSize=8.5,
                                       leading=11, textColor=colors.HexColor("#10303A")))
            tbl = Table([[pre]], colWidths=[16.0*cm])
            tbl.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),CODEBG),
                                     ("BOX",(0,0),(-1,-1),0.5,colors.HexColor("#D5DEE0")),
                                     ("LEFTPADDING",(0,0),(-1,-1),8),
                                     ("RIGHTPADDING",(0,0),(-1,-1),8),
                                     ("TOPPADDING",(0,0),(-1,-1),6),
                                     ("BOTTOMPADDING",(0,0),(-1,-1),6)]))
            story.append(tbl); story.append(Spacer(1, 6))
            continue
        # table block
        if "|" in ln and i+1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|", lines[i+1]):
            flush_bullets()
            tlines = []
            while i < len(lines) and "|" in lines[i]:
                tlines.append(lines[i]); i += 1
            def cells(row):
                row = row.strip()
                if row.startswith("|"): row = row[1:]
                if row.endswith("|"): row = row[:-1]
                return [c.strip() for c in row.split("|")]
            header = cells(tlines[0])
            body_rows = [cells(r) for r in tlines[2:]]
            ncol = len(header)
            data = [[Paragraph(inline(c), CELLH) for c in header]]
            for r in body_rows:
                r = (r + [""]*ncol)[:ncol]
                data.append([Paragraph(inline(c), CELL) for c in r])
            avail = 16.0*cm
            cw = [avail/ncol]*ncol
            t = Table(data, colWidths=cw, repeatRows=1)
            t.setStyle(TableStyle([
                ("BACKGROUND",(0,0),(-1,0),TEAL),
                ("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white, colors.HexColor("#F3F8F8")]),
                ("GRID",(0,0),(-1,-1),0.4,colors.HexColor("#CFD8DA")),
                ("VALIGN",(0,0),(-1,-1),"TOP"),
                ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
                ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
            story.append(t); story.append(Spacer(1, 8))
            continue
        # headings
        if ln.startswith("### "):
            flush_bullets(); story.append(Paragraph(inline(ln[4:]), H3))
        elif ln.startswith("## "):
            flush_bullets(); story.append(Paragraph(inline(ln[3:]), H2))
        elif ln.startswith("# "):
            flush_bullets(); story.append(Paragraph(inline(ln[2:]), H1))
        elif re.match(r"^\s*[-*]\s+", ln):
            bullets.append(re.sub(r"^\s*[-*]\s+", "", ln))
        elif re.match(r"^\s*\d+\.\s+", ln):
            flush_bullets()
            story.append(Paragraph(inline(ln.strip()), BUL))
        elif ln.strip() in ("---", "***", "___"):
            flush_bullets()
            story.append(HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#CFD8DA"),
                                    spaceBefore=4, spaceAfter=6))
        elif ln.strip() == "":
            flush_bullets(); story.append(Spacer(1, 3))
        else:
            flush_bullets(); story.append(Paragraph(inline(ln), BODY))
        i += 1
    flush_bullets()

    # page furniture
    def on_page(canv, doc):
        canv.saveState()
        canv.setFillColor(TEAL)
        canv.setFont("Helvetica-Bold", 9)
        canv.drawString(2.0*cm, A4[1]-1.15*cm, "Clinical Data Analysis in R  -  Phase I")
        canv.setFillColor(GREY); canv.setFont("Helvetica", 8)
        canv.drawRightString(A4[0]-2.0*cm, A4[1]-1.15*cm, title)
        canv.setStrokeColor(TEAL); canv.setLineWidth(0.8)
        canv.line(2.0*cm, A4[1]-1.3*cm, A4[0]-2.0*cm, A4[1]-1.3*cm)
        canv.setFillColor(STEEL); canv.setFont("Helvetica", 8)
        canv.drawCentredString(A4[0]/2, 1.0*cm, "Neudata  |  #ClearDataClearImpact")
        canv.setFillColor(GREY)
        canv.drawRightString(A4[0]-2.0*cm, 1.0*cm, "Page %d" % doc.page)
        canv.restoreState()

    doc = BaseDocTemplate(pdf_path, pagesize=A4,
                          leftMargin=2.0*cm, rightMargin=2.0*cm,
                          topMargin=1.7*cm, bottomMargin=1.6*cm, title=title,
                          author="Bernard Isekah Osang'ir | Neudata")
    frame = Frame(2.0*cm, 1.5*cm, A4[0]-4.0*cm, A4[1]-3.3*cm, id="main")
    doc.addPageTemplates([PageTemplate(id="t", frames=[frame], onPage=on_page)])
    doc.build(story)
    print("Wrote", pdf_path)


if __name__ == "__main__":
    make_pdf(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "")
