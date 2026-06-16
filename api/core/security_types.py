"""Shared type definitions for security events.

These types provide a common schema for rate limiting, security events,
audit logging, and tenant isolation checks across the MyOwnClone API.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional

# Rate limiting key schema constants
RATE_LIMIT_KEY_PREFIX = "ratelimit"
"""Prefix for all rate limiting keys in Redis."""

RATE_LIMIT_KEY_FORMAT_PUBLIC = "ratelimit:{ip}:{endpoint}"
"""Key format for public (unauthenticated) rate limiting."""

RATE_LIMIT_KEY_FORMAT_AUTHENTICATED = "ratelimit:{tenant_id}:{endpoint}"
"""Key format for authenticated (tenant-scoped) rate limiting."""


class RateLimitKeyType(Enum):
    """Classification of rate limit key type."""

    PUBLIC = "public"
    """Unauthenticated request, keyed by IP address."""

    AUTHENTICATED = "authenticated"
    """Authenticated request, keyed by tenant ID."""


@dataclass(frozen=True)
class RateLimitKey:
    """A rate limiting key used for Redis-based rate limiting.

    Attributes:
        prefix: Always 'ratelimit' for Redis key namespace.
        identifier: Either IP address (public) or tenant_id (authenticated).
        endpoint: The API endpoint being rate limited.
        key_type: Whether this is a public or authenticated key.

    Example:
        >>> key = RateLimitKey(
        ...     identifier="192.168.1.1",
        ...     endpoint="/api/chat",
        ...     key_type=RateLimitKeyType.PUBLIC
        ... )
        >>> key.to_redis_key()
        'ratelimit:192.168.1.1:/api/chat'
    """

    identifier: str
    endpoint: str
    key_type: RateLimitKeyType = RateLimitKeyType.PUBLIC
    prefix: str = field(default=RATE_LIMIT_KEY_PREFIX, init=False)

    def to_redis_key(self) -> str:
        """Convert to Redis key string.

        Returns:
            Redis key in format 'ratelimit:{identifier}:{endpoint}'.
        """
        return f"{self.prefix}:{self.identifier}:{self.endpoint}"

    def to_redis_key_bytes(self) -> bytes:
        """Convert to Redis key as bytes.

        Returns:
            Redis key as bytes for Redis client operations.
        """
        return self.to_redis_key().encode("utf-8")


@dataclass
class SecurityEvent:
    """A security-relevant event that should be logged.

    Attributes:
        event_type: Classification of the security event.
        timestamp: When the event occurred (UTC).
        tenant_id: Tenant associated with the event (if authenticated).
        ip_address: Source IP of the request.
        endpoint: API endpoint that triggered the event.
        details: Additional event-specific data.
        blocked: Whether the request was blocked due to this event.
        severity: Severity level of the event.
    """

    event_type: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    tenant_id: Optional[str] = None
    ip_address: Optional[str] = None
    endpoint: Optional[str] = None
    details: dict = field(default_factory=dict)
    blocked: bool = False
    severity: str = "medium"


class SecurityEventType:
    """Constants for security event types."""

    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    """Too many requests from a source."""

    AUTHENTICATION_FAILURE = "authentication_failure"
    """Failed login or auth attempt."""

    AUTHORIZATION_FAILURE = "authorization_failure"
    """Access denied due to permissions."""

    PROMPT_INJECTION_SUSPECTED = "prompt_injection_suspected"
    """Potential prompt injection attempt detected."""

    XSS_ATTEMPT = "xss_attempt"
    """Potential cross-site scripting attempt."""

    IDOR_ATTEMPT = "idor_attempt"
    """Potential insecure direct object reference attempt."""

    CSRF_ATTEMPT = "csrf_attempt"
    """Potential cross-site request forgery attempt."""

    SUSPICIOUS_REQUEST = "suspicious_request"
    """Request with suspicious characteristics."""

    ADMIN_PRIVILEGE_ESCALATION = "admin_privilege_escalation"
    """Attempted privilege escalation to admin."""

    REDIS_FAILURE = "redis_failure"
    """Redis connection failure affecting security controls."""


@dataclass
class AuditLogEntry:
    """An audit log entry for compliance and debugging.

    Attributes:
        entry_id: Unique identifier for this log entry.
        timestamp: When the action occurred (UTC).
        tenant_id: Tenant that performed the action.
        user_id: User who performed the action (if applicable).
        action: The action performed (e.g., 'create', 'update', 'delete').
        resource_type: Type of resource affected.
        resource_id: ID of the resource affected.
        ip_address: Source IP of the request.
        user_agent: User agent string of the request.
        details: Additional action-specific details.
        success: Whether the action succeeded.
    """

    entry_id: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    tenant_id: Optional[str] = None
    user_id: Optional[str] = None
    action: Optional[str] = None
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    ip_address: Optional[str] = None
    user_agent: Optional[str] = None
    details: dict = field(default_factory=dict)
    success: bool = True


class AuditAction:
    """Constants for audit log actions."""

    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"
    LOGIN = "login"
    LOGOUT = "logout"
    GRANT_ACCESS = "grant_access"
    REVOKE_ACCESS = "revoke_access"
    ADMIN_ACTION = "admin_action"


@dataclass
class TenantResource:
    """Represents a resource that belongs to a tenant.

    Used for tenant isolation checks to ensure resources are only
    accessible by their owning tenant.

    Attributes:
        resource_id: Unique identifier of the resource.
        resource_type: Type of the resource (e.g., 'clone', 'booking').
        tenant_id: ID of the tenant that owns this resource.
        created_at: When the resource was created.
    """

    resource_id: str
    resource_type: str
    tenant_id: str
    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass
class TenantIsolationCheck:
    """Result of a tenant isolation verification.

    Attributes:
        resource: The resource being checked.
        requesting_tenant_id: Tenant ID of the requester.
        is_isolated: Whether the resource is properly isolated.
        violation_reason: If not isolated, why not.
    """

    resource: TenantResource
    requesting_tenant_id: str
    is_isolated: bool
    violation_reason: Optional[str] = None

    def __post_init__(self) -> None:
        """Validate the isolation check result."""
        if not self.is_isolated and self.violation_reason is None:
            self.violation_reason = (
                f"Tenant '{self.requesting_tenant_id}' cannot access "
                f"resource '{self.resource.resource_id}' of type "
                f"'{self.resource.resource_type}' belonging to tenant "
                f"'{self.resource.tenant_id}'"
            )