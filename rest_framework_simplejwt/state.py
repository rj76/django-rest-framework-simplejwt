from .backends import TokenBackend
from .settings import api_settings

from django.db import connection


def get_token_backend():
	return TokenBackend(
    api_settings.ALGORITHM,
    api_settings.SIGNING_KEY,
    api_settings.VERIFYING_KEY,
    api_settings.AUDIENCE,
    api_settings.ISSUER,
    api_settings.JWK_URL,
    api_settings.LEEWAY,
    api_settings.JSON_ENCODER,
)

token_backend = get_token_backend()
