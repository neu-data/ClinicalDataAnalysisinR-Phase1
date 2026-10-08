# -*- coding: utf-8 -*-
"""
Assemble Clinical_Data_Analysis_in_R_Phase1.pptx from a list of slide specs,
cloning the Neudata template tree and writing generated slides + notes.

Usage:  python assemble.py            (imports content.py -> SLIDES)
"""
import os, shutil, re
import engine as E

HERE = os.path.dirname(os.path.abspath(__file__))        # .../Deck_and_Build/deckbuild
DECKROOT = os.path.dirname(HERE)                          # .../Deck_and_Build
ROOT = os.path.dirname(DECKROOT)                          # project root
TPL_UNPACKED = os.path.join(ROOT, "unpacked")
BUILD = os.path.join(HERE, "build")
OUT = os.path.join(DECKROOT, "Slides", "Clinical_Data_Analysis_in_R_Phase1.pptx")
RES = os.path.join(ROOT, "Course", "Resources")

A_NS = ('xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
        'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"')

GRP = ('<p:nvGrpSpPr><p:cNvPr id="1" name=""/>'
       '<p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr><a:xfrm>'
       '<a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/>'
       '<a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>')


def slide_xml(shapes, bg_white=False):
    bg = ('<p:bg><p:bgPr><a:solidFill><a:schemeClr val="bg1"/></a:solidFill>'
          '<a:effectLst/></p:bgPr></p:bg>') if bg_white else ""
    return (f'<?xml version="1.0" encoding="utf-8"?>\n<p:sld {A_NS}>'
            f'<p:cSld>{bg}<p:spTree>{GRP}{shapes}</p:spTree></p:cSld>'
            f'<p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>')


# ----------------------------------------------------------------------------
# Special full-slide builders
# ----------------------------------------------------------------------------
def build_title(spec, logo_rid):
    # big centred logo (slide1 geometry)
    logo = E.pic(2, "Logo", logo_rid, 768613, 4410394, 2566257, 2447606)
    # course title (teal, Arial ~40pt, centred)
    title_lines = spec["title"] if isinstance(spec["title"], list) else [spec["title"]]
    tparas = "".join(
        E.para(E.run(t, sz=spec.get("title_sz",4000), color=E.TEAL_TITLE, bold=True,
                     font=E.CG), algn="ctr", space_before=0)
        for t in title_lines)
    title = E.textbox(3, "Title", 0, 1500000, E.SLIDE_W, 1700000, tparas, anchor="ctr",
                      lIns=457200, tIns=0)
    # subtitle lines (Segoe UI 20pt, centred)
    subs = "".join(
        E.para(E.run(s, sz=2000, color="000000", font=E.SEG), algn="ctr")
        for s in spec.get("subtitle", []))
    sub = E.textbox(5, "Subtitle", 0, 3250000, E.SLIDE_W, 1000000, subs, anchor="t",
                    lIns=457200)
    # date (Segoe UI 14pt bold, right)
    date = E.textbox(6, "Date", 7902094, 5833766, 3465009, 326571,
                     E.para(E.run("Date: " + spec.get("date","__-__-____"), sz=1400,
                                  color="000000", bold=True, font=E.SEG),
                            algn="r", space_before=0), anchor="b", lIns=0, tIns=0)
    num = ('<p:sp><p:nvSpPr><p:cNvPr id="7" name="Slide Number"/>'
           '<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
           '<p:nvPr><p:ph type="sldNum" sz="quarter" idx="12"/></p:nvPr></p:nvSpPr>'
           '<p:spPr><a:xfrm><a:off x="11330000" y="6470000"/><a:ext cx="620000" cy="320000"/></a:xfrm></p:spPr><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:pPr algn="r"/>'
           '<a:fld id="{C1FF6DA9-008F-8B48-92A6-B652298478BF}" type="slidenum">'
           '<a:rPr lang="en-US" sz="1050" smtClean="0"><a:solidFill><a:schemeClr val="accent5"><a:lumMod val="50000"/></a:schemeClr></a:solidFill></a:rPr><a:t>1</a:t></a:fld>'
           '<a:endParaRPr lang="en-US"/></a:p></p:txBody></p:sp>')
    return logo + title + sub + date + num


def build_divider(spec, logo_rid):
    # teal title (Arial 32pt bold) like template slide2
    tt = E.textbox(6, "DayTitle", E.ML, 548640, 11430000, 700000,
                   E.para(E.run(spec["title"], sz=3200, color=E.TEAL, bold=True,
                                font=E.CG), space_before=0), anchor="t")
    rule = (f'<p:sp><p:nvSpPr><p:cNvPr id="7" name="Rule"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{E.ML}" y="1325880"/><a:ext cx="{E.CW}" cy="19050"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
            f'<a:solidFill><a:srgbClr val="{E.TEAL}"/></a:solidFill><a:ln><a:noFill/></a:ln></p:spPr>'
            f'<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:endParaRPr/></a:p></p:txBody></p:sp>')
    # agenda body (blue "Plan" header + list) like slide2
    paras = []
    if spec.get("plan_label", True):
        paras.append(E.para(E.run(spec.get("plan_title","Plan"), sz=2800, color=E.BLUE,
                                  font=E.CG), space_before=0))
        paras.append(E.empty_para(800))
    for it in spec.get("agenda", []):
        paras.append(E.para(E.run(it, sz=1900, color="000000"), bullet=True,
                            marL=274320, indent=-274320))
    body = E.textbox(8, "Agenda", E.ML, 1600000, E.CW, 4400000, "".join(paras)) if paras else ""
    return tt + rule + body + E.footer_logo_num(logo_rid)


COPYRIGHT = [
    "All property rights and copyright are reserved.",
    "",
    "This presentation contains proprietary data, information, and materials developed by "
    "Neudata for dedicated use only and may not be communicated, copied, reproduced, "
    "distributed, published, or cited, in whole or in part, without the prior written "
    "consent of Neudata.",
    "Where explicit written permission has been granted, appropriate attribution must be "
    "included, followed by “by courtesy of Neudata”.",
    "",
    "Any unauthorized use or infringement of these materials may give rise to legal action "
    "and claims for damages, without prejudice to any other rights of Neudata, including "
    "rights relating to patents, trademarks, or other forms of intellectual property protection.",
]


def build_closing(spec, logo_rid):
    logo = E.pic(2, "Logo", logo_rid, 4438553, 723719, 3314894, 2906250)
    head = E.textbox(3, "CopyHead", 1100000, 3650000, 9000000, 500000,
                     E.para(E.run("Copyright © Neudata, 2026", sz=2400, color="4472C4",
                                  bold=True, font=E.CG), space_before=0), anchor="t", lIns=0)
    cps = "".join(
        E.empty_para(800) if not c else
        E.para(E.run(c, sz=1200, color="000000", font="Courier New"), space_before=100)
        for c in COPYRIGHT)
    body = E.textbox(4, "CopyBody", 1100000, 4200000, 9991440, 2200000, cps, anchor="t", lIns=0)
    footer = E.textbox(
        901, "Footer", 4599946, 6458701, 2845651, 276999,
        f'<a:p><a:r><a:rPr lang="en-US" sz="1200" dirty="0">'
        f'<a:solidFill><a:schemeClr val="accent5"><a:lumMod val="50000"/></a:schemeClr></a:solidFill>'
        f'<a:latin typeface="{E.VERD}"/></a:rPr>'
        f'<a:t>Neudata | #ClearDataClearImpact</a:t></a:r></a:p>', wrap="none")
    num = ('<p:sp><p:nvSpPr><p:cNvPr id="905" name="Slide Number"/>'
           '<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
           '<p:nvPr><p:ph type="sldNum" sz="quarter" idx="12"/></p:nvPr></p:nvSpPr>'
           '<p:spPr><a:xfrm><a:off x="11330000" y="6470000"/><a:ext cx="620000" cy="320000"/></a:xfrm></p:spPr><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:pPr algn="r"/>'
           '<a:fld id="{C1FF6DA9-008F-8B48-92A6-B652298478BF}" type="slidenum">'
           '<a:rPr lang="en-US" sz="1050" smtClean="0"><a:solidFill><a:schemeClr val="accent5"><a:lumMod val="50000"/></a:schemeClr></a:solidFill></a:rPr><a:t>x</a:t></a:fld>'
           '<a:endParaRPr lang="en-US"/></a:p></p:txBody></p:sp>')
    return logo + head + body + footer + num


# ----------------------------------------------------------------------------
# Notes slide
# ----------------------------------------------------------------------------
def notes_xml(notes_text):
    paras = ""
    for line in (notes_text or "Speaker notes.").split("\n"):
        line = line.strip()
        if not line:
            paras += '<a:p><a:endParaRPr lang="en-US" sz="1400"/></a:p>'
            continue
        bold = "1" if line.endswith(":") or line.isupper() else "0"
        paras += (f'<a:p><a:r><a:rPr lang="en-US" sz="1400" b="{bold}" dirty="0"/>'
                  f'<a:t>{E.esc(line)}</a:t></a:r></a:p>')
    return (f'<?xml version="1.0" encoding="utf-8"?>\n<p:notes {A_NS}><p:cSld><p:spTree>'
            '<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
            '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/>'
            '<a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
            '<p:sp><p:nvSpPr><p:cNvPr id="2" name="Slide Image Placeholder 1"/>'
            '<p:cNvSpPr><a:spLocks noGrp="1" noRot="1" noChangeAspect="1"/></p:cNvSpPr>'
            '<p:nvPr><p:ph type="sldImg"/></p:nvPr></p:nvSpPr><p:spPr/></p:sp>'
            '<p:sp><p:nvSpPr><p:cNvPr id="3" name="Notes Placeholder 2"/>'
            '<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
            '<p:nvPr><p:ph type="body" idx="1"/></p:nvPr></p:nvSpPr><p:spPr/>'
            f'<p:txBody><a:bodyPr/><a:lstStyle/>{paras}</p:txBody></p:sp>'
            '<p:sp><p:nvSpPr><p:cNvPr id="4" name="Slide Number Placeholder 3"/>'
            '<p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
            '<p:nvPr><p:ph type="sldNum" sz="quarter" idx="10"/></p:nvPr></p:nvSpPr>'
            '<p:spPr/><p:txBody><a:bodyPr/><a:lstStyle/><a:p>'
            '<a:fld id="{F7021451-1387-4CA6-816F-3879F97B5CBC}" type="slidenum">'
            '<a:rPr lang="en-US"/><a:t>1</a:t></a:fld></a:p></p:txBody></p:sp>'
            '</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:notes>')


# ----------------------------------------------------------------------------
# Main assembly
# ----------------------------------------------------------------------------
def build(slides):
    if os.path.exists(BUILD):
        shutil.rmtree(BUILD)
    shutil.copytree(TPL_UNPACKED, BUILD)
    sld_dir = os.path.join(BUILD, "ppt", "slides")
    notes_dir = os.path.join(BUILD, "ppt", "notesSlides")
    media_dir = os.path.join(BUILD, "ppt", "media")
    # wipe template's example slides + notes
    for d in (sld_dir, notes_dir):
        for f in os.listdir(d):
            if f.endswith(".xml"):
                os.remove(os.path.join(d, f))
        rels = os.path.join(d, "_rels")
        for f in os.listdir(rels):
            os.remove(os.path.join(rels, f))

    LOGO_RID = "rId3"
    img_cache = {}     # source path -> media filename
    media_idx = [1]    # image1.jpg already exists (logo)

    def add_media(src):
        if src in img_cache:
            return img_cache[src]
        media_idx[0] += 1
        ext = os.path.splitext(src)[1].lower() or ".png"
        fn = f"image{media_idx[0]}{ext}"
        shutil.copy(src, os.path.join(media_dir, fn))
        img_cache[src] = fn
        return fn

    pres_rels = []   # (rId, target)
    ctypes_slides = []
    sld_ids = []     # (slideId, rId)
    next_pres_rid = [100]

    for i, spec in enumerate(slides, start=1):
        t = spec["type"]
        extra_img_rels = []   # (rId, target media filename)
        if t == "title":
            shapes = build_title(spec, LOGO_RID); white = True
        elif t == "divider":
            shapes = build_divider(spec, LOGO_RID); white = True
        elif t == "closing":
            shapes = build_closing(spec, LOGO_RID); white = True
        else:
            white = True
            head = E.title_and_rule(spec["title"], color=spec.get("title_color"))
            if t == "content":
                body = E.build_content(spec)
            elif t == "bullets":
                body = E.build_bullets(spec)
            elif t == "two_column":
                body = E.build_two_column(spec)
            elif t == "code":
                body = E.build_code(spec)
            elif t == "table":
                body = E.build_table(spec)
            elif t == "image":
                fn = add_media(os.path.join(RES, spec["image"]) if not os.path.isabs(spec["image"]) else spec["image"])
                rid = "rId4"
                extra_img_rels.append((rid, fn))
                body = E.build_image(spec, rid)
            else:
                raise ValueError("unknown slide type: " + t)
            shapes = head + body + E.footer_logo_num(LOGO_RID)

        # write slide xml
        with open(os.path.join(sld_dir, f"slide{i}.xml"), "w", encoding="utf-8") as f:
            f.write(slide_xml(shapes, bg_white=white))
        # slide rels
        rels = ['<?xml version="1.0" encoding="utf-8"?>',
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">',
                f'<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout7.xml"/>',
                f'<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/notesSlide" Target="../notesSlides/notesSlide{i}.xml"/>',
                f'<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/image1.jpg"/>']
        for rid, fn in extra_img_rels:
            rels.append(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="../media/{fn}"/>')
        rels.append('</Relationships>')
        with open(os.path.join(sld_dir, "_rels", f"slide{i}.xml.rels"), "w", encoding="utf-8") as f:
            f.write("\n".join(rels))
        # notes slide + rels
        with open(os.path.join(notes_dir, f"notesSlide{i}.xml"), "w", encoding="utf-8") as f:
            f.write(notes_xml(spec.get("notes", "")))
        with open(os.path.join(notes_dir, "_rels", f"notesSlide{i}.xml.rels"), "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n'
                    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/notesMaster" Target="../notesMasters/notesMaster1.xml"/>'
                    f'<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="../slides/slide{i}.xml"/>'
                    '</Relationships>')
        # presentation rel + ids
        rid = f"rId{next_pres_rid[0]}"; next_pres_rid[0] += 1
        pres_rels.append((rid, f"slides/slide{i}.xml"))
        sld_ids.append((255 + i, rid))
        ctypes_slides.append((i,))

    _write_presentation(BUILD, pres_rels, sld_ids)
    _write_content_types(BUILD, len(slides))
    return len(slides)


def _write_presentation(build, pres_rels, sld_ids):
    pres_path = os.path.join(build, "ppt", "presentation.xml")
    xml = open(pres_path, encoding="utf-8").read()
    lst = "<p:sldIdLst>" + "".join(
        f'<p:sldId id="{sid}" r:id="{rid}"/>' for sid, rid in sld_ids) + "</p:sldIdLst>"
    xml = re.sub(r"<p:sldIdLst>.*?</p:sldIdLst>", lst, xml, flags=re.S)
    open(pres_path, "w", encoding="utf-8").write(xml)
    # rebuild presentation rels: keep non-slide rels, add slide rels
    rels_path = os.path.join(build, "ppt", "_rels", "presentation.xml.rels")
    rx = open(rels_path, encoding="utf-8").read()
    keep = [m.group(0) for m in re.finditer(r"<Relationship [^>]*/>", rx)
            if "/slide" not in m.group(0) or "slideMaster" in m.group(0)
            or "slideLayout" in m.group(0)]
    keep = [k for k in keep if "officeDocument/2006/relationships/slide\"" not in k
            and "/slides/slide" not in k]
    add = "".join(f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="{tgt}"/>'
                  for rid, tgt in pres_rels)
    new = ('<?xml version="1.0" encoding="utf-8"?>\n'
           '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
           + "".join(keep) + add + "</Relationships>")
    open(rels_path, "w", encoding="utf-8").write(new)


def _write_content_types(build, n):
    ct_path = os.path.join(build, "[Content_Types].xml")
    xml = open(ct_path, encoding="utf-8").read()
    # strip existing slide/notesSlide overrides
    xml = re.sub(r'<Override PartName="/ppt/slides/slide\d+\.xml"[^>]*/>', "", xml)
    xml = re.sub(r'<Override PartName="/ppt/notesSlides/notesSlide\d+\.xml"[^>]*/>', "", xml)
    adds = ""
    for i in range(1, n + 1):
        adds += (f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
                 f'<Override PartName="/ppt/notesSlides/notesSlide{i}.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml"/>')
    xml = xml.replace("</Types>", adds + "</Types>")
    # ensure png/jpg default exists
    if 'Extension="png"' not in xml:
        xml = xml.replace("</Types>", '<Default Extension="png" ContentType="image/png"/></Types>')
    open(ct_path, "w", encoding="utf-8").write(xml)


def pack():
    """Zip the fully-unpacked OOXML tree in BUILD into a .pptx (self-contained;
    no external skill dependency). [Content_Types].xml is written first."""
    import zipfile
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    files = []
    for root, _dirs, names in os.walk(BUILD):
        for n in names:
            full = os.path.join(root, n)
            arc = os.path.relpath(full, BUILD).replace(os.sep, "/")
            files.append((full, arc))
    # [Content_Types].xml must come first in the package
    files.sort(key=lambda t: (t[1] != "[Content_Types].xml", t[1]))
    if os.path.exists(OUT):
        os.remove(OUT)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for full, arc in files:
            z.write(full, arc)
    return OUT


if __name__ == "__main__":
    import content
    n = build(content.SLIDES)
    print("Built", n, "slides")
    pack()
    print("Wrote", OUT)
