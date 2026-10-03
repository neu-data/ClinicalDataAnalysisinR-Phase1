# -*- coding: utf-8 -*-
"""Course advertising poster (A3 portrait) - CLASSIC ACADEMIC FLYER.
Rev 3: serif typography, warm off-white stock, double ruled border, centred
formal layout, minimal graphics - a printed university seminar announcement.
Neudata teal retained only for the wordmark and thin rules."""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LOGO = os.path.join(ROOT, "Course", "Images", "neudata_logo.jpg")
OUT_PDF = os.path.join(ROOT, "Course", "Images", "Course_Poster.pdf")

W, H = A3                       # 842 x 1191 pt
PAPER = colors.HexColor("#FDFBF6")
INK = colors.HexColor("#1C1C1C")
ACCENT = colors.HexColor("#0D7377")
ACCENTD = colors.HexColor("#093F41")
GREY = colors.HexColor("#4A4A4A")

SR, SB = "Times-Roman", "Times-Bold"
SI, SBI = "Times-Italic", "Times-BoldItalic"

c = canvas.Canvas(OUT_PDF, pagesize=A3)
CM = 76                         # inner content margin
CW = W - 2*CM


def ty(y):
    return H - y


def text(x, y_top, s, font=SR, size=12, color=INK, align="c"):
    c.setFont(font, size); c.setFillColor(color)
    if align == "l":
        c.drawString(x, ty(y_top), s)
    elif align == "c":
        c.drawCentredString(x, ty(y_top), s)
    else:
        c.drawRightString(x, ty(y_top), s)


def wrap(x, y_top, s, font, size, color, maxw, leading, align="l"):
    c.setFont(font, size); c.setFillColor(color)
    words = s.split(); line = ""; yy = y_top
    for w in words:
        t = (line + " " + w).strip()
        if c.stringWidth(t, font, size) <= maxw:
            line = t
        else:
            _put(x, yy, line, maxw, align); line = w; yy += leading
    if line:
        _put(x, yy, line, maxw, align); yy += leading
    return yy


def _put(x, yy, line, maxw, align):
    if align == "c":
        c.drawCentredString(x + maxw/2, ty(yy), line)
    else:
        c.drawString(x, ty(yy), line)


def rule(x1, x2, y, color=ACCENT, w=0.8):
    c.setStrokeColor(color); c.setLineWidth(w); c.line(x1, ty(y), x2, ty(y))


def diamond(cx, y, r=4.2, color=ACCENT):
    p = c.beginPath(); p.moveTo(cx - r, ty(y)); p.lineTo(cx, ty(y) + r)
    p.lineTo(cx + r, ty(y)); p.lineTo(cx, ty(y) - r); p.close()
    c.setFillColor(color); c.drawPath(p, fill=1, stroke=0)


def ornament(y, half=None):
    half = half or CW/2
    rule(W/2 - half, W/2 - 16, y, ACCENT, 0.9)
    rule(W/2 + 16, W/2 + half, y, ACCENT, 0.9)
    diamond(W/2, y)


def _tracked(x, y, s, size, track, font):
    xi = x
    for ch in s:
        c.drawString(xi, ty(y), ch)
        xi += c.stringWidth(ch, font, size) + track
    return xi - track - x


def tcaps_c(y, s, size, color, track, font=SB):
    c.setFont(font, size); c.setFillColor(color)
    w = c.stringWidth(s, font, size) + track*(len(s) - 1)
    _tracked(W/2 - w/2, y, s, size, track, font)
    return w


def tcaps_l(x, y, s, size, color, track, font=SB):
    c.setFont(font, size); c.setFillColor(color)
    return _tracked(x, y, s, size, track, font)


def head_center(y, s, size=17, track=3.2):
    w = c.stringWidth(s, SB, size) + track*(len(s) - 1)
    gap = w/2 + 22
    rule(W/2 - CW/2, W/2 - gap, y - size*0.32, ACCENT, 0.9)
    rule(W/2 + gap, W/2 + CW/2, y - size*0.32, ACCENT, 0.9)
    tcaps_c(y, s, size, ACCENTD, track)


def head_left(x, y, w, s, size=15, track=2.6):
    tcaps_l(x, y, s, size, ACCENTD, track)
    rule(x, x + w, y + 10, ACCENT, 0.9)
    return y + 30


# ================================================================ background
c.setFillColor(PAPER); c.rect(0, 0, W, H, fill=1, stroke=0)
# double ruled border
c.setStrokeColor(ACCENT); c.setLineWidth(1.8); c.rect(34, 34, W - 68, H - 68, fill=0, stroke=1)
c.setStrokeColor(ACCENT); c.setLineWidth(0.7); c.rect(41, 41, W - 82, H - 82, fill=0, stroke=1)

# ================================================================ crest / wordmark
try:
    img = ImageReader(LOGO); iw, ih = img.getSize(); ar = ih/iw
    dh = 50; dw = dh/ar
    c.drawImage(img, W/2 - dw/2, ty(92) - dh/2, dw, dh, mask='auto')
except Exception:
    tcaps_c(96, "NEUDATA", 26, ACCENT, 6)
text(W/2, 128, "Insight  ·  Impact  ·  Innovation", SI, 12.5, GREY)

ornament(150)

# ================================================================ title block
text(W/2, 224, "Clinical Data Analysis in R", SB, 45, INK)
text(W/2, 264, "Phase I — Introduction to R for Clinical Research", SI, 21, ACCENTD)

ornament(300, half=150)

text(W/2, 344, "A Five-Session Evening Course for", SI, 17, GREY)
text(W/2, 374, "Doctors  ·  Nurses  ·  Medical Researchers  ·  Allied Health Professionals",
     SB, 16, INK)

# ================================================================ schedule
head_center(440, "Course Schedule", 17, 3.4)
text(W/2, 482, "Five sessions  ·  Every Tuesday  ·  8:00 pm  ·  90 minutes each", SR, 17.5, INK)
text(W/2, 512, "8 September – 6 October 2026", SB, 18.5, ACCENTD)

ornament(548, half=150)

# ================================================================ overview (full width)
y = wrap(CM, 598,
         ("Many healthcare professionals collect valuable clinical data but lack the tools "
          "to analyse it. This practical course builds foundational skills in R, basic "
          "biostatistics, common medical statistical tests, and publication-ready tables "
          "and figures — with no prior programming experience assumed."),
         SR, 15, INK, CW, 24, align="c")

# ================================================================ two columns
colY = y + 46
GAPC = 54
colW = (CW - GAPC)/2
LX = CM
RX = CM + colW + GAPC


def daylist(x, y0, w):
    yy = head_left(x, y0, w, "What You Will Learn", 15, 2.6)
    days = [("Day 1", "Introduction to R & RStudio"),
            ("Day 2", "Understanding & Cleaning Clinical Data"),
            ("Day 3", "Descriptive Statistics, Tables & Figures"),
            ("Day 4", "Common Medical Statistical Tests"),
            ("Day 5", "Introduction to Regression & Interpreting Output")]
    for d, t in days:
        c.setFont(SB, 14.5); c.setFillColor(ACCENTD); c.drawString(x, ty(yy), d)
        end = wrap(x + 58, yy, t, SR, 14.5, INK, w - 58, 19, align="l")
        yy = max(yy + 19, end) + 15
    return yy


def wholist(x, y0, w):
    yy = head_left(x, y0, w, "Who Should Apply", 15, 2.6)
    who = ["Medical Doctors & Residents", "Nurses", "Clinical Researchers",
           "Clinical / Hospital Pharmacists", "Public Health Professionals",
           "Hospital Research Staff", "Masters & PhD Students"]
    for it in who:
        c.setFillColor(ACCENT); c.circle(x + 3, ty(yy) + 4.6, 2.0, fill=1, stroke=0)
        text(x + 14, yy, it, SR, 14.5, INK, "l")
        yy += 30.5
    return yy


ly = daylist(LX, colY, colW)
ry = wholist(RX, colY, colW)
# vertical divider between columns
midx = CM + colW + GAPC/2
rule(midx, midx, colY + 4, ACCENT, 0)  # noop placeholder
c.setStrokeColor(colors.HexColor("#D8CFBE")); c.setLineWidth(0.8)
c.line(midx, ty(max(ly, ry) - 6), midx, ty(colY + 4))

by = max(ly, ry) + 16
ornament(by, half=150)

# ================================================================ outcome (full width)
head_center(by + 40, "Course Outcome", 15, 3.0)
wrap(CM, by + 72,
     ("By the end of the course, participants will be able to analyse their own clinical "
      "data in R, choose and interpret appropriate statistical tests, and produce "
      "publication-ready tables and figures."),
     SR, 14.5, INK, CW, 21, align="c")

# ================================================================ footer
fy = H - 118
rule(CM, W - CM, fy, ACCENT, 0.9)
tcaps_c(fy + 30, "ENQUIRIES & REGISTRATION", 13, ACCENTD, 3.0)
text(W/2, fy + 56, "Vương Mỹ Lượng   ·   myluong.1710@gmail.com", SB, 14.5, INK)
text(W/2, fy + 78, "www.neu-data.com", SR, 13.5, ACCENT)

c.showPage(); c.save()
print("Wrote", OUT_PDF)
