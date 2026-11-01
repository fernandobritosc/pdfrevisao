# ADR-005: Deploy Surge a Cada Alteração (Independente de Git)

**Status**: Aceito
**Data**: 2026-08-23 (esclarecido 23/08/2026 após deploy esquecido)
**Autores**: Fernando Brito

## Contexto

Regra original: "Não commitar no decorrer da aula — acumular mudanças na working tree. Commitar e `git push origin main` SOMENTE quando o usuário encerrar a aula."

Problema: Deploy no Surge ficava preso ao commit. Se usuário esquecesse de commitar ao encerrar, deploy não acontecia (incidente 23/08/2026).

## Decisão

**Publicação no Surge é independente do git**:
- Deploy a **TODA alteração** (questão TEC colada, correção, novo resumo)
- Antes do deploy: `build-search-index.py` + `build-changelog.py` regenerados
- Após deploy: verificação HTTP 200
- Git: commit único de encerramento da aula (mudanças acumuladas na working tree)

Fluxo:
```
Alteração (TEC, correção, novo resumo)
    ↓
build-search-index.py
build-changelog.py
    ↓
npx surge "PDF Revisão\Resumo_estudos" resumos-hermes.surge.sh
    ↓
Verifica HTTP 200
    ↓
(Usuário encerra aula) → git add + commit + push
```

## Consequências

### Positivas
- **Confiabilidade**: Deploy nunca esquecido — acontece a cada alteração
- **Feedback imediato**: Usuário vê mudança online em segundos
- **Desacoplamento**: Git vira apenas histórico/backup; Surge é source of truth do conteúdo publicado

### Negativas / Riscos
- **Working tree suja**: Muitas alterações não commitadas durante aula (mitigado: `.gitignore` já exclui PDFs e .rar)
- **Histórico git menos granular**: Um commit por aula (aceitável: histórico de conteúdo está no changelog do Surge)

### Neutras
- Regra de "não commitar durante aula" mantida para git
- Surge continua servindo só `Resumo_estudos/` (nunca pasta raiz)

## Alternativas Consideradas

1. **Deploy atrelado ao commit** — Rejeitado: causou deploy esquecido
2. **Deploy automático via GitHub Actions** — Rejeitado: adiciona complexidade, Surge CLI já é simples
3. **Commit a cada alteração** — Rejeitado: viola regra do usuário (19/08/2026)

## Referências

- [Glossário: Deploy Surge, Pipeline de Build](./../../GLOSSARY.md)
- [AGENTS.md: Fluxo de trabalho (itens 5-6)](AGENTS.md#L60)
- Esclarecimento do usuário 23/08/2026 após deploy esquecido