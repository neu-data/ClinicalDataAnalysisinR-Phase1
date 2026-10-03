"""Convert a knitted book chapter (restricted Markdown, see Book/AUTHORING.md) to LaTeX
for the neudatabook class.

    from md2tex import convert
    tex = convert(markdown_text, bib_keys, figure_dir="figures")
"""
import re

# ----------------------------------------------------------------- inline text
SPECIAL = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "$": r"\$", "&": r"\&",
           "%": r"\%", "#": r"\#", "_": r"\_", "^": r"\textasciicircum{}",
           "~": r"\textasciitilde{}"}
# characters missing from the text font: typeset them as maths
SYMBOLS = {"≤": r"$\leq$", "≥": r"$\geq$", "×": r"$\times$", "±": r"$\pm$", "→": r"$\rightarrow$",
           "←": r"$\leftarrow$", "≠": r"$\neq$", "≈": r"$\approx$", "−": r"$-$", "√": r"$\surd$",
           "χ": r"$\chi$", "β": r"$\beta$", "α": r"$\alpha$", "μ": r"$\mu$", "σ": r"$\sigma$",
           "²": r"\textsuperscript{2}", "³": r"\textsuperscript{3}", "✓": r"$\checkmark$",
           "⇒": r"$\Rightarrow$", "∞": r"$\infty$", "Δ": r"$\Delta$"}


def esc(s):
    out = []
    for ch in s:
        if ch in SPECIAL:
            out.append(SPECIAL[ch])
        elif ch in SYMBOLS:
            out.append(SYMBOLS[ch])
        else:
            out.append(ch)
    return "".join(out)


def esc_code_inline(s):
    # inside \code{}: escape and allow line breaks after common separators
    t = esc(s)
    return re.sub(r"(\\_|/|\.|,|\(|=)", lambda m: m.group(1) + r"\allowbreak{}", t)


class Inline:
    def __init__(self, bib_keys):
        self.keys = bib_keys

    def cite(self, inner):
        """'@a; @b, p. 4' -> \\parencite[p.~4]{a,b}"""
        parts = [p.strip() for p in inner.split(";")]
        keys, post = [], ""
        for p in parts:
            m = re.match(r"-?@([\w:.\-]+)\s*(?:,\s*(.+))?$", p)
            if not m or m.group(1) not in self.keys:
                return None
            keys.append(m.group(1))
            if m.group(2):
                post = m.group(2).replace("p. ", "p.~").replace("pp. ", "pp.~")
        opt = f"[{esc(post)}]" if post else ""
        return rf"\parencite{opt}{{{','.join(keys)}}}"

    def __call__(self, text):
        # protect segments that must not be escaped
        store = []

        def keep(s):
            store.append(s)
            return f"\x00{len(store) - 1}\x00"

        t = text
        t = re.sub(r"`([^`]+)`", lambda m: keep(r"\code{" + esc_code_inline(m.group(1)) + "}"), t)
        t = re.sub(r"(?<!\\)\$\$(.+?)\$\$", lambda m: keep(r"\[" + m.group(1) + r"\]"), t)
        t = re.sub(r"(?<![\\$])\$(?!\s)([^$\n]+?)(?<!\s)\$(?!\d)", lambda m: keep("$" + m.group(1) + "$"), t)

        def citerep(m):
            c = self.cite(m.group(1))
            return keep(c) if c else m.group(0)
        t = re.sub(r"\[([^\[\]]*@[^\[\]]+)\]", citerep, t)
        # links [text](url)
        t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
                   lambda m: keep(r"\href{" + m.group(2).replace("%", r"\%").replace("#", r"\#")
                                  + "}{" + self.emph(esc(m.group(1))) + "}"), t)
        t = re.sub(r"<(https?://[^>\s]+)>", lambda m: keep(r"\url{" + m.group(1) + "}"), t)
        # in-text citations @key
        t = re.sub(r"(?<![\w.@])@([A-Za-z][\w:\-]*\w)",
                   lambda m: keep(rf"\textcite{{{m.group(1)}}}") if m.group(1) in self.keys else m.group(0), t)
        # bare URLs
        t = re.sub(r"(?<![({\w])(https?://[^\s)]+[^\s).,;:])", lambda m: keep(r"\url{" + m.group(1) + "}"), t)
        t = esc(t)
        t = self.emph(t)
        while "\x00" in t:
            t = re.sub(r"\x00(\d+)\x00", lambda m: store[int(m.group(1))], t)
        return t

    @staticmethod
    def emph(t):
        t = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", t)
        t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\\emph{\1}", t)
        t = re.sub(r"(?<![\w\\])\\_(?!\s)(.+?)(?<!\s)\\_(?!\w)", r"\\emph{\1}", t)
        return t


# symbols printed by R packages (cli) that the code font lacks
CONSOLE = str.maketrans({"ℹ": "i", "✔": "v", "✖": "x", "❯": ">", "→": "->", "…": "..."})

# ----------------------------------------------------------------- R code highlighting
R_KEYWORDS = {"if", "else", "for", "while", "function", "return", "in", "next", "break",
              "TRUE", "FALSE", "NULL", "NA", "Inf", "NaN", "repeat", "library", "require"}
TOKEN = re.compile(r"""
    (?P<comment>\#.*$)
  | (?P<string>"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')
  | (?P<number>\b\d+(?:\.\d+)?(?:[eE][+-]?\d+)?L?\b)
  | (?P<func>[A-Za-z_.][\w.]*(?=\())
  | (?P<word>[A-Za-z_.][\w.]*)
  | (?P<op><-|->|\|>|%>%|%in%|==|!=|<=|>=|&&|\|\||[~=+\-*/^<>!&|])
  | (?P<other>.)
""", re.X)


def vesc(s):
    """Escape for an fvextra Verbatim with commandchars=\\\\\\{\\}."""
    return s.replace("\\", r"\textbackslash{}").replace("{", r"\{").replace("}", r"\}") \
            .replace(r"\textbackslash\{\}", r"\textbackslash{}")


def highlight_line(line):
    out = []
    for m in TOKEN.finditer(line):
        kind, val = m.lastgroup, m.group()
        v = vesc(val)
        if kind == "comment":
            out.append(r"\RComment{" + v + "}")
        elif kind == "string":
            out.append(r"\RString{" + v + "}")
        elif kind == "number":
            out.append(r"\RNumber{" + v + "}")
        elif kind == "func":
            out.append(r"\RFunction{" + v + "}")
        elif kind == "word" and val in R_KEYWORDS:
            out.append(r"\RKeyword{" + v + "}")
        elif kind == "op":
            out.append(r"\ROperator{" + v + "}")
        else:
            out.append(v)
    return "".join(out)


# ----------------------------------------------------------------- tables
def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    cells, cur, in_code = [], "", False
    for ch in line:
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append(cur.strip()); cur = ""
        else:
            cur += ch
    cells.append(cur.strip())
    return cells


def table_tex(lines, caption, inline):
    header = split_row(lines[0])
    aligns = []
    for spec in split_row(lines[1]):
        t = spec.strip()
        aligns.append("c" if t.startswith(":") and t.endswith(":") else "r" if t.endswith(":") else "l")
    rows = [split_row(l) for l in lines[2:]]
    n = len(header)
    rows = [(r + [""] * n)[:n] for r in rows]
    lens = [max(len(re.sub(r"[`*]", "", x[c])) for x in [header] + rows) for c in range(n)]
    wide = sum(lens) + 3 * n > 92
    if wide:
        capped = [min(max(L, 4), 45) for L in lens]
        avail = 0.98 - 0.022 * n                        # leave room for column padding
        cols = "".join(r">{\RaggedRight\arraybackslash}p{%.3f\linewidth}" % (avail * c / sum(capped))
                       for c in capped)
    else:
        cols = "".join(aligns[:n])
    head = " & ".join(r"\nbth{" + inline(h.replace("**", "")) + "}" for h in header) + r" \\"
    body = []
    for i, r in enumerate(rows):
        shade = r"\rowcolor{NeudataMist}" if i % 2 else ""
        body.append(shade + " & ".join(inline(c) for c in r) + r" \\")
    size = r"\footnotesize" if wide else r"\small"
    cap = (r"\caption{" + inline(caption) + "}") if caption else ""
    if len(rows) > 18:                                  # long tables break across pages
        return "\n".join([r"\begingroup" + size, rf"\begin{{longtable}}{{{cols}}}",
                          (cap + r"\\") if cap else "", r"\toprule", r"\nbheader " + head, r"\midrule",
                          r"\endfirsthead", r"\nbheader " + head, r"\midrule", r"\endhead",
                          r"\bottomrule", r"\endlastfoot", *body, r"\end{longtable}", r"\endgroup"])
    out = [r"\begin{table}[htbp]", r"\centering", size]
    if cap:
        out.append(cap)
    out += [rf"\begin{{tabular}}{{{cols}}}", r"\toprule", r"\nbheader " + head,
            r"\midrule", *body, r"\bottomrule", r"\end{tabular}", r"\end{table}"]
    return "\n".join(out)


# ----------------------------------------------------------------- blocks
HEADING = re.compile(r"^(#{1,4})\s+(.*?)\s*(\{[^}]*\})?\s*$")
DIV_OPEN = re.compile(r"^:::+\s*\{\.([\w-]+)(?:\s+title=\"([^\"]*)\")?[^}]*\}\s*$")
IMAGE = re.compile(r"^!\[(.*)\]\(([^)\s]+)\)(\{[^}]*\})?\s*$")
LIST_ITEM = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")


def convert(md, bib_keys, figure_dir="figures", heading_offset=0, unnumbered_sections=False):
    inline = Inline(bib_keys)
    lines = md.replace("\r\n", "\n").split("\n")
    out = []
    i = 0

    def flush_para(buf):
        if buf:
            out.append(inline(" ".join(s.strip() for s in buf)))
            out.append("")
        buf.clear()

    para = []
    front = False          # inside an unnumbered chapter (preface): its sections are unnumbered too
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # fenced code / output
        if stripped.startswith("```"):
            flush_para(para)
            lang = stripped[3:].strip().strip("{}").strip()
            j = i + 1
            block = []
            while j < len(lines) and not lines[j].strip().startswith("```"):
                block.append(lines[j]); j += 1
            i = j + 1
            if lang.lower() in ("r", "r ") or lang.lower().startswith("r"):
                out.append(r"\begin{rcode}")
                out.append(r"\begin{RCodeV}")
                out += [highlight_line(b) for b in block]
                out.append(r"\end{RCodeV}")
                out.append(r"\end{rcode}")
            else:
                out.append(r"\begin{routput}")
                out.append(r"\begin{ROutputV}")
                out += [b.translate(CONSOLE) for b in block]
                out.append(r"\end{ROutputV}")
                out.append(r"\end{routput}")
            out.append("")
            continue

        # display maths
        if stripped.startswith("$$"):
            flush_para(para)
            if stripped != "$$" and stripped.endswith("$$") and len(stripped) > 4:
                out.append(r"\[" + stripped[2:-2] + r"\]"); i += 1; out.append(""); continue
            j = i + 1
            block = [stripped[2:]] if stripped != "$$" else []
            while j < len(lines) and not lines[j].strip().endswith("$$"):
                block.append(lines[j]); j += 1
            last = lines[j].strip()[:-2] if j < len(lines) else ""
            if last:
                block.append(last)
            out.append(r"\[" + "\n".join(block) + r"\]")
            out.append("")
            i = j + 1
            continue

        # headings
        m = HEADING.match(line)
        if m and not stripped.startswith("#>"):
            flush_para(para)
            level = len(m.group(1)) + heading_offset
            title = inline(m.group(2))
            attrs = m.group(3) or ""
            label = re.search(r"#([\w-]+)", attrs)
            unnum = ".unnumbered" in attrs or "-}" in attrs or (unnumbered_sections and level >= 3)
            if level == 1:
                front = unnum
            elif front:
                unnum = True
            cmd = {1: "chapter", 2: "section", 3: "subsection", 4: "subsubsection"}.get(level, "paragraph")
            if unnum:
                out.append(rf"\{cmd}*{{{title}}}")
                if cmd == "chapter" or (cmd == "section" and not front):
                    out.append(rf"\addcontentsline{{toc}}{{{cmd}}}{{{title}}}")
                if cmd == "chapter":
                    out.append(rf"\markboth{{{title}}}{{{title}}}")
            else:
                out.append(rf"\{cmd}{{{title}}}")
            if label:
                out.append(rf"\label{{{label.group(1)}}}")
            out.append("")
            i += 1
            continue

        # fenced divs
        m = DIV_OPEN.match(stripped)
        if m:
            flush_para(para)
            kind, title = m.group(1), m.group(2) or ""
            depth, j, block = 1, i + 1, []
            while j < len(lines):
                s = lines[j].strip()
                if DIV_OPEN.match(s):
                    depth += 1
                elif re.match(r"^:::+\s*$", s):
                    depth -= 1
                    if depth == 0:
                        break
                block.append(lines[j]); j += 1
            i = j + 1
            inner = convert("\n".join(block), bib_keys, figure_dir)
            if kind.startswith("callout-"):
                out.append(rf"\begin{{nbcallout}}{{{kind[8:]}}}{{{inline(title)}}}")
                out.append(inner.strip())
                out.append(r"\end{nbcallout}")
            elif kind == "objectives":
                out += [r"\begin{objectives}", inner.strip(), r"\end{objectives}"]
            elif kind == "exercise":
                out += [rf"\begin{{exercise}}{{{inline(title)}}}", inner.strip(), r"\end{exercise}"]
            else:
                out.append(inner.strip())
            out.append("")
            continue

        # images
        m = IMAGE.match(stripped)
        if m:
            flush_para(para)
            cap, path = m.group(1), m.group(2)
            name = path.split("/")[-1].rsplit(".", 1)[0]
            out += [r"\begin{figure}[htbp]", r"\centering",
                    rf"\includegraphics[width=0.86\linewidth]{{{figure_dir}/{name}}}"]
            if cap:
                out.append(r"\caption{" + inline(cap) + "}")
            out += [r"\end{figure}", ""]
            i += 1
            continue

        # tables (optional "Table: caption" line before or after)
        cap = None
        if stripped.startswith("Table:"):
            k = i + 1
            while k < len(lines) and not lines[k].strip():
                k += 1
            if k < len(lines) and lines[k].strip().startswith("|"):
                flush_para(para)
                cap = stripped[6:].strip()
                i = k
                line, stripped = lines[i], lines[i].strip()
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            flush_para(para)
            j, block = i, []
            while j < len(lines) and lines[j].strip().startswith("|"):
                block.append(lines[j]); j += 1
            i = j
            out.append(table_tex(block, cap, inline))
            out.append("")
            continue

        # lists
        m = LIST_ITEM.match(line)
        if m:
            flush_para(para)
            j, items = i, []
            while j < len(lines):
                mm = LIST_ITEM.match(lines[j])
                if mm:
                    items.append([len(mm.group(1)), mm.group(2), mm.group(3)])
                elif lines[j].strip() and items and (lines[j].startswith("  ") or lines[j].startswith("\t")):
                    items[-1][2] += " " + lines[j].strip()
                elif not lines[j].strip():
                    # a blank line ends the list unless the next line continues it
                    if j + 1 < len(lines) and LIST_ITEM.match(lines[j + 1]):
                        j += 1; continue
                    break
                else:
                    break
                j += 1
            i = j
            out.append(render_list(items, inline))
            out.append("")
            continue

        # horizontal rule
        if re.match(r"^(-{3,}|\*{3,})$", stripped):
            flush_para(para); i += 1; continue
        if stripped.startswith("<!--"):
            while i < len(lines) and "-->" not in lines[i]:
                i += 1
            i += 1
            continue
        if not stripped:
            flush_para(para); i += 1; continue
        para.append(line)
        i += 1
    flush_para(para)
    return "\n".join(out)


def render_list(items, inline):
    out, stack = [], []
    for indent, marker, text in items:
        env = "enumerate" if marker[0].isdigit() else "itemize"
        level = 0 if indent < 2 else 1
        while len(stack) > level + 1:
            out.append(rf"\end{{{stack.pop()}}}")
        if len(stack) < level + 1:
            stack.append(env); out.append(rf"\begin{{{env}}}")
        elif stack[-1] != env:
            out.append(rf"\end{{{stack.pop()}}}"); stack.append(env); out.append(rf"\begin{{{env}}}")
        out.append(r"\item " + inline(text))
    while stack:
        out.append(rf"\end{{{stack.pop()}}}")
    return "\n".join(out)
