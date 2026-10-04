from llm.mock_client import MockLLMClient


client = MockLLMClient()

response = client.generate(
    "Explain RAG in one simple sentence."
)

print(response)