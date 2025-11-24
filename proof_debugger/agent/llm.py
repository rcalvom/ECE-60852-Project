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
        
    def tool_run_bash_command(self):
        """Run a bash command using the LLM tool"""
    
    def tool_run_cscope_query(self):
        """Run a cscope query using the LLM tool"""
