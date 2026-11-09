"""Migra os resumos para o padrao visual travado (tokens --mat por materia).

Onda 1/2 trocam a folha de estilo da pagina (primeiro <style> sem atributos) pelo
CSS canonico de templates/template-sumario.html; onda 3 remove os justify restantes
e completa os tokens do dark mode. Blocos de add-on (com id) nunca sao tocados.

Uso:
  python apply-visual-migration.py --dry-run
  python apply-visual-migration.py --wave 1
  python apply-visual-migration.py --wave 2
  python apply-visual-migration.py --wave 3
"""

import argparse
import glob
import hashlib
import os
import re

ROOT = "Resumo_estudos"
TEMPLATE = os.path.join(ROOT, "templates", "template-sumario.html")

LEGACY_WAVE1 = {"2e834799", "2cedef2a"}
LEGACY_WAVE2 = {"3006b0f2", "01f847a2"}

# (mat, strong, soft, line)
TOKENS = {
    "AFO": (("#16a34a", "#15803d", "#e8f6ec", "#bbf7d0"), ("#4ade80", "#86efac", "#14532d", "#166534")),
    "Administração Pública e Geral": (("#0d9488", "#0b7a70", "#e6f4f2", "#b8e3de"), ("#2dd4bf", "#7de0d6", "#0f3330", "#14584f")),
    "Arquivologia": (("#92400e", "#7c2d12", "#f4e9df", "#e5cfc0"), ("#dfa787", "#f0c9b0", "#2b2018", "#5b4230")),
    "Contabilidade Pública": (("#db2777", "#be185d", "#fce7f3", "#fbcfe8"), ("#f472b6", "#f9a8d4", "#500724", "#831843")),
    "Direito Administrativo": (("#2563eb", "#1d4ed8", "#e8effd", "#c3d5fa"), ("#8ab0fe", "#a9c3ef", "#1d2739", "#33507e")),
    "Direito Constitucional": (("#7c3aed", "#6d28d9", "#ede9fe", "#ddd6fe"), ("#a78bfa", "#c4b5fd", "#241b38", "#4c3a75")),
    "Direito Processual do Trabalho": (("#0891b2", "#0e7490", "#e3f4f8", "#aedbe4"), ("#7dd3e8", "#a5e3f0", "#14313a", "#1f5566")),
    "Direito do Trabalho": (("#d97706", "#b45309", "#fdf0dc", "#f2d9ad"), ("#f0a92e", "#e6c36d", "#33290f", "#6e5a1e")),
    "Informática": (("#3b82f6", "#2563eb", "#dbeafe", "#bfdbfe"), ("#8ab0fe", "#a9c3ef", "#1d2739", "#33507e")),
    "Legislação institucional - TCE": (("#475569", "#334155", "#f1f5f9", "#cbd5e1"), ("#94a3b8", "#cbd5e1", "#1e293b", "#334155")),
    "Português": (("#0891b2", "#0e7490", "#e0f2f8", "#a5e3f1"), ("#22d3ee", "#67e8f9", "#0c323a", "#155e6b")),
    "RML": (("#65a30d", "#4d7c0f", "#ecf7df", "#cde9a8"), ("#a3e635", "#bef264", "#1a2e05", "#3f6212")),
}

STYLE_RE = re.compile(r"<style([^>]*)>(.*?)</style>", re.S)
JUSTIFY_RE = re.compile(r"text-align:\s*justify")
NAMES = ("--mat", "--mat-strong", "--mat-soft", "--mat-line")
DARK_SECNUM_RE = re.compile(r'(html\[data-theme="dark"\]\s*\.aula\s+\.sec-num\s*\{\s*color:\s*)(#[0-9a-fA-F]{3,8})')
FILLED_SECNUM_RE = re.compile(r"(\.aula \.sec-num\s*\{\s*)background:\s*#[0-9a-fA-F]{3,8};\s*color:\s*#fff;")
CARD_ALT = (
    '<style id="rh-extra">'
    ".card-alt{background:#f2f5fa}"
    'html[data-theme="dark"] .card-alt{background:#242b36}'
    "</style>"
)


def page_css(html):
    m = STYLE_RE.search(html)
    return m.group(2) if m else ""


def css_hash(css):
    return hashlib.md5(css.encode("utf-8")).hexdigest()[:8]


def root_tokens(css):
    m = re.search(r":root\s*\{(.*?)\}", css, re.S)
    if not m:
        return None
    out = []
    for name in NAMES:
        v = re.search(re.escape(name) + r":\s*(#[0-9a-fA-F]{3,8})", m.group(1))
        if not v:
            return None
        out.append(v.group(1))
    return tuple(out)


def has_dark_tokens(html):
    for css in STYLE_RE.findall(html):
        for block in re.findall(r'html\[data-theme="dark"\]\s*\{(.*?)\}', css[1], re.S):
            if "--mat:" in block:
                return True
    return False


def mat_block(subject, light=None):
    light = light or TOKENS[subject][0]
    dark = TOKENS[subject][1]
    fmt = lambda vals: ";".join(f"{n}:{v}" for n, v in zip(NAMES, vals))
    return (
        '<style id="rh-mat">'
        f":root{{{fmt(light)}}}"
        f'html[data-theme="dark"]{{{fmt(dark)}}}'
        "code{overflow-wrap:anywhere}"
        ".aula .sec-title{min-width:0;overflow-wrap:anywhere}"
        "</style>"
    )


def canonical_css():
    return page_css(open(TEMPLATE, encoding="utf-8").read())


def ensure_font(html):
    legacy = "family=Space+Grotesk:wght@500;600;700&family=IBM+Plex+Mono"
    if "JetBrains+Mono" in html or legacy not in html:
        return html
    return html.replace(legacy, "family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@500;600&family=IBM+Plex+Mono")


def ensure_tokens(html, subject):
    existing = re.search(r'<style id="rh-mat">(.*?)</style>', html, re.S)
    if existing and "overflow-wrap:anywhere" in existing.group(1) and ".sec-title" in existing.group(1):
        return html
    light = root_tokens(existing.group(1)) if existing else None
    if light is None:
        m = re.search(r"(<style[^>]*>.*?</style>)", html, re.S)
        light = root_tokens(m.group(1)) if m else None
    block = mat_block(subject, light)
    if existing:
        return html[: existing.start()] + block + html[existing.end():]
    if "</head>" not in html:
        return html
    return html.replace("</head>", block + "\n</head>", 1)


def replace_page_css(html, css):
    m = re.search(r"<style>[^<]*</style>", html, re.S)
    if not m:
        return html
    return html[: m.start()] + "<style>" + css + "</style>" + html[m.end():]


COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)


def _norm(text):
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s*([,:>+~;(){}])\s*", r"\1", text)
    return text.lower()


def parse_rules(css, media=""):
    """Divide o CSS em (media, seletor, corpo) sem depender de parser externo."""
    css = COMMENT_RE.sub("", css)
    out, i, n, start = [], 0, len(css), None
    while i < n:
        ch = css[i]
        if ch == "{":
            selector = css[start:i].strip() if start is not None else ""
            depth, j = 1, i + 1
            while j < n and depth:
                if css[j] == "{":
                    depth += 1
                elif css[j] == "}":
                    depth -= 1
                j += 1
            inner = css[i + 1 : j - 1]
            if selector.startswith("@"):
                atomic = selector.split()[0] in ("@font-face", "@page", "@charset") or "keyframes" in selector
                if atomic:
                    out.append((media, selector, inner))
                else:
                    out.extend(parse_rules(inner, (media + " " + selector).strip()))
            elif selector:
                out.append((media, selector, inner))
            start, i = None, j
        elif ch == "}":
            start, i = None, i + 1
        else:
            if start is None and not ch.isspace():
                start = i
            i += 1
    return out


def split_selectors(selector):
    parts, depth, buf = [], 0, []
    for ch in selector:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf))
    return [p.strip() for p in parts if p.strip()]


VAR_RE = re.compile(r"var\(\s*(--[\w-]+)")

# regras legadas que nao devem ser preservadas: .dot nao e usado por nenhuma
# pagina e .aula .sidebar{display:none} no mobile quebra a gaveta do menu.
DEAD_EXTRAS = {_norm(s) for s in (".dot", ".dot.a", ".dot.b", ".dot.c", ".dot.g", ".dot.p", ".dot.r", ".aula .sidebar")}

# utilitario de conteudo usado pela AP Aula 08 (realce de subtitulo)
DESTAQUE_SEL = ".sec-subtitle.destaque"
DESTAQUE_BODY = (
    "color:var(--mat-strong);font-weight:700;font-size:1.05rem;"
    "border-left:5px solid var(--mat);padding-left:.8rem;margin-top:1.8rem;margin-bottom:1.2rem"
)


def page_extras(legacy_css, canon_css):
    """Regras do CSS legado que o canonico nao possui (preservadas na troca)."""
    canon = set()
    for media, selector, _body in parse_rules(canon_css):
        for sel in split_selectors(selector):
            canon.add((_norm(media), _norm(sel)))
    extras, conflicts = [], 0
    for media, selector, body in parse_rules(legacy_css):
        kept = []
        for sel in split_selectors(selector):
            key = _norm(sel)
            if key in DEAD_EXTRAS:
                continue
            if (_norm(media), key) in canon:
                conflicts += 1
            else:
                kept.append(sel)
        if not kept:
            continue
        if selector.startswith("@") and selector.split()[0] in ("@font-face", "@page", "@charset") or "keyframes" in selector:
            extras.append((media, selector, body))
        else:
            extras.append((media, ", ".join(kept), body))
    return extras, conflicts


def render_extras(extras, legacy_css, canon_css):
    if not extras:
        return ""
    defined = set(re.findall(r"(--[\w-]+)\s*:", legacy_css))
    needed = {v for _m, _s, b in extras for v in VAR_RE.findall(b)}
    missing = sorted(needed & defined - set(re.findall(r"(--[\w-]+)\s*:", canon_css)))
    blocks, by_media = {}, []
    for media, selector, body in extras:
        if media not in blocks:
            blocks[media] = []
            by_media.append(media)
        blocks[media].append(f"{selector}{{{' '.join(body.split())}}}")
    parts = []
    if missing:
        decls = []
        for name in missing:
            m = re.search(re.escape(name) + r"\s*:\s*([^;]+);", legacy_css)
            if m:
                decls.append(f"{name}:{m.group(1).strip()}")
        if decls:
            parts.append(":root{" + ";".join(decls) + "}")
    for media in by_media:
        inner = "\n".join(blocks[media])
        parts.append(f"{media}{{{inner}}}" if media else inner)
    return '<style id="rh-page-extra">\n' + "\n".join(parts) + "\n</style>"


def swap_page_css(html):
    """Troca o CSS da pagina pelo canonico preservando regras proprias."""
    legacy = page_css(html)
    canon = canonical_css()
    extras, conflicts = page_extras(legacy, canon)
    if re.search(r'class="[^"]*\bdestaque\b', html) and not any(_norm(s) == _norm(DESTAQUE_SEL) for _m, s, _b in extras):
        extras.append(("", DESTAQUE_SEL, DESTAQUE_BODY))
    extra_block = render_extras(extras, legacy, canon)
    html = replace_page_css(html, canon)
    old = re.search(r'<style id="rh-page-extra">.*?</style>\n?', html, re.S)
    if old:
        html = html[: old.start()] + html[old.end():]
    if extra_block and "</head>" in html:
        html = html.replace("</head>", extra_block + "\n</head>", 1)
    return html, len(extras), conflicts


def fix_dark_secnum(html):
    def repl(m):
        if m.group(2).lower() in ("#fff", "#ffffff"):
            return m.group(0)
        return m.group(1) + "var(--mat)"
    return DARK_SECNUM_RE.sub(repl, html)


def apply_file(path, mode):
    html = open(path, encoding="utf-8").read()
    subject = os.path.relpath(path, ROOT).split(os.sep)[0]
    original = html
    result = {"extras": 0, "conflicts": 0}

    if mode in ("1", "2", "swap-a", "swap-b", "extras"):
        if mode in ("swap-a", "swap-b", "extras"):
            html, result["extras"], result["conflicts"] = swap_page_css(html)
        else:
            html = replace_page_css(html, canonical_css())
    if 'id="rh-extra"' not in html and re.search(r'class="[^"]*\bcard-alt\b', html) and mode in ("1", "2", "swap-a", "swap-b"):
        html = html.replace("</head>", CARD_ALT + "\n</head>", 1)

    html = ensure_font(html)
    html = ensure_tokens(html, subject)
    html = fix_dark_secnum(html)
    html = FILLED_SECNUM_RE.sub(r"\1background: transparent; color: var(--mat);", html)

    m = re.search(r"(<style[^>]*>)(.*?)(</style>)", html, re.S)
    if m:
        fixed = JUSTIFY_RE.sub("text-align: left", m.group(2))
        html = html[: m.start(2)] + fixed + html[m.end(2):]

    if html == original:
        return False, result
    open(path, "w", encoding="utf-8", newline="").write(html)
    return True, result


def legacy_files(only=None):
    out = []
    canon = canonical_css()
    for path in sorted(glob.glob(os.path.join(ROOT, "*", "*", "resumo-aula-*.html"))):
        if only and only.replace("/", os.sep) not in path:
            continue
        html = open(path, encoding="utf-8").read()
        if page_css(html) != canon:
            out.append(path)
    return out


def select(mode, only=None, force=False):
    if mode in ("swap-a", "swap-b"):
        groups = {}
        for path in legacy_files(only):
            h = css_hash(page_css(open(path, encoding="utf-8").read()))
            groups.setdefault(h, []).append(path)
        out = []
        for items in groups.values():
            big = len(items) >= 3
            if (mode == "swap-a") == big:
                out.extend(items)
        return sorted(out)
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, "*", "*", "resumo-aula-*.html"))):
        if only and only.replace("/", os.sep) not in path:
            continue
        html = open(path, encoding="utf-8").read()
        if mode == "extras":
            if 'id="rh-page-extra"' in html or re.search(r'class="[^"]*\bdestaque\b', html):
                out.append(path)
            continue
        if mode == "tokens":
            m = re.search(r'<style id="rh-mat">(.*?)</style>', html, re.S)
            if not m or "overflow-wrap:anywhere" not in m.group(1) or ".sec-title" not in m.group(1):
                out.append(path)
            continue
        if mode == "dark":
            if any(c.lower() not in ("#fff", "#ffffff") for _, c in DARK_SECNUM_RE.findall(html)):
                out.append(path)
            continue
        if 'id="rh-mat"' in html and not force:
            continue
        css = page_css(html)
        legacy = root_tokens(css) is None
        h = css_hash(css)
        if mode == "1" and legacy and (h in LEGACY_WAVE1 or force):
            out.append(path)
        elif mode == "2" and legacy and (h in LEGACY_WAVE2 or force):
            out.append(path)
        elif mode == "3" and not legacy and (JUSTIFY_RE.search(css) or not has_dark_tokens(html)):
            out.append(path)
    return out


def dry_run_swap(files):
    canon = canonical_css()
    for path in files:
        html = open(path, encoding="utf-8").read()
        extras, conflicts = page_extras(page_css(html), canon)
        print(f"  {os.path.relpath(path, ROOT)}")
        print(f"    regras proprias preservadas: {len(extras)} | sobrepostas pelo canonico: {conflicts}")
        for media, selector, _body in extras:
            print(f"      {selector[:110]}{'  [' + media + ']' if media else ''}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wave", choices=["1", "2", "3", "swap-a", "swap-b", "extras", "dark", "tokens", "all"], default="all")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", help="aplica apenas em caminhos que contenham este trecho")
    ap.add_argument("--force", action="store_true", help="refaz arquivos ja migrados")
    args = ap.parse_args()

    modes = ["1", "2", "3", "dark", "tokens"] if args.wave == "all" else [args.wave]
    total = changed = 0
    for mode in modes:
        files = select(mode, args.only, args.force)
        print(f"onda {mode}: {len(files)} arquivo(s)")
        if args.dry_run and mode in ("swap-a", "swap-b"):
            dry_run_swap(files)
            total += len(files)
            continue
        for path in files:
            total += 1
            if args.dry_run:
                print(f"  [dry] {os.path.relpath(path, ROOT)}")
                continue
            ok, info = apply_file(path, mode)
            changed += ok
            detail = ""
            if mode.startswith("swap"):
                detail = f" (extras: {info['extras']}, sobrepostas: {info['conflicts']})"
            print(f"  {'[ok]  ' if ok else '[skip]'} {os.path.relpath(path, ROOT)}{detail}")
    if args.dry_run:
        print(f"total que seria tocado: {total}")
    else:
        print(f"migrados: {changed} | sem alteracao: {total - changed}")


if __name__ == "__main__":
    main()
