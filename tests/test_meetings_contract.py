from datetime import date, time

import pytest
from pydantic import ValidationError

from api.controllers.console.myownclone.booking import (
    AvailabilityPayload,
    BookingPayload,
    MeetingTypePayload,
    _availability_payload_values,
    _availability_to_dict,
    _booking_to_dict,
    _meeting_type_to_dict,
    _parse_date,
    _parse_time,
)
from api.models.meeting import Availability, Booking, MeetingType_


def test_meeting_type_payload_validates_public_contract():
    payload = MeetingTypePayload.model_validate({
        "name": "Discovery",
        "duration_minutes": 45,
        "price_cents": 2500,
        "color": "#22c55e",
    })

    assert payload.name == "Discovery"
    assert payload.active is True

    with pytest.raises(ValidationError):
        MeetingTypePayload.model_validate({"name": "", "color": "#22c55e"})

    with pytest.raises(ValidationError):
        MeetingTypePayload.model_validate({"name": "Bad color", "color": "green"})

    with pytest.raises(ValidationError):
        MeetingTypePayload.model_validate({"name": "Bad price", "price_cents": -1})


def test_availability_payload_parses_times_and_rejects_invalid_ranges():
    payload = AvailabilityPayload.model_validate({
        "day_of_week": 1,
        "start_time": "09:00",
        "end_time": "17:30",
        "buffer_minutes": 10,
    })

    values = _availability_payload_values(payload)

    assert values["start_time"] == time(9, 0)
    assert values["end_time"] == time(17, 30)

    with pytest.raises(ValidationError):
        AvailabilityPayload.model_validate({
            "day_of_week": 1,
            "start_time": "17:00",
            "end_time": "09:00",
        })


def test_booking_payload_and_parse_helpers_validate_expected_formats():
    payload = BookingPayload.model_validate({
        "meeting_type_id": "mt_1",
        "visitor_name": "Ada",
        "visitor_email": "ada@example.com",
        "date": "2026-06-12",
        "start_time": "09:15",
    })

    assert _parse_date(payload.date) == date(2026, 6, 12)
    assert _parse_time(payload.start_time) == time(9, 15)

    with pytest.raises(ValidationError):
        BookingPayload.model_validate({
            "meeting_type_id": "mt_1",
            "visitor_name": "",
            "visitor_email": "ada@example.com",
            "date": "2026-06-12",
            "start_time": "09:15",
        })


def test_meeting_serializers_match_frontend_contract():
    meeting_type = MeetingType_(
        id="mt_1",
        clone_id="clone_1",
        name="Discovery",
        duration_minutes=30,
        price_cents=0,
        description="Intro call",
        color="#6366f1",
        active=True,
    )
    availability = Availability(
        id="av_1",
        clone_id="clone_1",
        day_of_week=2,
        start_time=time(10, 0),
        end_time=time(14, 30),
        buffer_minutes=15,
    )
    booking = Booking(
        id="bk_1",
        meeting_type_id="mt_1",
        visitor_name="Ada",
        visitor_email="ada@example.com",
        date=date(2026, 6, 12),
        start_time=time(10, 0),
        end_time=time(10, 30),
        status="confirmed",
        meeting_url="https://meet.example.com/bk_1",
    )

    assert _meeting_type_to_dict(meeting_type) == {
        "id": "mt_1",
        "clone_id": "clone_1",
        "name": "Discovery",
        "duration_minutes": 30,
        "price_cents": 0,
        "description": "Intro call",
        "color": "#6366f1",
        "active": True,
    }
    assert _availability_to_dict(availability) == {
        "id": "av_1",
        "clone_id": "clone_1",
        "day_of_week": 2,
        "start_time": "10:00:00",
        "end_time": "14:30:00",
        "buffer_minutes": 15,
    }
    assert _booking_to_dict(booking) == {
        "id": "bk_1",
        "meeting_type_id": "mt_1",
        "visitor_name": "Ada",
        "visitor_email": "ada@example.com",
        "date": "2026-06-12",
        "start_time": "10:00:00",
        "end_time": "10:30:00",
        "status": "confirmed",
        "meeting_url": "https://meet.example.com/bk_1",
    }
