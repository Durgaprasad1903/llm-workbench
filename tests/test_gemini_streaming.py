from unittest.mock import MagicMock, patch

from llm.gemini_client import GeminiClient


def test_gemini_streaming(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")

    mock_client = MagicMock()

    mock_client.models.generate_content_stream.return_value = [
        MagicMock(text="Hello "),
        MagicMock(text="World!")
    ]

    with patch(
        "llm.gemini_client.genai.Client",
        return_value=mock_client
    ):
        client = GeminiClient()

        result = list(client.stream("Say hello"))

    assert result == ["Hello ", "World!"]
    