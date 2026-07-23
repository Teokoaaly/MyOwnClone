from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NGINX_CONFIG = ROOT / "ops" / "nginx-myownclone.conf"
LOCATION_BLOCK = re.compile(r"location[^\{]+\{(?P<body>[^}]*)\}", re.DOTALL)


def test_frontend_proxies_mark_the_upstream_connection_as_http() -> None:
    config = NGINX_CONFIG.read_text(encoding="utf-8")
    frontend_blocks = [
        match.group("body")
        for match in LOCATION_BLOCK.finditer(config)
        if "proxy_pass http://127.0.0.1:3000" in match.group("body")
    ]

    assert frontend_blocks
    assert all(
        "proxy_set_header X-Forwarded-Proto http;" in block
        for block in frontend_blocks
    )


def test_backend_proxies_preserve_the_public_request_scheme() -> None:
    config = NGINX_CONFIG.read_text(encoding="utf-8")
    backend_blocks = [
        match.group("body")
        for match in LOCATION_BLOCK.finditer(config)
        if "proxy_pass http://127.0.0.1:5001" in match.group("body")
    ]

    assert backend_blocks
    assert all(
        "proxy_set_header X-Forwarded-Proto $scheme;" in block
        for block in backend_blocks
    )
