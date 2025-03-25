# history.py
class MessageHistory:
    def __init__(self, system_prompt="You are a helpful assistant."):
        self.messages = [{"role": "system", "content": system_prompt}]

    def add_user(self, message):
        self.messages.append({"role": "user", "content": message})

    def add_assistant(self, message):
        self.messages.append({"role": "assistant", "content": message})

    def get(self):
        return self.messages