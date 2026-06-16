"""Deploy trigger API — runs git pull + npm build + systemctl restart on the frontend.

Protected by DEPLOY_SECRET (request header X-Deploy-Secret or env var).
Intended for CI/CD automation (e.g. GitHub webhook) hitting the backend API.
"""

import hmac
import logging
import os
import re
import shlex
import subprocess

from flask import Blueprint, jsonify, request

logger = logging.getLogger(__name__)

deploy_bp = Blueprint("deploy", __name__, url_prefix="/api")

# Internal paths that should not be exposed in HTTP responses
INTERNAL_PATHS = ["/opt/myownclone-frontend", "/home/", "/var/", "/app/"]

# Regex patterns for sanitization
_PATH_PATTERN = re.compile(r"(?:/[\w\-\.]+)+/?")
_ENV_VAR_PATTERN = re.compile(r"\b[A-Z_][A-Z0-9_]*\s*=\s*[^\s]+")
_INTERNAL_IP_PATTERN = re.compile(r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3})\b")
_STACK_TRACE_PATTERN = re.compile(r"File\s+\"[^\"]+\",\s+line\s+\d+,\s+in\s+\w+|Traceback \(most recent call last\)|^\s+at\s+[\w\.]+\(.*\)$", re.MULTILINE)


def _sanitize_output(output: str, max_length: int = 500) -> str:
    """Remove internal paths, env vars, IPs, stack traces and truncate output before sending in response."""
    if not output:
        return ""
    # Remove stack traces first
    output = _STACK_TRACE_PATTERN.sub("[stack trace]", output)
    # Remove internal paths from output
    for path in INTERNAL_PATHS:
        output = output.replace(path, "[internal]")
    # Remove other common file paths
    output = _PATH_PATTERN.sub("[path]", output)
    # Remove environment variables
    output = _ENV_VAR_PATTERN.sub("[ENV_VAR]", output)
    # Remove internal IPs
    output = _INTERNAL_IP_PATTERN.sub("[internal-ip]", output)
    # Truncate long output
    if len(output) > max_length:
        output = output[:max_length] + "... [truncated]"
    return output


def _log_full_output(step: str, output: str) -> None:
    """Log full output internally for debugging without exposing in HTTP response."""
    logger.debug("Full output for '%s': %s", step, output)


def _check_secret() -> bool:
    """Validate the deploy secret from header or env using a timing-safe compare."""
    env_secret = os.getenv("DEPLOY_SECRET", "")
    if not env_secret:
        return False
    header_secret = request.headers.get("X-Deploy-Secret", "")
    if not header_secret:
        return False
    return hmac.compare_digest(header_secret.encode("utf-8"), env_secret.encode("utf-8"))


def _run(cmd: str, cwd: str | None = None, timeout: int = 120) -> tuple[int, str]:
    """Run a shell command, return (returncode, stdout+stderr)."""
    try:
        result = subprocess.run(
            shlex.split(cmd),
            shell=False,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        output = (result.stdout or "") + (result.stderr or "")
        return result.returncode, output
    except subprocess.TimeoutExpired:
        return 124, f"Command timed out after {timeout}s"
    except Exception as e:
        return 1, str(e)


@deploy_bp.route("/deploy", methods=["POST"])
def trigger_deploy():
    """Trigger a frontend deploy: git pull + npm run build + systemctl restart.

    Requires X-Deploy-Secret header matching the DEPLOY_SECRET env var.
    Returns JSON with status and output from each step.
    """
    if not _check_secret():
        logger.warning("Deploy attempt with invalid or missing secret from %s", request.remote_addr)
        return jsonify({"error": "invalid or missing deploy secret"}), 401

    frontend_dir = "/opt/myownclone-frontend/MyOwnClone"
    service_name = "myownclone-frontend"

    steps = []
    overall_status = "success"

    #1. git pull
    code, out = _run("git pull origin master", cwd=frontend_dir)
    _log_full_output("git pull", out)
    steps.append({"step": "git pull", "returncode": code, "output": _sanitize_output(out)})
    if code != 0:
        overall_status = "failed"
        return jsonify({"status": overall_status, "steps": steps}), 200

    # 2. npm run build
    code, out = _run("npm run build", cwd=frontend_dir)
    _log_full_output("npm run build", out)
    steps.append({"step": "npm run build", "returncode": code, "output": _sanitize_output(out)})
    if code != 0:
        overall_status = "failed"
        return jsonify({"status": overall_status, "steps": steps}), 200

    # 3. systemctl restart
    code, out = _run(f"systemctl restart {service_name}")
    _log_full_output("systemctl restart", out)
    steps.append({"step": f"systemctl restart {service_name}", "returncode": code, "output": _sanitize_output(out)})
    if code != 0:
        overall_status = "failed"

    logger.info("Deploy triggered — status: %s", overall_status)
    return jsonify({"status": overall_status, "steps": steps}), 200
