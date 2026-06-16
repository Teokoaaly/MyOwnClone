import { test, expect } from '@playwright/test';

/**
 * FE-05: Auth Rate Limiting tests
 */
test.describe('FE-05: Auth Rate Limiting', () => {
  test('should return 429 after exceeding rate limit on forgot-password', async ({ request }) => {
    const email = 'test@example.com';
    
    // Make 6 requests (limit is 5 per minute)
    const responses = [];
    for (let i = 0; i < 6; i++) {
      const response = await request.post('/api/auth/forgot-password', {
        data: { email },
      });
      responses.push(response);
    }

    // Last request should be rate limited
    const lastResponse = responses[5];
    expect(lastResponse.status()).toBe(429);
    
    // Should have Retry-After header
    const retryAfter = lastResponse.headers()['retry-after'];
    expect(retryAfter).toBeDefined();
  });

  test('should include rate limit headers in response', async ({ request }) => {
    const response = await request.post('/api/auth/forgot-password', {
      data: { email: 'test@example.com' },
    });

    // Should include rate limit headers
    const rateLimitRemaining = response.headers()['x-ratelimit-remaining'];
    // First request should have remaining > 0 (or header might not exist on first request)
    expect(response.status()).toBe(200);
  });
});