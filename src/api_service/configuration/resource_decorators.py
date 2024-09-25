from functools import wraps
from typing import Any, Callable
from flask import request

from exceptions import UnauthorizedError
from api_service.configuration.authorization import verify_access_token


def validate_authorization_token(f: Callable) -> Callable:
    @wraps(f)
    def wrapper(*args: Any, **kw: Any) -> Any:
        verify_access_token(get_authorization_header())
        return f(*args, **kw)

    return wrapper


def get_authorization_header(token_prefix: str = "Bearer ") -> str:
    authorization_token = request.headers.get("Authorization")
    if not authorization_token:
        raise UnauthorizedError("Missing Authorization Header")
    if authorization_token[: len(token_prefix)] != token_prefix:
        raise UnauthorizedError('Wrong format, missing keyword "Bearer" in the Authorization Header')
    return authorization_token[len(token_prefix):]
