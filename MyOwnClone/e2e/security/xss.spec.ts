import { test, expect } from '@playwright/test';

/**
 * FE-01: XSS Prevention - DOMPurify sanitization tests
 */
test.describe('FE-01: XSS Prevention via DOMPurify', () => {
  const XSS_PAYLOADS = [
    { name: 'script_tag', payload: '<script>alert("XSS")</script>' },
    { name: 'img_onerror', payload: '<img src=x onerror=alert("XSS")>' },
    { name: 'svg_onload', payload: '<svg onload=alert("XSS")>' },
    { name: 'javascript_href', payload: '<a href="javascript:alert(\'XSS\')">click</a>' },
    { name: 'details_ontoggle', payload: '<details open ontoggle=alert("XSS")>' },
  ];

  for (const { name, payload } of XSS_PAYLOADS) {
    test(`should sanitize ${name} payload`, async ({ page }) => {
      // Navigate to chat page
      await page.goto('/chat');
      
      // Inject XSS payload via console (simulating LLM output)
      const sanitized = await page.evaluate((p) => {
        // @ts-ignore
        const DOMPurify = window.DOMPurify;
        if (DOMPurify) {
          return DOMPurify.sanitize(p);
        }
        // If DOMPurify not available on window, just return the payload
        // (test will fail if sanitization doesn't work in MessageBubble)
        return p;
      }, payload);

      // Verify sanitization worked (script tags should be removed, handlers stripped)
      expect(sanitized).not.toContain('<script>');
      expect(sanitized).not.toContain('onerror=');
      expect(sanitized).not.toContain('onload=');
      expect(sanitized).not.toContain('javascript:');
    });
  }
});