import pytest

from llm.structured_output import parse_json_response
from llm.response_models import TopicResponse
from llm.structured_output import parse_structured_response


def test_parse_structured_response():
    response = """
    {
        "topic": "RAG",
        "difficulty": "Beginner",
        "score": 90
    }
    """

    result = parse_structured_response(response, TopicResponse)

    assert result.topic == "RAG"
    assert result.difficulty == "Beginner"
    assert result.score == 90

def test_parse_valid_json():
    response = '{"topic": "RAG", "difficulty": "Beginner"}'

    result = parse_json_response(response)

    assert result["topic"] == "RAG"
    assert result["difficulty"] == "Beginner"


def test_parse_invalid_json():
    response = '{"topic": "RAG",}'

    with pytest.raises(ValueError, match="Invalid JSON response"):
        parse_json_response(response)
        