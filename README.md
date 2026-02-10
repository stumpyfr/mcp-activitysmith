## ActivitySmith MCP Server

This MCP server exposes [ActivitySmith](https://activitysmith.com/) notifications and live activity tools.

### MCP Client Config (stdio)

Example mcp.json:

```json
{
	"mcpServers": {
		"activitysmith": {
			"command": "uv",
			"args": ["run", "mcp-activitysmith"],
			"env": {
				"API_KEY": "your_key_here"
			}
		}
	}
}
```

Example mcp.json with input prompt (VS Code):

```json
{
	"inputs": [
		{
			"id": "activitysmithApiKey",
			"type": "promptString",
			"description": "ActivitySmith API key",
			"password": true
		}
	],
	"mcpServers": {
		"activitysmith": {
			"command": "uv",
			"args": ["run", "mcp-activitysmith"],
			"env": {
				"API_KEY": "${input:activitysmithApiKey}"
			}
		}
	}
}
```

### MCP Client Config (HTTP)

Example mcp.json:

```json
{
	"mcpServers": {
		"activitysmith": {
			"url": "http://127.0.0.1:8000",
			"headers": {
				"Authorization": "Bearer your_key_here"
			}
		}
	}
}
```

Example mcp.json with input prompt (VS Code):

```json
{
	"inputs": [
		{
			"id": "activitysmithApiKey",
			"type": "promptString",
			"description": "ActivitySmith API key",
			"password": true
		}
	],
	"mcpServers": {
		"activitysmith": {
			"url": "http://127.0.0.1:8000",
			"headers": {
				"Authorization": "Bearer ${input:activitysmithApiKey}"
			}
		}
	}
}
```

### Dev requirements

- Python 3.12+
- ActivitySmith API key

### Install

```bash
uv sync
```

If you change the package name or entry point, rerun `uv sync` to refresh the script.

### Run (stdio)

```bash
API_KEY=your_key_here uv run mcp-activitysmith
```

### Run (HTTP)

```bash
uv run mcp-activitysmith --server
```

### Notes

- HTTP mode reads the API key from the Authorization header on each request.
- Stdio mode reads the API key from the API_KEY environment variable.
