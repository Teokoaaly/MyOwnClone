import pytest
from pydantic import ValidationError

from api.controllers.console.myownclone.booking import ProductPayload, _product_to_dict
from api.models.meeting import Product


def test_product_to_dict_matches_frontend_contract():
    product = Product(
        id="prod_1",
        clone_id="clone_1",
        name="Pro consulting",
        description="Premium advisory package",
        price_cents=9900,
        url="https://example.com/pro",
        image_url="https://example.com/pro.png",
        priority=10,
        active=True,
    )

    assert _product_to_dict(product) == {
        "id": "prod_1",
        "clone_id": "clone_1",
        "name": "Pro consulting",
        "description": "Premium advisory package",
        "price_cents": 9900,
        "url": "https://example.com/pro",
        "image_url": "https://example.com/pro.png",
        "priority": 10,
        "active": True,
    }


def test_product_payload_rejects_negative_price():
    with pytest.raises(ValidationError):
        ProductPayload.model_validate({
            "name": "Broken product",
            "price_cents": -1,
        })


def test_product_payload_requires_name():
    with pytest.raises(ValidationError):
        ProductPayload.model_validate({
            "name": "",
            "price_cents": 0,
        })
