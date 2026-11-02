import pytest
from pydantic import ValidationError

from llm.response_models import TopicResponse


def test_valid_response():
    result = TopicResponse(
        topic="RAG",
        difficulty="Beginner",
        score=90
    )

    assert result.topic == "RAG"
    assert result.score == 90


def test_invalid_score():
    with pytest.raises(ValidationError):
        TopicResponse(
            topic="RAG",
            difficulty="Beginner",
            score=150
        )