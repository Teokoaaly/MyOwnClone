"""Clonify analytics API — questions, gaps, and usage data for the creator dashboard."""

import logging

from flask_restx import Resource
from sqlalchemy import func, select

from controllers.common.schema import register_response_schema_models
from controllers.console import console_ns
from controllers.console.wraps import account_initialization_required, setup_required
from extensions.ext_database import db
from fields.base import ResponseModel
from libs.login import current_account_with_tenant, login_required
from models.clonify import AnalyticsGap, AnalyticsQuestion, CostTracking, CloneConfig
from models.model import App, Conversation, Message

logger = logging.getLogger(__name__)


def _verify_clone_access(clone_id: str, tenant_id: str) -> None:
    from werkzeug.exceptions import NotFound
    clone = db.session.execute(
        select(CloneConfig).where(
            CloneConfig.id == clone_id,
            CloneConfig.tenant_id == tenant_id,
        )
    ).scalar_one_or_none()
    if not clone:
        raise NotFound("clone not found")


class AnalyticsOverviewResponse(ResponseModel):
    total_conversations: int = 0
    total_messages: int = 0
    questions_answered: int = 0
    gaps_count: int = 0


class TopQuestionResponse(ResponseModel):
    question: str
    count: int


class GapResponse(ResponseModel):
    id: str
    question: str
    count: int
    suggested_source: str | None = None
    status: str


class CostBreakdownResponse(ResponseModel):
    clone_response_cents: int = 0
    content_ingestion_cents: int = 0
    platform_ops_cents: int = 0
    total_cents: int = 0


register_response_schema_models(
    console_ns,
    AnalyticsOverviewResponse,
    TopQuestionResponse,
    GapResponse,
    CostBreakdownResponse,
)


@console_ns.route("/clonify/clones/<string:clone_id>/analytics/overview")
class AnalyticsOverviewApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)

        gaps_count = db.session.execute(
            select(func.count(AnalyticsGap.id)).where(
                AnalyticsGap.clone_id == clone_id,
                AnalyticsGap.status == "open",
            )
        ).scalar() or 0

        questions_answered = db.session.execute(
            select(func.sum(AnalyticsQuestion.count)).where(
                AnalyticsQuestion.clone_id == clone_id,
            )
        ).scalar() or 0

        # Get the clone's tenant to count related conversations and messages
        clone = db.session.execute(
            select(CloneConfig).where(CloneConfig.id == clone_id)
        ).scalar_one_or_none()

        if clone is None:
            return {"error": "clone not found"}, 404

        # Count conversations for apps belonging to this clone's tenant
        app_ids = [str(a.id) for a in db.session.execute(
            select(App.id).where(App.tenant_id == clone.tenant_id)
        ).scalars().all()]

        total_conversations = 0
        total_messages = 0

        if app_ids:
            total_conversations = db.session.execute(
                select(func.count(Conversation.id)).where(
                    Conversation.app_id.in_(app_ids),
                    Conversation.is_deleted.is_(False),
                )
            ).scalar() or 0

            total_messages = db.session.execute(
                select(func.count(Message.id)).where(
                    Message.app_id.in_(app_ids),
                )
            ).scalar() or 0

        return {
            "total_conversations": total_conversations,
            "total_messages": total_messages,
            "questions_answered": questions_answered,
            "gaps_count": gaps_count,
        }, 200


@console_ns.route("/clonify/clones/<string:clone_id>/analytics/top-questions")
class TopQuestionsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        questions = db.session.execute(
            select(AnalyticsQuestion)
            .where(AnalyticsQuestion.clone_id == clone_id)
            .order_by(AnalyticsQuestion.count.desc())
            .limit(10)
        ).scalars().all()
        return [
            {"question": q.question, "count": q.count}
            for q in questions
        ], 200


@console_ns.route("/clonify/clones/<string:clone_id>/analytics/gaps")
class AnalyticsGapsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        gaps = db.session.execute(
            select(AnalyticsGap)
            .where(AnalyticsGap.clone_id == clone_id)
            .order_by(AnalyticsGap.count.desc())
            .limit(20)
        ).scalars().all()
        return [
            {
                "id": g.id,
                "question": g.question,
                "count": g.count,
                "suggested_source": g.suggested_source,
                "status": g.status,
            }
            for g in gaps
        ], 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        from flask import request
        data = request.json or {}
        gap = AnalyticsGap(
            clone_id=clone_id,
            question=data.get("question", ""),
            count=data.get("count", 1),
            suggested_source=data.get("suggested_source"),
            status="open",
        )
        db.session.add(gap)
        db.session.commit()
        return {
            "id": gap.id,
            "question": gap.question,
            "count": gap.count,
            "status": gap.status,
        }, 201


@console_ns.route("/clonify/clones/<string:clone_id>/analytics/costs")
class CostBreakdownApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        clone = db.session.execute(
            select(CloneConfig).where(
                CloneConfig.id == clone_id,
                CloneConfig.tenant_id == tenant_id,
            )
        ).scalar_one_or_none()
        if not clone:
            return {"error": "clone not found"}, 404

        rows = db.session.execute(
            select(CostTracking.category, func.sum(CostTracking.cost_cents).label("total"))
            .where(CostTracking.tenant_id == tenant_id)
            .group_by(CostTracking.category)
        ).all()

        costs = {
            "clone_response_cents": 0,
            "content_ingestion_cents": 0,
            "platform_ops_cents": 0,
        }
        for row in rows:
            key = f"{row[0]}_cents"
            if key in costs:
                costs[key] = row[1] or 0

        return {**costs, "total_cents": sum(costs.values())}, 200
