import argparse
from os import getenv

from .server import create_mcp


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Activity Smith MCP server")
    parser.add_argument(
        "--server",
        action="store_true",
        help="Run the HTTP server instead of stdio",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    mcp = create_mcp()
    if args.server:
        mcp.run(transport="streamable-http")
    else:
        if getenv("API_KEY") is None:
            raise ValueError("API_KEY environment variable is not set")
        mcp.run()
