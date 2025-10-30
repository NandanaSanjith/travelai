from typing import Optional
from pathlib import Path
import os
from datetime import datetime
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv() 
ANTHROPIC_API_KEY=os.getenv("ANTHROPIC_API_KEY")

BASE_DIR = Path(__file__).parent.parent.parent.parent  # Adjust the number of parents as needed
MCP_PATH = BASE_DIR / "mcp"  # Adjust this path to where your MCP code is located
UV_PATH = os.environ.get('UV_PATH')  # Fallback to known path

class ClaudeClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.client = Anthropic()

    async def connect_to_server(self):
        """Connect to an MCP server

        Args:
            server_script_path: Path to the server script (.py or .js)
        """
        server_params = StdioServerParameters(
            command=str(UV_PATH),
            args=["--directory", str(MCP_PATH), "run", "main.py"],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()

    async def initialize(self):
        await self.connect_to_server()

    async def close(self):
        await self.exit_stack.aclose()


    async def _send_chat_message(self, message: str) -> str:
        """Process a query using Claude and available tools"""
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Append user message to conversation history
        self.messages.append({"role": "user", "content": message})
    
        response = await self.session.list_tools()
        available_tools = [{
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.inputSchema
        } for tool in response.tools]

        # Process response and handle tool calls
        final_text = []

        while True:
            response = self.client.messages.create(
                model="claude-3-7-sonnet-20250219",
                max_tokens=1000,
                system=f"The current date is {current_date}. Use this date when interpreting or invoking tools that rely on today's date.",
                messages=self.messages,
                tools=available_tools
            )

            tool_invoked=False
            for content in response.content:
                if content.type == 'text':
                    final_text.append(content.text)
                    self.messages.append({"role": "assistant", "content": content.text})
                elif content.type == 'tool_use':
                    tool_invoked = True
                    # Execute tool via MCP session
                    tool_result = await self.session.call_tool(content.name, content.input)

                    # Append tool call and result to conversation
                    self.messages.append({"role": "assistant", "content": [content]})
                    self.messages.append({
                        "role": "user",
                        "content": [{"type": "tool_result", "tool_use_id": content.id, "content": tool_result.content}]
                    })

            if not tool_invoked:
                break
        return "\n".join(final_text)
    
    async def send_chat_message(self, message: str, reset_conversation: bool = False):
        """
        Public method to send a message to Claude and receive response.
        Returns a dictionary with status and text.
        """
        if reset_conversation:
            self.reset_conversation()
        final_text_md = await self._send_chat_message(message=message)
        return {"status": "success", "response": final_text_md}

    def reset_conversation(self):
        """Reset conversation history."""
        self.messages = []
