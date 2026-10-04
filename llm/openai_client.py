import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate(prompt: str) -> str:
    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt
    )

    return response.output_text