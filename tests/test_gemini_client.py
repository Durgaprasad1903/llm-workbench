from unittest.mock import MagicMock, patch

from llm.gemini_client import GeminiClient


def test_generate_returns_response_text(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")

    mock_client = MagicMock()
    mock_client.models.generate_content.return_value.text = "Mocked Gemini response"

    with patch(
        "llm.gemini_client.genai.Client",
        return_value=mock_client
    ):
        client = GeminiClient()
        result = client.generate("Explain RAG")

    assert result == "Mocked Gemini response"