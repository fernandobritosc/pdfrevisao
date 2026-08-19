# -*- coding: utf-8 -*-
"""Aplica a marcação pessoal (vacilo) nos resumos: botão 🏷 no toolbar,
marca cards/blocos em vermelho com persistência em localStorage,
export/import de backup JSON.

Uso: python apply-marks-mode.py
Idempotente: arquivos com id="rhMarks" são pulados.
"""
import glob
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Resumo_estudos")
GLOBS = [
    os.path.join(ROOT, "*", "Aula *", "resumo-*.html"),
    os.path.join(ROOT, "templates", "template-sumario.html"),
]

BUTTON = '\n  <button type="button" id="rhMarks" title="Marcar vacilos (cards) — exportar/importar backup" aria-label="Marcar vacilos" aria-pressed="false">\U0001F3F7\uFE0F</button>'

CSS = """
/* ===== RH marcação pessoal (vacilo) ===== */
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
"""

JS = """
<script id="rh-marks">
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
</script>
"""


def apply(path):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    if "id=\"rhMarks\"" in content:
        return False
    content = re.sub(r'(id="rhRev"[^>]*>.*?</button>)', r"\1" + BUTTON, content, count=1, flags=re.S)
    idx = content.rfind("</style>")
    if idx == -1:
        print("!! sem </style>: %s" % os.path.relpath(path, ROOT))
    else:
        content = content[:idx] + CSS + content[idx:]
    idx = content.rfind("<!--/rh:ui-->")
    if idx == -1:
        print("!! sem marcador rh:ui: %s" % os.path.relpath(path, ROOT))
    else:
        content = content[:idx] + JS + "\n" + content[idx:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    return True


def main():
    total = 0
    for pattern in GLOBS:
        for path in sorted(glob.glob(pattern)):
            if apply(path):
                total += 1
                print("aplicado:", os.path.relpath(path, ROOT))
    print("total aplicados:", total)


if __name__ == "__main__":
    sys.exit(main())