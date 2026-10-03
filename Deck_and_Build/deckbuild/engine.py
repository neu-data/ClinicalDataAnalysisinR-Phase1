# -*- coding: utf-8 -*-
"""
Neudata deck engine.

Builds Clinical_Data_Analysis_in_R_Phase1.pptx from JSON slide specs, reusing
the EXACT design language of "Neudata Template.pptx":
  - Fonts: Century Gothic (titles/body), Segoe UI (title-slide subtitle), Verdana (footer)
  - Colours: teal 0D7377 (day titles + rule), 006666 (title-slide title),
             section headers accent5/75%, body 000000, footer accent5/50%, blue 0070C0
  - Every content slide carries the Neudata footer, bottom-left logo and a slide number.
  - Title / Day-divider / Sectioned-content / Copyright patterns mirror template slides 1-4.

Output is assembled by cloning the template's unpacked tree, dropping the 4 example
slides, and writing freshly generated slides + speaker notes, then repackaging.
"""
import os, re, shutil, html

# ----------------------------------------------------------------------------
# Geometry (EMU) and palette - lifted directly from the template
# ----------------------------------------------------------------------------
EMU = 914400
SLIDE_W, SLIDE_H = 12192000, 6858000
ML = 457200                      # left margin
CW = 11277600                    # content width (title/rule)
TEAL = "0D7377"                  # primary brand teal (day titles + rule)
TEAL_TITLE = "006666"            # title-slide "Workshop" teal
BLUE = "0070C0"                  # secondary blue
BLACK = "000000"
GREY = "595959"
CG = os.environ.get("DECK_TITLE_FONT", "Century Gothic")   # override for non-Latin builds
VERD = os.environ.get("DECK_FOOTER_FONT", "Verdana")
SEG = os.environ.get("DECK_SUBTITLE_FONT", "Segoe UI")
MONO = "Consolas"                # code font (monospace)

# language of engine-generated labels (callout tags, "Console output", etc.)
_VI = os.environ.get("DECK_LANG") == "vi"


def _L(en, vi):
    return vi if _VI else en


# callout palettes: (fill tint, header colour, label)
CALLOUTS = {
    "tip":            ("E8F4F4", "0D7377", _L("TIP", "MẸO")),
    "warning":        ("FBE9E7", "B23B2E", _L("WARNING", "CẢNH BÁO")),
    "mistake":        ("FFF4E5", "B5651D", _L("COMMON MISTAKE", "LỖI THƯỜNG GẶP")),
    "interpretation": ("EAF1F7", "1F5C7A", _L("CLINICAL INTERPRETATION", "DIỄN GIẢI LÂM SÀNG")),
    "note":           ("F0F0F0", "404040", _L("NOTE", "LƯU Ý")),
}


def esc(s):
    """XML-escape text, preserving smart quotes as entities."""
    if s is None:
        s = ""
    s = str(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = s.replace("’", "&#x2019;").replace("‘", "&#x2018;")
    s = s.replace("“", "&#x201c;").replace("”", "&#x201d;")
    s = s.replace("–", "&#x2013;").replace("—", "&#x2014;")
    s = s.replace("•", "-")  # no raw bullet chars in text
    return s


# ----------------------------------------------------------------------------
# Low-level run / paragraph builders
# ----------------------------------------------------------------------------
def _has_vietnamese(text):
    """True if text uses letters Century Gothic lacks (e.g. the name Vương Mỹ Lượng)."""
    return any(ch in "ĂăĐđƠơƯư" or "Ạ" <= ch <= "ỹ" for ch in str(text or ""))


def run(text, sz=1600, color=BLACK, bold=False, italic=False, font=CG):
    if font == "Century Gothic" and _has_vietnamese(text):
        font = "Segoe UI"            # Vietnamese-safe, as in the VN deck
    b = ' b="1"' if bold else ""
    i = ' i="1"' if italic else ""
    return (
        f'<a:r><a:rPr lang="en-US" sz="{sz}"{b}{i} dirty="0">'
        f'<a:solidFill><a:srgbClr val="{color}"/></a:solidFill>'
        f'<a:latin typeface="{font}"/><a:cs typeface="{font}"/></a:rPr>'
        f'<a:t>{esc(text)}</a:t></a:r>'
    )


def para(runs_xml, algn="l", bullet=False, marL=0, indent=0, space_before=440,
         line=None):
    """One <a:p>. runs_xml is a string of <a:r> elements (may be empty)."""
    if bullet:
        bu = (f'<a:buFont typeface="Arial"/><a:buChar char="&#8226;"/>')
        marL = marL or 274320
        indent = indent or -274320
    else:
        bu = "<a:buNone/>"
    ln = f'<a:lnSpc><a:spcPct val="{line}"/></a:lnSpc>' if line else ""
    sb = f'<a:spcBef><a:spcPts val="{space_before}"/></a:spcBef>' if space_before else ""
    return (
        f'<a:p><a:pPr marL="{marL}" indent="{indent}" algn="{algn}">'
        f'{ln}{sb}{bu}</a:pPr>{runs_xml}</a:p>'
    )


def empty_para(sz=1000):
    return f'<a:p><a:pPr><a:buNone/></a:pPr><a:endParaRPr sz="{sz}"/></a:p>'


def textbox(spid, name, x, y, cx, cy, paras_xml, anchor="t",
            lIns=91440, tIns=45720, wrap="square"):
    return (
        f'<p:sp><p:nvSpPr><p:cNvPr id="{spid}" name="{name}"/>'
        f'<p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>'
        f'<p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
        f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/><a:ln><a:noFill/></a:ln></p:spPr>'
        f'<p:txBody><a:bodyPr wrap="{wrap}" lIns="{lIns}" tIns="{tIns}" rIns="{lIns}" '
        f'bIns="{tIns}" rtlCol="0" anchor="{anchor}"/><a:lstStyle/>{paras_xml}</p:txBody></p:sp>'
    )


def filled_box(spid, name, x, y, cx, cy, paras_xml, fill, anchor="t", round_=True,
               lIns=137160, tIns=91440):
    geom = "roundRect" if round_ else "rect"
    av = '<a:avLst><a:gd name="adj" fmla="val 6000"/></a:avLst>' if round_ else "<a:avLst/>"
    return (
        f'<p:sp><p:nvSpPr><p:cNvPr id="{spid}" name="{name}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
        f'<p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
        f'<a:prstGeom prst="{geom}">{av}</a:prstGeom>'
        f'<a:solidFill><a:srgbClr val="{fill}"/></a:solidFill><a:ln><a:noFill/></a:ln></p:spPr>'
        f'<p:txBody><a:bodyPr wrap="square" lIns="{lIns}" tIns="{tIns}" rIns="{lIns}" '
        f'bIns="{tIns}" rtlCol="0" anchor="{anchor}"/><a:lstStyle/>{paras_xml}</p:txBody></p:sp>'
    )


def pic(spid, name, rid, x, y, cx, cy):
    return (
        f'<p:pic><p:nvPicPr><p:cNvPr id="{spid}" name="{name}"/>'
        f'<p:cNvPicPr><a:picLocks noChangeAspect="1"/></p:cNvPicPr><p:nvPr/></p:nvPicPr>'
        f'<p:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></p:blipFill>'
        f'<p:spPr><a:xfrm><a:off x="{x}" y="{y}"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
        f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></p:spPr></p:pic>'
    )


# ----------------------------------------------------------------------------
# Recurring chrome: title + rule, footer, logo, slide number
# ----------------------------------------------------------------------------
def title_and_rule(title, color=None, sz=2800):
    color = color or TEAL
    t = textbox(10, "Title", ML, 160000, CW, 750000,
                para(run(title, sz=sz, color=color, bold=True), space_before=0),
                anchor="ctr")
    rule = (
        f'<p:sp><p:nvSpPr><p:cNvPr id="11" name="Rule"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
        f'<p:spPr><a:xfrm><a:off x="{ML}" y="940000"/><a:ext cx="{CW}" cy="0"/></a:xfrm>'
        f'<a:prstGeom prst="line"><a:avLst/></a:prstGeom>'
        f'<a:ln w="19050"><a:solidFill><a:srgbClr val="{TEAL}"/></a:solidFill></a:ln></p:spPr>'
        f'<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:endParaRPr/></a:p></p:txBody></p:sp>'
    )
    return t + rule


def footer_logo_num(logo_rid):
    footer = textbox(
        901, "Footer", 4599946, 6458701, 2845651, 276999,
        f'<a:p><a:r><a:rPr lang="en-US" sz="1200" dirty="0">'
        f'<a:solidFill><a:schemeClr val="accent5"><a:lumMod val="50000"/></a:schemeClr></a:solidFill>'
        f'<a:latin typeface="{VERD}"/></a:rPr>'
        f'<a:t>Neudata | #ClearDataClearImpact</a:t></a:r></a:p>',
        anchor="t", wrap="none")
    logo = pic(902, "Logo", logo_rid, 138853, 6122125, 716763, 683623)
    num = (
        '<p:sp><p:nvSpPr><p:cNvPr id="903" name="Slide Number"/>'
        '<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
        '<p:nvPr><p:ph type="sldNum" sz="quarter" idx="12"/></p:nvPr></p:nvSpPr>'
        '<p:spPr><a:xfrm><a:off x="11330000" y="6470000"/><a:ext cx="620000" cy="320000"/></a:xfrm></p:spPr>'
        '<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:pPr algn="r"/>'
        '<a:fld id="{C1FF6DA9-008F-8B48-92A6-B652298478BF}" type="slidenum">'
        '<a:rPr lang="en-US" sz="1050" smtClean="0"><a:solidFill><a:schemeClr val="accent5"><a:lumMod val="50000"/></a:schemeClr></a:solidFill></a:rPr><a:t>2</a:t></a:fld>'
        '<a:endParaRPr lang="en-US"/></a:p></p:txBody></p:sp>'
    )
    return footer + logo + num


# ----------------------------------------------------------------------------
# Slide body builders by type  ->  return inner spTree shapes string
# ----------------------------------------------------------------------------
def body_region(paras_xml, y=1080000, cy=4780000, anchor="ctr"):
    # default: vertically centre content in the band between the rule and the footer
    return textbox(20, "Body", ML, y, CW, cy, paras_xml, anchor=anchor)


def build_content(spec):
    """blocks: list of {header?, lines?[], bullets?bool, callout?kind}"""
    paras = []
    first = True
    for blk in spec.get("blocks", []):
        if not first:
            paras.append(empty_para(1050))
        first = False
        if blk.get("callout"):
            continue  # callouts rendered as separate boxes below
        if blk.get("header"):
            paras.append(para(run(blk["header"], sz=blk.get("hsz",2050), color=TEAL,
                                  bold=True), space_before=360))
        bullet = blk.get("bullets", False)
        for ln in blk.get("lines", []):
            if isinstance(ln, dict):
                paras.append(para(run(ln["text"], sz=ln.get("sz",1800),
                                      color=ln.get("color",BLACK), bold=ln.get("bold",False)),
                                  bullet=ln.get("bullet",bullet), marL=ln.get("marL",0),
                                  line="108000"))
            else:
                paras.append(para(run(ln, sz=blk.get("sz",1800)), bullet=bullet,
                                  line="108000"))
    calls = [b for b in spec.get("blocks", []) if b.get("callout")]
    # top-anchor when callouts occupy the lower band; otherwise vertically centre
    if paras:
        if calls:
            shapes = body_region("".join(paras), cy=3150000, anchor="t")
        else:
            shapes = body_region("".join(paras))
    else:
        shapes = ""

    # render callout boxes, bottom-anchored so they never collide with the footer
    if calls:
        BOTTOM = 5880000           # keep clear of footer/logo band
        gap = 130000
        heights = [340000 + 235000 * (len(c.get("lines", [])) + 1) for c in calls]
        total = sum(heights) + gap * (len(calls) - 1)
        y = min(spec.get("callout_y", BOTTOM - total), BOTTOM - total)
        sid = 40
        for c, h in zip(calls, heights):
            fill, hcol, label = CALLOUTS.get(c["callout"], CALLOUTS["note"])
            lbl = c.get("label", label)
            cp = [para(run(lbl + ("  -  " + c["header"] if c.get("header") else ""),
                           sz=1300, color=hcol, bold=True), space_before=0)]
            for ln in c.get("lines", []):
                cp.append(para(run(ln, sz=1300, color=BLACK), space_before=100))
            shapes += filled_box(sid, "Callout", ML, y, CW, h, "".join(cp), fill)
            y += h + gap
            sid += 1
    return shapes


def build_bullets(spec):
    paras = []
    if spec.get("intro"):
        paras.append(para(run(spec["intro"], sz=1900, color=GREY, italic=True),
                          space_before=0, line="108000"))
        paras.append(empty_para(950))
    for it in spec.get("items", []):
        if isinstance(it, dict):
            paras.append(para(run(it["text"], sz=it.get("sz",1950),
                                  bold=it.get("bold",False),
                                  color=it.get("color",BLACK)),
                              bullet=True, marL=274320 + it.get("level",0)*342900,
                              indent=-274320, space_before=560, line="106000"))
        else:
            paras.append(para(run(it, sz=1950), bullet=True, space_before=560,
                              line="106000"))
    return body_region("".join(paras))


def build_two_column(spec):
    halfw = (CW - 320040) // 2
    rx = ML + halfw + 320040
    def col(side, x, sid):
        paras = []
        if side.get("header"):
            paras.append(para(run(side["header"], sz=2050, color=TEAL, bold=True),
                              space_before=0))
        bullet = side.get("bullets", True)
        for ln in side.get("lines", []):
            paras.append(para(run(ln, sz=1650), bullet=bullet, space_before=520,
                              line="106000"))
        return textbox(sid, "Col", x, 1150000, halfw, 5050000, "".join(paras))
    shapes = ""
    if spec.get("left"):  shapes += col(spec["left"], ML, 21)
    if spec.get("right"): shapes += col(spec["right"], rx, 22)
    return shapes


def build_code(spec):
    shapes = ""
    y = 1080000
    if spec.get("intro"):
        shapes += textbox(20, "Intro", ML, y, CW, 520000,
                          para(run(spec["intro"], sz=1600, color=GREY, italic=True),
                               space_before=0))
        y += 560000
    code = spec.get("code", "")
    clines = code.split("\n")
    cparas = "".join(
        para(run(cl if cl else " ", sz=spec.get("code_sz",1300), color="1B3A4B",
                 font=MONO), space_before=0, line="100000")
        for cl in clines)
    ch = 180000 + 210000 * len(clines)
    shapes += filled_box(30, "Code", ML, y, CW, ch, cparas, "EDF1F2", round_=True)
    y += ch + 150000
    if spec.get("output"):
        olines = spec["output"].split("\n")
        oparas = (para(run(_L("Console output", "Kết quả (console)"), sz=1150, color=GREY, bold=True),
                       space_before=0)
                  + "".join(para(run(ol if ol else " ", sz=1250, color="1A1A1A",
                                     font=MONO), space_before=0, line="100000")
                            for ol in olines))
        oh = 300000 + 200000 * len(olines)
        shapes += filled_box(31, "Output", ML, y, CW, oh, oparas, "F2EFE6")
        y += oh + 140000
    if spec.get("note"):
        fill, hcol, label = CALLOUTS["interpretation"]
        np_ = para(run(_L("INTERPRETATION", "DIỄN GIẢI") + "  -  " + spec["note"], sz=1300, color=hcol,
                       bold=False), space_before=0)
        nh = 470000
        # never let the note box ride into the logo/footer band
        if y + nh > 6020000:
            y = 6020000 - nh
        shapes += filled_box(32, "Note", ML, y, CW, nh, np_, fill)
    return shapes


def build_image(spec, img_rid):
    # optional left-side notes column, image on right (or full width)
    notes = spec.get("side_notes")
    cap = spec.get("caption", "")
    iw = spec.get("img_w", 7000000)
    ih = spec.get("img_h", int(iw * spec.get("aspect", 0.75)))
    MAXH = 4850000   # keep clear of the footer/logo band (~5.95M EMU)

    def fit(iw, ih, avail_w, max_h):
        if iw > avail_w:
            ih = int(ih * avail_w / iw); iw = avail_w
        if ih > max_h:
            iw = int(iw * max_h / ih); ih = max_h
        return iw, ih

    if notes:
        colw = 3600000
        paras = []
        if spec.get("side_header"):
            paras.append(para(run(spec["side_header"], sz=1700, color=TEAL, bold=True),
                              space_before=0))
        for n in notes:
            paras.append(para(run(n, sz=1450), bullet=True))
        shapes = textbox(20, "Notes", ML, 1150000, colw, 5000000, "".join(paras))
        ix = ML + colw + 250000
        avail = (ML + CW) - ix
        iw, ih = fit(iw, ih, avail, MAXH)
        iy = 1150000 + max(0, (MAXH - ih)//2)
        shapes += pic(25, "Figure", img_rid, ix, iy, iw, ih)
    else:
        cap_h = 380000 if cap else 0
        iw, ih = fit(iw, ih, CW, MAXH - cap_h)
        ix = ML + (CW - iw)//2
        iy = 1150000
        shapes = pic(25, "Figure", img_rid, ix, iy, iw, ih)
        if cap:
            shapes += textbox(26, "Caption", ML, iy + ih + 60000, CW, 400000,
                              para(run(cap, sz=1300, color=GREY, italic=True),
                                   algn="ctr", space_before=0))
    return shapes


def build_table(spec):
    headers = spec["headers"]; rows = spec["rows"]
    ncol = len(headers)
    tw = CW
    colw = [tw // ncol] * ncol
    colw[-1] = tw - sum(colw[:-1])
    grid = "".join(f'<a:gridCol w="{w}"/>' for w in colw)
    def cell(text, header=False):
        col = "FFFFFF" if header else BLACK
        fill = (f'<a:solidFill><a:srgbClr val="{TEAL}"/></a:solidFill>' if header
                else '<a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill>')
        b = '1' if header else '0'
        return (f'<a:tc><a:txBody><a:bodyPr/><a:lstStyle/>'
                f'<a:p><a:pPr algn="l"/><a:r><a:rPr lang="en-US" sz="1300" b="{b}" dirty="0">'
                f'<a:solidFill><a:srgbClr val="{col}"/></a:solidFill>'
                f'<a:latin typeface="{CG}"/></a:rPr><a:t>{esc(text)}</a:t></a:r></a:p></a:txBody>'
                f'<a:tcPr marL="73152" marR="73152" marT="36576" marB="36576" anchor="ctr">{fill}</a:tcPr></a:tc>')
    rowh = 380000
    hrow = f'<a:tr h="{rowh}">' + "".join(cell(h, True) for h in headers) + "</a:tr>"
    brows = ""
    for r in rows:
        brows += f'<a:tr h="{rowh}">' + "".join(cell(c) for c in r) + "</a:tr>"
    tbl = (
        f'<a:tbl><a:tblPr firstRow="1" bandRow="1">'
        f'<a:tableStyleId>{{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}}</a:tableStyleId></a:tblPr>'
        f'<a:tblGrid>{grid}</a:tblGrid>{hrow}{brows}</a:tbl>'
    )
    th = rowh * (len(rows) + 1)
    gf = (f'<p:graphicFrame><p:nvGraphicFramePr><p:cNvPr id="30" name="Table"/>'
          f'<p:cNvGraphicFramePr/><p:nvPr/></p:nvGraphicFramePr>'
          f'<p:xfrm><a:off x="{ML}" y="1150000"/><a:ext cx="{tw}" cy="{th}"/></p:xfrm>'
          f'<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/table">'
          f'{tbl}</a:graphicData></a:graphic></p:graphicFrame>')
    shapes = gf
    if spec.get("caption"):
        # allow for row wrapping: estimate generously so caption clears the table
        cap_y = 1150000 + (len(rows) + 1) * 470000 + 90000
        shapes += textbox(31, "Caption", ML, cap_y, CW, 500000,
                          para(run(spec["caption"], sz=1300, color=GREY, italic=True),
                               space_before=0))
    return shapes
