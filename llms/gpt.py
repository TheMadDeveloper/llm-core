# gpt.py
import os
from dotenv import load_dotenv
import openai
from llms.llm import LLM

class GPT(LLM):
    def __init__(self, api_key: str, model: str = "gpt-3.5-turbo", temperature: float = 0.7):
        import openai
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        openai.api_key = self.api_key
        self.client = openai.OpenAI(api_key=self.api_key)

    def call(self, messages: list, **kwargs) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            **kwargs
        )
        return response.choices[0].message.content

    def name(self):
        return "OpenAI GPT"