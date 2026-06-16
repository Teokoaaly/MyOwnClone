import { test, expect } from '@playwright/test';

/**
 * FE-03: CSRF Protection verification tests
 */
test.describe('FE-03: CSRF Protection', () => {
  test('should reject POST request without CSRF token', async ({ request }) => {
    // Try to make a POST without CSRF token
    const response = await request.post('/api/bookings', {
      data: {
        meetingTypeId: 'test-id',
        visitorName: 'Test',
        visitorEmail: 'test@example.com',
        date: '2026-06-20',
      },
    });

    // Should get 403 Forbidden for missing CSRF token
    expect(response.status()).toBe(403);
  });

  test('should accept POST request with valid CSRF token', async ({ request }) => {
    // First get a CSRF token
    const csrfResponse = await request.get('/api/csrf');
    expect(csrfResponse.status()).toBe(200);
    const csrfToken = (await csrfResponse.json()).token;

    // Make POST with valid CSRF token in cookie
    // Note: The token is set as a cookie, so we need to include it
    const response = await request.post('/api/bookings', {
      headers: {
        'x-csrf-token': csrfToken,
      },
      data: {
        meetingTypeId: 'test-id',
        visitorName: 'Test',
        visitorEmail: 'test@example.com',
        date: '2026-06-20',
      },
    });

    // Should not be 403 (might be 400 for invalid data, but not 403 CSRF)
    expect(response.status()).not.toBe(403);
  });
});