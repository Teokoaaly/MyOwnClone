import enum
from datetime import date, datetime, time as time_type
from typing import Optional

import sqlalchemy as sa
from sqlalchemy import Boolean, Date, DateTime, Integer, String, Time, func, text
from sqlalchemy.orm import Mapped, mapped_column

from libs.datetime_utils import naive_utc_now
from libs.uuid_utils import uuidv7

from ..base import DefaultFieldsDCMixin, TypeBase
from ..types import LongText


class MeetingType_(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "meeting_types"

    clone_id: Mapped[str] = mapped_column(String(36), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, server_default=text("30"), default=30)
    price_cents: Mapped[int] = mapped_column(Integer, server_default=text("0"), default=0)
    description: Mapped[Optional[str]] = mapped_column(LongText, nullable=True, default=None)
    color: Mapped[str] = mapped_column(String(7), server_default=text("'#6366f1'"), default="#6366f1")
    active: Mapped[bool] = mapped_column(Boolean, server_default=text("true"), default=True)


class Availability(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "availability"

    clone_id: Mapped[str] = mapped_column(String(36), nullable=False)
    day_of_week: Mapped[int] = mapped_column(Integer, nullable=False)
    start_time: Mapped[time_type] = mapped_column(Time, nullable=False)
    end_time: Mapped[time_type] = mapped_column(Time, nullable=False)
    buffer_minutes: Mapped[int] = mapped_column(Integer, server_default=text("15"), default=15)


class BookingStatus(enum.StrEnum):
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"


class Booking(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "bookings"

    meeting_type_id: Mapped[str] = mapped_column(String(36), nullable=False)
    visitor_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    visitor_email: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    start_time: Mapped[Optional[time_type]] = mapped_column(Time, nullable=True)
    end_time: Mapped[Optional[time_type]] = mapped_column(Time, nullable=True)
    status: Mapped[str] = mapped_column(String(20), server_default=text("'confirmed'"), default="confirmed")
    meeting_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True, default=None)
    recording_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True, default=None)
    transcript: Mapped[Optional[str]] = mapped_column(LongText, nullable=True, default=None)
    notes: Mapped[Optional[str]] = mapped_column(LongText, nullable=True, default=None)


class Product(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "products"

    clone_id: Mapped[str] = mapped_column(String(36), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(LongText, nullable=True)
    price_cents: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    image_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    priority: Mapped[int] = mapped_column(Integer, server_default=text("0"), default=0)
    active: Mapped[bool] = mapped_column(Boolean, server_default=text("true"), default=True)
