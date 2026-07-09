"""Onboarding API endpoints — track tour progress per user.

Provides CRUD for onboarding status and tour step completion.
"""

from __future__ import annotations

import logging

from flask import request, g
from flask_restx import Resource
from sqlalchemy import select

from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.extensions.ext_database import db
from api.libs.login import login_required

logger = logging.getLogger(__name__)


def _account_id() -> str:
    return str(getattr(g, "account_id", "") or "")


@console_ns.route("/myownclone/onboarding/status")
class OnboardingStatusApi(Resource):
    """Get or update onboarding status for the current user."""

    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        from api.models.account import Account
        from api.models.onboarding import OnboardingStep
        from api.core.tour_definitions import TOURS

        account_id = _account_id()
        account = db.session.get(Account, account_id)
        if not account:
            return {"error": "account not found"}, 404

        # Get all completed steps
        steps = db.session.execute(
            select(OnboardingStep).where(OnboardingStep.account_id == account_id)
        ).scalars().all()

        completed_map: dict[str, set[str]] = {}
        for s in steps:
            completed_map.setdefault(s.tour_id, set()).add(s.step_key)

        # Build tour progress
        tours = {}
        for tour_id, definition in TOURS.items():
            completed = completed_map.get(tour_id, set())
            total = len(definition.steps)
            progress = round(len(completed) / total * 100) if total > 0 else 0

            # Current step = first uncompleted
            current_step = None
            for step in definition.steps:
                if step.key not in completed:
                    current_step = step.key
                    break

            tours[tour_id] = {
                "completed_steps": sorted(completed),
                "total_steps": total,
                "progress_percent": progress,
                "current_step": current_step,
                "is_complete": len(completed) >= total,
            }

        return {
            "account_id": account_id,
            "onboarding_status": account.onboarding_status,
            "tours": tours,
        }, 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        from api.models.account import Account, OnboardingStatus

        account_id = _account_id()
        account = db.session.get(Account, account_id)
        if not account:
            return {"error": "account not found"}, 404

        data = request.get_json(silent=True) or {}
        new_status = data.get("status", "").strip()

        if not new_status:
            return {"error": "status is required"}, 400

        # Validate status value
        valid_statuses = [s.value for s in OnboardingStatus]
        if new_status not in valid_statuses:
            return {"error": f"invalid status. Must be one of: {valid_statuses}"}, 400

        account.onboarding_status = new_status
        db.session.commit()

        return {"status": new_status, "message": "Onboarding status updated"}, 200


@console_ns.route("/myownclone/onboarding/tours")
class OnboardingToursApi(Resource):
    """List all tours with progress for the current user."""

    @login_required
    @account_initialization_required
    @setup_required
    def get(self):
        from api.models.onboarding import OnboardingStep
        from api.core.tour_definitions import TOURS

        account_id = _account_id()
        steps = db.session.execute(
            select(OnboardingStep).where(OnboardingStep.account_id == account_id)
        ).scalars().all()

        completed_map: dict[str, set[str]] = {}
        for s in steps:
            completed_map.setdefault(s.tour_id, set()).add(s.step_key)

        tours = []
        for tour_id, definition in TOURS.items():
            completed = completed_map.get(tour_id, set())
            total = len(definition.steps)
            tours.append({
                "id": tour_id,
                "name": definition.name,
                "total_steps": total,
                "completed_steps": len(completed),
                "progress_percent": round(len(completed) / total * 100) if total > 0 else 0,
                "is_complete": len(completed) >= total,
                "steps": [
                    {
                        "key": s.key,
                        "title": s.title,
                        "description": s.description,
                        "position": s.position,
                        "completed": s.key in completed,
                    }
                    for s in definition.steps
                ],
            })

        return {"tours": tours}, 200


@console_ns.route("/myownclone/onboarding/tours/<string:tour_id>/steps/<string:step_key>/complete")
class OnboardingStepCompleteApi(Resource):
    """Mark a tour step as completed."""

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, tour_id: str, step_key: str):
        from api.models.onboarding import OnboardingStep, OnboardingEvent
        from api.core.tour_definitions import get_tour

        account_id = _account_id()
        tour = get_tour(tour_id)
        if not tour:
            return {"error": f"tour '{tour_id}' not found"}, 404

        step_def = tour.get_step(step_key)
        if not step_def:
            return {"error": f"step '{step_key}' not found in tour '{tour_id}'"}, 404

        # Check if already completed
        existing = db.session.execute(
            select(OnboardingStep).where(
                OnboardingStep.account_id == account_id,
                OnboardingStep.tour_id == tour_id,
                OnboardingStep.step_key == step_key,
            )
        ).scalar_one_or_none()

        if existing:
            return {"message": "step already completed", "completed_at": existing.completed_at.isoformat()}, 200

        # Create step completion
        step = OnboardingStep(
            account_id=account_id,
            tour_id=tour_id,
            step_key=step_key,
        )
        db.session.add(step)

        # Log event
        event = OnboardingEvent(
            account_id=account_id,
            event="tour_step_completed",
            tour_id=tour_id,
            step_key=step_key,
        )
        db.session.add(event)
        db.session.commit()

        logger.info("Step completed: account=%s tour=%s step=%s", account_id, tour_id, step_key)
        return {"message": "step completed", "step_key": step_key, "tour_id": tour_id}, 201


@console_ns.route("/myownclone/onboarding/tours/<string:tour_id>/reset")
class OnboardingTourResetApi(Resource):
    """Reset all steps for a tour."""

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, tour_id: str):
        from api.models.onboarding import OnboardingStep, OnboardingEvent
        from api.core.tour_definitions import get_tour

        account_id = _account_id()
        tour = get_tour(tour_id)
        if not tour:
            return {"error": f"tour '{tour_id}' not found"}, 404

        # Delete all steps for this tour
        db.session.query(OnboardingStep).filter(
            OnboardingStep.account_id == account_id,
            OnboardingStep.tour_id == tour_id,
        ).delete()

        # Log event
        event = OnboardingEvent(
            account_id=account_id,
            event="tour_reset",
            tour_id=tour_id,
        )
        db.session.add(event)
        db.session.commit()

        return {"message": f"tour '{tour_id}' reset", "deleted_steps": len(tour.steps)}, 200


@console_ns.route("/myownclone/onboarding/events")
class OnboardingEventsApi(Resource):
    """Log onboarding analytics events."""

    @login_required
    @account_initialization_required
    @setup_required
    def post(self):
        from api.models.onboarding import OnboardingEvent

        account_id = _account_id()
        data = request.get_json(silent=True) or {}

        event_name = data.get("event", "").strip()
        if not event_name:
            return {"error": "event is required"}, 400

        event = OnboardingEvent(
            account_id=account_id,
            event=event_name,
            tour_id=data.get("tour_id"),
            step_key=data.get("step_key"),
            properties=data.get("properties"),
        )
        db.session.add(event)
        db.session.commit()

        return {"message": "event recorded"}, 201
