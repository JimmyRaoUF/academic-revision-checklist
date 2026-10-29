#!/usr/bin/env python3
"""flag_candidates.py: list the places worth reading against the mechanical rules of this checklist.

Usage:
    python3 flag_candidates.py FILE [FILE ...] [--max-para 180] [--summary] [--md OUT.md]

FILE can be .tex, .md or .txt. LaTeX tables, figures, equations and comments are skipped; Markdown code blocks,
tables and headings are skipped. Sentence splitting and word counts are approximate.

A flag is a place to READ, not a verdict. Many flags will be fine on reading (a negation that carries content,
a colon that introduces a list, a parallel series that is meant to be parallel). Decide each one in context.

Checks (codes match references/patterns.md):
  P59  em dashes                                      P57  colons (read each: list, quotation, question, definition?)
  P58  contrast set-ups ("not A but B", "rather than")  P60a five sentences in a row of nearly the same length
  P60b three sentences in a row opening the same way   P61a hollow transitions and generated-sounding words
  P61b paragraph endings that may only summarize       P34  paragraphs over --max-para words
  P8   comparatives that may lack their second side    P9   "significant" near a share, percentage or mean
  P42  words that tell how the text was revised (now, originally, previously, revised, turned out)
"""
import argparse, re, sys
from pathlib import Path

# ---------- text extraction ----------

ABBREV = {"e.g", "i.e", "al", "dr", "vs", "cf", "p", "pp", "fig", "figs", "no", "approx", "st", "ph.d", "u.s",
          "a.m", "p.m", "ch", "sec", "eq", "vol", "ed", "eds", "mr", "ms", "mrs", "jr", "inc", "ltd", "resp", "ca"}
TEX_SKIP = ("table", "table*", "figure", "figure*", "tabular", "tabular*", "longtable", "verbatim", "equation",
            "equation*", "align", "align*", "minipage", "lstlisting", "tikzpicture", "quote", "quotation")
TEX_LIST = ("itemize", "enumerate", "description")
TEX_HEADING = re.compile(r"^\s*\\(part|chapter|section|subsection|subsubsection|paragraph)\*?[\[{]")


def _strip_tex_comment(line):
    out, i = [], 0
    while i < len(line):
        if line[i] == "\\" and i + 1 < len(line):
            out.append(line[i:i + 2]); i += 2; continue
        if line[i] == "%":
            break
        out.append(line[i]); i += 1
    return "".join(out)


def _unwrap(text, names, keep):
    pat = re.compile(r"\\(" + "|".join(names) + r")\*?(\[[^\]]*\])*\{")
    while True:
        m = pat.search(text)
        if not m:
            return text
        depth, j = 1, m.end()
        while j < len(text) and depth:
            if text[j] == "\\":
                j += 2; continue
            depth += {"{": 1, "}": -1}.get(text[j], 0)
            j += 1
        text = text[:m.start()] + (text[m.end():j - 1] if keep else "") + text[j:]


def tex_to_prose(t):
    t = re.sub(r"~?\\(cite[a-z]*)\*?(\[[^\]]*\])*\{[^}]*\}", "", t)
    t = re.sub(r"\\(ref|cref|Cref|autoref|eqref|pageref)\{[^}]*\}", "1", t)
    t = re.sub(r"\\label\{[^}]*\}", "", t)
    t = _unwrap(t, ["footnote"], keep=False)
    t = _unwrap(t, ["textbf", "textit", "emph", "texttt", "underline", "mbox", "textsc", "text", "textrm",
                    "textsf", "href", "url", "enquote", "small", "footnotesize"], keep=True)
    t = re.sub(r"\$([^$]*)\$", lambda m: re.sub(r"[\\{}^_]", " ", m.group(1)), t)
    t = t.replace("---", "\u2014").replace("--", "\u2013").replace("``", "\u201c").replace("''", "\u201d")
    for a, b in (("\\%", "%"), ("\\&", "&"), ("\\S", "\u00a7"), ("\\$", "$"), ("\\_", "_"), ("\\,", " "),
                 ("\\ ", " "), ("\\@", ""), ("\\/", ""), ("~", " ")):
        t = t.replace(a, b)
    t = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", "", t)
    return re.sub(r"\s+", " ", t.replace("{", "").replace("}", "")).strip()


def md_to_prose(t):
    t = re.sub(r"`[^`]*`", "", t)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()


def units(path):
    """Return paragraphs as dicts: line, prose, kind ('para' or 'heading')."""
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    is_tex = path.suffix.lower() == ".tex"
    if not is_tex:
        # YAML front matter (Pandoc, Quarto, SKILL.md) is metadata, not prose: blank it, keeping line numbers.
        m = re.match(r"---[ \t]*\n.*?\n(---|\.\.\.)[ \t]*(\n|$)", text, re.S)
        if m:
            text = "\n" * m.group(0).count("\n") + text[m.end():]
    out, cur, start, skip = [], [], None, 0
    in_code = False

    def flush():
        nonlocal cur, start
        if cur:
            raw = "\n".join(cur)
            prose = tex_to_prose(raw) if is_tex else md_to_prose(raw)
            if prose:
                out.append({"line": start, "prose": prose, "kind": "para"})
        cur, start = [], None

    for n, line in enumerate(text.split("\n"), 1):
        if is_tex:
            if line.lstrip().startswith("%"):
                continue
            s = _strip_tex_comment(line)
            begins = re.findall(r"\\begin\{([^}]*)\}", s)
            ends = re.findall(r"\\end\{([^}]*)\}", s)
            if skip:
                skip += sum(b in TEX_SKIP for b in begins) - sum(e in TEX_SKIP for e in ends)
                continue
            if any(b in TEX_SKIP for b in begins):
                flush()
                skip = sum(b in TEX_SKIP for b in begins) - sum(e in TEX_SKIP for e in ends)
                continue
            if TEX_HEADING.match(s):
                flush(); out.append({"line": n, "prose": tex_to_prose(s), "kind": "heading"}); continue
            if any(b in TEX_LIST for b in begins) or any(e in TEX_LIST for e in ends) or s.strip().startswith("\\item"):
                flush()
                s = re.sub(r"\\(begin|end)\{[^}]*\}(\[[^\]]*\])?|\\item(\[[^\]]*\])?", "", s)
            if not s.strip():
                flush(); continue
        else:
            s = line
            if s.strip().startswith("```"):
                in_code = not in_code; flush(); continue
            if in_code or s.strip().startswith("|"):
                flush(); continue
            if re.match(r"^\s*#{1,6}\s", s):
                flush(); out.append({"line": n, "prose": md_to_prose(s.lstrip("# ")), "kind": "heading"}); continue
            if re.match(r"^\s*([-*+]|\d+\.)\s", s):
                flush(); s = re.sub(r"^\s*([-*+]|\d+\.)\s", "", s)
            if not s.strip():
                flush(); continue
        if start is None:
            start = n
        cur.append(s)
    flush()
    return out


def sentences(prose):
    parts = re.split(r"(?<=[.!?])([\u201d\u2019\")\]]*)\s+(?=[\u201c\"(\[]?[A-Z0-9\u00a7])", prose)
    out, buf = [], ""
    for i in range(0, len(parts), 2):
        piece = parts[i] + (parts[i + 1] if i + 1 < len(parts) else "")
        buf = (buf + " " + piece).strip() if buf else piece
        m = re.search(r"([A-Za-z][A-Za-z.]*)\.[\u201d\u2019\")\]]*$", buf)
        if m and i + 2 < len(parts):
            tok = m.group(1).lower()
            if tok in ABBREV or tok.rstrip(".") in ABBREV or re.fullmatch(r"[a-z]", tok) or re.fullmatch(r"([a-z]\.)+[a-z]", tok):
                continue
        out.append(buf); buf = ""
    if buf:
        out.append(buf)
    return [s for s in out if s.strip()]

# ---------- rules ----------

HOLLOW = [r"\bOverall\b", r"\bIn summary\b", r"\bworth noting\b", r"\bCrucially\b", r"\bImportantly\b",
          r"\bUltimately\b", r"\bIn conclusion\b", r"\bNotably\b", r"\bInterestingly\b", r"\bIn short\b",
          r"\bIn sum\b", r"\bTo summarize\b", r"\bIn essence\b", r"\bAt its core\b", r"\bIt is important to note\b",
          r"\bIt should be noted\b", r"\bNeedless to say\b", r"\b[Dd]elve", r"\b[Uu]nderscor", r"\b[Pp]ivotal\b",
          r"\b[Tt]apestry\b", r"\b[Rr]ealm\b", r"\b[Ll]andscape\b", r"\bshed(s)? light\b", r"\bpave(s|d)? the way\b",
          r"\ba testament\b", r"\bgame[- ]changer\b", r"\bcutting[- ]edge\b", r"\bever[- ]evolving\b",
          r"\b[Ss]eamless", r"\b[Hh]olistic", r"\b[Mm]ultifaceted\b", r"\b[Ii]ntricate",
          r"\bplays? an? (key|crucial|vital|central|pivotal|important|critical) role\b", r"\b[Gg]enuinely\b",
          r"\b[Ff]undamentally\b", r"^Taken together\b", r"^Together,", r"^Furthermore\b", r"^Moreover\b",
          r"^Additionally\b", r"^Indeed\b", r"^Clearly\b", r"\b[Ll]everag", r"\b[Rr]obust", r"\b[Nn]uanced\b",
          r"\bserves? as\b", r"\b[Ff]oster", r"\b[Hh]arness", r"\b[Uu]nlock", r"\bbridg(e|es|ing) the gap\b",
          r"\b[Kk]ey insight\b", r"\bSo the question becomes\b", r"\bThe question is not\b"]
CONTRAST = [r"\b(is|are|was|were|be|been|does|do|did)\s+not\b[^.;:]{0,90}\bbut\b", r"\bnot\s+(only|just|merely|simply)\b",
            r"\bnot\b[^.;:]{1,70},\s*but\b", r"\brather than\b", r"\binstead of\b", r"^(It|This|That|These|They) (is|are|was|were) not\b",
            r"^Not\b", r"\bless about\b"]
END_OPENERS = re.compile(r"^(This|These|Such|Together|Taken together|Thus|Hence|Therefore|In this way|In short|Overall|In sum|Ultimately)\b")
END_WORDS = re.compile(r"\b(important|importance|highlight|underscor|valuable|insight|crucial|essential|broader|significance|meaningful|promise|potential)\b", re.I)
COMPARATIVE = re.compile(r"\b(more|less|fewer|higher|lower|greater|larger|smaller|better|worse|stronger|weaker)\b(?![^.]*\bthan\b)", re.I)
SIG_SHARE = re.compile(r"\b(share|proportion|percentage|percent|mean|average|rate)\b[^.]{0,60}\b(not )?significant"
                       r"|\bsignificant(ly)?\b[^.]{0,30}\b(share|proportion|percentage|mean)\b"
                       r"|\bsignificant(ly)?\b[^.]{0,40}\d+(\.\d+)?\s?%(?!\s?(CI|confidence))"
                       r"|\d+(\.\d+)?\s?%(?!\s?(CI|confidence))[^.]{0,60}\bsignificant", re.I)
HISTORY = re.compile(r"\b(now|previously|originally|formerly|no longer|was revised|were revised|turned out|was added|were added)\b", re.I)


def first_word(s):
    m = re.findall(r"[A-Za-z0-9']+", s)
    return m[0].lower() if m else ""


def check(path, max_para):
    hits = []
    us = units(path)
    for u in us:
        if u["kind"] == "heading":
            continue
        loc = f"{path.name}:{u['line']}"
        ss = sentences(u["prose"])
        wc = [len(s.split()) for s in ss]
        if "\u2014" in u["prose"]:
            hits.append(("P59", loc, "em dash: " + u["prose"][:100]))
        for s in ss:
            if ":" in re.sub(r"\d:\d|https?:", "", s):
                hits.append(("P57", loc, "colon: " + s[:140]))
            for p in CONTRAST:
                if re.search(p, s):
                    hits.append(("P58", loc, s[:140])); break
            for p in HOLLOW:
                if re.search(p, s):
                    hits.append(("P61a", loc, f"[{p.strip('^').replace(chr(92) + 'b', '')}] " + s[:120])); break
            if COMPARATIVE.search(s):
                hits.append(("P8", loc, "comparative without 'than'? " + s[:120]))
            if SIG_SHARE.search(s):
                hits.append(("P9", loc, "'significant' near a share, percentage or mean: " + s[:120]))
            if HISTORY.search(s):
                hits.append(("P42", loc, "revision-history word? " + s[:120]))
        for i in range(len(ss) - 4):
            if max(wc[i:i + 5]) - min(wc[i:i + 5]) < 5:
                hits.append(("P60a", loc, f"sentences {i + 1}-{i + 5}, words {wc[i:i + 5]}: " + ss[i][:80]))
        run = 1
        for k in range(1, len(ss)):
            run = run + 1 if first_word(ss[k]) and first_word(ss[k]) == first_word(ss[k - 1]) else 1
            if run == 3:
                hits.append(("P60b", loc, f"3 sentences open with '{first_word(ss[k])}': " + ss[k][:80]))
        if len(ss) > 1 and (END_OPENERS.match(ss[-1]) or END_WORDS.search(ss[-1])):
            hits.append(("P61b", loc, "last sentence: " + ss[-1][:140]))
        if sum(wc) > max_para:
            hits.append(("P34", loc, f"{sum(wc)} words"))
    return hits


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+")
    ap.add_argument("--max-para", type=int, default=180)
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--md", help="write the flags to a Markdown file")
    a = ap.parse_args()
    lines = []
    for f in a.files:
        p = Path(f)
        hits = check(p, a.max_para)
        counts = {}
        for h in hits:
            counts[h[0]] = counts.get(h[0], 0) + 1
        head = f"{p.name}: " + (", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "no flags")
        print(head); lines.append(f"## {head}\n")
        if not a.summary:
            for code, loc, txt in hits:
                print(f"  {code:5s} {loc:24s} {txt}")
                lines.append(f"- [ ] **{code}** `{loc}` {txt}")
        lines.append("")
    if a.md:
        Path(a.md).write_text("# Places to read\n\nA flag is a place to read, not a verdict.\n\n" + "\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
