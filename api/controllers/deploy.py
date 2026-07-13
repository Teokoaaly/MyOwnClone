"""Deploy trigger API — runs git pull + npm build + systemctl restart on the frontend.

Protected by DEPLOY_SECRET (request header X-Deploy-Secret or env var).
Intended for CI/CD automation (e.g. GitHub webhook) hitting the backend API.
"""

import hmac
import logging
import os
import subprocess

from flask import Blueprint, jsonify, request

logger = logging.getLogger(__name__)

deploy_bp = Blueprint("deploy", __name__, url_prefix="/api")


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
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        output = (result.stdout or "") + (result.stderr or "")
        return result.returncode, output
    except subprocess.TimeoutExpired:
        return 124, f"Command timed out after {timeout}s: {cmd}"
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
    steps.append({"step": "git pull", "returncode": code, "output": out})
    if code != 0:
        overall_status = "failed"
        return jsonify({"status": overall_status, "steps": steps}), 200

    # 2. npm run build
    code, out = _run("npm run build", cwd=frontend_dir)
    steps.append({"step": "npm run build", "returncode": code, "output": out})
    if code != 0:
        overall_status = "failed"
        return jsonify({"status": overall_status, "steps": steps}), 200

    # 3. systemctl restart
    code, out = _run(f"systemctl restart {service_name}")
    steps.append({"step": f"systemctl restart {service_name}", "returncode": code, "output": out})
    if code != 0:
        overall_status = "failed"

    logger.info("Deploy triggered — status: %s", overall_status)
    return jsonify({"status": overall_status, "steps": steps}), 200
