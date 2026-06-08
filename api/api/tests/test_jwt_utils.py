"""Round-trip test for jwt_utils."""
import jwt
from api.libs.jwt_utils import _verify_token, _get_secret_key, _decode_jwt_payload, DEFAULT_JWT_SECRET

def test_round_trip():
    secret = _get_secret_key()
    token = jwt.encode({"sub": "user-1", "role": "member"}, secret, algorithm="HS256")
    payload = _decode_jwt_payload(token)
    assert payload["sub"] == "user-1"
    assert payload["role"] == "member"

def test_verify_valid_token():
    secret = _get_secret_key()
    token = jwt.encode({"sub": "user-2"}, secret, algorithm="HS256")
    assert _verify_token(token) is not None

def test_verify_invalid_token():
    assert _verify_token("not-a-valid-token") is None