#!/usr/bin/env python3
"""Assemble Book 24 into HTML and EPUB; tables/figures come from sim results."""
import csv, glob, html, os, re, zipfile, uuid
import markdown

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "build", "out")
os.makedirs(OUT, exist_ok=True)
TITLE = "3D NAND Slit Etch"

PARTS = {1: "Part I — Foundations", 5: "Part II — Slit Etch Physics",
         9: "Part III — Process Integration",
         13: "Part IV — Measurement, Control and Outlook"}

rows = list(csv.DictReader(open(os.path.join(ROOT, "sim", "transport_results.csv"))))
for r in rows:
    r["AR"] = int(r["AR"]); r["s"] = float(r["s"])
    for k in ("slot", "hole", "se_slot", "se_hole"):
        r[k] = float(r[k])
ARS = sorted({r["AR"] for r in rows}); SS = sorted({r["s"] for r in rows})
get = lambda ar, s: next(r for r in rows if r["AR"] == ar and r["s"] == s)


def fmt(x):
    return f"{x:.4f}" if x >= 1e-3 else f"{x:.1e}"


def table(head, body):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in body)
    return f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>"


def t_s0():
    return table(["AR", "W slot", "W hole", "slot/hole", "W·AR slot", "W·AR hole"],
                 [[a, fmt(get(a, 0)["slot"]), fmt(get(a, 0)["hole"]),
                   f"{get(a,0)['slot']/get(a,0)['hole']:.2f}",
                   f"{get(a,0)['slot']*a:.2f}", f"{get(a,0)['hole']*a:.2f}"] for a in ARS])


def t_sweep():
    sel = [0.01, 0.1]
    return table(["AR"] + [f"{k} s={s}" for s in sel for k in ("slot", "hole")],
                 [[a] + [fmt(get(a, s)[k]) for s in sel for k in ("slot", "hole")] for a in ARS])


def t_full(key):
    return table(["AR"] + [f"s={s}" for s in SS],
                 [[a] + [fmt(get(a, s)[key]) for s in SS] for a in ARS])


def t_ratio():
    return table(["AR"] + [f"s={s}" for s in SS],
                 [[a] + [f"{get(a,s)['slot']/max(get(a,s)['hole'],1e-12):.1f}" for s in SS]
                  for a in ARS])


def svg_plot(series, title, xlabel, ylabel):
    import math
    W, H, L, R, T, B = 620, 380, 70, 20, 30, 55
    xs = [p[0] for _, pts in series for p in pts]
    ys = [p[1] for _, pts in series for p in pts if p[1] > 0]
    x0, x1 = math.log10(min(xs)), math.log10(max(xs))
    y0, y1 = math.floor(math.log10(min(ys))), math.ceil(math.log10(max(ys)))
    px = lambda x: L + (math.log10(x) - x0) / (x1 - x0) * (W - L - R)
    py = lambda y: T + (y1 - math.log10(max(y, 10**y0))) / (y1 - y0) * (H - T - B)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif" font-size="12">',
         f'<rect width="{W}" height="{H}" fill="white"/>',
         f'<text x="{W/2}" y="18" text-anchor="middle" font-weight="bold">{title}</text>']
    for e in range(y0, y1 + 1):
        y = py(10**e)
        o.append(f'<line x1="{L}" x2="{W-R}" y1="{y}" y2="{y}" stroke="#ddd"/>'
                 f'<text x="{L-6}" y="{y+4}" text-anchor="end">1e{e}</text>')
    for x in sorted(set(xs)):
        if x in (1, 2, 5, 10, 20, 40, 100, 150):
            o.append(f'<line x1="{px(x)}" x2="{px(x)}" y1="{T}" y2="{H-B}" stroke="#eee"/>'
                     f'<text x="{px(x)}" y="{H-B+16}" text-anchor="middle">{x}</text>')
    o.append(f'<rect x="{L}" y="{T}" width="{W-L-R}" height="{H-T-B}" fill="none" stroke="#444"/>')
    o.append(f'<text x="{(L+W-R)/2}" y="{H-12}" text-anchor="middle">{xlabel}</text>')
    o.append(f'<text transform="translate(16 {(T+H-B)/2}) rotate(-90)" text-anchor="middle">{ylabel}</text>')
    cols = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e", "#555"]
    for i, (name, pts) in enumerate(series):
        c = cols[i % len(cols)]
        d = " ".join(f"{px(x):.1f},{py(y):.1f}" for x, y in pts)
        dash = ' stroke-dasharray="6 3"' if "hole" in name else ""
        o.append(f'<polyline points="{d}" fill="none" stroke="{c}" stroke-width="2"{dash}/>')
        o.append(f'<rect x="{L+10}" y="{H-B-12-(len(series)-i)*16}" width="12" height="3" fill="{c}"/>'
                 f'<text x="{L+28}" y="{H-B-6-(len(series)-i)*16}">{name}</text>')
    o.append("</svg>")
    return "\n".join(o)


def fig_t_vs_ar():
    s = [("slot s=0", [(a, get(a, 0)["slot"]) for a in ARS]),
         ("hole s=0", [(a, get(a, 0)["hole"]) for a in ARS])]
    return ("Figure 4.1", "Transmission probability versus aspect ratio, non-reactive species (s = 0).",
            svg_plot(s, "Transmission vs aspect ratio", "aspect ratio", "transmission W"))


def fig_t_vs_s():
    s = []
    for sv in (0.01, 0.1):
        s.append((f"slot s={sv}", [(a, get(a, sv)["slot"]) for a in ARS]))
        s.append((f"hole s={sv}", [(a, get(a, sv)["hole"]) for a in ARS]))
    return ("Figure 4.2", "Transmission with wall loss. The slot floors at direct line of sight; the hole decays much faster. Hole values below about 1e-4 rest on only a handful of counted molecules and are noisy.",
            svg_plot(s, "Transmission with wall loss", "aspect ratio", "transmission W"))


def figure_html(f, name):
    label, cap, svg = f()
    open(os.path.join(ROOT, "figures", name + ".svg"), "w").write(svg)
    return f'<figure>{svg}<figcaption><b>{label}.</b> {cap}</figcaption></figure>'


def subst(md):
    rep = {"{{TABLE:s0}}": t_s0(), "{{TABLE:s_sweep}}": t_sweep(),
           "{{TABLE:full_slot}}": t_full("slot"), "{{TABLE:full_hole}}": t_full("hole"),
           "{{TABLE:ratio}}": t_ratio(),
           "{{FIG:t_vs_ar}}": figure_html(fig_t_vs_ar, "t_vs_ar"),
           "{{FIG:t_vs_s}}": figure_html(fig_t_vs_s, "t_vs_s")}
    for k, v in rep.items():
        md = md.replace(k, "\n\n" + v + "\n\n")
    return md


def read(p):
    return open(p, encoding="utf-8").read()


# ---- collect sections: (id, label, title, markdown)
secs = [("front", "", "Preface", read(os.path.join(ROOT, "frontmatter.md")))]
for p in sorted(glob.glob(os.path.join(ROOT, "chapters", "*.md"))):
    n = int(os.path.basename(p).split("-")[0])
    md = read(p)
    secs.append((f"ch{n:02d}", str(n), md.splitlines()[0].lstrip("# ").strip(), md))
for p in sorted(glob.glob(os.path.join(ROOT, "appendices", "*.md"))):
    L = os.path.basename(p)[0]
    md = read(p)
    secs.append((f"app{L}", L, md.splitlines()[0].lstrip("# ").strip(), md))
secs.append(("glossary", "", "Glossary", read(os.path.join(ROOT, "backmatter", "glossary.md"))))

# ---- index
plain = {s[0]: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s[3])) for s in secs}
def ref(sid):
    return sid[2:].lstrip("0") if sid.startswith("ch") else ("App. " + sid[3:] if sid.startswith("app") else None)
idx = {}
for line in read(os.path.join(ROOT, "backmatter", "index_terms.txt")).splitlines():
    if not line.strip():
        continue
    term, *pats = line.split("|")
    hits = []
    for sid, text in plain.items():
        r = ref(sid)
        if r and any(re.search(re.escape(p), text, re.I) for p in pats):
            hits.append((sid, r))
    idx[term] = hits
idx_md = "# Index\n\n" + "\n\n".join(
    f"**{t}** — " + ", ".join(f'<a href="#{sid}">{r}</a>' for sid, r in h)
    for t, h in sorted(idx.items(), key=lambda kv: kv[0].lower()) if h) + "\n"
secs.append(("index", "", "Index", idx_md))

md_ext = ["tables", "fenced_code", "sane_lists"]
bodies = {}
for sid, lab, title, md in secs:
    bodies[sid] = markdown.markdown(subst(md), extensions=md_ext)

CSS = """body{font:17px/1.6 Georgia,serif;max-width:46em;margin:2em auto;padding:0 1em;color:#222}
h1{border-bottom:2px solid #333;padding-bottom:.2em;margin-top:2.5em}h2{margin-top:1.8em}
table{border-collapse:collapse;margin:1em 0;font:14px sans-serif}td,th{border:1px solid #bbb;padding:3px 8px;text-align:right}
th{background:#eee}td:first-child,th:first-child{text-align:left}blockquote{border-left:4px solid #999;margin:1em 0;padding:.2em 1em;color:#444}
code,pre{background:#f3f3f3;font-size:14px}pre{padding:.7em;overflow-x:auto}figure{margin:1.5em 0}figure svg{width:100%;height:auto}
figcaption{font:14px sans-serif;color:#444}.part{font:700 1.1em sans-serif;text-transform:uppercase;letter-spacing:.1em;margin-top:4em;color:#555}"""

# ---- HTML
toc = ["<h1>Contents</h1><ul>"]
for sid, lab, title, _ in secs:
    pre = ""
    if sid.startswith("ch") and int(sid[2:]) in PARTS:
        toc.append(f'<li><b>{PARTS[int(sid[2:])]}</b></li>')
    toc.append(f'<li><a href="#{sid}">{title}</a></li>')
toc.append("</ul>")
parts_html = []
for sid, lab, title, _ in secs:
    pre = ""
    if sid.startswith("ch") and int(sid[2:]) in PARTS:
        pre = f'<div class="part">{PARTS[int(sid[2:])]}</div>'
    parts_html.append(f'{pre}<section id="{sid}">{bodies[sid]}</section>')
doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{TITLE}</title>'
       f'<meta name="viewport" content="width=device-width,initial-scale=1"><style>{CSS}</style></head><body>'
       + parts_html[0] + "".join(toc) + "".join(parts_html[1:]) + "</body></html>")
open(os.path.join(OUT, "book24-3d-nand-slit-etch.html"), "w", encoding="utf-8").write(doc)

# ---- EPUB
def xhtml(title, body):
    body = re.sub(r"<(br|hr|img)([^>]*?)(?<!/)>", r"<\1\2/>", body)
    return ('<?xml version="1.0" encoding="utf-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml">'
            f'<head><meta charset="utf-8"/><title>{html.escape(title)}</title><link rel="stylesheet" href="style.css"/></head>'
            f'<body>{body}</body></html>')

epub = os.path.join(OUT, "book24-3d-nand-slit-etch.epub")
uid = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "recess-etch/book24"))
with zipfile.ZipFile(epub, "w") as z:
    z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip")
    z.writestr("META-INF/container.xml", '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>', zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/style.css", CSS, zipfile.ZIP_DEFLATED)
    items, spine, nav = [], [], []
    for sid, lab, title, _ in secs:
        fn = f"{sid}.xhtml"
        z.writestr("OEBPS/" + fn, xhtml(title, bodies[sid].replace('href="#', f'href="all.xhtml#')) if False else xhtml(title, re.sub(r'href="#(\w+)"', r'href="\1.xhtml"', bodies[sid])), zipfile.ZIP_DEFLATED)
        items.append(f'<item id="{sid}" href="{fn}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="{sid}"/>')
        nav.append(f'<li><a href="{fn}">{html.escape(title)}</a></li>')
    z.writestr("OEBPS/nav.xhtml", '<?xml version="1.0" encoding="utf-8"?><!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"><head><title>Contents</title></head><body><nav epub:type="toc"><h1>Contents</h1><ol>' + "".join(nav) + "</ol></nav></body></html>", zipfile.ZIP_DEFLATED)
    z.writestr("OEBPS/content.opf", f'<?xml version="1.0" encoding="utf-8"?><package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="id"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="id">{uid}</dc:identifier><dc:title>{TITLE}</dc:title><dc:language>en</dc:language><meta property="dcterms:modified">2026-10-04T00:00:00Z</meta></metadata><manifest><item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/><item id="css" href="style.css" media-type="text/css"/>' + "".join(items) + "</manifest><spine>" + "".join(spine) + "</spine></package>", zipfile.ZIP_DEFLATED)
words = sum(len(t.split()) for t in plain.values())
print(f"built {len(secs)} sections, ~{words} words -> {OUT}")
