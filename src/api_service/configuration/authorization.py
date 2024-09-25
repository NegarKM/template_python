import hashlib
from api_service.configuration.config import AppConfig
from exceptions import UnauthorizedError


def verify_access_token(token: str) -> None:
    if hashlib.md5(token.encode()).hexdigest() != AppConfig.API_KEY_SECRET:
        raise UnauthorizedError("Invalid API Key")

