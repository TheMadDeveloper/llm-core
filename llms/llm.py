# llm.py
from abc import ABC, abstractmethod

class LLM(ABC):
    @abstractmethod
    def call(self, messages: list, **kwargs) -> str:
        """Send messages to the LLM and return the response."""
        pass

    @abstractmethod
    def name(self):
        pass