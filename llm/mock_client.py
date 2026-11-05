from llm.base_client import BaseLLMClient


class MockLLMClient(BaseLLMClient):

    def generate(self, prompt: str) -> str:
        return f"Mock response for: {prompt}"

    def stream(self, prompt: str):
        response = self.generate(prompt)

        for word in response.split():
            yield word + " "


if __name__ == "__main__":
    client = MockLLMClient()

    print(client.generate("Explain RAG."))

    for chunk in client.stream("Explain RAG."):
        print(chunk, end="", flush=True)