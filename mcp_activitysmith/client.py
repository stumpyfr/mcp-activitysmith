from typing import Optional

from activitysmith import ActivitySmith
from fastmcp import Context

from .auth import get_api_key


def get_activitysmith(ctx: Optional[Context]) -> ActivitySmith:
    return ActivitySmith(api_key=get_api_key(ctx))
