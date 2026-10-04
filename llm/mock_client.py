class MockLLMClient:
    def generate(self, prompt: str) -> str:
        return f"Mock response for: {prompt}"


if __name__ == "__main__":
    client = MockLLMClient()

    response = client.generate(
        "Explain RAG in one simple sentence."
    )

    print(response)