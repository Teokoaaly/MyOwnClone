import { NextRequest } from "next/server";

/**
 * CSRF Verification Utility
 * 
 * Implements Synchronizer Token pattern for CSRF protection:
 * 1. Token is generated and stored in a cookie (readable by JS)
 * 2. Frontend reads token from cookie and sends as header (X-CSRF-Token)
 * 3. Backend verifies header token matches cookie token
 * 
 * This protects against CSRF attacks where malicious sites make requests
 * on behalf of authenticated users.
 */

const CSRF_TOKEN_HEADER = "x-csrf-token";
const CSRF_TOKEN_COOKIE = "csrf-token";

/**
 * Verify CSRF token from request
 * 
 * Compares the token from the X-CSRF-Token header with the token in the csrf-token cookie.
 * If they match, the request is legitimate (not a CSRF attack).
 * 
 * @param request - Next.js request object
 * @returns true if CSRF token is valid, false otherwise
 */
export function verifyCsrfToken(request: NextRequest): boolean {
  // Get token from header
  const headerToken = request.headers.get(CSRF_TOKEN_HEADER);
  
  // Get token from cookie
  const cookieToken = request.cookies.get(CSRF_TOKEN_COOKIE)?.value;
  
  // Both must be present and match
  if (!headerToken || !cookieToken) {
    return false;
  }
  
  if (headerToken !== cookieToken) {
    return false;
  }
  
  return true;
}

/**
 * Create CSRF error response
 * Returns 403 Forbidden with CSRF error message
 */
export function createCsrfErrorResponse() {
  return new Response(
    JSON.stringify({ error: "CSRF verification failed" }),
    {
      status: 403,
      headers: { "Content-Type": "application/json" },
    }
  );
}
