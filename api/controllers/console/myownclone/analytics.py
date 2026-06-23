"""MyOwnClone analytics API — questions, gaps, and usage data for the creator dashboard."""

import logging

from flask_restx import Resource
from sqlalchemy import func, select

from api.controllers.common.schema import register_response_schema_models
from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.extensions.ext_database import db
from api.fields.base import ResponseModel
from api.libs.login import current_account_with_tenant, login_required
from api.models import Conversation, Message
from api.models.analytics import CostCategory
from api.models.myownclone import AnalyticsGap, AnalyticsQuestion, CostTracking, CloneConfig

logger = logging.getLogger(__name__)

# Defect #3: explicit mapping from the typed ``CostCategory`` enum to the
# response field names. Replaces the previous implicit ``f"{row[0]}_cents"``
# derivation, which silently coupled the API response shape to raw DB string
# values and dropped/mis-bucketed any category whose name did not happen to
# match the ``<value>_cents`` convention.
_COST_CATEGORY_TO_FIELD: dict[CostCategory, str] = {
    CostCategory.CLONE_RESPONSE: "clone_response_cents",
    CostCategory.CONTENT_INGESTION: "content_ingestion_cents",
    CostCategory.PLATFORM_OPS: "platform_ops_cents",
}


def _verify_clone_access(clone_id: str, tenant_id: str) -> None:
    from werkzeug.exceptions import NotFound
    # SECURITY (H5): scope the clone by tenant unconditionally. The previous
    # `tenant_id.startswith("proxy-")` carve-out disabled tenant scoping for any
    # caller able to inject such a prefix, which is a latent cross-tenant read
    # vector. Legitimate proxy/service accounts must use a real tenant_id (or a
    # dedicated platform-admin path), not a magic prefix that skips the check.
    stmt = select(CloneConfig).where(CloneConfig.id == clone_id)
    if tenant_id:
        stmt = stmt.where(CloneConfig.tenant_id == tenant_id)
    clone = db.session.execute(stmt).scalar_one_or_none()
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


@console_ns.route("/myownclone/clones/<string:clone_id>/analytics/overview")
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

        total_conversations = db.session.execute(
            select(func.count(Conversation.id)).where(
                Conversation.clone_id == clone_id,
            )
        ).scalar() or 0

        total_messages = db.session.execute(
            select(func.count(Message.id))
            .select_from(Message)
            .join(Conversation, Conversation.id == Message.conversation_id)
            .where(Conversation.clone_id == clone_id)
        ).scalar() or 0

        return {
            "total_conversations": total_conversations,
            "total_messages": total_messages,
            "questions_answered": questions_answered,
            "gaps_count": gaps_count,
        }, 200


@console_ns.route("/myownclone/clones/<string:clone_id>/analytics/top-questions")
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


@console_ns.route("/myownclone/clones/<string:clone_id>/analytics/gaps")
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


@console_ns.route("/myownclone/clones/<string:clone_id>/analytics/costs")
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

        costs = {field: 0 for field in _COST_CATEGORY_TO_FIELD.values()}
        for category_value, total in rows:
            try:
                category = CostCategory(category_value)
            except ValueError:
                logger.warning(
                    "Unknown cost category %r ignored in breakdown (tenant=%s)",
                    category_value,
                    tenant_id,
                )
                continue
            costs[_COST_CATEGORY_TO_FIELD[category]] = total or 0

        return {**costs, "total_cents": sum(costs.values())}, 200
