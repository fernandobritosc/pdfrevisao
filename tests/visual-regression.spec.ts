import { test, expect } from '@playwright/test';

const TEST_URL = 'visual-test.html';

test.describe('Visual Regression — Design System', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(TEST_URL, { waitUntil: 'networkidle' });
    // Wait for fonts to load
    await page.waitForLoadState('networkidle');
    await page.evaluate(() => document.fonts.ready);
  });

  test('Light mode — Full page screenshot', async ({ page }) => {
    // Ensure light mode
    await page.evaluate(() => {
      document.documentElement.setAttribute('data-theme', 'light');
      localStorage.setItem('theme', 'light');
    });
    await page.waitForTimeout(300); // Allow CSS transitions
    
    await expect(page).toHaveScreenshot('light-mode-full.png', {
      fullPage: true,
      animations: 'disabled',
    });
  });

  test('Dark mode — Full page screenshot', async ({ page }) => {
    await page.evaluate(() => {
      document.documentElement.setAttribute('data-theme', 'dark');
      localStorage.setItem('theme', 'dark');
    });
    await page.waitForTimeout(300);
    
    await expect(page).toHaveScreenshot('dark-mode-full.png', {
      fullPage: true,
      animations: 'disabled',
    });
  });

  test('Light mode — Cards section', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    const section = page.locator('section').filter({ hasText: '🃏 Cards' });
    await expect(section).toHaveScreenshot('light-cards-section.png', {
      animations: 'disabled',
    });
  });

  test('Dark mode — Cards section', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
    await page.waitForTimeout(300);
    
    const section = page.locator('section').filter({ hasText: '🃏 Cards' });
    await expect(section).toHaveScreenshot('dark-cards-section.png', {
      animations: 'disabled',
    });
  });

  test('Light mode — Callouts section', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    const section = page.locator('section').filter({ hasText: '📢 Callouts' });
    await expect(section).toHaveScreenshot('light-callouts-section.png', {
      animations: 'disabled',
    });
  });

  test('Dark mode — Callouts section', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
    await page.waitForTimeout(300);
    
    const section = page.locator('section').filter({ hasText: '📢 Callouts' });
    await expect(section).toHaveScreenshot('dark-callouts-section.png', {
      animations: 'disabled',
    });
  });

  test('Light mode — Toolbar', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    const toolbar = page.locator('.rh-toolbar');
    await expect(toolbar).toHaveScreenshot('light-toolbar.png', {
      animations: 'disabled',
    });
  });

  test('Dark mode — Toolbar', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
    await page.waitForTimeout(300);
    
    const toolbar = page.locator('.rh-toolbar');
    await expect(toolbar).toHaveScreenshot('dark-toolbar.png', {
      animations: 'disabled',
    });
  });

  test('Light mode — Search box', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    const searchBox = page.locator('.sr-box');
    await expect(searchBox).toHaveScreenshot('light-search-box.png', {
      animations: 'disabled',
    });
  });

  test('Dark mode — Search box', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
    await page.waitForTimeout(300);
    
    const searchBox = page.locator('.sr-box');
    await expect(searchBox).toHaveScreenshot('dark-search-box.png', {
      animations: 'disabled',
    });
  });

  test('Light mode — Search box with results', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    // Type in search to trigger results
    const input = page.locator('#sr-input');
    await input.fill('card');
    await page.waitForTimeout(500); // Wait for search to process
    
    const searchBox = page.locator('.sr-box');
    await expect(searchBox).toHaveScreenshot('light-search-with-results.png', {
      animations: 'disabled',
    });
  });

  test('Light mode — Table', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    const table = page.locator('.table-wrap');
    await expect(table).toHaveScreenshot('light-table.png', {
      animations: 'disabled',
    });
  });

  test('Dark mode — Table', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
    await page.waitForTimeout(300);
    
    const table = page.locator('.table-wrap');
    await expect(table).toHaveScreenshot('dark-table.png', {
      animations: 'disabled',
    });
  });

  test('Light mode — Buttons', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    const section = page.locator('section').filter({ hasText: '🔘 Botões' });
    await expect(section).toHaveScreenshot('light-buttons.png', {
      animations: 'disabled',
    });
  });

  test('Dark mode — Buttons', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
    await page.waitForTimeout(300);
    
    const section = page.locator('section').filter({ hasText: '🔘 Botões' });
    await expect(section).toHaveScreenshot('dark-buttons.png', {
      animations: 'disabled',
    });
  });

  test('Light mode — Tags', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    const section = page.locator('section').filter({ hasText: '🏷️ Tags' });
    await expect(section).toHaveScreenshot('light-tags.png', {
      animations: 'disabled',
    });
  });

  test('Dark mode — Tags', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
    await page.waitForTimeout(300);
    
    const section = page.locator('section').filter({ hasText: '🏷️ Tags' });
    await expect(section).toHaveScreenshot('dark-tags.png', {
      animations: 'disabled',
    });
  });

  test('Light mode — Subject colors', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    const section = page.locator('section').filter({ hasText: '🎨 Cores por Matéria' });
    await expect(section).toHaveScreenshot('light-subject-colors.png', {
      animations: 'disabled',
    });
  });

  test('Dark mode — Subject colors', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
    await page.waitForTimeout(300);
    
    const section = page.locator('section').filter({ hasText: '🎨 Cores por Matéria' });
    await expect(section).toHaveScreenshot('dark-subject-colors.png', {
      animations: 'disabled',
    });
  });

  test('Light mode — Practice panel', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    // Manually show the panel (JS not loaded in test environment)
    await page.evaluate(() => {
      const panel = document.getElementById('rhPracticePanel');
      if (panel) panel.classList.add('show');
    });
    await page.waitForTimeout(300);
    
    const panel = page.locator('#rhPracticePanel');
    await expect(panel).toBeVisible();
    await expect(panel).toHaveScreenshot('light-practice-panel.png', {
      animations: 'disabled',
    });
  });

  test('Light mode — Marks panel', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    // Manually show the panel (JS not loaded in test environment)
    await page.evaluate(() => {
      const panel = document.getElementById('rhMarkPanel');
      if (panel) panel.classList.add('show');
    });
    await page.waitForTimeout(300);
    
    const panel = page.locator('#rhMarkPanel');
    await expect(panel).toBeVisible();
    await expect(panel).toHaveScreenshot('light-marks-panel.png', {
      animations: 'disabled',
    });
  });

  test('Light mode — Search box with query', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    const input = page.locator('#sr-input');
    await input.fill('conceito');
    await page.waitForTimeout(500);
    
    const searchBox = page.locator('.sr-box');
    await expect(searchBox).toHaveScreenshot('light-search-query.png', {
      animations: 'disabled',
    });
  });

  test('Print mode — Light', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    // Emulate print media
    await page.emulateMedia({ media: 'print' });
    await page.waitForTimeout(300);
    
    await expect(page).toHaveScreenshot('print-light.png', {
      fullPage: true,
      animations: 'disabled',
    });
  });

  test('Print mode — Dark', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'dark'));
    await page.waitForTimeout(300);
    
    await page.emulateMedia({ media: 'print' });
    await page.waitForTimeout(300);
    
    await expect(page).toHaveScreenshot('print-dark.png', {
      fullPage: true,
      animations: 'disabled',
    });
  });

  test('Reduced motion — Light', async ({ page }) => {
    await page.evaluate(() => document.documentElement.setAttribute('data-theme', 'light'));
    await page.waitForTimeout(300);
    
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.waitForTimeout(300);
    
    await expect(page).toHaveScreenshot('reduced-motion-light.png', {
      fullPage: true,
      animations: 'disabled',
    });
  });
});