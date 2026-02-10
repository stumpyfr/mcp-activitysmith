from fastmcp import FastMCP

from .tools import register_tools


def create_mcp() -> FastMCP:
    mcp = FastMCP(
        "Activity Smith",
        "A tool to send notifications and live activities to iOS devices",
    )
    register_tools(mcp)
    return mcp
