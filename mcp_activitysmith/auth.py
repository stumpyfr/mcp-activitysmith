from os import getenv
from typing import Optional

from fastmcp import Context
from fastmcp.server.dependencies import get_http_request


def get_bearer_token(auth_header: Optional[str]) -> Optional[str]:
    if not auth_header:
        return None

    parts = auth_header.split()
    if len(parts) == 2 and parts[0].lower() == "bearer":
        return parts[1]
    return None


def get_api_key(ctx: Optional[Context]) -> str:
    request = None
    if ctx is not None and ctx.request_context is not None:
        request = ctx.request_context.request
    if request is None:
        try:
            request = get_http_request()
        except RuntimeError:
            request = None

    if request is not None:
        token = get_bearer_token(request.headers.get("authorization"))
        if not token:
            raise ValueError("Authorization header missing or invalid")
        return token

    api_key = getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")
    return api_key
