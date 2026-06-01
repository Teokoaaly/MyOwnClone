"""MyOwnClone booking & meeting API — CRUD for meeting types, availability, and bookings."""

import logging
from datetime import date as date_type, time as time_type

from flask import request
from flask_restx import Resource
from pydantic import BaseModel, Field
from sqlalchemy import select
from werkzeug.exceptions import NotFound

from controllers.common.schema import register_response_schema_models, register_schema_models
from controllers.console import console_ns
from controllers.console.wraps import account_initialization_required, setup_required
from extensions.ext_database import db
from libs.login import current_account_with_tenant, login_required
from models.myownclone import Availability, Booking, CloneConfig, MeetingType_, Product

logger = logging.getLogger(__name__)


class MeetingTypePayload(BaseModel):
    name: str
    duration_minutes: int = 30
    price_cents: int = 0
    description: str | None = None
    color: str = "#6366f1"
    active: bool = True


class AvailabilityPayload(BaseModel):
    day_of_week: int = Field(ge=0, le=6)
    start_time: str
    end_time: str
    buffer_minutes: int = 15


class BookingPayload(BaseModel):
    meeting_type_id: str
    visitor_name: str
    visitor_email: str
    date: str
    start_time: str


class ProductPayload(BaseModel):
    name: str
    description: str | None = None
    price_cents: int | None = None
    url: str | None = None
    image_url: str | None = None
    priority: int = 0
    active: bool = True


register_schema_models(
    console_ns, MeetingTypePayload, AvailabilityPayload, BookingPayload, ProductPayload
)


# Meeting Types
@console_ns.route("/myownclone/clones/<string:clone_id>/meeting-types")
class MeetingTypeApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        items = db.session.execute(
            select(MeetingType_).where(MeetingType_.clone_id == clone_id)
            .order_by(MeetingType_.name)
        ).scalars().all()
        return [
            {"id": t.id, "name": t.name, "duration_minutes": t.duration_minutes,
             "price_cents": t.price_cents, "description": t.description,
             "color": t.color, "active": t.active}
            for t in items
        ], 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        data = MeetingTypePayload.model_validate(request.json)
        mt = MeetingType_(clone_id=clone_id, **data.model_dump(exclude={"id"}), id=None)
        db.session.add(mt)
        db.session.commit()
        return {"id": mt.id, "name": mt.name}, 201


# Availability
@console_ns.route("/myownclone/clones/<string:clone_id>/availability")
class AvailabilityApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        items = db.session.execute(
            select(Availability).where(Availability.clone_id == clone_id)
            .order_by(Availability.day_of_week, Availability.start_time)
        ).scalars().all()
        return [
            {"id": a.id, "day_of_week": a.day_of_week, "start_time": str(a.start_time),
             "end_time": str(a.end_time), "buffer_minutes": a.buffer_minutes}
            for a in items
        ], 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        data = AvailabilityPayload.model_validate(request.json)
        av = Availability(clone_id=clone_id, **data.model_dump(exclude={"id"}), id=None)
        db.session.add(av)
        db.session.commit()
        return {"id": av.id}, 201


# Products
@console_ns.route("/myownclone/clones/<string:clone_id>/products")
class ProductsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def post(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        data = ProductPayload.model_validate(request.json)
        prod = Product(clone_id=clone_id, **data.model_dump(exclude={"id"}), id=None)
        db.session.add(prod)
        db.session.commit()
        return {"id": prod.id, "name": prod.name}, 201


# Bookings
@console_ns.route("/myownclone/clones/<string:clone_id>/bookings")
class BookingsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        bookings = db.session.execute(
            select(Booking).where(
                Booking.meeting_type_id.in_(
                    select(MeetingType_.id).where(MeetingType_.clone_id == clone_id)
                )
            ).order_by(Booking.date.desc(), Booking.start_time)
        ).scalars().all()
        return [
            {
                "id": b.id, "meeting_type_id": b.meeting_type_id,
                "visitor_name": b.visitor_name, "visitor_email": b.visitor_email,
                "date": str(b.date) if b.date else None,
                "start_time": str(b.start_time) if b.start_time else None,
                "end_time": str(b.end_time) if b.end_time else None,
                "status": b.status, "meeting_url": b.meeting_url,
            }
            for b in bookings
        ], 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        data = BookingPayload.model_validate(request.json)

        booking_date = date_type.fromisoformat(data.date) if data.date else None
        start_t = time_type.fromisoformat(data.start_time) if data.start_time else None

        if booking_date and start_t:
            conflict = db.session.execute(
                select(Booking).where(
                    Booking.meeting_type_id == data.meeting_type_id,
                    Booking.date == booking_date,
                    Booking.start_time == start_t,
                    Booking.status != "cancelled",
                )
            ).scalar_one_or_none()
            if conflict:
                return {"error": "Time slot already booked for this meeting type"}, 409

        booking = Booking(
            meeting_type_id=data.meeting_type_id,
            visitor_name=data.visitor_name,
            visitor_email=data.visitor_email,
            date=booking_date,
            start_time=start_t,
            status="confirmed",
        )
        db.session.add(booking)
        db.session.commit()
        return {
            "id": booking.id, "status": booking.status,
            "visitor_name": booking.visitor_name,
        }, 201


def _verify_clone_access(clone_id: str, tenant_id: str) -> None:
    clone = db.session.execute(
        select(CloneConfig).where(
            CloneConfig.id == clone_id,
            CloneConfig.tenant_id == tenant_id,
        )
    ).scalar_one_or_none()
    if not clone:
        raise NotFound("clone not found")
