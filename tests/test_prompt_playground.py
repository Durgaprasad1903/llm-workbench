import pytest

from llm.prompt_builder import build_prompt


def test_explain_topic():
    result = build_prompt("1", "Machine Learning")
    assert result == "Explain this topic simply:\nMachine Learning"


def test_summarize_text():
    result = build_prompt("2", "Artificial Intelligence")
    assert result == "Summarize the following text:\nArtificial Intelligence"


def test_answer_question():
    result = build_prompt("3", "What is Python?")
    assert result == "Answer this question:\nWhat is Python?"


def test_invalid_choice():
    with pytest.raises(ValueError):
        build_prompt("5", "Python")


def test_empty_input():
    with pytest.raises(ValueError):
        build_prompt("1", "   ")