import os

from dotenv import load_dotenv
from openai import OpenAI


class OpenAIClient:
    def __init__(self, model: str = "gpt-6-luna"):
        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set")

        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )

        return response.output_text
    def stream(self, prompt: str):
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
            stream=True
        )

        for event in response:
            if event.type == "response.output_text.delta":
                yield event.delta    