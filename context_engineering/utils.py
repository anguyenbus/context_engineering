"""
Utility functions for context engineering notebooks.
"""

import os
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
import json

console = Console()


def load_env():
    """Load .env file from project root.

    Looks for .env in the project root (parent of context_engineering directory)
    and loads environment variables from it. This should be called before
    any code that requires API keys or other environment variables.
    """
    # Get the project root (parent of context_engineering directory)
    project_root = Path(__file__).parent.parent
    env_file = project_root / ".env"

    if env_file.exists():
        from dotenv import load_dotenv
        load_dotenv(env_file)
        console.print(f"[green]Loaded .env from {env_file}[/green]")
    else:
        console.print(f"[yellow]No .env file found at {env_file}[/yellow]")


def format_message_content(message):
    """Convert message content to displayable string"""
    if isinstance(message.content, str):
        return message.content
    elif isinstance(message.content, list):
        # Handle complex content like tool calls
        parts = []
        for item in message.content:
            if item.get('type') == 'text':
                parts.append(item['text'])
            elif item.get('type') == 'tool_use':
                parts.append(f"\n🔧 Tool Call: {item['name']}")
                parts.append(f"   Args: {json.dumps(item['input'], indent=2)}")
        return "\n".join(parts)
    else:
        return str(message.content)


def format_messages(messages):
    """Format and display a list of messages with Rich formatting"""
    for m in messages:
        msg_type = m.__class__.__name__.replace('Message', '')
        content = format_message_content(m)

        if msg_type == 'Human':
            console.print(Panel(content, title="🧑 Human", border_style="blue"))
        elif msg_type == 'Ai':
            console.print(Panel(content, title="🤖 Assistant", border_style="green"))
        elif msg_type == 'Tool':
            console.print(Panel(content, title="🔧 Tool Output", border_style="yellow"))
        else:
            console.print(Panel(content, title=f"📝 {msg_type}", border_style="white"))


def format_message(messages):
    """Alias for format_messages for backward compatibility"""
    return format_messages(messages)