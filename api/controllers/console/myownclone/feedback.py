"""MyOwnClone feedback API — thumbs up/down on clone responses."""

import logging
from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import func, select

from api.controllers.common.schema import register_schema_models
from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.extensions.ext_database import db
from api.libs.login import current_account_with_tenant, login_required
from api.models.myownclone import CloneConfig, Feedback

logger = logging.getLogger(__name__)


def _clone_owned_by_tenant(clone_id: str, tenant_id: str | None) -> bool:
    """SECURITY (H2): ensure the clone belongs to the caller's tenant before any
    feedback read/write. Returns True only when a CloneConfig row exists for the
    given clone_id scoped to tenant_id."""
    if not clone_id or not tenant_id:
        return False
    found = db.session.execute(
        select(CloneConfig.id).where(
            CloneConfig.id == clone_id,
            CloneConfig.tenant_id == tenant_id,
        )
    ).scalar_one_or_none()
    return found is not None


class FeedbackPayload(BaseModel):
    clone_id: str
    message_id: str
    rating: str = Field(pattern="^(up|down)$")
    comment: str | None = None


register_schema_models(console_ns, FeedbackPayload)


@console_ns.route("/myownclone/feedback")
class FeedbackApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        account, tenant_id = current_account_with_tenant()
        data = FeedbackPayload.model_validate(request.json)

        # SECURITY (H2): reject feedback against clones the caller doesn't own.
        if not _clone_owned_by_tenant(data.clone_id, tenant_id):
            return {"error": "clone not found"}, 404

        fb = Feedback(
            clone_id=data.clone_id,
            message_id=data.message_id,
            rating=data.rating,
            comment=data.comment,
        )
        db.session.add(fb)
        db.session.commit()

        logger.info(
            "Feedback: clone=%s message=%s rating=%s user=%s",
            data.clone_id,
            data.message_id,
            data.rating,
            account.id,
        )

        return {"status": "received", "rating": data.rating}, 200


@console_ns.route("/myownclone/feedback/stats")
class FeedbackStatsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        account, tenant_id = current_account_with_tenant()
        clone_id = request.args.get("clone_id")
        if not clone_id:
            return {"up": 0, "down": 0, "total": 0}, 200

        # SECURITY (H2): only return stats for clones the caller owns.
        if not _clone_owned_by_tenant(clone_id, tenant_id):
            return {"up": 0, "down": 0, "total": 0}, 200

        total = db.session.execute(
            select(func.count(Feedback.id)).where(Feedback.clone_id == clone_id)
        ).scalar() or 0
        up = db.session.execute(
            select(func.count(Feedback.id)).where(
                Feedback.clone_id == clone_id,
                Feedback.rating == "up",
            )
        ).scalar() or 0
        down = db.session.execute(
            select(func.count(Feedback.id)).where(
                Feedback.clone_id == clone_id,
                Feedback.rating == "down",
            )
        ).scalar() or 0

        return {"up": up, "down": down, "total": total}, 200
