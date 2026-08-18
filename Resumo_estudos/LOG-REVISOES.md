# LOG de Revisões — Resumo_estudos

Registro das alterações feitas nos resumos. Formato:

```
[DATA] <Arquivo>
  - <o que foi alterado> (seção / linha aproximada)
```

---

## 2026-08-17

**`Resumo_estudos` (geral) — redesign do front end (design system "caderno de um aprovado")**
- Aplicado novo visual em **54 arquivos HTML** (template-sumario, index raiz, 2 index de matéria e 50 resumos): bloco `<style>` substituído + link Google Fonts injetado no head de cada um.
- Novo design system (guia: skill frontend-design): papel quente `#F5F4F0` + tinta `#1F2733` + pauta `#E2DFD7`; cores de matéria preservadas (usadas inline nos cards).
- Tipografia: **Archivo** (títulos), **IBM Plex Sans** (corpo), **IBM Plex Mono** (rótulos, tags, números de seção).
- Assinatura: faixa de "capa de apostila" no topo da sidebar (gradiente das cores de matéria), `sec-num` como carimbo de tinta, sublinha dupla de pauta nos títulos de seção, cards com elevação sutil.
- A11y: `:focus-visible` e `prefers-reduced-motion`.
- Todas as classes/estrutura HTML preservadas (validação: `erros: []` em 54/54).
- Skills de apoio instaladas no projeto: `.opencode/skills/frontend-design/` e `.opencode/skills/canvas-design/`.

---

## 2026-08-17

**`Direito Administrativo/Aula 00/resumo-aula-00-principios-administrativos.html`** — revisão dirigida (DA M16.2)
- Questão TEC de impessoalidade processada (acerto): nome de prefeito em obra pública (parque público) viola a impessoalidade — promoção pessoal (CF, art. 37, § 1º); pegadinha: publicidade é distrator (nome em obra ≠ violação da publicidade; sindicabilidade ≠ impessoalidade).
- Tema já coberto (Situação 1 — parque com nome do prefeito; card TEC de promoção pessoal; sindicabilidade na seção dos princípios) — sem detalhe novo, bloco não reescrito.
- Incidência incrementada: Impessoalidade — promoção pessoal na publicidade (art. 37, § 1º): 1 → 2.
- HTML validado (`erros: []`); publicado no Surge.

---

## 2026-08-17

**`Resumo_estudos` (geral) — merge com origin/main (sincronização)**
- Remoto havia avançado com a revisão dirigida da análise de desempenho (12 commits, 17/08): Aula 00 DA regenerada no padrão atual (9 seções, LIMPE, implícitos, ~10 blocos TEC com incidências), index atualizado (idx11, seção "🎯 Revisão dirigida — análise de desempenho (17/08/2026)"), BACKLOG Item E reescrito como revisão dirigida.
- Merge resolvido: index.html manteve a versão do remoto (seção Revisão dirigida com links DA/DC/DPT/AP); resumo DA Aula 00 manteve a versão regenerada do remoto.
- Aprendizado local da questão FGV MPE GO 2022 (ADI 6522/DF — § 1º do art. 37 sem flexibilização por norma infraconstitucional/regulamentar) já era coberto parcialmente; adicionado apenas o **detalhe novo** da ADI 6522/DF (Info 1017) como complemento no card TEC de promoção pessoal (seção Impessoalidade) — incidência não duplicada (tema já contava 1).
- HTMLs validados (`erros: []`); push + Surge realizados.

---

## 2026-08-15

**`Direito Administrativo/Aula 00/resumo-aula-00-principios-administrativos.html`** — revisão da análise de desempenho (Item E do BACKLOG, M16.2)
- Questão TEC de impessoalidade processada (acerto), sem referência à questão/banca.
- Bloco de aprendizado adicionado na seção 3 (Impessoalidade) do resumo então vigente: publicidade oficial (art. 37, § 1º, CF) com caráter educativo/informativo/orientação social, vedada promoção pessoal; **STF ADI 6522/DF (Info 1017)** — § 1º do art. 37 não admite flexibilização por norma infraconstitucional/regulamentar; pegadinha: "flexibilização por lei federal"/"autonomia federativa" não justificam constitucionalidade.
- Texto do art. 37, § 1º conferido no material-fonte (`Aula 00 - Princípios Administrativos.md`, linhas 261-264/950-953).
- **Nota pós-merge (17/08)**: o resumo foi regenerado pelo remoto (9 seções) e o tema já estava coberto; o aprendizado da ADI 6522/DF foi mantido como detalhe novo no card TEC de promoção pessoal; incidência não duplicada.

---

## 2026-08-15

**`Português/Aula 05/resumo-aula-05-funcoes-sintaticas.html`** — AULA ENCERRADA
- **Aula encerrada em 15/08/2026 (20:36)** — usuário não concluiu o ciclo de questões (3 coladas, todas com resultado negativo); voltará à base das matérias anteriores antes de retomar.
- Aula 05 processada: 3 questões TEC integradas (sujeito posposto × complemento; "se" apassivador × reflexivo; locução adjetiva; aposto × CN; oração relativa; indefinido não indetermina) + incidência TEC com 10 temas.
- Push realizado (aula encerrada — regra do AGENTS.md).

---

## 2026-08-15

**`Português/Aula 05/resumo-aula-05-funcoes-sintaticas.html`** — 3ª questão TEC colada
- Questão CEBRASPE (sujeito posposto × complemento direto) processada, sem referência à questão/banca.
- Bloco novo na Seção 2: "Vigorava, portanto, a compreensão de que..." — sujeito posposto (ordem invertida), verbo intransitivo "vigorar" não pede complemento; método: identificar o sujeito ANTES do complemento ("o que é que vigorava?").
- Seção 3: linha nova na tabela (3ª pessoa do singular coloquial "Diz que..." = "dizem que") + bloco novo (pronome indefinido NÃO indetermina: "Alguém abriu a porta" = sujeito determinado simples).
- Incidência TEC: Identificação de funções sintáticas 3 (tag-red); novos temas Sujeito posposto × complemento e Indeterminado × pronome indefinido (1 cada).
- HTML validado (`erros: []`). Publicado no Surge (regra do usuário: publicar toda alteração).

---

## 2026-08-15

**`Português/Aula 05/resumo-aula-05-funcoes-sintaticas.html`** — 2ª questão TEC colada
- Questão CEBRASPE (sujeito paciente oracional × OD oracional) processada, sem referência à questão/banca.
- Bloco novo na Seção 2: "Estima-se que tenham sido gastos..." — oração "que" = sujeito paciente oracional (substantiva subjetiva), "se" apassivador (voz passiva sintética), verbo na 3ª pessoa do singular; sem "se" vira OD oracional com sujeito oculto; conversão à passiva analítica; pegadinha: "se" reflexivo (Deu-se o direito / Arrogou-se o poder) e "se" indeterminador (PIS) não são apassivadores.
- Incidência TEC: Identificação de funções sintáticas 2 (tag-red); novos temas Sujeito paciente oracional e "Se" apassivador × reflexivo (1 cada, tag-amber).
- HTML validado (`erros: []`). Commit local (push apenas no encerramento da aula).

---

## 2026-08-15

**`Português/Aula 05/resumo-aula-05-funcoes-sintaticas.html`** — 1ª questão TEC colada
- Questão FGV (identificação de funções sintáticas) processada; a banca deu letra C, mas o gabarito mais adequado é anulação (sem resposta certa). Conteúdo integrado, sem referência à questão/banca.
- Blocos de aprendizado nas seções temáticas: Seção 2 (núcleo do sujeito — "indicação"/"alunos" não são aposto nem advérbio), Seção 7 (locução adjetiva = função de adjetivo/adjunto adnominal), Seção 10 (aposto explicativo × complemento nominal: CN quase sempre preposicionado e dispensa vírgulas), Seção 11 (advérbio "rapidamente" × locução adjetiva "de mais qualidade"), Seção 13 (oração relativa = oração subordinada adjetiva).
- Incidência de temas (TEC) criada: Identificação de funções sintáticas 1 (tag-red); Aposto × CN, Locução adjetiva, Núcleo do sujeito, Oração relativa e Advérbio 1 cada (tag-amber).
- HTML validado (`erros: []`). Commit local (push apenas no encerramento da aula, regra do AGENTS.md).

---

## 2026-08-15

**`Português/Aula 04/resumo-aula-04-classe-palavras-verbos.html`** (nova aula)
- Ciclo `/nova-aula` completo: PDFs convertidos para .md e excluídos (completo, simplificado, mapa mental, marcação do aprovado); typo normalizado (`aula-04-Classe de palavras - verbos`).
- Resumo HTML criado com 16 seções no padrão do template (1 Verbo conceito/estrutura; 2 Conjugações e modelos; 3 Modo indicativo; 4 Modo subjuntivo; 5 Modo imperativo; 6 Formas nominais; 7 Tempos compostos; 8 Particípios; 9 Transitividade; 10 Classificação dos verbos; 11 Verbos que merecem atenção; 12 Correlação dos tempos verbais; 13 Locução verbal × tempo composto; 14 Vozes verbais; 15 Pontos que mais caem em prova; 16 Incidência de temas (TEC) — ordem padrão do Item A do BACKLOG).
- Conteúdo-chave: querer × requerer (requeIro/requeIra, não derivado de querer); pôr e derivados (puser/pusesse/pusera); imperativo duplo (dize/diz, faze/faz, traze/traz, requere/requer); defectivos (abolir, precaver, reaver, falir, adequar — só nós/vós no presente); NÃO defectivos (caber, valer, redimir, polir, sortir, rir, escapulir, entupir, sacudir); verbos vicários (ser/fazer + demonstrativo); correlações ("Se eu pudesse, viajaria"; "Se eu puder, viajarei"; "Caso eu possa, viajarei"); locução verbal × tempo composto; vozes (ativa/analítica/sintética, VTD+SE, impossibilidade de conversão, passiva × indeterminação, causativos); "Não se espera que..." = sujeito paciente; "trago"/"chego" não existem.
- HTML validado (`erros: []` / `restam abertos: []`); card Aula 04 adicionado na seção PT do `index.html`; título do índice para `?v=idx9`.

**`Português/Aula 05/resumo-aula-05-funcoes-sintaticas.html`** (nova aula)
- PDFs convertidos para .md e excluídos (completo, simplificado, marcação do aprovado).
- Resumo HTML criado com 15 seções (1 Ordem direta e oração; 2 Sujeito — tipos; 3 Indeterminação e oração sem sujeito; 4 Sujeito × referente; 5 Objeto direto; 6 Objeto indireto; 7 Complemento nominal × adjunto adnominal; 8 Predicativos; 9 Tipos de predicado; 10 Vocativo e aposto; 11 Adjunto adverbial; 12 Agente da passiva; 13 Frase × oração × período; 14 Pontos que mais caem em prova; 15 Incidência de temas — penúltima/última na ordem padrão).
- Conteúdo-chave: ordem direta SuVeCA; sujeito (simples/composto/oculto/oracional/paciente); pronome oblíquo como sujeito só com causativos/sensitivos (mandei-o sair, NÃO "mandei-lhe sair"); indeterminação (3ª plural, PIS com VTI/VI/VL, infinitivo impessoal); "trata-se de" sempre invariável; oração sem sujeito (haver impessoal contamina a locução); sujeito × referente ("Disseram que..." = oculto, não indeterminado); OD (pleonástico, interno, preposicionado — "a todos" é OD, não OI); CN × AA (sentido agente × paciente, substituição por adjetivo); predicativo × adjunto (teste da pronominalização do OD); tipos de predicado; aposto especificativo ("praia da Pipa") × adjunto; agente da passiva ("por/pelo/de"); frase × oração × período.
- HTML validado (`erros: []` / `restam abertos: []`); card Aula 05 adicionado na seção PT do `index.html`.

---

## 2026-08-15

**`Direito Processual do Trabalho/Aula 03/resumo-aula-03-prazos-custas-nulidades-peticao-inicial.html`**
- Sessão TEC processada (~26 questões, FCC/CEBRASPE/AOCP 2018-2024, com 1 anulada), bloco a bloco, integradas nas Seções 1-5.
- Regras do usuário persistidas (15/08/2026) no AGENTS.md e na skill nova-aula: **rótulo único** (📌 Aprendizado só na 1ª linha; assuntos seguintes com `→ <strong>Nome:</strong>`) e **espaçamento `<br><br>`** entre parágrafos/assuntos (nunca `<br>` simples).
- Conteúdo novo integrado: início do prazo no processo eletrônico (Lei 11.419/06, art. 4º, §§3º-4º); suspensão × interrupção; reinício em dia não útil (21/01 domingo → 22/01, sem devolução de dias); ato publicado no recesso não inicia prazo; férias coletivas dos Ministros do TST suspendem prazos recursais (art. 177, §1º, RITST + Súmula 262, II); mandados só após 07/01; bizu "diferença de dias ÷ 7" para dia da semana; NCPC 212 §2º e art. 190 CPC (negociação processual) inaplicáveis à JT (art. 2º, II, IN 39/16); prorrogação de prazos (art. 775, §1º); certificação do vencimento (art. 776) — card novo; prazo em dobro inaplicável (OJ 310, SDI-I) + quem tem dobro (DL 779/69 e MPT) — card novo; notificação postal (art. 841, §1º + Súmula 16, TST + art. 774, p.ú.) — card novo; edital na execução (art. 880, §3º: 2x em 48h, edital 5 dias); CNPJ/CPF não obrigatório na qualificação; nulidades: incompetência de matéria ex officio (art. 64, §1º, CPC), pré-questionamento (OJ 62, SDI-I), prejuízo processual do art. 794; CCP: reforma NÃO alterou, estabilidade altruísta, comissão 510-A (empresa, +200 empregados).
- Quebras de linhas amontoadas com `→` + `<br><br>`: pegadinha CCP (4 assuntos), estabilidade (3), suspensão × interrupção (2), intimação eletrônica (3), efeito de cada grau (3).
- Auditoria (a pedido do usuário): HTML validado (`erros: []`); dispositivos legais conferidos no material-fonte (arts. 770, 773, 775, 775-A, 786, 789, 794-798, 813, 840, 850, 852-B, 895, 222 CPC, 731 e 833 CLT); âncoras das 7 seções íntegras; removidas 5 referências a banca ("FCC") dos blocos de conteúdo; quebrada linha longa de intimação eletrônica.
- Seção 7 "Incidência de temas (TEC)" arrumada: ordem decrescente de incidência, tag-red para 5+ (Suspensão 9, Atos processuais 7, CCP 5), nome completo da CCP (arts. 625-A a 625-H) e legenda de critério.
- **Aula encerrada em 15/08/2026** — meta nº7 do plano (DPT — Prazos processuais, exercícios) concluída.

---

## 2026-08-15

**`Administração Pública e Geral/Aula 05/resumo-aula-05-lideranca.html`**
- Sessões TEC de "Direção. Liderança" processadas (2 levadas: CNJ 29 questões — 22 acertos/7 erros — e
  leva TEC de liderança com ~30 questões coladas, bloco a bloco).
- **Normalização da aula**: removida a seção "Questões Comentadas" (20 questões + gabaritos, 7 fora do
  tema — estruturas organizacionais); corrigido link morto `#sec11` na sidebar; subtítulo da Seção 10
  corrigido; 30 marcadores `•` → `→` (enumerações verticalizadas, regra do AGENTS.md).
- Seção 11 "Incidência de temas (TEC)" criada e depois renumerada para Seção 12 quando a Seção 11
  "Gestão de Conflitos — Chiavenato" foi criada (5 estilos × assertividade/cooperação, segregação de
  funções, negociação distributiva × integrativa (Robbins), tipos de conflito, mediação × conciliação).
- Conteúdo novo integrado: dicas e bizus (4 enfoques Chiavenato, autêntica/servidora/LMX); Caminho-Meta
  (combinações contingenciais FGV); Hersey e Blanchard (coluna Exemplo M1-M4 × E1-E4, lógica da curva,
  pegadinha M3, callout "Não confunda os modelos" H&B × Fiedler); Grid (coordenadas, nomes alternativos,
  quadro "Identifique a teoria pelo termo-chave"); Vergara; Teorias X/Y (McGregor) × Barnard (4 condições);
  líder inspirador; definição FCC de liderança comportamental; pegadinhas (poder × reação, transacional
  curto prazo, laissez-faire × equipes multiprofissionais, negociação distributiva com recursos fixos e
  mediador).
- Seção 12 (Incidência TEC) reestruturada em 3 blocos de prioridade: 🔴 alta (Hersey e Blanchard 6,
  Transacional 5, Gestão de conflitos 5) · 🟠 média (mediação × conciliação 2, negociação 2, teorias
  comportamentais 2, Grid 2) · 🟡 baixa (8 temas com 1).
- **Aula encerrada em 15/08/2026** — meta nº4 do plano (AP — Direção. Liderança, exercícios) concluída.

---

## 2026-08-14

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Sessão TEC (11 questões): blocos/cards novos — locação de imóveis (arts. 2º, III; 51; 74, V);
  instrumento de contrato facultativo e contrato verbal (art. 95, Decreto 12.343/2024);
  meios alternativos de resolução de controvérsias (arts. 151-154); PMI (art. 81);
  detalhes dos critérios de julgamento (arts. 34-35); detalhes de impugnação/linhas de defesa
  (arts. 164, parágrafo único; 169, § 3º, I; 171, § 1º); saneamento × anulação, convalidação e
  LINDB (arts. 71, 165, § 3º e 5º); competência exclusiva da inidoneidade (art. 156, § 6º, I).
- **Correção crítica**: efeito suspensivo de recurso e pedido de reconsideração — material dizia
  que não havia; o art. 168 manda o contrário (ambos têm efeito suspensivo). Corrigido no card de
  recursos, na dica de prova e no resumo legado `aula 07/resumo-aula-07.html`.
- Cards reforçados (tema fraco no TEC): formalização dos contratos (arts. 89-94);
  alienação de bens (arts. 76-77); duração/vigência ampliada (arts. 105-114).
- Seção 8 "Pontos que mais caem em prova" atualizada com os aprendizados da sessão.
- Incidências: matriz de riscos 3x (🔴); serviços dedicação exclusiva 3x (🔴); linhas de defesa 2x;
  revogação/anulação 2x; diálogo competitivo 2x; credenciamento/pré-qualificação 2x; + novas tags
  (locação, art. 95, controvérsias, PMI, critérios de julgamento, formalização, alienação, recursos 165-168).
- **Aula encerrada em 14/08/2026.**

---

## 2026-08-09

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Removida a seção 4 "Questões comentadas" (18 questões) — resumos não devem conter questões.
- Removida a seção 5 "Gabarito final" (tabela) — usuário resolve questões no TEC.
- Renumeradas as seções: "Pontos que mais caem em prova" virou seção 4 (sidebar atualizada).
- Adicionada a seção 5 "Incidência de temas (TEC)" com contador por tema.
- Adicionada subseção "Formas de execução indireta — empreitadas (art. 46)" na seção 3
  (conteúdo convertido a partir de questão do TEC: empreitada por preço global, art. 6º, XXIX).
- Contador de incidência: Empreitada por preço global = 1.

---

## 2026-08-09

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 2 (Âmbito de aplicação): adicionado card "Recursos de organismos internacionais (art. 1º, § 3º)"
  com conteúdo de estudo (aprendizado + base legal + 3 alíneas) convertido de questão do TEC.
- Corrigida imprecisão no callout "Não se aplica (em regra)": removida a menção a "recursos de
  agências internacionais (regras próprias)" — na verdade a lei se aplica, apenas admite condições
  peculiares do organismo (art. 1º, § 3º).
- Seção 5 (Incidência de temas): novo contador "Recursos de organismos internacionais: 1".

---

## 2026-08-09

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Princípios, objetivos e regras técnicas): adicionada subseção
  "Serviços contínuos com dedicação exclusiva de mão de obra (art. 6º, XVI)"
  com conteúdo de estudo (aprendizado + base legal das alíneas a/b/c) convertido
  de questão do TEC (TSE 2024). Tema era novo no resumo.
- Seção 5 (Incidência de temas): novo contador "Serviços com dedicação exclusiva de mão de obra: 1".
- Seção 3 (subseção "Serviços contínuos com dedicação exclusiva de mão de obra"): adicionado
  callout-info com exemplo prático (porteiro não pode atuar em dois órgãos simultaneamente),
  fornecido pelo usuário como complemento didático da questão TSE 2024.
- Seção 5 (Incidência de temas): "Serviços com dedicação exclusiva de mão de obra" incrementado
  para 2 (nova questão TSE 2024, art. 6º, XVI, "a" — alínea já coberta; nenhum detalhe novo
  adicionado ao conteúdo).

---

## 2026-08-09

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3: adicionada subseção "Agentes públicos — requisitos e vedações (art. 7º)"
  com conteúdo de estudo convertido de questão do TEC (TSE 2024): vedações de parentesco
  até o 3º grau (art. 7º, III), requisitos I e II, e pegadinha (primos = 4º grau não vedam).
- Seção 5 (Incidência de temas): novo contador "Requisitos e vedações dos agentes (art. 7º): 1".

---

## 2026-08-09

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 5 (Incidência de temas): novo contador "Diálogo competitivo: 1". Tema já coberto
  na seção 3 (definição art. 6º, XLII + etapas art. 32); nenhum detalhe novo adicionado.

---

## 2026-08-09

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (subseção "Segregação de funções"): corrigida a base legal de "art. 8º" para
  "art. 7º, § 1º" (fundamento principal do princípio), com destaque para o detalhe novo da
  questão FCC TRT-20 (2024): vedação de designação do mesmo agente para funções suscetíveis
  a risco, reduzindo ocultação de erros e fraudes.
- Seção 5 (Incidência de temas): novo contador "Segregação de funções: 1".

---

## 2026-08-09

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (subseção "Modalidades (art. 28)"): adicionado callout-info "Leilão — procedimento
  simplificado (art. 31, § 4º)" com conteúdo de estudo convertido de questão do TEC (TSE 2024):
  sem registro cadastral prévio, sem fase de habilitação, homologação após lances + fase recursal
  + pagamento.
- Seção 5 (Incidência de temas): novo contador "Leilão: 1".

---

---

---

## 2026-08-09

**`Direito Administrativo/Aula 06/resumo-aula-06-atos-administrativos.html`** (novo)
- Criado resumo da Aula 06 (Atos Administrativos) no padrão do template-sumario, seguindo o modelo da Aula 07.
- Seções: 1) Conceito e conceitos relacionados; 2) Atributos (PATI); 3) Elementos (COM FIFORMOOB);
  4) Vícios; 5) Mérito; 6) Classificação; 7) Espécies; 8) Extinção; 9) Convalidação;
  10) Pontos que mais caem em prova; 11) Incidência de temas (TEC) — vazia (nenhuma questão colada).
- Conteúdo extraído do simplificado/resumo/mapa mental (Estratégia Concursos, Herbert Almeida).
- Incluídas pegadinhas com base nas questões comentadas da própria aula: presunção de veracidade ×
  inversão do ônus da prova (Cebraspe/EMBRAPA 2025), silêncio discricionário sob controle judicial,
  vício de objeto em licença a servidor falecido, ato de colegiado = simples, certidão não revogável,
  visto = legitimidade formal, ordinatórios = poder hierárquico, ausência de motivação = vício de forma.

**`Resumo_estudos/index.html`**
- Card da Aula 06 (Direito Administrativo) atualizado de "Em breve" para link ativo
  `Direito Administrativo/Aula 06/resumo-aula-06-atos-administrativos.html`.

---

## 2026-08-09

**`Direito Administrativo/Aula 02/resumo-aula-02-organizacao-administrativa.html`** (novo)
- Criado resumo da Aula 02 (Organização Administrativa) no padrão do template-sumario, seguindo o modelo das Aulas 06/07.
- Seções: 1) Conceito de organização administrativa; 2) Centralização × Descentralização · Concentração ×
  Desconcentração; 3) Administração direta × indireta; 4) Autarquias, agências reguladoras e executivas;
  5) Órgãos públicos; 6) Hierarquia × vinculação; 7) Pontos que mais caem em prova; 8) Incidência de temas (TEC) — vazia.
- Conteúdo extraído do simplificado + completo (Estratégia Concursos, Herbert Almeida).
- Incluídas pegadinhas com base nas questões comentadas da própria aula: outorga × delegação (transferência de
  titularidade), desconcentração = mesma pessoa jurídica, administração direta = centralizada / indireta =
  descentralizada, criação de autarquia só por lei específica (art. 37, XIX), extinção de estatais por autorização
  genérica (ADI 6241), órgãos sem personalidade jurídica (Súmula 525/STJ), agências reguladoras = autarquias de
  regime especial da admin. indireta, agência executiva qualificada por decreto, vinculação (não subordinação),
  conselhos profissionais prestam contas ao TCU e OAB fora da Administração.

**`Resumo_estudos/index.html`**
- Adicionado card "Aula 02 — Organização Administrativa" (Direito Administrativo) com link ativo
  `Direito Administrativo/Aula 02/resumo-aula-02-organizacao-administrativa.html`.

---

## 2026-08-09

**`Direito Administrativo/Aula 00/resumo-aula-00-principios-administrativos.html`** (novo)
- Criado resumo da Aula 00 (Princípios Administrativos + Origem/Conceito/Fontes) no padrão do template-sumario.
- Seções: 1) Origem, conceito e fontes; 2) Regime Jurídico Administrativo; 3) Princípios explícitos (L.I.M.P.E.);
  4) Demais princípios (implícitos); 5) Pontos que mais caem em prova; 6) Incidência de temas (TEC) — vazia.
- Conteúdo extraído do "Aula 00 - Princípios Administrativos.md" + "TEC Concursos - Origem, Conceito e Fontes".
- Incluídos mnemônicos (L.I.M.P.E.), tabelas comparativas, callouts e gotchas (nepotismo/SV 13, Súmulas 346 e 473 STF).

**`Direito Administrativo/Aula 01/resumo-aula-01-estado-governo-e-administracao-publica.html`** (novo)
- Criado resumo da Aula 01 (Estado, Governo e Administração Pública + Regime Jurídico Administrativo).
- Seções: 1) Estado, governo e Adm. Pública; 2) Elementos/estrutura do Estado; 3) Adm. Pública (sentidos);
  4) Regime Jurídico Administrativo; 5) Pontos que mais caem; 6) Incidência de temas (TEC) — vazia.
- Conteúdo extraído do "Aula 01 - ... simplificado.md" + "Aula01 - O Regime Jurídico Administrativo.md".

**`Direito Administrativo/Aula 03/resumo-aula-03-fundacoes-empresas-publicas-sociedades-de-economia-mista.html`** (novo)
- Criado resumo da Aula 03 (Fundações públicas, Empresas públicas e Sociedades de economia mista).
- Seções: 1) Considerações gerais da adm. indireta; 2) Fundações públicas; 3) Empresas públicas;
  4) Sociedades de economia mista; 5) Quadro comparativo EP × SEM × Fundação; 6) Pontos que mais caem;
  7) Incidência de temas (TEC) — vazia.
- Conteúdo extraído do simplificado + completo (Lei 13.303/2016).

**`Direito Administrativo/Aula 04/resumo-aula-04-paraestatais-e-terceiro-setor.html`** (novo)
- Criado resumo da Aula 04 (Entidades paraestatais e terceiro setor).
- Seções: 1) Conceito de paraestatais/terceiro setor; 2) Sistema S; 3) Organizações Sociais;
  4) OSCIP; 5) Marco Regulatório OSC (Lei 13.019/2014); 6) Quadro comparativo; 7) Pontos que mais caem;
  8) Incidência de temas (TEC) — vazia.
- Conteúdo extraído do simplificado + mapa mental + completo.

**`Direito Administrativo/Aula 05/resumo-aula-05-poderes-e-deveres-da-administracao.html`** (novo)
- Criado resumo da Aula 05 (Poderes e Deveres da Administração Pública).
- Seções: 1) Uso e abuso de poder; 2) Vinculado × discricionário; 3) Poder hierárquico; 4) Poder disciplinar;
  5) Poder regulamentar; 6) Poder de polícia; 7) Deveres do administrador; 8) Pontos que mais caem;
  9) Incidência de temas (TEC) — vazia.
- Conteúdo extraído do simplificado + mapa mental + completo (inclui Tema 532 STF sobre delegação do poder de polícia).

**`Resumo_estudos/index.html`**
- Reorganizada a seção "AD — Direito Administrativo": adicionados cards ativos das Aulas 00, 01, 03, 04 e 05
  (Aulas 02, 06 e 07 já existentes), todos em ordem 00–07. Título do índice atualizado para `?v=idx7`.

---

## 2026-08-09

**`AFO/Aula 00/resumo-aula-00-orcamento-publico.html`** (novo)
- Criado resumo da Aula 00 (Orçamento Público). Seções: 1) Conceito; 2) Visão da doutrina (Giacomoni);
  3) Normas gerais de direito financeiro (Lei 4.320/64); 4) Atividade financeira do Estado (PPA/LDO/LOA);
  5) Pontos que mais caem; 6) Incidência de temas (TEC) — vazia. Fonte: simplificado + completo.

**`Direito Constitucional/Aula 00/resumo-aula-00-natureza-conceito-interpretacao.html`** (novo)
- Criado resumo (Natureza, Conceito e Interpretação). 6 seções, incluindo sentidos de Constituição
  (Lassalle, Schmitt, Kelsen, Hesse), métodos e princípios de interpretação. Fontes: 4 arquivos da Aula 00 (DC).

**`Direito Constitucional/Aula 02/resumo-aula-02-direitos-e-deveres-art5.html`** (novo)
- Criado resumo (Direitos e Deveres — art. 5º). 7 seções, com SV e Temas de repercussão geral citados nas fontes.

**`Direito Constitucional/Aula 03/resumo-aula-03-direitos-e-deveres-individuais-coletivos.html`** (novo)
- Criado resumo (Direitos Individuais e Coletivos). 8 seções, incisos XXXII–LXXIX do art. 5º + remédios constitucionais.

**`Direito Constitucional/Aula 04/resumo-aula-04-direitos-sociais.html`** (novo)
- Criado resumo (Direitos Sociais). 7 seções: art. 6º (ECs 26, 64, 90, 114), art. 7º em tabela, urbanos/rurais/domésticos, arts. 8º-11.

**`Direito Constitucional/Aula 05/resumo-aula-05-nacionalidade.html`** (novo)
- Criado resumo (Nacionalidade). 8 seções: natos e naturalizados, quase-nacionalidade, cargos privativos, perda/reaquisição (EC 131/2023).

**`Direito do Trabalho/Aula 00/resumo-aula-00-relacoes-de-trabalho-e-emprego.html`** (novo)
- Criado resumo (Relações de Trabalho e Emprego). 6 seções. Fonte: simplificado (meta 03).

**`Direito do Trabalho/Aula 01/resumo-aula-01-principios-do-direito-do-trabalho.html`** (novo)
- Criado resumo (Princípios do DT). 9 seções, incluindo subprincípios de Plá Rodriguez, Súmula 212 TST, art. 468 CLT.

**`Direito do Trabalho/Aula 02/resumo-aula-02-relacoes-de-trabalho-e-emprego.html`** (novo)
- Criado resumo (Relações de Trabalho e Emprego — aprofundado). 7 seções: grupo econômico, sucessão, responsabilidade, poderes do empregador.

**`Direito do Trabalho/Aula 03/resumo-aula-03-contrato-de-trabalho.html`** (novo)
- Criado resumo (Contrato de Trabalho). 9 seções: características (PISTACO), elementos, duração, alteração, interrupção × suspensão, contratos especiais.

**`Direito do Trabalho/Aula 04/resumo-aula-04-termino-do-contrato-de-trabalho.html`** (novo)
- Criado resumo (Término do Contrato). 9 seções: formas de extinção, justa causa (art. 482), 484-A, aviso prévio proporcional, verbas rescisórias.

**`Direito Processual do Trabalho/Aula 00/resumo-aula-00-processo-do-trabalho.html`** (novo)
- Criado resumo (Introdução ao DPT). 8 seções. Arquivo renomeado (nome inicial continha typo "diretto").

**`Direito Processual do Trabalho/Aula 01/resumo-aula-01-competencia-da-justica-do-trabalho.html`** (novo)
- Criado resumo (Competência da JT). 7 seções, art. 114 CF + repercussão geral (994, 544, 1143, 36, 74).

**`Direito Processual do Trabalho/Aula 02/resumo-aula-02-servicos-auxiliares-da-justica-do-trabalho.html`** (novo)
- Criado resumo (Serviços Auxiliares da JT). 7 seções (arts. 710-721 CLT). Seção de peritos/depositário marcada como não tratada nas fontes.

**`Direito Processual do Trabalho/Aula 03/resumo-aula-03-prazos-custas-nulidades-peticao-inicial.html`** (novo)
- Criado resumo (Prazos, Custas, Nulidades e Petição Inicial). 6 seções (arts. 770, 789, 794-798, 840 CLT).

**`Informática/Aula 00/resumo-aula-00-conceitos-basicos-de-redes.html`** (novo)
- Criado resumo (Conceitos Básicos de Redes). 6 seções: classificação PAN/LAN/MAN/WAN, topologias, arquiteturas, meios guiados × não-guiados.

**`Informática/Aula 01/resumo-aula-01-protocolos-de-comunicacao.html`** (novo)
- Criado resumo (Protocolos de Comunicação). 8 seções: OSI, TCP/IP, protocolos de rede/transporte/aplicação, portas padrão com faixas de incidência.

**`Informática/Aula 02/resumo-aula-02-sitios-de-busca-e-pesquisa.html`** (novo)
- Criado resumo (Sítios de Busca e Pesquisa). 6 seções: buscadores, indexação, 16 operadores de pesquisa em tabela, PageRank/SEO.

**`Informática/Aula 03/resumo-aula-03-computacao-em-nuvem.html`** (novo)
- Criado resumo (Computação em Nuvem). 7 seções: características essenciais (MEARA), IaaS/PaaS/SaaS, modelos de implantação, armazenamento e colaboração.

**`Informática/Aula 04/resumo-aula-04-redes-sociais.html`** (novo)
- Criado resumo (Redes Sociais). 6 seções: plataformas em tabelas, uso administrativo (LAI/transparência), verificação 2 fatores, Notas da Comunidade.

**`Informática/Aula 05/resumo-aula-05-internet-e-navegacao.html`** (novo)
- Criado resumo (Internet e Navegação). 7 seções: navegadores, interface, abas/favoritos/histórico, cookies/cache, segurança e atalhos.

**`Resumo_estudos/index.html`**
- Adicionados cards ativos: AFO Aula 00; Direito Constitucional Aulas 00, 02, 03, 04, 05;
  Direito do Trabalho Aulas 00-04; Direito Processual do Trabalho Aulas 00-03;
  Informática Aulas 00-05; Português Aula 03 (link que estava "Em breve"). Título atualizado para `?v=idx8`.

---

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Modalidades — art. 28): adicionado card "Pregão e serviços comuns de engenharia"
  convertido de questão do TEC (FCC 2024 — TRT-20): pregão obrigatório para bens/serviços comuns
  (art. 6º, XLI) e facultativo para serviços comuns de engenharia (art. 29, parágrafo único);
  conceito de serviço comum (art. 6º, XXI, "a") e especial (alínea "b"); Súmula 257-TCU;
  pegadinhas (projeto de engenharia não afasta pregão; obras não admitem pregão, mas serviços
  comuns admitem; modalidade definida pela natureza do objeto, não por alçada de valor).
- Seção 3 (Modalidades — art. 28): adicionado card "Controle dos Tribunais de Contas e impugnação"
  convertido da mesma questão: impugnação ao edital até 3 dias úteis antes da abertura (art. 164);
  recursos e pedido de reconsideração (art. 165); TC fiscaliza todas as fases e integra a 3ª linha
  de defesa (art. 169, III e § 4º); pegadinha (impugnação ao pregoeiro não exclui o TC).
- Seção 5 (Incidência de temas): novos contadores "Pregão e serviços comuns de engenharia: 1"
  e "Controle do TC e impugnação ao edital: 1".

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Modalidades — art. 28): callout "Leilão" complementado com detalhes novos de questão
  do TEC (FCC 2024 — TRT-20): leilão pode ser cometido a leiloeiro oficial ou servidor designado
  (art. 31, caput) e edital pode ser divulgado por outros meios para ampliar publicidade (art. 31,
  § 3º). Base legal já coberta (art. 31, § 4º) mantida.
- Seção 5 (Incidência de temas): "Leilão" incrementado para 2.

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (adjudicação compulsória): adicionado card "Revogação e anulação após as fases de
  julgamento e habilitação (art. 71)" convertido de questão do TEC (TSE): autoridade superior pode
  revogar por conveniência e oportunidade mesmo após julgamento/habilitação + recursos exauridos
  (art. 71, II), retorno dos autos para saneamento (I), anulação por ilegalidade insanável (III),
  adjudicar/homologar (IV); § 2º fato superveniente comprovado; § 3º prévia manifestação dos
  interessados; STJ MS 4.513/DF (adjudicação = mera expectativa de direito).
- Seção 5 (Incidência de temas): novo contador "Revogação e anulação do certame (art. 71): 1".

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Fases do procedimento): adicionado card "Prazos mínimos para apresentação de propostas
  e lances (art. 55)" convertido de questão do TEC (TRT-20): prazos dependem do tipo de objeto e
  do critério de julgamento, não da modalidade; tabela completa (bens 8/15; serviços e obras comuns
  10; especiais 25; contratação integrada 60; semi-integrada 35; maior lance 15; técnica e preço 35);
  pegadinha (contratação integrada = 60 dias úteis).
- Seção 5 (Incidência de temas): novo contador "Prazos mínimos de propostas (art. 55): 1".

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Contratação direta): adicionado card "Inexigibilidade por fornecedor exclusivo
  (art. 74, I e § 1º)" convertido de questão do TEC (TRF-6): demonstração da inviabilidade de
  competição por atestado/contrato de exclusividade, declaração do fabricante ou outro documento
  idôneo; vedada a preferência por marca específica.
- Seção 5 (Incidência de temas): novo contador "Inexigibilidade por fornecedor exclusivo (art. 74, I): 1".

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Contratação direta): adicionado gotcha "Art. 72, I: atenção à lista dupla" com detalhe
  de questão do TEC (TRT-20): art. 72, I exige ETP e análise de riscos; matriz de repartição de
  riscos NÃO consta do art. 72 (pertence à contratação integrada/semi-integrada — arts. 22 e 46).
  (Removida menção à duplicidade de gabarito/anulação a pedido do usuário.)
- Seção 5 (Incidência de temas): novo contador "Contratação direta — documentos (art. 72): 1".

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Procedimentos auxiliares): adicionado card "Registro de preços e critério de julgamento
  (art. 82, V)" convertido de questão do TEC (CEBRASPE/TRF-6 2025): SRP = concorrência ou pregão
  com critério menor preço ou maior desconto; maior retorno econômico é exclusivo de contrato de
  eficiência (art. 39).
- Seção 5 (Incidência de temas): novo contador "Registro de preços — critério de julgamento (art. 82, V): 1".

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Procedimentos auxiliares): adicionado card "Credenciamento × pré-qualificação
  (art. 6º, XLIII e XLIV; art. 79)" convertido de questão do TEC (CEBRASPE/TRF-6 2025): distinção
  dos conceitos (descrição de "procedimento seletivo prévio à licitação" = pré-qualificação) e
  hipóteses do credenciamento (paralela e não excludente, seleção a critério de terceiros,
  mercados fluidos).
- Seção 5 (Incidência de temas): novo contador "Credenciamento e pré-qualificação (art. 6º, XLIII/XLIV): 1".

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Prorrogação, alteração e execução contratual): adicionado card "Vigência dos contratos —
  regras especiais (arts. 107-114)" convertido de questão do TEC (FCC 2024 — TRT-20): prorrogação
  sucessiva de contínuos (art. 107, teto decenal), prazo indeterminado só em monopólio (art. 109),
  35 anos em contratos com investimento (art. 110, II), 15 anos em sistemas estruturantes de TI
  (art. 114), 1 ano em emergência/calamidade com vedação à prorrogação e recontratação (art. 75,
  VIII; ADI 6890). Art. 111 (escopo) já coberto.
- Seção 5 (Incidência de temas): novo contador "Vigência dos contratos (arts. 107-114): 1".

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Serviços contínuos com dedicação exclusiva de mão de obra): adicionado card
  "Asseguração de obrigações trabalhistas (art. 121, § 3º)" convertido de questão do TEC (TSE):
  medidas I a V (caução/fiança/seguro-garantia, condicionar pagamento à quitação, depósito em
  conta vinculada, pagamento direto de verbas em inadimplemento, pagamento por fato gerador);
  pegadinha (conta vinculada É instrumento próprio).
- Seção 5 (Incidência de temas): "Serviços com dedicação exclusiva de mão de obra" incrementado
  para 3.

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 5 (Incidência de temas): novo contador "Preposto na execução (art. 118): 1". Conteúdo
  (preposto aceito pela Administração no local da obra/serviço) já coberto no card de Execução;
  questão do TEC não trouxe detalhe novo.
- Removidas referências de banca/prova dos títulos dos cards (a pedido do usuário).
- Contador de temas reorganizado em ordem decrescente de incidência; cor vermelha (🔴) apenas
  para temas com maior incidência.

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Alteração contratual — arts. 124-130): reforçado bullet da transfiguração do objeto
  (art. 126) com detalhe de questão do TEC (CEBRASPE/TRF-6 2025): vedação vale em qualquer caso,
  inclusive alterações consensuais, sob pena de burla à licitação (TCU).
- Seção 5 (Incidência de temas): novo contador "Alteração contratual — transfiguração do objeto (art. 126): 1".

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 5 (Incidência de temas): novo contador "Alteração contratual — unilateral e consensual
  (art. 124): 1". Conteúdo (art. 124, I unilateral / II por acordo) já coberto no card de Alteração
  contratual; questão do TRF-6 não trouxe detalhe novo.

## 2026-08-10

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Prorrogação, alteração e execução contratual): adicionado card "Formalização do termo
  aditivo (art. 132)" convertido de questão do TEC (TRF-6): formalização é condição para a execução,
  exceto em justificada necessidade de antecipação de efeitos (formalização em até 1 mês).
- Seção 5 (Incidência de temas): novo contador "Formalização do termo aditivo (art. 132): 1".

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Alteração contratual): adicionado card "Apostila — registros que não caracterizam alteração
  (art. 136)" convertido de questão do TEC (CEBRASPE/TSE 2024): apostila dispensa termo aditivo nas
  hipóteses I a IV (reajuste/repactuação, atualizações/penalizações, alteração de razão/denominação
  social, empenho de dotações orçamentárias).
- Seção 5 (Incidência de temas): novo contador "Apostila (art. 136): 1".

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Execução contratual): adicionado card "Garantias contratuais (arts. 96-98 e 137, § 4º)"
  convertido de questão do TEC (TSE): modalidades (caução, seguro-garantia, fiança bancária, título de
  capitalização); escolha da modalidade é do contratado; garantia depende de previsão no edital;
  emitentes devem ser notificados do início de processo de apuração de descumprimento (art. 137, § 4º).
- Seção 5 (Incidência de temas): novo contador "Garantias contratuais (arts. 96-98 e 137, § 4º): 1".

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Execução contratual): adicionado card "Recebimento do objeto (art. 140)" convertido de
  questão do TEC (CEBRASPE/TSE 2024): obras/serviços recebidos provisoriamente mediante termo detalhado
  (cumpridas exigências técnicas); compras recebidas provisoriamente de forma sumária; definitivo por
  servidor/comissão com termo detalhado; prazos/métodos definidos em regulamento ou contrato.
- Seção 5 (Incidência de temas): novo contador "Recebimento do objeto (art. 140): 1".

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Sanções): adicionado card "Reabilitação do licitante/contratado (art. 163)" convertido de
  questão do TEC (CEBRASPE/TSE 2024): 5 requisitos cumulativos (reparação integral do dano, pagamento
  da multa, prazo mínimo de 1 ano no impedimento/3 anos na inidoneidade, condições do ato punitivo,
  análise jurídica prévia); pegadinha: só dano+multa não bastam.
- Seção 5 (Incidência de temas): novo contador "Reabilitação (art. 163): 1".

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção 3 (Sanções): adicionado card "Dosimetria das sanções (art. 156, § 1º)" convertido de questão
  do TEC (CEBRASPE/TSE 2024): 5 critérios (natureza/gravidade, peculiaridades do caso concreto,
  agravantes/atenuantes, danos à Administração, programa de integridade); pegadinha: a lista completa
  vai além dos 3 fatores citados na assertiva.
- Seção 5 (Incidência de temas): novo contador "Dosimetria das sanções (art. 156, § 1º): 1".

**`Direito Administrativo/Aula 07/resumo-aula-07-licitacoes-publicas.html`**
- Seção (Controle): complementado o card "Controle dos Tribunais de Contas e impugnação" com as linhas
  de defesa do art. 169 (1ª: servidores/empregados públicos, agentes de licitação e autoridades da
  governança; 2ª: assessoramento jurídico e controle interno; 3ª: órgão central de controle interno e
  TC) e pegadinha de que o Poder Judiciário NÃO integra linha de defesa. Questão do TEC (TRF-6).
- Seção 5 (Incidência de temas): novo contador "Linhas de defesa das contratações (art. 169): 1".

## 2026-08-10

**`Resumo_estudos/**` (todos os 48 arquivos HTML)**
- Conversão do tema escuro para **tema claro** (readability/palette clara).
- Cada arquivo recebeu um **CSS claro canônico** (união de todos os seletores do site) no bloco
  `<style>`, idempotente. Palette: `--bg:#f4f7fb`, `--sidebar:#e2e8f0`, `--card:#ffffff`,
  `--border:#cbd5e1`, `--text:#1e293b`, `--blue:#2563eb`, `--amber:#d97706`, `--green:#059669`,
  `--red:#dc2626`, `--purple:#7c3aed`, `--teal:#0d9488`.
- `<body>` recebeu classe `aula` (45 páginas com sidebar) ou `landing` (3 índices) para layout.
- Corrigidos blocos `<style>` corrompidos por dupla execução do script de mapeamento (tags com
  `background == color`, `--card`/`--text` invertidos, etc.).
- Reparados 2 arquivos com `<title>`/`<style>` quebrados: `Administração Pública e Geral/index.html`
  e `Administração Pública e Geral/Aula 03/resumo-aula-03-ferramentas-estrategicas.html`.
- Corrigidos back-links inline escuros em `Português/Aula 02` e `Aula 03`
  (`background:#1e293b;color:#f4f7fb` → `background:#e2e8f0;color:#0f172a`).
- Mnemônicos, callouts, tags, tabelas, gotchas, legal-blocks e questionários convertidos para claro.
- UTF-8 sem BOM preservado; estrutura de seções/sidebar intacta.

---

**Criado por:** fluxo de revisão da seção AGENTS.md.
