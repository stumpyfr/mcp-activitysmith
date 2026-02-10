from typing import Any, Dict

from fastmcp import Context, FastMCP
from fastmcp.dependencies import CurrentContext

from .client import get_activitysmith


def send_notifications(
    title: str, message: str, ctx: Context = CurrentContext()
) -> Dict[str, Any]:
    """Send a notification with a title and message"""
    try:
        activitysmith = get_activitysmith(ctx)
        response = activitysmith.notifications.send(
            {
                "title": title,
                "message": message,
            }
        )
        return response
    except Exception as err:
        print("Request failed:", err)
        raise err


def start_activity(
    title: str,
    subtitle: str,
    current_step: int,
    number_of_step: int,
    color: str = "blue",
    current_step_color: str = "blue",
    ctx: Context = CurrentContext(),
) -> Dict[str, Any]:
    """Start an activity with a title and message

    Args:
        title (str): The title to show when the activity starts
        subtitle (str): The subtitle to show when the activity starts
        current_step (int): The current step to show when the activity starts
        number_of_step (int): The total number of steps to show when the activity starts
        color (str, optional): The color to show when the activity starts. Defaults to "blue".
        current_step_color (str, optional): The color of the current step to show when the activity starts. Defaults to "blue".
    """
    try:
        activitysmith = get_activitysmith(ctx)
        start = activitysmith.live_activities.start(
            {
                "content_state": {
                    "title": title,
                    "subtitle": subtitle,
                    "number_of_steps": number_of_step,
                    "current_step": current_step,
                    "type": "segmented_progress",
                    "color": color,
                    "step_color": current_step_color,
                }
            }
        )
        return start
    except Exception as err:
        print("Request failed:", err)
        raise err


def update_activity(
    activity_id: str,
    title: str,
    subtitle: str,
    current_step: int,
    color: str = "blue",
    current_step_color: str = "blue",
    ctx: Context = CurrentContext(),
) -> Dict[str, Any]:
    """Update an activity with a title and message

    Args:
        activity_id (str): The ID of the activity to update
        title (str): The title to show when the activity is updated
        subtitle (str): The subtitle to show when the activity is updated
        current_step (int): The current step to show when the activity is updated
        color (str, optional): The color to show when the activity ends. Defaults to "blue".
        current_step_color (str, optional): The color of the current step to show when the activity ends. Defaults to "blue".
    """
    try:
        activitysmith = get_activitysmith(ctx)
        start = activitysmith.live_activities.update(
            {
                "activity_id": activity_id,
                "content_state": {
                    "title": title,
                    "subtitle": subtitle,
                    "current_step": current_step,
                    "color": color,
                    "step_color": current_step_color,
                },
            }
        )
        return start
    except Exception as err:
        print("Request failed:", err)
        raise err


def end_activity(
    activity_id: str,
    title: str,
    subtitle: str,
    current_step: int,
    auto_dismiss_minutes: int = 2,
    color: str = "blue",
    current_step_color: str = "blue",
    ctx: Context = CurrentContext(),
) -> Dict[str, Any]:
    """End an activity with a title and message

    Args:
        activity_id (str): The ID of the activity to end
        title (str): The title to show when the activity ends
        subtitle (str): The subtitle to show when the activity ends
        current_step (int): The current step to show when the activity ends
        auto_dismiss_minutes (int, optional): The number of minutes after which the activity will be automatically dismissed. Defaults to 2.
        color (str, optional): The color to show when the activity ends. Defaults to "blue".
        current_step_color (str, optional): The color of the current step to show when the activity ends. Defaults to "blue".
    """
    try:
        activitysmith = get_activitysmith(ctx)
        start = activitysmith.live_activities.end(
            {
                "activity_id": activity_id,
                "content_state": {
                    "title": title,
                    "subtitle": subtitle,
                    "current_step": current_step,
                    "auto_dismiss_minutes": auto_dismiss_minutes,
                    "color": color,
                    "step_color": current_step_color,
                },
            }
        )
        return start
    except Exception as err:
        print("Request failed:", err)
        raise err


def register_tools(mcp: FastMCP) -> None:
    mcp.tool(send_notifications)
    mcp.tool(start_activity)
    mcp.tool(update_activity)
    mcp.tool(end_activity)
