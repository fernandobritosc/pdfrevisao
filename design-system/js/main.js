/**
 * main.js — Entry point do design system
 * Importa todos os módulos na ordem correta de dependência.
 */

// 1. Theme init (deve rodar primeiro, antes de qualquer UI)
import './modules/theme-init.js';

// 2. Toolbar (depende de theme-init)
import './modules/toolbar.js';

// 3. Feature modules (independentes, usam toolbar se disponível)
import './modules/review-mode.js';
import './modules/marks-mode.js';
import './modules/search-v2.js';
import './modules/practice-mode.js';

// 4. PWA (independente)
import './modules/pwa.js';

// Exporta API pública
export const DesignSystem = {
  version: '1.0.0',
  name: 'Resumos Hermes Design System'
};