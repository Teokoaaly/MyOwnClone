/**
 * Shared type definitions for security events.
 *
 * These types provide a common schema for security events and audit logging
 * across the MyOwnClone frontend application.
 */

/**
 * Severity levels for security events.
 */
export type SecuritySeverity = "low" | "medium" | "high" | "critical";

/**
 * Classification of rate limit key type.
 */
export type RateLimitKeyType = "public" | "authenticated";

/**
 * A rate limiting key used for Redis-based rate limiting.
 *
 * @example
 * // Public rate limit (by IP)
 * const publicKey: RateLimitKey = {
 *   identifier: "192.168.1.1",
 *   endpoint: "/api/chat",
 *   keyType: "public"
 * };
 *
 * // Authenticated rate limit (by tenant)
 * const authKey: RateLimitKey = {
 *   identifier: "tenant-123",
 *   endpoint: "/api/chat",
 *   keyType: "authenticated"
 * };
 */
export interface RateLimitKey {
  /** Either IP address (public) or tenant ID (authenticated). */
  identifier: string;
  /** The API endpoint being rate limited. */
  endpoint: string;
  /** Whether this is a public or authenticated key. */
  keyType: RateLimitKeyType;
}

/**
 * A security-relevant event that should be logged.
 */
export interface SecurityEvent {
  /** Classification of the security event. */
  eventType: SecurityEventType;
  /** When the event occurred (UTC). */
  timestamp: string;
  /** Tenant associated with the event (if authenticated). */
  tenantId?: string;
  /** Source IP of the request. */
  ipAddress?: string;
  /** API endpoint that triggered the event. */
  endpoint?: string;
  /** Additional event-specific data. */
  details?: Record<string, unknown>;
  /** Whether the request was blocked due to this event. */
  blocked: boolean;
  /** Severity level of the event. */
  severity: SecuritySeverity;
}

/**
 * Constants for security event types.
 */
export enum SecurityEventType {
  RateLimitExceeded = "rate_limit_exceeded",
  /** Too many requests from a source. */

  AuthenticationFailure = "authentication_failure",
  /** Failed login or auth attempt. */

  AuthorizationFailure = "authorization_failure",
  /** Access denied due to permissions. */

  PromptInjectionSuspected = "prompt_injection_suspected",
  /** Potential prompt injection attempt detected. */

  XssAttempt = "xss_attempt",
  /** Potential cross-site scripting attempt. */

  IdorAttempt = "idor_attempt",
  /** Potential insecure direct object reference attempt. */

  CsrfAttempt = "csrf_attempt",
  /** Potential cross-site request forgery attempt. */

  SuspiciousRequest = "suspicious_request",
  /** Request with suspicious characteristics. */

  AdminPrivilegeEscalation = "admin_privilege_escalation",
  /** Attempted privilege escalation to admin. */

  RedisFailure = "redis_failure",
  /** Redis connection failure affecting security controls. */
}

/**
 * An audit log entry for compliance and debugging.
 */
export interface AuditLogEntry {
  /** Unique identifier for this log entry. */
  entryId: string;
  /** When the action occurred (UTC). */
  timestamp: string;
  /** Tenant that performed the action. */
  tenantId?: string;
  /** User who performed the action (if applicable). */
  userId?: string;
  /** The action performed (e.g., 'create', 'update', 'delete'). */
  action?: AuditAction;
  /** Type of resource affected. */
  resourceType?: string;
  /** ID of the resource affected. */
  resourceId?: string;
  /** Source IP of the request. */
  ipAddress?: string;
  /** User agent string of the request. */
  userAgent?: string;
  /** Additional action-specific details. */
  details?: Record<string, unknown>;
  /** Whether the action succeeded. */
  success: boolean;
}

/**
 * Constants for audit log actions.
 */
export enum AuditAction {
  Create = "create",
  Read = "read",
  Update = "update",
  Delete = "delete",
  Login = "login",
  Logout = "logout",
  GrantAccess = "grant_access",
  RevokeAccess = "revoke_access",
  AdminAction = "admin_action",
}

/**
 * Represents a resource that belongs to a tenant.
 *
 * Used for tenant isolation checks to ensure resources are only
 * accessible by their owning tenant.
 */
export interface TenantResource {
  /** Unique identifier of the resource. */
  resourceId: string;
  /** Type of the resource (e.g., 'clone', 'booking'). */
  resourceType: string;
  /** ID of the tenant that owns this resource. */
  tenantId: string;
  /** When the resource was created. */
  createdAt: string;
}

/**
 * Result of a tenant isolation verification.
 */
export interface TenantIsolationCheck {
  /** The resource being checked. */
  resource: TenantResource;
  /** Tenant ID of the requester. */
  requestingTenantId: string;
  /** Whether the resource is properly isolated. */
  isIsolated: boolean;
  /** If not isolated, why not. */
  violationReason?: string;
}

/**
 * Rate limiting key schema constants.
 */
export const RATE_LIMIT_KEY_PREFIX = "ratelimit";

/**
 * Key format for public (unauthenticated) rate limiting.
 * Format: `ratelimit:{ip}:{endpoint}`
 */
export const RATE_LIMIT_KEY_FORMAT_PUBLIC = "ratelimit:{ip}:{endpoint}";

/**
 * Key format for authenticated (tenant-scoped) rate limiting.
 * Format: `ratelimit:{tenant_id}:{endpoint}`
 */
export const RATE_LIMIT_KEY_FORMAT_AUTHENTICATED =
  "ratelimit:{tenant_id}:{endpoint}";

/**
 * Build a Redis key for rate limiting.
 *
 * @param identifier - IP address or tenant ID
 * @param endpoint - API endpoint path
 * @param keyType - Whether public (IP) or authenticated (tenant)
 * @returns Redis key string
 *
 * @example
 * const key = buildRateLimitKey("192.168.1.1", "/api/chat", "public");
 * // Returns: "ratelimit:192.168.1.1:/api/chat"
 */
export function buildRateLimitKey(
  identifier: string,
  endpoint: string,
  keyType: RateLimitKeyType
): string {
  return `${RATE_LIMIT_KEY_PREFIX}:${identifier}:${endpoint}`;
}