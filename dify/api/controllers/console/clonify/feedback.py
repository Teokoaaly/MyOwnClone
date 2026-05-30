"""Clonify feedback API — thumbs up/down on clone responses."""

import logging
from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import func, select

from controllers.common.schema import register_schema_models
from controllers.console import console_ns
from controllers.console.wraps import account_initialization_required, setup_required
from extensions.ext_database import db
from libs.login import current_account_with_tenant, login_required
from models.clonify import Feedback

logger = logging.getLogger(__name__)


class FeedbackPayload(BaseModel):
    clone_id: str
    message_id: str
    rating: str = Field(pattern="^(up|down)$")
    comment: str | None = None


register_schema_models(console_ns, FeedbackPayload)


@console_ns.route("/clonify/feedback")
class FeedbackApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        account, _ = current_account_with_tenant()
        data = FeedbackPayload.model_validate(request.json)

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


@console_ns.route("/clonify/feedback/stats")
class FeedbackStatsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        clone_id = request.args.get("clone_id")
        if not clone_id:
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
