import os

from dotenv import load_dotenv
from google import genai


class GeminiClient:
    def __init__(self, model: str = "gemini-2.5-flash"):
        load_dotenv()

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set")

        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text
    def stream(self, prompt: str):
        response = self.client.models.generate_content_stream(
            model=self.model,
            contents=prompt
        )

        for chunk in response:
            if chunk.text:
                yield chunk.text