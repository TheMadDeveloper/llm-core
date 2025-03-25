# main.py
import os
from dotenv import load_dotenv
from llms.gpt import GPT
from history import MessageHistory

def prompt_menu(options: list, name: str, prompt = "Enter your choice"):
    print(f"=== {name} ===")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    response = input(f"{prompt}: ")

    return options[int(response) - 1]

def select_model():
    options = ["OpenAI GPT", "AWS SageMaker", "Exit"]

    while True:
        response = prompt_menu(options, "Model Selection")

        if response == "OpenAI GPT":
            print("OpenAI GPT selected.")
            # Return an instance of your GPT model
            return GPT(api_key=os.getenv("OPENAI_API_KEY"))
        elif response == "AWS SageMaker":
            print("SageMaker Model selected (not yet implemented).")
            # You could return a placeholder or raise a NotImplementedError
            raise NotImplementedError("SageMaker integration is not implemented yet.")
        elif response == "Exit":
            print("Exiting. Bye!")
            exit(0)
        else:
            print("Invalid selection.")

def main():
    history = MessageHistory()
    print("Welcome to LLM Core. Type 'exit' to quit.\n")

    load_dotenv()  # Load variables from .env file
    model = select_model()

    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Exiting. Bye!")
            break

        history.add_user(user_input)
        response = model.call(history.get())
        history.add_assistant(response)

        print(f"\nAssistant: {response}\n")


if __name__ == "__main__":
    main()