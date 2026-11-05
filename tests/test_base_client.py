from llm.base_client import BaseLLMClient
from llm.mock_client import MockLLMClient


def test_mock_client_implements_base_interface():
    client = MockLLMClient()

    assert isinstance(client, BaseLLMClient)


def test_mock_generate():
    client = MockLLMClient()

    result = client.generate("Explain RAG.")

    assert result == "Mock response for: Explain RAG."


def test_mock_stream():
    client = MockLLMClient()

    result = "".join(client.stream("Explain RAG."))

    assert result == "Mock response for: Explain RAG. " 
from llm.client_factory import get_llm_client


def test_factory_returns_mock_client():
    client = get_llm_client("mock")

    assert isinstance(client, MockLLMClient)


def test_factory_mock_generation():
    client = get_llm_client("mock")

    result = client.generate("Explain AI.")

    assert result == "Mock response for: Explain AI."


def test_factory_invalid_provider():
    import pytest

    with pytest.raises(ValueError):
        get_llm_client("invalid")