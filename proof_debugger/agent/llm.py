""" LLM handler"""

# System
import os

# OpenAI
from openai import OpenAI


class LLM():
    """Handler for OpenAI implementation"""

    def __init__(self) -> None:
        openai_api_key = os.getenv("OPENAI_API_KEY", None)
        if not openai_api_key:
            raise EnvironmentError("No OpenAI API key found")
        self.client = OpenAI(api_key=openai_api_key)

    def create_chat(self):
        """Create a new conversation with the LLM"""

    def prompt_in_chat(self):
        """Prompt a message into a chat"""
