configure claude mcp 
1) create c:\users\username\appdata\roaming\claude\claude_desktop_config.json
2) copy and paste below code
{
  "mcpServers": {
    "AItravel": {
      "command": "c:\\Users\\MEGHA\\.local\\bin\\uv.exe",
      "args": [
        "--directory",
        "C:\\project\\travelai\\backend\\mcp",
        "run",
        "main.py"
      ]
    }
  }
}