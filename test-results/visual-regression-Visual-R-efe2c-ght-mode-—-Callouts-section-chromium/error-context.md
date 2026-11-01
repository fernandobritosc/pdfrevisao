# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: visual-regression.spec.ts >> Visual Regression — Design System >> Light mode — Callouts section
- Location: tests\visual-regression.spec.ts:60:7

# Error details

```
Error: expect(locator).toHaveScreenshot(expected) failed

Locator: locator('section').filter({ hasText: '📢 Callouts' })
  Expected an image 329px by 444px, received 1200px by 376px. 15127 pixels (ratio 0.03 of all image pixels) are different.

  Snapshot: light-callouts-section.png

Call log:
  - Expect "toHaveScreenshot(light-callouts-section.png)" locator('section').filter({ hasText: '📢 Callouts' }) with timeout 5000ms
    - verifying given screenshot expectation
  - waiting for locator('section').filter({ hasText: '📢 Callouts' })
    - locator resolved to <section class="section">…</section>
  - taking element screenshot
    - disabled all CSS animations
  - waiting for fonts to load...
  - fonts loaded
  - attempting scroll into view action
    - waiting for element to be stable
  - Expected an image 329px by 444px, received 1200px by 376px. 15127 pixels (ratio 0.03 of all image pixels) are different.
  - waiting 100ms before taking screenshot
  - waiting for locator('section').filter({ hasText: '📢 Callouts' })
    - locator resolved to <section class="section">…</section>
  - taking element screenshot
    - disabled all CSS animations
  - waiting for fonts to load...
  - fonts loaded
  - attempting scroll into view action
    - waiting for element to be stable
  - captured a stable screenshot
  - Expected an image 329px by 444px, received 1200px by 376px. 15127 pixels (ratio 0.03 of all image pixels) are different.

```

# Page snapshot

```yaml
- generic [active] [ref=e1]:
  - button "🌙 Dark" [ref=e2] [cursor=pointer]
  - generic [ref=e3]:
    - heading "Visual Regression Test — Design System" [level=1] [ref=e4]
    - paragraph [ref=e5]: Página de teste para visual regression. Testa todos os componentes do design system em light/dark mode.
    - generic [ref=e6]:
      - heading "🃏 Cards" [level=2] [ref=e7]
      - generic [ref=e8]:
        - generic [ref=e9]:
          - generic [ref=e10]: Card Padrão
          - generic [ref=e11]:
            - text: Conteúdo padrão do card com
            - strong [ref=e12]: texto em negrito
            - text: .
          - generic [ref=e13]: Segunda linha com mais conteúdo para testar altura.
        - generic [ref=e14]:
          - generic [ref=e15]: Card Contraste
          - generic [ref=e16]: Card com borda azul e título verde.
          - generic [ref=e17]:
            - generic [ref=e18]: Card Longo
            - generic [ref=e19]: Este card tem bastante conteúdo para testar como o layout se comporta com diferentes alturas de conteúdo. Deve crescer naturalmente.
            - generic [ref=e20]: Mais uma linha para garantir altura suficiente.
            - generic [ref=e21]: Última linha do card longo.
          - generic [ref=e22]:
            - generic [ref=e23]:
              - text: 📌
              - generic [ref=e24]: Card com Ícone
            - generic [ref=e25]:
              - text: Card com header contendo ícone e título.
              - generic [ref=e26]: Metadado do card
              - generic [ref=e27]:
                - link "Link 1" [ref=e28] [cursor=pointer]:
                  - /url: "#"
                - link "Link 2" [ref=e29] [cursor=pointer]:
                  - /url: "#"
    - generic [ref=e30]:
      - heading "📢 Callouts" [level=2] [ref=e31]
      - generic [ref=e32]:
        - generic [ref=e33]: ℹ️
        - generic [ref=e34]:
          - strong [ref=e35]: "Info:"
          - text: Informação adicional de apoio.
      - generic [ref=e36]:
        - generic [ref=e37]: ⚠️
        - generic [ref=e38]:
          - strong [ref=e39]: "Atenção:"
          - text: Ponto que costuma cair em prova.
      - generic [ref=e40]:
        - generic [ref=e41]: ✅
        - generic [ref=e42]:
          - strong [ref=e43]: "Dica:"
          - text: Orientação direta para a prova.
      - generic [ref=e44]:
        - generic [ref=e45]: ❌
        - generic [ref=e46]:
          - strong [ref=e47]: "Erro comum:"
          - text: Equívoco que a banca explora.
    - generic [ref=e48]:
      - heading "🚨 Gotchas" [level=2] [ref=e49]
      - generic [ref=e50]:
        - generic [ref=e51]: 🚨 Pegadinha da banca
        - text: "Descrição da pegadinha: o que a banca costuma inverter ou confundir."
      - generic [ref=e52]:
        - generic [ref=e53]: 🚨 Outra pegadinha
        - text: Mais uma pegadinha para testar múltiplos gotchas.
    - generic [ref=e54]:
      - heading "🔘 Botões" [level=2] [ref=e55]
      - generic [ref=e56]:
        - button "Botão Primário" [ref=e57] [cursor=pointer]
        - button "Sucesso" [ref=e58] [cursor=pointer]
        - button "Aviso" [ref=e59] [cursor=pointer]
        - button "Perigo" [ref=e60] [cursor=pointer]
        - button "Desabilitado" [disabled] [ref=e61] [cursor=pointer]
    - generic [ref=e62]:
      - heading "🏷️ Tags" [level=2] [ref=e63]
      - generic [ref=e64]:
        - generic [ref=e65]: Padrão
        - generic [ref=e66]: Azul
        - generic [ref=e67]: Verde
        - generic [ref=e68]: Âmbar
        - generic [ref=e69]: Vermelho
        - generic [ref=e70]: Roxo
        - generic [ref=e71]: Teal
        - generic [ref=e72]: Cinza
        - generic [ref=e73]: Correta
        - generic [ref=e74]: Incorreta
        - generic [ref=e75]: Atenção
        - generic [ref=e76]: Especial
    - generic [ref=e77]:
      - heading "📊 Tabelas" [level=2] [ref=e78]
      - table [ref=e80]:
        - rowgroup [ref=e81]:
          - row [ref=e82]:
            - columnheader "Coluna 1" [ref=e83]
            - columnheader "Coluna 2" [ref=e84]
            - columnheader "Coluna 3" [ref=e85]
        - rowgroup [ref=e86]:
          - row [ref=e87]:
            - cell "Item A" [ref=e88]
            - cell "Descrição do item A" [ref=e89]
            - cell [ref=e90]:
              - strong [ref=e91]: Exemplo
          - row [ref=e92]:
            - cell "Item B" [ref=e93]
            - cell "Descrição do item B" [ref=e94]
            - cell "Observação" [ref=e95]
          - row [ref=e96]:
            - cell "Item C" [ref=e97]
            - cell "Descrição do item C" [ref=e98]
            - cell "Outra coisa" [ref=e99]
          - row [ref=e100]:
            - cell "Item D" [ref=e101]
            - cell "Descrição do item D" [ref=e102]
            - cell "Mais um" [ref=e103]
          - row [ref=e104]:
            - cell "Item E" [ref=e105]
            - cell "Descrição do item E" [ref=e106]
            - cell "Final" [ref=e107]
    - generic [ref=e108]:
      - heading "🔲 Grid de Cards" [level=2] [ref=e109]
      - generic [ref=e110]:
        - generic [ref=e111]:
          - generic [ref=e112]: Card 1
          - generic [ref=e113]: Conteúdo 1
        - generic [ref=e114]:
          - generic [ref=e115]: Card 2
          - generic [ref=e116]: Conteúdo 2
        - generic [ref=e117]:
          - generic [ref=e118]: Card 3
          - generic [ref=e119]: Conteúdo 3
        - generic [ref=e120]:
          - generic [ref=e121]: Card 4
          - generic [ref=e122]: Conteúdo 4
        - generic [ref=e123]:
          - generic [ref=e124]: Card 5
          - generic [ref=e125]: Conteúdo 5
        - generic [ref=e126]:
          - generic [ref=e127]: Card 6
          - generic [ref=e128]: Conteúdo 6
    - generic [ref=e129]:
      - heading "🛠️ Toolbar" [level=2] [ref=e130]
      - group "Ferramentas de leitura" [ref=e131]:
        - button "Alternar modo claro/escuro" [ref=e132] [cursor=pointer]: 🌙
        - button "Diminuir tamanho da fonte" [ref=e133] [cursor=pointer]: A−
        - button "Aumentar tamanho da fonte" [ref=e134] [cursor=pointer]: A+
        - button "Alternar modo revisão" [ref=e135] [cursor=pointer]: 🧠
        - button "Marcar vacilos" [ref=e136] [cursor=pointer]: 🏷️
        - button "Abrir modo prática" [ref=e137] [cursor=pointer]: 🎯
    - generic [ref=e138]:
      - heading "🔍 Search Box" [level=2] [ref=e139]
      - generic [ref=e140]:
        - searchbox "Buscar palavra no resumo…" [ref=e141]
        - generic [ref=e142]:
          - generic [ref=e143]: 0 blocos
          - generic [ref=e144]:
            - button "↑" [disabled] [ref=e145]
            - button "↓" [disabled] [ref=e146]
          - button "limpar" [ref=e147] [cursor=pointer]
    - heading "🏷️ Marks Panel" [level=2] [ref=e149]
    - heading "🎯 Practice Panel" [level=2] [ref=e151]
    - generic [ref=e152]:
      - heading "🎨 Cores por Matéria" [level=2] [ref=e153]
      - generic [ref=e154]:
        - generic [ref=e155]:
          - generic [ref=e156]: AFO
          - generic [ref=e157]: "#16a34a"
        - generic [ref=e158]:
          - generic [ref=e159]: AP
          - generic [ref=e160]: "#0d9488"
        - generic [ref=e161]:
          - generic [ref=e162]: AD
          - generic [ref=e163]: "#2563eb"
        - generic [ref=e164]:
          - generic [ref=e165]: DC
          - generic [ref=e166]: "#7c3aed"
        - generic [ref=e167]:
          - generic [ref=e168]: DT
          - generic [ref=e169]: "#d97706"
        - generic [ref=e170]:
          - generic [ref=e171]: DPT
          - generic [ref=e172]: "#dc2626"
        - generic [ref=e173]:
          - generic [ref=e174]: PT
          - generic [ref=e175]: "#0891b2"
        - generic [ref=e176]:
          - generic [ref=e177]: INF
          - generic [ref=e178]: "#3b82f6"
        - generic [ref=e179]:
          - generic [ref=e180]: CP
          - generic [ref=e181]: "#db2777"
        - generic [ref=e182]:
          - generic [ref=e183]: RML
          - generic [ref=e184]: "#65a30d"
        - generic [ref=e185]:
          - generic [ref=e186]: ARC
          - generic [ref=e187]: "#92400e"
    - generic [ref=e188]:
      - heading "📑 Section Header" [level=2] [ref=e189]
      - generic [ref=e190]:
        - generic [ref=e191]: "1"
        - generic [ref=e192]: Título da Seção
      - generic [ref=e193]:
        - generic [ref=e194]: "2"
        - generic [ref=e195]: Título Longo da Seção Para Testar Quebra de Linha
    - generic [ref=e196]:
      - heading "📝 Section Header com Subtitle" [level=2] [ref=e197]
      - generic [ref=e198]:
        - generic [ref=e199]: "3"
        - generic [ref=e200]: Título com Subtitle
      - generic [ref=e201]: Subtítulo opcional com fonte/banca
```

# Test source

```ts
  1   | import { test, expect } from '@playwright/test';
  2   | 
  3   | const TEST_URL = 'visual-test.html';
  4   | 
  5   | test.describe('Visual Regression — Design System', () => {
  6   |   test.beforeEach(async ({ page }) => {
  7   |     await page.goto(TEST_URL, { waitUntil: 'networkidle' });
  8   |     // Wait for fonts to load
  9   |     await page.waitForLoadState('networkidle');
  10  |     await page.evaluate(() => document.fonts.ready);
  11  |   });
  12  | 
  13  |   test('Light mode — Full page screenshot', async ({ page }) => {
  14  |     // Ensure light mode
  15  |     await page.evaluate(() => {
  16  |       document.documentElement.setAttribute('data-theme', 'light');
  17  |       localStorage.setItem('theme', 'light');
  18  |     });
  19  |     await page.waitForTimeout(300); // Allow CSS transitions
  20  |     
  21  |     await expect(page).toHaveScreenshot('light-mode-full.png', {
  22  |       fullPage: true,
  23  |       animations: 'disabled',
  24  |     });
  25  |   });
  26  | 
  27  |   test('Dark mode — Full page screenshot', async ({ page }) => {
  28  |     await page.evaluate(() => {
  29  |       document.documentElement.setAttribute('data-theme', 'dark');
  30  |       localStorage.setItem('theme', 'dark');
  31  |     });
  32  |     await page.waitForTimeout(300);
  33  |     
  34  |     await expect(page).toHaveScreenshot('dark-mode-full.png', {
  35  |       fullPage: true,
  36  |       animations: 'disabled',
  37  |     });
  38  |   });
  39  | 
  40  |   test('Light mode — Cards section', async ({ page }) => {
  41  |     await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
  42  |     await page.waitForTimeout(300);
  43  |     
  44  |     const section = page.locator('section').filter({ hasText: '🃏 Cards' });
  45  |     await expect(section).toHaveScreenshot('light-cards-section.png', {
  46  |       animations: 'disabled',
  47  |     });
  48  |   });
  49  | 
  50  |   test('Dark mode — Cards section', async ({ page }) => {
  51  |     await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  52  |     await page.waitForTimeout(300);
  53  |     
  54  |     const section = page.locator('section').filter({ hasText: '🃏 Cards' });
  55  |     await expect(section).toHaveScreenshot('dark-cards-section.png', {
  56  |       animations: 'disabled',
  57  |     });
  58  |   });
  59  | 
  60  |   test('Light mode — Callouts section', async ({ page }) => {
  61  |     await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
  62  |     await page.waitForTimeout(300);
  63  |     
  64  |     const section = page.locator('section').filter({ hasText: '📢 Callouts' });
> 65  |     await expect(section).toHaveScreenshot('light-callouts-section.png', {
      |                           ^ Error: expect(locator).toHaveScreenshot(expected) failed
  66  |       animations: 'disabled',
  67  |     });
  68  |   });
  69  | 
  70  |   test('Dark mode — Callouts section', async ({ page }) => {
  71  |     await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  72  |     await page.waitForTimeout(300);
  73  |     
  74  |     const section = page.locator('section').filter({ hasText: '📢 Callouts' });
  75  |     await expect(section).toHaveScreenshot('dark-callouts-section.png', {
  76  |       animations: 'disabled',
  77  |     });
  78  |   });
  79  | 
  80  |   test('Light mode — Toolbar', async ({ page }) => {
  81  |     await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
  82  |     await page.waitForTimeout(300);
  83  |     
  84  |     const toolbar = page.locator('.rh-toolbar');
  85  |     await expect(toolbar).toHaveScreenshot('light-toolbar.png', {
  86  |       animations: 'disabled',
  87  |     });
  88  |   });
  89  | 
  90  |   test('Dark mode — Toolbar', async ({ page }) => {
  91  |     await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  92  |     await page.waitForTimeout(300);
  93  |     
  94  |     const toolbar = page.locator('.rh-toolbar');
  95  |     await expect(toolbar).toHaveScreenshot('dark-toolbar.png', {
  96  |       animations: 'disabled',
  97  |     });
  98  |   });
  99  | 
  100 |   test('Light mode — Search box', async ({ page }) => {
  101 |     await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
  102 |     await page.waitForTimeout(300);
  103 |     
  104 |     const searchBox = page.locator('.sr-box');
  105 |     await expect(searchBox).toHaveScreenshot('light-search-box.png', {
  106 |       animations: 'disabled',
  107 |     });
  108 |   });
  109 | 
  110 |   test('Dark mode — Search box', async ({ page }) => {
  111 |     await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  112 |     await page.waitForTimeout(300);
  113 |     
  114 |     const searchBox = page.locator('.sr-box');
  115 |     await expect(searchBox).toHaveScreenshot('dark-search-box.png', {
  116 |       animations: 'disabled',
  117 |     });
  118 |   });
  119 | 
  120 |   test('Light mode — Search box with results', async ({ page }) => {
  121 |     await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
  122 |     await page.waitForTimeout(300);
  123 |     
  124 |     // Type in search to trigger results
  125 |     const input = page.locator('#sr-input');
  126 |     await input.fill('card');
  127 |     await page.waitForTimeout(500); // Wait for search to process
  128 |     
  129 |     const searchBox = page.locator('.sr-box');
  130 |     await expect(searchBox).toHaveScreenshot('light-search-with-results.png', {
  131 |       animations: 'disabled',
  132 |     });
  133 |   });
  134 | 
  135 |   test('Light mode — Table', async ({ page }) => {
  136 |     await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
  137 |     await page.waitForTimeout(300);
  138 |     
  139 |     const table = page.locator('.table-wrap');
  140 |     await expect(table).toHaveScreenshot('light-table.png', {
  141 |       animations: 'disabled',
  142 |     });
  143 |   });
  144 | 
  145 |   test('Dark mode — Table', async ({ page }) => {
  146 |     await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
  147 |     await page.waitForTimeout(300);
  148 |     
  149 |     const table = page.locator('.table-wrap');
  150 |     await expect(table).toHaveScreenshot('dark-table.png', {
  151 |       animations: 'disabled',
  152 |     });
  153 |   });
  154 | 
  155 |   test('Light mode — Buttons', async ({ page }) => {
  156 |     await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
  157 |     await page.waitForTimeout(300);
  158 |     
  159 |     const section = page.locator('section').filter({ hasText: '🔘 Botões' });
  160 |     await expect(section).toHaveScreenshot('light-buttons.png', {
  161 |       animations: 'disabled',
  162 |     });
  163 |   });
  164 | 
  165 |   test('Dark mode — Buttons', async ({ page }) => {
```