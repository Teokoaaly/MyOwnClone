"""MyOwnClone booking & meeting API — CRUD for meeting types, availability, and bookings."""

import logging
from datetime import date as date_type, time as time_type

from flask import request
from flask_restx import Resource
from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator, model_validator
from sqlalchemy import select
from werkzeug.exceptions import NotFound

from api.controllers.common.schema import register_response_schema_models, register_schema_models
from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.extensions.ext_database import db
from api.libs.login import current_account_with_tenant, login_required
from api.models.myownclone import Availability, Booking, CloneConfig, MeetingType_, Product

logger = logging.getLogger(__name__)


class MeetingTypePayload(BaseModel):
    name: str = Field(min_length=1)
    duration_minutes: int = Field(default=30, ge=5, le=480)
    price_cents: int = Field(default=0, ge=0)
    description: str | None = None
    color: str = Field(default="#6366f1", pattern=r"^#[0-9A-Fa-f]{6}$")
    active: bool = True


class AvailabilityPayload(BaseModel):
    day_of_week: int = Field(ge=0, le=6)
    start_time: str
    end_time: str
    buffer_minutes: int = Field(default=15, ge=0, le=240)

    @field_validator("end_time")
    @classmethod
    def end_must_be_after_start(cls, value: str, info):
        start = info.data.get("start_time")
        if start and _parse_time(value) <= _parse_time(start):
            raise ValueError("end_time must be after start_time")
        return value


class BookingPayload(BaseModel):
    meeting_type_id: str = Field(..., min_length=1)
    visitor_name: str = Field(..., min_length=1, max_length=200)
    visitor_email: EmailStr
    date: str
    start_time: str

    @field_validator("date")
    @classmethod
    def validate_date(cls, v: str) -> str:
        try:
            _parse_date(v)
        except ValueError:
            raise ValueError("date must be in YYYY-MM-DD format")
        return v

    @field_validator("start_time")
    @classmethod
    def validate_start_time(cls, v: str) -> str:
        try:
            _parse_time(v)
        except ValueError:
            raise ValueError("start_time must be in HH:MM or HH:MM:SS format")
        return v


class BookingCreate(BaseModel):
    meeting_type_id: str = Field(..., min_length=1)
    visitor_name: str = Field(..., min_length=1, max_length=200)
    visitor_email: EmailStr
    date: str
    start_time: str | None = None

    @field_validator("date")
    @classmethod
    def validate_date(cls, v: str) -> str:
        if not v:
            raise ValueError("date is required")
        try:
            _parse_date(v)
        except ValueError:
            raise ValueError("date must be in YYYY-MM-DD format")
        return v

    @field_validator("start_time")
    @classmethod
    def validate_start_time(cls, v: str | None) -> str | None:
        if v is None:
            return v
        try:
            _parse_time(v)
        except ValueError:
            raise ValueError("start_time must be in HH:MM or HH:MM:SS format")
        return v


class BookingUpdate(BaseModel):
    status: str = Field(...)

    @model_validator(mode="after")
    def validate_status(self):
        if self.status not in {"confirmed", "cancelled", "completed"}:
            raise ValueError("status must be one of: confirmed, cancelled, completed")
        return self


class ProductPayload(BaseModel):
    name: str = Field(min_length=1)
    description: str | None = None
    price_cents: int | None = Field(default=None, ge=0)
    url: str | None = None
    image_url: str | None = None
    priority: int = 0
    active: bool = True


register_schema_models(
    console_ns, MeetingTypePayload, AvailabilityPayload, BookingPayload, BookingCreate, BookingUpdate, ProductPayload
)


def _product_to_dict(product: Product) -> dict:
    return {
        "id": product.id,
        "clone_id": product.clone_id,
        "name": product.name,
        "description": product.description,
        "price_cents": product.price_cents,
        "url": product.url,
        "image_url": product.image_url,
        "priority": product.priority,
        "active": product.active,
    }


def _meeting_type_to_dict(meeting_type: MeetingType_) -> dict:
    return {
        "id": meeting_type.id,
        "clone_id": meeting_type.clone_id,
        "name": meeting_type.name,
        "duration_minutes": meeting_type.duration_minutes,
        "price_cents": meeting_type.price_cents,
        "description": meeting_type.description,
        "color": meeting_type.color,
        "active": meeting_type.active,
    }


def _availability_to_dict(availability: Availability) -> dict:
    return {
        "id": availability.id,
        "clone_id": availability.clone_id,
        "day_of_week": availability.day_of_week,
        "start_time": str(availability.start_time) if availability.start_time else None,
        "end_time": str(availability.end_time) if availability.end_time else None,
        "buffer_minutes": availability.buffer_minutes,
    }


def _booking_to_dict(booking: Booking) -> dict:
    return {
        "id": booking.id,
        "meeting_type_id": booking.meeting_type_id,
        "visitor_name": booking.visitor_name,
        "visitor_email": booking.visitor_email,
        "date": str(booking.date) if booking.date else None,
        "start_time": str(booking.start_time) if booking.start_time else None,
        "end_time": str(booking.end_time) if booking.end_time else None,
        "status": booking.status,
        "meeting_url": booking.meeting_url,
    }


def _parse_time(value: str) -> time_type:
    return time_type.fromisoformat(value)


def _parse_date(value: str) -> date_type:
    return date_type.fromisoformat(value)


def _availability_payload_values(payload: AvailabilityPayload) -> dict:
    values = payload.model_dump()
    values["start_time"] = _parse_time(values["start_time"])
    values["end_time"] = _parse_time(values["end_time"])
    return values


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
        return [_meeting_type_to_dict(t) for t in items], 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        try:
            data = MeetingTypePayload.model_validate(request.json)
        except ValidationError as e:
            return {"errors": e.errors()}, 422
        mt = MeetingType_(clone_id=clone_id, **data.model_dump(exclude={"id"}), id=None)
        db.session.add(mt)
        db.session.commit()
        return _meeting_type_to_dict(mt), 201


@console_ns.route("/myownclone/clones/<string:clone_id>/meeting-types/<string:meeting_type_id>")
class MeetingTypeItemApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str, meeting_type_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        meeting_type = _get_meeting_type_or_404(clone_id, meeting_type_id)
        return _meeting_type_to_dict(meeting_type), 200

    @login_required
    @account_initialization_required
    @setup_required
    def put(self, clone_id: str, meeting_type_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        meeting_type = _get_meeting_type_or_404(clone_id, meeting_type_id)
        try:
            data = MeetingTypePayload.model_validate(request.json)
        except ValidationError as e:
            return {"errors": e.errors()}, 422
        for key, value in data.model_dump().items():
            setattr(meeting_type, key, value)
        db.session.commit()
        return _meeting_type_to_dict(meeting_type), 200

    @login_required
    @account_initialization_required
    @setup_required
    def delete(self, clone_id: str, meeting_type_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        meeting_type = _get_meeting_type_or_404(clone_id, meeting_type_id)
        has_bookings = db.session.execute(
            select(Booking.id)
            .where(Booking.meeting_type_id == meeting_type_id)
            .limit(1)
        ).scalar_one_or_none()
        if has_bookings:
            meeting_type.active = False
            db.session.commit()
            return {"deleted": False, "deactivated": True, "id": meeting_type_id}, 200
        db.session.delete(meeting_type)
        db.session.commit()
        return {"deleted": True, "id": meeting_type_id}, 200


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
        return [_availability_to_dict(a) for a in items], 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        try:
            data = AvailabilityPayload.model_validate(request.json)
        except ValidationError as e:
            return {"errors": e.errors()}, 422
        av = Availability(clone_id=clone_id, **_availability_payload_values(data), id=None)
        db.session.add(av)
        db.session.commit()
        return _availability_to_dict(av), 201


@console_ns.route("/myownclone/clones/<string:clone_id>/availability/<string:availability_id>")
class AvailabilityItemApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str, availability_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        availability = _get_availability_or_404(clone_id, availability_id)
        return _availability_to_dict(availability), 200

    @login_required
    @account_initialization_required
    @setup_required
    def put(self, clone_id: str, availability_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        availability = _get_availability_or_404(clone_id, availability_id)
        try:
            data = AvailabilityPayload.model_validate(request.json)
        except ValidationError as e:
            return {"errors": e.errors()}, 422
        for key, value in _availability_payload_values(data).items():
            setattr(availability, key, value)
        db.session.commit()
        return _availability_to_dict(availability), 200

    @login_required
    @account_initialization_required
    @setup_required
    def delete(self, clone_id: str, availability_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        availability = _get_availability_or_404(clone_id, availability_id)
        db.session.delete(availability)
        db.session.commit()
        return {"deleted": True, "id": availability_id}, 200


# Products
@console_ns.route("/myownclone/clones/<string:clone_id>/products")
class ProductsApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        items = db.session.execute(
            select(Product)
            .where(Product.clone_id == clone_id)
            .order_by(Product.priority.desc(), Product.name)
        ).scalars().all()
        return [_product_to_dict(item) for item in items], 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        try:
            data = ProductPayload.model_validate(request.json)
        except ValidationError as e:
            return {"errors": e.errors()}, 422
        prod = Product(clone_id=clone_id, **data.model_dump(exclude={"id"}), id=None)
        db.session.add(prod)
        db.session.commit()
        return _product_to_dict(prod), 201


@console_ns.route("/myownclone/clones/<string:clone_id>/products/<string:product_id>")
class ProductApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str, product_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        product = _get_product_or_404(clone_id, product_id)
        return _product_to_dict(product), 200

    @login_required
    @account_initialization_required
    @setup_required
    def put(self, clone_id: str, product_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        product = _get_product_or_404(clone_id, product_id)
        try:
            data = ProductPayload.model_validate(request.json)
        except ValidationError as e:
            return {"errors": e.errors()}, 422
        for key, value in data.model_dump().items():
            setattr(product, key, value)
        db.session.commit()
        return _product_to_dict(product), 200

    @login_required
    @account_initialization_required
    @setup_required
    def delete(self, clone_id: str, product_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        product = _get_product_or_404(clone_id, product_id)
        db.session.delete(product)
        db.session.commit()
        return {"deleted": True, "id": product_id}, 200


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
        return [_booking_to_dict(b) for b in bookings], 200

    @login_required
    @account_initialization_required
    @setup_required
    def post(self, clone_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        try:
            data = BookingCreate.model_validate(request.json)
        except ValidationError as e:
            return {"errors": e.errors()}, 422
        meeting_type = _get_meeting_type_or_404(clone_id, data.meeting_type_id)

        booking_date = _parse_date(data.date) if data.date else None
        start_t = _parse_time(data.start_time) if data.start_time else None

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
            meeting_type_id=meeting_type.id,
            visitor_name=data.visitor_name,
            visitor_email=data.visitor_email,
            date=booking_date,
            start_time=start_t,
            status="confirmed",
        )
        db.session.add(booking)
        db.session.commit()
        return _booking_to_dict(booking), 201


@console_ns.route("/myownclone/clones/<string:clone_id>/bookings/<string:booking_id>")
class BookingItemApi(Resource):
    @login_required
    @account_initialization_required
    @setup_required
    def get(self, clone_id: str, booking_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        booking = _get_booking_or_404(clone_id, booking_id)
        return _booking_to_dict(booking), 200

    @login_required
    @account_initialization_required
    @setup_required
    def put(self, clone_id: str, booking_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        booking = _get_booking_or_404(clone_id, booking_id)
        try:
            data = BookingUpdate.model_validate(request.json)
        except ValidationError as e:
            return {"errors": e.errors()}, 422
        booking.status = data.status
        db.session.commit()
        return _booking_to_dict(booking), 200

    @login_required
    @account_initialization_required
    @setup_required
    def delete(self, clone_id: str, booking_id: str):
        account, tenant_id = current_account_with_tenant()
        _verify_clone_access(clone_id, tenant_id)
        booking = _get_booking_or_404(clone_id, booking_id)
        booking.status = "cancelled"
        db.session.commit()
        return _booking_to_dict(booking), 200


def _verify_clone_access(clone_id: str, tenant_id: str) -> None:
    clone = db.session.execute(
        select(CloneConfig).where(
            CloneConfig.id == clone_id,
            CloneConfig.tenant_id == tenant_id,
        )
    ).scalar_one_or_none()
    if not clone:
        raise NotFound("clone not found")


def _get_product_or_404(clone_id: str, product_id: str) -> Product:
    product = db.session.execute(
        select(Product).where(
            Product.id == product_id,
            Product.clone_id == clone_id,
        )
    ).scalar_one_or_none()
    if not product:
        raise NotFound("product not found")
    return product


def _get_meeting_type_or_404(clone_id: str, meeting_type_id: str) -> MeetingType_:
    meeting_type = db.session.execute(
        select(MeetingType_).where(
            MeetingType_.id == meeting_type_id,
            MeetingType_.clone_id == clone_id,
        )
    ).scalar_one_or_none()
    if not meeting_type:
        raise NotFound("meeting type not found")
    return meeting_type


def _get_availability_or_404(clone_id: str, availability_id: str) -> Availability:
    availability = db.session.execute(
        select(Availability).where(
            Availability.id == availability_id,
            Availability.clone_id == clone_id,
        )
    ).scalar_one_or_none()
    if not availability:
        raise NotFound("availability not found")
    return availability


def _get_booking_or_404(clone_id: str, booking_id: str) -> Booking:
    booking = db.session.execute(
        select(Booking)
        .join(MeetingType_, MeetingType_.id == Booking.meeting_type_id)
        .where(
            Booking.id == booking_id,
            MeetingType_.clone_id == clone_id,
        )
    ).scalar_one_or_none()
    if not booking:
        raise NotFound("booking not found")
    return booking
