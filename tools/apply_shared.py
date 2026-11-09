# -*- coding: utf-8 -*-
"""
apply_shared.py — Engine compartilhado para injeção HTML nos scripts apply-*.

Extrai a lógica comum de:
- apply-review-mode.py
- apply-marks-mode.py
- apply-search.py
- apply-practice-mode.py
- apply-pwa.py

Uso:
    from apply_shared import ApplyConfig, HtmlInjectionEngine

    config = ApplyConfig(...)
    engine = HtmlInjectionEngine()
    new_html = engine.apply(html, config)
    if new_html is not None:
        write_file(path, new_html)
"""
import re
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ApplyConfig:
    """Configuração para uma injeção específica (review, marks, search, practice, pwa)."""
    # Seletores CSS/HTML para encontrar pontos de injeção
    anchors: dict[str, str] = field(default_factory=dict)

    # Conteúdo a injetar
    css: str = ""
    js: str = ""
    html: str = ""

    # Chave de idempotência: se já presente no HTML, pula (None = sempre tenta)
    idempotency_key: Optional[str] = None

    # Upgrade v1 -> v2: remove blocos antigos antes de injetar
    upgrade_v1_patterns: list[str] = field(default_factory=list)
    upgrade_v1_regex: list[tuple[str, dict]] = field(default_factory=list)  # (pattern, flags_dict)

    # Ponto de injeção do CSS (antes de </style>)
    css_anchor: str = r"</style>"
    css_anchor_flags: dict = field(default_factory=dict)

    # Ponto de injeção do JS/HTML (antes de </body> ou marcador customizado)
    js_anchor: str = r"</body>"
    js_anchor_flags: dict = field(default_factory=dict)
    html_anchor: Optional[str] = None  # se None, usa js_anchor
    html_anchor_flags: dict = field(default_factory=dict)

    # Se True, injeta DEPOIS do match (match.end()) em vez de ANTES (match.start())
    inject_html_after: bool = False

    # Função opcional de validação/customização do HTML final
    post_process: Optional[callable] = None


class HtmlInjectionEngine:
    """
    Engine de injeção HTML reutilizável.

    Fluxo:
    1. Checa idempotency_key — se já presente, retorna None (sem mudança)
    2. Remove blocos v1 (upgrade_v1_patterns/regex)
    3. Injeta CSS no css_anchor
    4. Injeta HTML no html_anchor (ou js_anchor)
    5. Injeta JS no js_anchor
    6. Chama post_process se fornecido
    """

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def apply(self, html: str, config: ApplyConfig) -> Optional[str]:
        """Aplica a configuração no HTML. Retorna novo HTML ou None se sem mudanças."""
        original = html

        # 1. Idempotência
        if config.idempotency_key and config.idempotency_key in html:
            if self.verbose:
                print(f"  [idempotent] {config.idempotency_key} já presente — pulando")
            return None

        # 2. Upgrade v1 -> v2 (remove blocos antigos)
        for pattern in config.upgrade_v1_patterns:
            if pattern in html:
                html = html.replace(pattern, "")
                if self.verbose:
                    print(f"  [upgrade] removido bloco v1 exato")

        for pattern, flags in config.upgrade_v1_regex:
            flags_val = 0
            if flags.get("multiline"):
                flags_val |= re.M
            if flags.get("dotall"):
                flags_val |= re.S
            html = re.sub(pattern, "", html, count=1, flags=flags_val)
            if self.verbose:
                print(f"  [upgrade] removido bloco v1 via regex")

        # 3. Injeta CSS
        html = self._inject_at_anchor(html, config.css_anchor, config.css, "CSS",
                                      flags=config.css_anchor_flags)
        if html is None:
            return None

        # 4. Injeta HTML (painel, botão, etc.)
        html_anchor = config.html_anchor or config.js_anchor
        html_anchor_flags = config.html_anchor_flags or config.js_anchor_flags
        if config.html:
            html = self._inject_at_anchor(html, html_anchor, config.html, "HTML",
                                          flags=html_anchor_flags, inject_after=config.inject_html_after)
            if html is None:
                return None

        # 5. Injeta JS
        if config.js:
            html = self._inject_at_anchor(html, config.js_anchor, config.js, "JS",
                                          flags=config.js_anchor_flags)
            if html is None:
                return None

        # 6. Post-process
        if config.post_process:
            html = config.post_process(html)

        if html == original:
            return None

        return html

    def _inject_at_anchor(self, html: str, anchor_pattern: str, content: str, label: str,
                          flags: dict = None, inject_after: bool = False) -> Optional[str]:
        """Injeta conteúdo antes (ou depois) da primeira ocorrência do anchor_pattern."""
        if not content:
            return html

        flags_val = 0
        if flags:
            if flags.get("multiline"):
                flags_val |= re.M
            if flags.get("dotall"):
                flags_val |= re.S
            if flags.get("ignorecase"):
                flags_val |= re.I

        # Tenta regex primeiro (para padrões complexos)
        match = re.search(anchor_pattern, html, flags_val)
        if match:
            pos = match.end() if inject_after else match.start()
            return html[:pos] + content + html[pos:]

        # Fallback: busca literal
        pos = html.find(anchor_pattern)
        if pos == -1:
            if self.verbose:
                print(f"  [warn] anchor '{anchor_pattern}' não encontrado para {label}")
            return None

        # Para busca literal, inject_after não faz sentido (não tem match.end)
        return html[:pos] + content + html[pos:]

    def find_anchor(self, html: str, selector: str) -> int:
        """Encontra posição de âncora (compatibilidade com código legado)."""
        match = re.search(selector, html)
        if match:
            return match.start()
        pos = html.find(selector)
        return pos


# ============================================================
# Configurações pré-definidas para cada script apply-*
# ============================================================

REV_CONFIG = ApplyConfig(
    idempotency_key='id="rhRev"',
    css_anchor=r"</style>",
    js_anchor=r"<!--/rh:ui-->",
    css="""\n/* ===== RH modo revisão (active recall) ===== */
html.rh-rev .card-text, html.rh-rev .gotcha, html.rh-rev .callout, html.rh-rev .table-wrap,
html.rh-rev .mnemonic-content, html.rh-rev .question-text, html.rh-rev .answer { display: none; }
html.rh-rev .card, html.rh-rev .gotcha, html.rh-rev .callout, html.rh-rev .table-wrap,
html.rh-rev .mnemonic, html.rh-rev .question { cursor: pointer; }
html.rh-rev .card.rev-open .card-text, html.rh-rev .gotcha.rev-open, html.rh-rev .callout.rev-open,
html.rh-rev .table-wrap.rev-open, html.rh-rev .mnemonic.rev-open .mnemonic-content,
html.rh-rev .question.rev-open .question-text, html.rh-rev .question.rev-open .answer { display: block; }
html.rh-rev .card.rev-open, html.rh-rev .gotcha.rev-open { border-color: var(--amber); }
.rh-toolbar button.on { border-color: var(--amber); background: #fdf3d8; }
html[data-theme="dark"] .rh-toolbar button.on { background: #33290f; border-color: #6e5a1e; }
""",
    js="""\n<script id="rh-rev">
(function(){
  var b=document.getElementById('rhRev'); if(!b) return;
  var root=document.documentElement;
  function on(){return root.classList.contains('rh-rev');}
  function apply(){
    var now=!on();
    root.classList.toggle('rh-rev', now);
    b.classList.toggle('on', now);
    try{localStorage.setItem('rh-rev', now?'1':'0');}catch(e){}
    b.setAttribute('aria-pressed', now?'true':'false');
  }
  b.addEventListener('click', apply);
  try{ if(localStorage.getItem('rh-rev')==='1') apply(); }catch(e){}
  document.addEventListener('click', function(ev){
    if(!on()) return;
    var el = ev.target && ev.target.closest ? ev.target.closest('.card,.gotcha,.callout,.table-wrap,.mnemonic,.question') : null;
    if(!el || ev.target.closest('a')) return;
    el.classList.toggle('rev-open');
  });
})();
</script>""",
    html='\n  <button type="button" id="rhRev" title="Modo revisão: oculte e se auto-teste" aria-label="Alternar modo revisão" aria-pressed="false">🧠</button>',
    html_anchor=r'(<button type="button" id="rhTop"[^>]*>↑</button>)',
    upgrade_v1_regex=[
        (r'<script id="rh-rev">[\s\S]*?</script>\n?', {}),
    ],
    post_process=lambda html: _rev_post_process(html),
)


def _rev_post_process(html: str) -> str:
    """Move o botão rhRev para DEPOIS do rhTop."""
    pattern = r'(<button type="button" id="rhRev"[^>]*>🧠</button>)(<button type="button" id="rhTop"[^>]*>↑</button>)'
    return re.sub(pattern, r'\2\1', html, count=1)


MARKS_CONFIG = ApplyConfig(
    idempotency_key='id="rhMarks"',
    css_anchor=r"</style>",
    js_anchor=r"<!--/rh:ui-->",
    css="""\n/* ===== RH marcação pessoal (vacilo) ===== */
html.rh-marking .card, html.rh-marking .gotcha, html.rh-marking .callout,
html.rh-marking .table-wrap, html.rh-marking .mnemonic, html.rh-marking .question { cursor: pointer; }
.rh-marked { border-color: var(--red) !important; box-shadow: 0 0 0 1px var(--red); }
#rhMarkPanel { position: fixed; right: 1.1rem; bottom: 5.6rem; z-index: 299; display: none;
  background: var(--card); border: 1px solid var(--border); border-radius: 10px;
  padding: .6rem .8rem; font-size: .8rem; box-shadow: 0 4px 14px rgba(31,39,51,.14); min-width: 180px; }
#rhMarkPanel.show { display: block; }
#rhMarkPanel .rhmp-count { font-family: 'IBM Plex Mono', 'Consolas', monospace; font-size: .72rem; color: var(--text2); margin-bottom: .4rem; }
#rhMarkPanel button { font-family: 'IBM Plex Mono', 'Consolas', monospace; font-size: .74rem; font-weight: 600;
  background: var(--card); border: 1px solid var(--border); border-radius: 6px; padding: .28rem .6rem;
  color: var(--text); cursor: pointer; margin-right: .3rem; }
#rhMarkPanel button:hover { border-color: var(--blue); }
@media print { #rhMarkPanel { display: none !important; } }
""",
    js="""\n<script id="rh-marks">
(function(){
  var b=document.getElementById('rhMarks'); if(!b) return;
  var root=document.documentElement;
  var LS='rh-marks', KEY=location.pathname||'local';
  var store={}; try{store=JSON.parse(localStorage.getItem(LS)||'{}')||{};}catch(e){}
  var panel=document.createElement('div'); panel.id='rhMarkPanel';
  panel.innerHTML='<div class="rhmp-count">Vacilos marcados: <span id="rhmpN">0</span></div>'+
    '<button type="button" id="rhmpExp">⬇ exportar</button>'+
    '<button type="button" id="rhmpImp">⬆ importar</button><input id="rhmpFile" type="file" accept="application/json" hidden>';
  document.body.appendChild(panel);
  var nEl=document.getElementById('rhmpN'), fileIn=document.getElementById('rhmpFile');
  function blkKey(el){
    var sec=el.closest('section'); var sid=sec?(sec.id||''):'';
    var t=el.querySelector('.card-title,.gotcha-title,.mnemonic-label');
    var txt='';
    if(t){txt=t.textContent.trim();}
    else{var th=el.querySelector('th'); txt=th?th.textContent.trim():'';}
    if(!txt){var f=el.firstElementChild; txt=(f?f.textContent:'')||'';}
    return (sid?sid+'|':'')+(txt.slice(0,60)||'bloco');
  }
  var SEL='.card,.gotcha,.callout,.table-wrap,.mnemonic,.question';
  function collect(){ var out=[]; document.querySelectorAll('.rh-marked').forEach(function(el){out.push(blkKey(el));}); return out; }
  function save(){ store[KEY]=collect(); try{localStorage.setItem(LS,JSON.stringify(store));}catch(e){} render(); }
  function render(){ nEl.textContent=String(collect().length); }
  function applyMarks(list){
    document.querySelectorAll('.rh-marked').forEach(function(el){el.classList.remove('rh-marked');});
    document.querySelectorAll(SEL).forEach(function(el){ if(list.indexOf(blkKey(el))>=0) el.classList.add('rh-marked'); });
    save();
  }
  function on(){return root.classList.contains('rh-marking');}
  b.addEventListener('click', function(){
    root.classList.toggle('rh-marking', b.classList.toggle('on', !on()));
    b.setAttribute('aria-pressed', on()?'true':'false');
    panel.classList.toggle('show', on());
  });
  document.addEventListener('click', function(ev){
    if(!on()) return;
    var el = ev.target && ev.target.closest ? ev.target.closest(SEL) : null;
    if(!el || ev.target.closest('a') || ev.target.closest('#rhMarkPanel')) return;
    el.classList.toggle('rh-marked');
    save();
  });
  document.getElementById('rhmpExp').addEventListener('click', function(){
    var blob=new Blob([JSON.stringify({version:1,path:KEY,marks:collect()},null,2)],{type:'application/json'});
    var a=document.createElement('a'); a.href=URL.createObjectURL(blob);
    a.download='marcacoes'+KEY.replace(/[^\\w]+/g,'-')+'.json'; a.click();
  });
  document.getElementById('rhmpImp').addEventListener('click', function(){ fileIn.click(); });
  fileIn.addEventListener('change', function(){
    var f=fileIn.files && fileIn.files[0]; if(!f) return;
    var r=new FileReader(); r.onload=function(){
      try{ var d=JSON.parse(r.result); if(d&&d.marks) applyMarks(d.marks); }catch(e){}
    }; r.readAsText(f);
  });
  try{
    var saved=(store[KEY]||[]);
    if(saved.length) applyMarks(saved);
  }catch(e){}
  render();
})();
</script>""",
    html='\n  <button type="button" id="rhMarks" title="Marcar vacilos (cards) — exportar/importar backup" aria-label="Marcar vacilos" aria-pressed="false">🏷️</button>',
    html_anchor=r'(<button type="button" id="rhRev"[^>]*>🧠</button>)',
    post_process=lambda html: _marks_post_process(html),
)


def _marks_post_process(html: str) -> str:
    """Move o botão rhMarks para DEPOIS do rhRev."""
    pattern = r'(<button type="button" id="rhMarks"[^>]*>🏷️</button>)(<button type="button" id="rhRev"[^>]*>🧠</button>)'
    return re.sub(pattern, r'\2\1', html, count=1)


SEARCH_CONFIG = ApplyConfig(
    idempotency_key='data-sr-v="2"',
    css_anchor=r"</head>",
    js_anchor=r"</body>",
    html_anchor=r'<div class="sidebar-sub">',
    css="""<style id="sr-style">
.sr-box { padding: .55rem .2rem .2rem; }
#sr-input {
  width: 100%; box-sizing: border-box; background: var(--card, #fff);
  border: 1px solid var(--border, #e2dfd7); border-radius: 8px; padding: .42rem .6rem;
  color: var(--text, #1f2733); font-family: 'JetBrains Mono', 'IBM Plex Mono', monospace; font-size: .72rem;
}
#sr-input:focus { outline: none; border-color: var(--mat, var(--blue, #2563eb)); }
.sr-info {
  display: flex; justify-content: space-between; align-items: center; gap: .3rem;
  margin-top: .3rem; font-family: 'JetBrains Mono', 'IBM Plex Mono', monospace;
  font-size: .62rem; color: var(--text2, #455064);
}
.sr-nav { display: inline-flex; align-items: center; gap: .25rem; }
.sr-nav button {
  background: none; border: 1px solid var(--border, #e2dfd7); border-radius: 5px;
  cursor: pointer; color: var(--text2, #455064); font-family: inherit;
  font-size: .62rem; padding: 0 .32rem; line-height: 1.5;
}
.sr-nav button:hover:not(:disabled) { border-color: var(--mat, var(--blue)); color: var(--mat-strong, var(--blue)); }
.sr-nav button:disabled { opacity: .35; cursor: default; }
#sr-pos { min-width: 3.2ch; text-align: center; color: var(--mat-strong, var(--blue, #2563eb)); font-weight: 600; }
#sr-clear {
  background: none; border: none; padding: 0; cursor: pointer;
  color: var(--mat-strong, var(--blue, #2563eb)); font-family: 'JetBrains Mono', 'IBM Plex Mono', monospace; font-size: .62rem;
}
#sr-clear:hover { text-decoration: underline; }
.sr-hide { display: none !important; }
section.sr-empty { opacity: .4; }
mark.sr-hit {
  background: rgba(217, 119, 6, .55); color: inherit;
  border-radius: 3px; padding: 0 1px; box-shadow: 0 0 0 1px rgba(217, 119, 6, .35);
}
[data-theme="dark"] mark.sr-hit { background: rgba(240, 169, 46, .45); }
mark.sr-first {
  background: rgba(220, 38, 38, .55); box-shadow: 0 0 0 2px rgba(220, 38, 38, .4);
}
@media print { .sr-box { display: none !important; } }
</style>""",
    js="""<script id="sr-script" data-sr-v="2">
(function () {
  var input = document.getElementById('sr-input');
  if (!input) return;
  var info = document.getElementById('sr-count');
  var posEl = document.getElementById('sr-pos');
  var bPrev = document.getElementById('sr-prev');
  var bNext = document.getElementById('sr-next');
  var clear = document.getElementById('sr-clear');
  var SEL = '.card, .gotcha, .callout';
  var blocks = Array.prototype.slice.call(document.querySelectorAll('.main ' + SEL));
  var total = blocks.length;
  var hits = [], cur = -1;
  var norm = function (s) {
    return (s || '').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');
  };
  function clearMarks(root) {
    root.querySelectorAll('mark.sr-hit').forEach(function (m) {
      var p = m.parentNode;
      if (!p) return;
      p.replaceChild(document.createTextNode(m.textContent), m);
      p.normalize();
    });
  }
  function highlight(block, words) {
    var walker = document.createTreeWalker(block, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.nodeValue || !n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        var p = n.parentNode;
        if (!p || /^(SCRIPT|STYLE|MARK)$/.test(p.nodeName)) return NodeFilter.FILTER_REJECT;
        var low = norm(n.nodeValue);
        for (var w = 0; w < words.length; w++) {
          if (low.indexOf(words[w]) >= 0) return NodeFilter.FILTER_ACCEPT;
        }
        return NodeFilter.FILTER_REJECT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (n) {
      var text = n.nodeValue, low = norm(text);
      var frag = document.createDocumentFragment(), i = 0;
      for (;;) {
        var best = -1, bestLen = 0;
        for (var w = 0; w < words.length; w++) {
          var idx = low.indexOf(words[w], i);
          if (idx >= 0 && (best < 0 || idx < best)) { best = idx; bestLen = words[w].length; }
        }
        if (best < 0) break;
        if (best > i) frag.appendChild(document.createTextNode(text.slice(i, best)));
        var mk = document.createElement('mark');
        mk.className = 'sr-hit';
        mk.textContent = text.slice(best, best + bestLen);
        frag.appendChild(mk);
        i = best + bestLen;
      }
      if (i < text.length) frag.appendChild(document.createTextNode(text.slice(i)));
      n.parentNode.replaceChild(frag, n);
    });
  }
  function setActive(n, scroll) {
    if (cur >= 0 && hits[cur]) hits[cur].classList.remove('sr-first');
    cur = n;
    if (!hits.length) { posEl.textContent = ''; sync(); return; }
    cur = ((n % hits.length) + hits.length) % hits.length;
    hits[cur].classList.add('sr-first');
    posEl.textContent = (cur + 1) + '/' + hits.length;
    if (scroll) hits[cur].scrollIntoView({ behavior: 'smooth', block: 'center' });
    sync();
  }
  function sync() {
    bPrev.disabled = bNext.disabled = hits.length === 0;
  }
  function run(scrollToFirst) {
    var q = norm(input.value.trim());
    var words = q ? q.split(/\\s+/).filter(Boolean) : [];
    blocks.forEach(function (b) { b.classList.remove('sr-hide'); clearMarks(b); });
    hits = []; cur = -1;
    if (words.length) {
      var found = 0;
      blocks.forEach(function (b) {
        var low = norm(b.textContent);
        var all = words.every(function (w) { return low.indexOf(w) >= 0; });
        if (all) { found++; highlight(b, words); }
        else { b.classList.add('sr-hide'); }
      });
      document.querySelectorAll('.main section').forEach(function (s) {
        var vis = s.querySelectorAll(SEL + ':not(.sr-hide)').length;
        s.classList.toggle('sr-empty', vis === 0);
      });
      info.textContent = found + ' de ' + total + ' blocos';
      hits = Array.prototype.slice.call(document.querySelectorAll('.main mark.sr-hit'));
      if (hits.length && scrollToFirst !== false) setActive(0, true); else sync();
      if (!hits.length) { posEl.textContent = ''; sync(); }
    } else {
      document.querySelectorAll('.main section').forEach(function (s) { s.classList.remove('sr-empty'); });
      info.textContent = total + ' blocos';
      posEl.textContent = ''; sync();
    }
  }
  input.addEventListener('input', function () { run(true); });
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { input.value = ''; run(true); }
    else if (e.key === 'Enter') { e.preventDefault(); setActive(hits.length ? cur + (e.shiftKey ? -1 : 1) : -1, true); }
  });
  bNext.addEventListener('click', function () { if (hits.length) setActive(cur + 1, true); });
  bPrev.addEventListener('click', function () { if (hits.length) setActive(cur - 1, true); });
  clear.addEventListener('click', function () { input.value = ''; run(true); input.focus(); });
  run(false);
})();
</script>""",
    html="""  <div class="sr-box" data-sr-v="2">
    <input id="sr-input" type="search" placeholder="Buscar palavra no resumo…" autocomplete="off">
    <div class="sr-info"><span id="sr-count" role="status" aria-live="polite"></span>
<span class="sr-nav"><button id="sr-prev" type="button" title="Ocorrência anterior (Shift+Enter)" disabled>↑</button>
<span id="sr-pos"></span>
<button id="sr-next" type="button" title="Próxima ocorrência (Enter)" disabled>↓</button></span>
<button id="sr-clear" type="button">limpar</button></div>
  </div>""",
    upgrade_v1_patterns=[
        """  <div class="sr-box">
    <input id="sr-input" type="search" placeholder="Buscar palavra no resumo…" autocomplete="off">
    <div class="sr-info"><span id="sr-count"></span><button id="sr-clear" type="button">limpar</button></div>
  </div>""",
    ],
    upgrade_v1_regex=[
        (r'[ \t]*<div class="sr-box"[^>]*>[\s\S]*?^[ \t]*</div>\n', {"multiline": True}),
        (r'<style id="sr-style">[\s\S]*?</style>\n?', {}),
        (r'<script id="sr-script"[^>]*>[\s\S]*?</script>\n?', {}),
    ],
    post_process=lambda html: _search_post_process(html),
)


def _search_post_process(html: str) -> str:
    """Move o sr-box para DEPOIS do sidebar-sub completo (incluindo </div>\n)."""
    # Engine injeta ANTES do <div class="sidebar-sub">.
    # Estrutura real: <div class="sr-box">...</div>  </div><div class="sidebar-sub">...
    # Precisamos mover sr-box para DEPOIS do sidebar-sub.
    pattern = r'(<div class="sr-box" data-sr-v="2">[\s\S]*?</div>\s*</div>\s*)(<div class="sidebar-sub">.*?</div>\n)'
    return re.sub(pattern, r'\2\1', html, count=1, flags=re.S)


PRACTICE_CONFIG = ApplyConfig(
    idempotency_key='<!--rh:practice:start-->',
    css_anchor=r"</style>",
    js_anchor=r"</body>",
    css="""\n/* ===== RH modo prática (quiz) ===== */
#rhPracticePanel { position: fixed; right: 1.1rem; bottom: 5.8rem; z-index: 301; display: none;
  width: min(390px, calc(100vw - 2.2rem)); max-height: min(72vh, 580px); overflow: auto;
  background: var(--card, #fff); border: 1px solid var(--border, #e2dfd7); border-radius: 12px;
  box-shadow: 0 8px 28px rgba(31,39,51,.2); padding: .85rem .95rem .95rem; }
#rhPracticePanel.show { display: block; }
#rhPracticePanel .rhpp-head { display: flex; align-items: center; gap: .5rem; margin-bottom: .3rem; }
#rhPracticePanel .rhpp-head strong { font-size: .88rem; color: var(--text, #1f2733); }
#rhPracticePanel .rhpp-score { font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: .7rem;
  color: var(--text2, #455064); margin-left: auto; white-space: nowrap; }
#rhPracticePanel .rhpp-close { background: none; border: none; font-size: 1.15rem; line-height: 1;
  cursor: pointer; color: var(--text2, #455064); padding: 0 .1rem; }
#rhPracticePanel .rhpp-item { margin: .55rem 0; }
#rhPracticePanel .rhpp-q { font-size: .83rem; font-weight: 700; color: var(--text, #1f2733);
  margin-bottom: .3rem; line-height: 1.45; }
#rhPracticePanel .rhpp-opt { display: block; width: 100%; text-align: left; font-size: .79rem; line-height: 1.45;
  font-family: inherit; background: var(--bg, #fff); color: var(--text, #1f2733);
  border: 1px solid var(--border, #e2dfd7); border-radius: 8px; padding: .4rem .6rem;
  margin: .25rem 0; cursor: pointer; }
#rhPracticePanel .rhpp-opt:hover:not(:disabled) { border-color: var(--mat, var(--blue, #2563eb)); }
#rhPracticePanel .rhpp-opt:disabled { cursor: default; opacity: .72; }
#rhPracticePanel .rhpp-opt.ok { border-color: #15803d; background: rgba(21,128,61,.1); opacity: 1; }
#rhPracticePanel .rhpp-opt.bad { border-color: var(--red, #b3261e); background: rgba(179,38,30,.08); opacity: 1; }
#rhPracticePanel .rhpp-why { font-size: .75rem; color: var(--text2, #455064); line-height: 1.5;
  background: var(--surface, #f6f4ee); border-left: 3px solid var(--mat, var(--blue, #2563eb));
  border-radius: 0 8px 8px 0; padding: .42rem .6rem; margin-top: .28rem; }
#rhPracticePanel .rhpp-reset { font-family: 'JetBrains Mono', 'Consolas', monospace; font-size: .72rem;
  font-weight: 600; background: var(--card, #fff); color: var(--mat, var(--blue, #2563eb));
  border: 1px solid var(--border, #e2dfd7); border-radius: 8px; padding: .35rem .7rem;
  cursor: pointer; margin-top: .55rem; }
html[data-theme="dark"] #rhPracticePanel { background: var(--surface, #1f232b); }
html[data-theme="dark"] #rhPracticePanel .rhpp-opt { background: var(--card, #262b34); }
html[data-theme="dark"] #rhPracticePanel .rhpp-why { background: rgba(255,255,255,.05); }
@media print { #rhPracticePanel { display: none !important; } }
""",
    js="""<script id="rh-practice">
(function(){
  var dataEl = document.getElementById('rhPracticeData');
  var btn = document.getElementById('rhPractice');
  var panel = document.getElementById('rhPracticePanel');
  if (!dataEl || !btn || !panel) return;
  var DATA; try { DATA = JSON.parse(dataEl.textContent); } catch (e) { return; }
  var qs = DATA.questoes || [];
  var list = document.getElementById('rhPracticeList');
  var scoreEl = document.getElementById('rhPracticeScore');
  var hits = 0, done = 0, total = qs.length;
  function score() { scoreEl.textContent = hits + ' acertos · ' + done + '/' + total; }
  function render() {
    hits = 0; done = 0; list.innerHTML = '';
    qs.forEach(function (item, qi) {
      var box = document.createElement('div'); box.className = 'rhpp-item';
      var q = document.createElement('div'); q.className = 'rhpp-q';
      q.textContent = 'Q' + (qi + 1) + ' · ' + item.q; box.appendChild(q);
      item.opts.forEach(function (o) {
        var b = document.createElement('button'); b.type = 'button';
        b.className = 'rhpp-opt'; b.textContent = o.t;
        b.addEventListener('click', function () {
          if (box.getAttribute('data-done') === '1') return;
          box.setAttribute('data-done', '1');
          var opts = box.querySelectorAll('.rhpp-opt');
          Array.prototype.forEach.call(opts, function (s, si) {
            s.disabled = true;
            if (item.opts[si] && item.opts[si].ok) s.classList.add('ok');
          });
          if (!o.ok) b.classList.add('bad');
          var why = document.createElement('div'); why.className = 'rhpp-why';
          why.setAttribute('role', 'status'); why.setAttribute('aria-live', 'polite');
          why.textContent = o.why || ''; box.appendChild(why);
          done++; if (o.ok) hits++; score();
        });
        box.appendChild(b);
      });
      list.appendChild(box);
    });
    score();
  }
  btn.addEventListener('click', function () {
    var show = !panel.classList.contains('show');
    panel.classList.toggle('show', show);
    btn.classList.toggle('on', show);
    btn.setAttribute('aria-pressed', show ? 'true' : 'false');
    if (show && !list.children.length) render();
  });
  document.getElementById('rhPracticeClose').addEventListener('click', function () {
    panel.classList.remove('show'); btn.classList.remove('on');
    btn.setAttribute('aria-pressed', 'false');
  });
  document.getElementById('rhPracticeReset').addEventListener('click', render);
})();
</script>""",
    html="""<!--rh:practice:start-->
<style id="rh-practice-style"></style>
<div id="rhPracticePanel" role="dialog" aria-label="Modo prática — quiz da aula">
  <div class="rhpp-head"><strong>🎯 Modo prática</strong>
<span class="rhpp-score" id="rhPracticeScore" role="status" aria-live="polite"></span>
<button type="button" class="rhpp-close" id="rhPracticeClose" aria-label="Fechar">×</button></div>
  <div id="rhPracticeList"></div>
  <button type="button" class="rhpp-reset" id="rhPracticeReset">Refazer</button>
</div>
<script type="application/json" id="rhPracticeData"></script>
<!--rh:practice:end-->""",
    upgrade_v1_regex=[
        (r'<!--rh:practice:start-->[\s\S]*?<!--rh:practice:end-->\n?', {}),
        (r'<!--rh:practice-btn:start-->[\s\S]*?<!--rh:practice-btn:end-->', {}),
    ],
)


PWA_CONFIG = ApplyConfig(
    idempotency_key='rel="manifest"',
    css_anchor=r"</head>",
    js_anchor=r"</head>",
    html="""<link rel="manifest" href="/manifest.webmanifest">
<link rel="apple-touch-icon" href="/icons/icon-180.png">
<meta name="theme-color" content="#F5F4F0">
<script>
if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
  navigator.serviceWorker.register('/sw.js').catch(function () {});
}
</script>""",
    css="",
    js="",
)


A11Y_CONFIG = ApplyConfig(
    idempotency_key='id="rh-nav-mobile"',
    # CSS no fim do <head>: precisa vencer o `display:none` que as páginas
    # aplicam ao sidebar em <=900px (mesma especificidade, ordem posterior).
    css_anchor=r"</head>",
    css="""<style id="rh-nav-css">
/* rh-nav-mobile v1 */
.rh-skip{position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden;z-index:400}
.rh-skip:focus{left:.75rem;top:.75rem;width:auto;height:auto;padding:.55rem .9rem;background:var(--card,#fff);color:var(--ink,#1f2733);border:2px solid var(--mat,#2563eb);border-radius:8px;font:600 .82rem/1.3 var(--font-body,system-ui,sans-serif);box-shadow:0 4px 16px rgba(31,39,51,.2)}
#conteudo:focus{outline:none}
.rh-navbtn{display:none}
.rh-navbackdrop{display:none}
.aula .sidebar a.rh-current{background:var(--mat-soft,#e8effd);color:var(--text,#1f2733);font-weight:600;box-shadow:inset 3px 0 0 var(--mat,#2563eb)}
html[data-theme="dark"] .aula .sidebar a.rh-current{background:rgba(255,255,255,.08);color:#fff}
@media(max-width:900px){
  .rh-navbtn{display:flex;align-items:center;justify-content:center;position:fixed;left:.8rem;bottom:calc(.9rem + env(safe-area-inset-bottom));width:46px;height:46px;border-radius:50%;border:1px solid var(--line-strong,#c9c5ba);background:var(--card,#fff);color:var(--ink,#1f2733);box-shadow:0 4px 14px rgba(31,39,51,.16);z-index:320;cursor:pointer;font-size:1.15rem;line-height:1;padding:0}
  .rh-navbtn[aria-expanded="true"]{background:var(--mat,#2563eb);color:#fff;border-color:var(--mat,#2563eb)}
  .aula .sidebar{display:block;transform:translateX(-105%);visibility:hidden;transition:transform .22s ease,visibility 0s linear .22s;box-shadow:0 12px 44px rgba(0,0,0,.22);z-index:330;padding-bottom:calc(1.5rem + env(safe-area-inset-bottom))}
  .aula .sidebar.rh-open{transform:none;visibility:visible;transition:transform .22s ease,visibility 0s}
  body.rh-nav-open{overflow:hidden}
  .rh-navbackdrop.rh-open{display:block;position:fixed;top:0;right:0;bottom:0;left:0;background:rgba(15,20,30,.42);z-index:310}
}
@media(prefers-reduced-motion:reduce){.aula .sidebar{transition:none}}
@media print{.rh-navbtn,.rh-navbackdrop,.rh-skip{display:none!important}}
</style>
""",
    html_anchor=r"<body[^>]*>",
    inject_html_after=True,
    html='<a class="rh-skip" href="#conteudo">Pular para o conteúdo</a>\n',
    js_anchor=r"</body>",
    js="""<button type="button" class="rh-navbtn" id="rhNavBtn" aria-label="Abrir navegação de seções" aria-expanded="false" aria-controls="rhSidebar">☰</button>
<div class="rh-navbackdrop" id="rhNavBackdrop"></div>
<script id="rh-nav-mobile">
(function(){
  var btn = document.getElementById('rhNavBtn');
  var sb = document.querySelector('.aula .sidebar');
  var bd = document.getElementById('rhNavBackdrop');
  if (!btn || !sb || !bd) return;
  sb.id = 'rhSidebar';
  var mq = window.matchMedia('(max-width: 900px)');
  function isOpen(){ return sb.classList.contains('rh-open'); }
  function open(){
    sb.classList.add('rh-open'); bd.classList.add('rh-open');
    document.body.classList.add('rh-nav-open');
    btn.setAttribute('aria-expanded','true');
    btn.setAttribute('aria-label','Fechar navegação de seções');
    var first = sb.querySelector('a');
    if (first) first.focus({preventScroll:true});
  }
  function close(returnFocus){
    sb.classList.remove('rh-open'); bd.classList.remove('rh-open');
    document.body.classList.remove('rh-nav-open');
    btn.setAttribute('aria-expanded','false');
    btn.setAttribute('aria-label','Abrir navegação de seções');
    if (returnFocus) btn.focus({preventScroll:true});
  }
  btn.addEventListener('click', function(){ if (isOpen()) close(true); else open(); });
  bd.addEventListener('click', function(){ close(true); });
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && isOpen()) close(true);
  });
  sb.addEventListener('click', function(e){
    var a = e.target.closest ? e.target.closest('a') : null;
    if (a && mq.matches) close(false);
  });
  var onMq = function(e){ if (!e.matches && isOpen()) close(false); };
  if (mq.addEventListener) mq.addEventListener('change', onMq);
  else if (mq.addListener) mq.addListener(onMq);

  var links = [].slice.call(sb.querySelectorAll('a[href^="#"]'));
  var byId = {};
  links.forEach(function(a){ var id = a.getAttribute('href').slice(1); if (id) byId[id] = a; });
  var secs = [].slice.call(document.querySelectorAll('.main section[id]'));
  if (!('IntersectionObserver' in window) || !secs.length) return;
  var cur = null;
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if (!en.isIntersecting) return;
      var a = byId[en.target.id];
      if (a && a !== cur) {
        if (cur) { cur.classList.remove('rh-current'); cur.removeAttribute('aria-current'); }
        cur = a; a.classList.add('rh-current'); a.setAttribute('aria-current','location');
      }
    });
  }, {rootMargin: '-12% 0px -72% 0px'});
  secs.forEach(function(s){ io.observe(s); });
})();
</script>
""",
)


A11Y_SKIP_CONFIG = ApplyConfig(
    idempotency_key='class="rh-skip"',
    css_anchor=r"</head>",
    css="""<style id="rh-skip-css">
.rh-skip{position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden;z-index:400}
.rh-skip:focus{left:.75rem;top:.75rem;width:auto;height:auto;padding:.55rem .9rem;background:var(--card,#fff);color:var(--ink,#1f2733);border:2px solid var(--mat,#2563eb);border-radius:8px;font:600 .82rem/1.3 var(--font-body,system-ui,sans-serif);box-shadow:0 4px 16px rgba(31,39,51,.2)}
#conteudo:focus{outline:none}
@media print{.rh-skip{display:none!important}}
</style>
""",
    html_anchor=r"<body[^>]*>",
    inject_html_after=True,
    html='<a class="rh-skip" href="#conteudo">Pular para o conteúdo</a>\n',
)


# Utilitários compartilhados

TOOLBAR_CSS = """
/* ===== RH toolbar base (reparo) ===== */
.rh-toolbar { position: fixed; right: 1.1rem; bottom: 1.1rem; display: flex; flex-direction: column; gap: .45rem; z-index: 300; }
.rh-toolbar button {
  width: 42px; height: 42px; border-radius: 50%; border: 1px solid var(--line-strong);
  background: var(--card); color: var(--text); cursor: pointer; padding: 0; line-height: 1;
  font-family: 'JetBrains Mono', 'Consolas', monospace; font-weight: 600; font-size: .9rem;
  box-shadow: 0 4px 14px rgba(31,39,51,.18); display: flex; align-items: center; justify-content: center;
  transition: transform .15s, border-color .15s;
}
.rh-toolbar button:hover { transform: translateY(-2px); border-color: var(--blue); }
.rh-toolbar button:disabled { opacity: .4; cursor: default; transform: none; }
.rh-toolbar button[hidden] { display: none; }
@media (max-width: 768px) { .rh-toolbar { right: .7rem; bottom: .7rem; } }
"""

REV_BTN = '\n  <button type="button" id="rhRev" title="Modo revisão: oculte e se auto-teste" aria-label="Alternar modo revisão" aria-pressed="false">🧠</button>'
PRAC_BTN = '<button type="button" id="rhPractice" title="Modo prática: quiz de recall da aula" aria-label="Abrir modo prática" aria-pressed="false">🎯</button>'
BTN_S, BTN_E = "<!--rh:practice-btn:start-->", "<!--rh:practice-btn:end-->"


def inject_toolbar_css(html: str) -> str:
    """Injeta CSS do toolbar antes de </style>."""
    idx = html.rfind("</style>")
    if idx == -1:
        return html
    return html[:idx] + TOOLBAR_CSS + html[idx:]


def ensure_rev_button(html: str) -> str:
    """Garante que o botão 🧠 existe (reparo)."""
    if 'id="rhRev"' in html:
        return html
    m = re.search(r'(id="rhTop"[^>]*>.*?</button>)', html)
    if m:
        return html[:m.end(1)] + REV_BTN + html[m.end(1):]
    return html


def ensure_practice_button(html: str) -> str:
    """Garante que o botão 🎯 existe (após 🧠 ou rhTop)."""
    if 'id="rhPractice"' in html:
        return html
    anchor = (re.search(r'(id="rhRev"[^>]*>.*?</button>)', html)
              or re.search(r'(id="rhTop"[^>]*>.*?</button>)', html))
    if anchor:
        btn = "\n  " + BTN_S + PRAC_BTN + BTN_E
        return html[:anchor.end(1)] + btn + html[anchor.end(1):]
    return html


def strip_practice_markers(html: str) -> str:
    """Remove marcadores antigos de prática."""
    html = re.sub(re.escape(BTN_S) + r".*?" + re.escape(BTN_E), "", html, flags=re.S)
    html = re.sub(r"<!--rh:practice:start-->[\s\S]*?<!--rh:practice:end-->\n?", "", html, flags=re.S)
    return html