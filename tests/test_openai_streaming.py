from unittest.mock import MagicMock, patch

from llm.openai_client import OpenAIClient


def test_openai_streaming(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")

    mock_client = MagicMock()

    mock_client.responses.create.return_value = [
        MagicMock(
            type="response.output_text.delta",
            delta="Hello "
        ),
        MagicMock(
            type="response.output_text.delta",
            delta="World!"
        )
    ]

    with patch(
        "llm.openai_client.OpenAI",
        return_value=mock_client
    ):
        client = OpenAIClient()

        result = list(client.stream("Say hello"))

    assert result == ["Hello ", "World!"]
    