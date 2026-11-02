from unittest.mock import MagicMock, patch

from llm.openai_client import OpenAIClient


def test_generate_returns_output_text(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")

    mock_client = MagicMock()
    mock_client.responses.create.return_value.output_text = "Mocked response"

    with patch(
        "llm.openai_client.OpenAI",
        return_value=mock_client
    ):
        client = OpenAIClient()
        result = client.generate("Explain RAG")

    assert result == "Mocked response"