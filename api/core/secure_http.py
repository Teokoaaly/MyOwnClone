from __future__ import annotations

import ipaddress
import socket
from dataclasses import dataclass
from urllib.parse import urljoin, urlparse

import requests

_CLOUD_METADATA_HOSTS = frozenset(
    {
        "169.254.169.254",
        "metadata.google.internal",
        "metadata",
        "169.254.170.2",
        "fd00:ec2::254",
    }
)
_REDIRECT_STATUS_CODES = frozenset({301, 302, 303, 307, 308})
_MAX_REDIRECTS = 5


@dataclass(frozen=True, slots=True)
class UnsafeURLError(ValueError):
    reason: str

    def __str__(self) -> str:
        return self.reason


def _is_blocked_ip(ip: ipaddress.IPv4Address | ipaddress.IPv6Address) -> bool:
    return (
        ip.is_private
        or ip.is_loopback
        or ip.is_link_local
        or ip.is_reserved
        or ip.is_multicast
        or ip.is_unspecified
    )


def _is_safe_url(url: str) -> None:
    if not url:
        raise UnsafeURLError("empty url")

    parsed = urlparse(url)
    if parsed.scheme.lower() not in ("http", "https"):
        raise UnsafeURLError(f"scheme not allowed: {parsed.scheme!r}")

    host = parsed.hostname
    if not host:
        raise UnsafeURLError("missing host")
    if parsed.username is not None or parsed.password is not None:
        raise UnsafeURLError("userinfo is not allowed")
    if host.lower() in _CLOUD_METADATA_HOSTS:
        raise UnsafeURLError(f"cloud metadata host blocked: {host}")

    try:
        literal_ip = ipaddress.ip_address(host)
    except ValueError:
        literal_ip = None
    if literal_ip is not None:
        if _is_blocked_ip(literal_ip):
            raise UnsafeURLError(f"ip address blocked: {literal_ip}")
        return

    try:
        addresses = socket.getaddrinfo(host, None)
    except socket.gaierror as exc:
        raise UnsafeURLError(f"unable to resolve host {host!r}: {exc}") from exc

    resolved_ips = {
        ipaddress.ip_address(address[4][0].split("%", 1)[0]) for address in addresses
    }
    if not resolved_ips:
        raise UnsafeURLError(f"host {host!r} did not resolve to any IP")
    blocked_ip = next((ip for ip in resolved_ips if _is_blocked_ip(ip)), None)
    if blocked_ip is not None:
        raise UnsafeURLError(f"host {host!r} resolves to blocked ip {blocked_ip}")


def _request_public_url(url: str, timeout: int) -> requests.Response:
    current_url = url
    for _redirect_count in range(_MAX_REDIRECTS + 1):
        _is_safe_url(current_url)
        response = requests.get(
            current_url,
            timeout=timeout,
            headers={"User-Agent": "MyOwnClone/1.0"},
            allow_redirects=False,
        )
        if response.status_code not in _REDIRECT_STATUS_CODES:
            response.raise_for_status()
            return response
        location = response.headers.get("Location", "").strip()
        if not location:
            raise UnsafeURLError("redirect without location")
        current_url = urljoin(current_url, location)
    raise UnsafeURLError("too many redirects")
