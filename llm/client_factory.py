from llm.mock_client import MockLLMClient
from llm.openai_client import OpenAIClient
from llm.gemini_client import GeminiClient


def get_llm_client(provider: str):

    if provider == "mock":
        return MockLLMClient()

    elif provider == "openai":
        return OpenAIClient()

    elif provider == "gemini":
        return GeminiClient()

    else:
        raise ValueError(f"Unsupported provider: {provider}")