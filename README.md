# Revisão PDF — Sistema de Resumos para Concursos (Resumos Hermes)

Repositório que transforma PDFs de aulas (Estratégia Concursos, TEC Concursos, fases do edital) em **resumos HTML navegáveis**, publicados em [resumos-hermes.surge.sh](https://resumos-hermes.surge.sh).

**Três trilhas de estudo** (mapeadas e mantidas aqui):
- **[TJ/TRT]** — Mentoria (trilha original, em andamento)
- **[TCE-GO]** — FCC · prova 17/01/2027 · Técnico de Controle Externo (`Resumo_estudos/tce-go-trilha.html`)
- **[IFG]** — AOCP · Assistente em Administração (cargo 301, Nível D) · prova 14/02/2027 · inscrições 24/11–23/12/2026 (`Resumo_estudos/ifg-trilha.html`) · grade de revisão semanal em `Resumo_estudos/ifg-revisao-semanal.md`

## Estrutura
- `Resumo_estudos/` — **o site publicado** (índice, resumos por matéria/aula, trilhas, changelog, busca full-text)
- `<Matéria>/<Aula NN>/` — fontes convertidas (`.md` a partir dos PDFs; os PDFs são excluídos após a conversão)
- `docs/edital/` — editais convertidos (fonte das trilhas)
- `docs/adr/`, `AGENTS.md`, `GLOSSARY.md`, `BACKLOG.md`, `PENDENCIAS.md` — decisões e pendências do projeto
- `design-system/` + `template-thin.html` + `build.py` — geração do template-base canônico
- `apply-*.py`, `tools/` — add-ons dos resumos (busca, revisão 🧠, marcação 🏷, PWA, prática 🎯) e validadores
- `.github/workflows/ci.yml` e `validate.yml` — build + gates (HTML, glossário, links) → deploy no Surge no merge na `main`

## Comandos essenciais
```bash
python build-search-index.py     # regenera Resumo_estudos/search-index.json (buscada do site)
python build-changelog.py        # regenera mudancas.html ("O que mudou")
python tools/check-html.py --dir Resumo_estudos --check   # gate de HTML do CI
python tools/check-links.py                             # gate de links (arquivos + âncoras)
python tools/check-glossary.py --all --strict           # vocab do GLOSSARY
```

Publicar é automático: **todo merge na `main` faz build e deploy no Surge** (secrets `SURGE_TOKEN`/`SURGE_DOMAIN` no Actions). Fallback manual: na máquina do usuário, `npx surge ./Resumo_estudos resumos-hermes.surge.sh` — ou rode o workflow de novo (*Actions → run → Re-run failed jobs*).

## Como estudar um resumo
Abra o arquivo da aula em `Resumo_estudos/<Matéria>/Aula NN/`. Use: sidebar de navegação e **busca por palavra** (Enter/Shift+Enter p/ navegar), **🧠 rever** (modo de revisão), **🏷 marcar** (grifar com persistência), **🎯 praticar** (quiz de recall com feedback imediato — `quiz.json` na pasta da aula), **🌙** tema escuro, **A−/A+** fonte, **↑** início. Cada aula tem ***Incidência de temas (TEC)*** para registrar recorrência de assuntos nas questões.

## Contribuir/estudar
Regras de conteúdo ("nada sem fonte"), fluxo `/nova-aula` e padrão visual estão em `AGENTS.md` e `docs/adr/` — leia antes de editar.
