"""Dry-run da migracao visual dos resumos para o padrao travado (tokens --mat).

Somente leitura: agrupa os resumos por folha de estilo, detecta o que falta em
cada grupo e sugere troca total do CSS ou ajuste cirurgico por regra.

Uso: python audit_visual_migration.py
"""

import glob
import hashlib
import os
import re
from collections import defaultdict

ROOT = os.path.join("Resumo_estudos")
TEMPLATE = os.path.join(ROOT, "templates", "template-sumario.html")

SUBJECT_KEY = {
    "AFO": "afo",
    "Administração Pública e Geral": "ap",
    "Arquivologia": "arc",
    "Contabilidade Pública": "cp",
    "Direito Administrativo": "ad",
    "Direito Constitucional": "dc",
    "Direito Processual do Trabalho": "dpt",
    "Direito do Trabalho": "dt",
    "Informática": "inf",
    "Legislação institucional - TCE": None,
    "Português": "pt",
    "RML": "rml",
}

STYLE_RE = re.compile(r"<style[^>]*>(.*?)</style>", re.S)
JUSTIFY_RE = re.compile(r"text-align:\s*justify")
DARK_RE = re.compile(r'html\[data-theme="dark"\]\s*\{(.*?)\}', re.S)


def page_css(html):
    blocks = STYLE_RE.findall(html)
    return blocks[0] if blocks else ""


def rule(css, selector):
    m = re.search(re.escape(selector) + r"\s*\{([^}]*)\}", css)
    return m.group(1) if m else ""


def body_classes(html):
    body = html.split("</head>", 1)[-1]
    classes = set()
    for chunk in re.findall(r'class="([^"]+)"', body):
        classes.update(chunk.split())
    return classes


def template_classes():
    html = open(TEMPLATE, encoding="utf-8").read()
    css = "".join(STYLE_RE.findall(html))
    return set(re.findall(r"\.([a-zA-Z][\w-]*)", css))


def token_set(css):
    out = {}
    for name in ("--mat", "--mat-strong", "--mat-soft", "--mat-line"):
        m = re.search(re.escape(name) + r":\s*(#[0-9a-fA-F]{3,8})", css)
        if m:
            out[name] = m.group(1)
    return out


def dark_tokens(html):
    for css in STYLE_RE.findall(html):
        for block in DARK_RE.findall(css):
            if "--mat:" in block:
                return token_set(block)
    return {}


def th_font(css):
    for selector, body in re.findall(r"([^{}]*\bth\b[^{}]*)\{([^}]*)\}", css):
        if "font-family" not in body:
            continue
        if "JetBrains Mono" in body:
            return "JetBrains"
        if "IBM Plex Mono" in body:
            return "IBM Plex Mono"
    return "?"


def main():
    known = template_classes()
    files = sorted(glob.glob(os.path.join(ROOT, "*", "*", "resumo-aula-*.html")))
    groups = defaultdict(list)

    for path in files:
        html = open(path, encoding="utf-8").read()
        css = page_css(html)
        subject = os.path.relpath(path, ROOT).split(os.sep)[0]
        info = {
            "path": os.path.relpath(path, ROOT),
            "subject": subject,
            "key": SUBJECT_KEY.get(subject, "?"),
            "mat": token_set(css),
            "dark": dark_tokens(html),
            "justify": len(JUSTIFY_RE.findall(css)),
            "radius": (re.search(r"--radius:\s*([^;]+);", css) or [None, "?"])[1].strip() if re.search(r"--radius:\s*([^;]+);", css) else "?",
            "secnum": "mat" if "var(--mat)" in rule(css, ".sec-num") else "legado",
            "cardbar": "sim" if ".card::before" in css else "nao",
            "thfont": th_font(css),
            "tldr": ".tldr" in css,
            "own_rules": sorted((body_classes(html) & (set(re.findall(r"\.([a-zA-Z][\w-]*)", css)) - known))),
            "extras": sorted(body_classes(html) - known),
            "vm": 'data-vm="1"' in html,
        }
        digest = hashlib.md5(css.encode()).hexdigest()[:8]
        groups[digest].append(info)

    print("=" * 78)
    print("DRY-RUN — migracao visual dos resumos")
    print("=" * 78)
    print(f"arquivos: {len(files)} | variantes de CSS: {len(groups)}")
    print()

    total_justify = sum(i["justify"] for g in groups.values() for i in g)
    print(f"regras text-align:justify a remover: {total_justify}")
    print()

    for digest, items in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        sample = items[0]
        subjects = sorted({i["subject"] for i in items})
        has_mat = sum(1 for i in items if i["mat"])
        dark = sum(1 for i in items if i["dark"])
        justify = sum(i["justify"] for i in items)
        extras = sorted({c for i in items for c in i["extras"]})
        secnum = sorted({i["secnum"] for i in items})
        cardbar = sorted({i["cardbar"] for i in items})
        thfont = sorted({i["thfont"] for i in items})
        radius = sorted({i["radius"] for i in items})
        tldr = sum(1 for i in items if i["tldr"])
        mat_keys = sorted({str(i["key"]) for i in items})

        print(f"[{digest}] {len(items)} arquivo(s) — ex.: {sample['path']}")
        print(f"  materias: {', '.join(subjects)}")
        print(f"  tokens --mat: {has_mat}/{len(items)} | dark com mat: {dark}/{len(items)} | tldr: {tldr}")
        print(f"  sec-num: {', '.join(secnum)} | faixa do card: {', '.join(cardbar)} | th: {', '.join(thfont)} | radius: {', '.join(radius)}")
        print(f"  justify: {justify} regra(s)")
        if extras:
            print(f"  classes do corpo fora do canonico: {', '.join(extras[:12])}{' ...' if len(extras) > 12 else ''}")
        if "?" in mat_keys:
            print("  ATENCAO: materia sem cor definida (Legislação institucional - TCE)")
        if len(items) >= 5 and set(secnum) == {"legado"}:
            strategy = "troca do <style> pelo canonico (corrigir extras listados)"
        else:
            strategy = "ajuste cirurgico por regra"
        print(f"  estrategia sugerida: {strategy}")
        print()

    no_mat = [i for g in groups.values() for i in g if not i["mat"]]
    print("-" * 78)
    print(f"sem tokens --mat: {len(no_mat)} arquivo(s)")
    by_subject = defaultdict(int)
    for i in no_mat:
        by_subject[i["subject"]] += 1
    for s, n in sorted(by_subject.items(), key=lambda kv: -kv[1]):
        print(f"  {s}: {n}")
    print()

    pontuais = [i for g in groups.values() for i in g if i["mat"] and (i["justify"] or not i["dark"])]
    print(f"pendencias pontuais (arquivo ja moderno): {len(pontuais)}")
    for i in pontuais:
        issues = []
        if i["justify"]:
            issues.append(f"{i['justify']} justify")
        if not i["dark"]:
            issues.append("sem --mat no dark")
        print(f"  {i['path']} — {', '.join(issues)}")
    print()

    extras_files = [(i["path"], i["own_rules"]) for g in groups.values() for i in g if i["own_rules"]]
    print("regras proprias fora do canonico (so relevante nos arquivos de troca de CSS):")
    for path, own in extras_files:
        print(f"  {path} — {', '.join(own)}")
    print()
    print("observacoes:")
    print("  - 'prev'/'next'/'aula-nav*' e 'tldr*' tem estilo proprio (nao contam como quebra).")
    print("  - 'card-alt' e 'tdah-*' precisam de regra carregada na migracao.")
    print("  - Legislação institucional - TCE nao tem cor de materia no template: definir antes.")


if __name__ == "__main__":
    main()
