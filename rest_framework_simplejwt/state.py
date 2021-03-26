from .backends import TokenBackend
from .settings import api_settings

from django.db import connection


def get_token_backend():
	return TokenBackend(api_settings.ALGORITHM, api_settings.SIGNING_KEY,
                        api_settings.VERIFYING_KEY, connection.tenant.schema_name, api_settings.ISSUER)
