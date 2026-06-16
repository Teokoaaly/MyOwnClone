// Simple in-memory rate limiter for auth endpoints
// Key: IP + endpoint path
// Limit: 5 requests per 60 seconds

const rateLimitMap = new Map<string, { count: number; resetTime: number }>();
const WINDOW_MS = 60 * 1000; // 1 minute
const MAX_REQUESTS = 5;

export function rateLimit(key: string): { success: boolean; remaining: number; resetIn: number } {
  const now = Date.now();
  const entry = rateLimitMap.get(key);

  if (!entry || now > entry.resetTime) {
    rateLimitMap.set(key, { count: 1, resetTime: now + WINDOW_MS });
    return { success: true, remaining: MAX_REQUESTS - 1, resetIn: WINDOW_MS };
  }

  if (entry.count >= MAX_REQUESTS) {
    return { success: false, remaining: 0, resetIn: entry.resetTime - now };
  }

  entry.count++;
  return { success: true, remaining: MAX_REQUESTS - entry.count, resetIn: entry.resetTime - now };
}

export function getRateLimitKey(request: Request, endpoint: string): string {
  const ip = request.headers.get('x-forwarded-for')?.split(',')[0]?.trim()
          || request.headers.get('x-real-ip')
          || 'unknown';
  return `${ip}:${endpoint}`;
}
