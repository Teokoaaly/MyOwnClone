/**
 * Security test helpers for Playwright E2E tests.
 *
 * Provides fixtures and utilities for testing:
 * - CSRF protection
 * - IDOR (Insecure Direct Object Reference)
 * - XSS (Cross-Site Scripting)
 */

import { test as base, Page, Request, Route } from '@playwright/test';

// ═══════════════════════════════════════════════════════════════════════════════
// CSRF Fixtures
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Extracts CSRF token from HTML response.
 */
export async function extractCsrfToken(page: Page, formSelector: string = 'form'): Promise<string | null> {
  const tokenInput = await page.locator(`${formSelector} input[name="csrf_token"], ${formSelector} input[name="_token"], ${formSelector} input[name="token"]`).first();
  if (await tokenInput.count() > 0) {
    return tokenInput.inputValue();
  }
  // Try meta tag (Laravel style)
  const metaToken = await page.locator('meta[name="csrf-token"]').getAttribute('content');
  return metaToken;
}

/**
 * Creates a CSRF-safe request by first fetching the page and extracting the token.
 */
export async function withCsrfToken(page: Page, endpoint: string, options: {
  method?: 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE';
  body?: Record<string, unknown>;
} = {}): Promise<Request> {
  const { method = 'POST', body = {} } = options;

  // Navigate to get CSRF token first (for form-based endpoints)
  if (method === 'POST' || method === 'PUT' || method === 'PATCH') {
    const pageUrl = new URL(endpoint, 'http://localhost:3000').toString();
    await page.goto(pageUrl, { waitUntil: 'networkidle' });

    const csrfToken = await extractCsrfToken(page);
    if (csrfToken) {
      body['csrf_token'] = csrfToken;
    }
  }

  const url = new URL(endpoint, 'http://localhost:3000').toString();
  return page.request[method.toLowerCase()](url, { data: body });
}

// ═══════════════════════════════════════════════════════════════════════════════
// IDOR Fixtures
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Tests for IDOR vulnerabilities by attempting to access resources with different IDs.
 */
export async function testIdorVulnerability(
  page: Page,
  endpointTemplate: string, // e.g., '/api/users/{id}/profile'
  currentUserId: string | number,
  otherUserIds: (string | number)[]
): Promise<{ endpoint: string; accessed: boolean; status: number }[]> {
  const results: { endpoint: string; accessed: boolean; status: number }[] = [];

  for (const id of otherUserIds) {
    const endpoint = endpointTemplate.replace('{id}', String(id));
    const url = new URL(endpoint, 'http://localhost:3000').toString();

    const response = await page.request.get(url);

    // IDOR exists if we can access another user's resource
    const accessed = response.status() === 200;
    results.push({ endpoint, accessed, status: response.status() });
  }

  return results;
}

/**
 * Sequential ID enumeration test for IDOR.
 */
export async function enumerateIds(
  page: Page,
  baseEndpoint: string,
  idRange: number[] = []
): Promise<{ id: number; accessible: boolean; status: number }[]> {
  const results: { id: number; accessible: boolean; status: number }[] = [];

  for (const id of idRange) {
    const url = new URL(`${baseEndpoint}/${id}`, 'http://localhost:3000').toString();
    const response = await page.request.get(url);

    results.push({
      id,
      accessible: response.status() === 200,
      status: response.status()
    });
  }

  return results;
}

// ═══════════════════════════════════════════════════════════════════════════════
// XSS Fixtures
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * XSS payload set for testing input sanitization.
 */
export const XSS_PAYLOADS = [
  "<script>alert('XSS')</script>",
  "<img src=x onerror=alert('XSS')>",
  "<svg/onload=alert('XSS')>",
  "<body onload=alert('XSS')>",
  "<input onfocus=alert('XSS') autofocus>",
  "javascript:alert('XSS')",
  "{{constructor.constructor('alert(1)')()}}",
  "<script>alert(document.cookie)</script>",
];

/**
 * Tests XSS vulnerability by injecting payloads into input fields.
 */
export async function testXssVulnerability(
  page: Page,
  inputSelector: string,
  submitSelector: string,
  getResultSelector: string = 'body'
): Promise<{ payload: string; reflected: boolean; executed: boolean }[]> {
  const results: { payload: string; reflected: boolean; executed: boolean }[] = [];

  for (const payload of XSS_PAYLOADS) {
    // Clear and fill the input
    await page.locator(inputSelector).clear();
    await page.locator(inputSelector).fill(payload);

    // Submit the form
    await page.locator(submitSelector).click();
    await page.waitForLoadState('networkidle');

    // Check if payload is reflected in the page
    const pageContent = await page.locator(getResultSelector).textContent();
    const reflected = pageContent?.includes(payload) ?? false;

    // Check if script execution occurred (via alert dialog)
    let executed = false;
    page.on('dialog', async dialog => {
      if (dialog.message().includes('XSS') || dialog.message().includes('alert')) {
        executed = true;
      }
      await dialog.dismiss();
    });

    results.push({ payload, reflected, executed });
  }

  return results;
}

/**
 * Sanitized version of XSS payloads for safe display in tests.
 */
export function sanitizeForDisplay(payload: string): string {
  return payload
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#x27;');
}

// ═══════════════════════════════════════════════════════════════════════════════
// Security Headers Fixtures
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Expected security headers that should be present on responses.
 */
export const EXPECTED_SECURITY_HEADERS = {
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': /^(DENY|SAMEORIGIN|ALLOW-FROM .+)$/,
  'X-XSS-Protection': '1; mode=block',
  'Strict-Transport-Security': /max-age=/,
  'Content-Security-Policy': /.+/,
};

/**
 * Checks if response has required security headers.
 */
export async function checkSecurityHeaders(response: Request): Promise<{
  missing: string[];
  present: string[];
}> {
  const headers = response.headers();
  const missing: string[] = [];
  const present: string[] = [];

  for (const [header, expected] of Object.entries(EXPECTED_SECURITY_HEADERS)) {
    const value = headers[header.toLowerCase()];
    if (value) {
      if (expected instanceof RegExp) {
        if (expected.test(value)) {
          present.push(header);
        } else {
          missing.push(`${header} (value "${value}" doesn't match ${expected})`);
        }
      } else if (value === expected) {
        present.push(header);
      } else {
        missing.push(`${header} (value "${value}" != "${expected}")`);
      }
    } else {
      missing.push(header);
    }
  }

  return { missing, present };
}

// ═══════════════════════════════════════════════════════════════════════════════
// CSRF Test Fixture
// ═══════════════════════════════════════════════════════════════════════════════

/**
 * Extended test fixture with security testing capabilities.
 */
export const test = base.extend<{
  withCsrfToken: typeof withCsrfToken;
  testIdorVulnerability: typeof testIdorVulnerability;
  testXssVulnerability: typeof testXssVulnerability;
  checkSecurityHeaders: typeof checkSecurityHeaders;
}>({
  withCsrfToken: async ({ page }, use) => {
    await use(withCsrfToken);
  },
  testIdorVulnerability: async ({ page }, use) => {
    await use(testIdorVulnerability);
  },
  testXssVulnerability: async ({ page }, use) => {
    await use(testXssVulnerability);
  },
  checkSecurityHeaders: async ({ page }, use) => {
    await use(checkSecurityHeaders);
  },
});