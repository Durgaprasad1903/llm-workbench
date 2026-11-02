from llm.prompt_templates import SUMMARY_PROMPT, QA_PROMPT


def test_summary_prompt():
    result = SUMMARY_PROMPT.format(
        sentences=3,
        text="RAG combines retrieval with language models."
    )

    assert "3 sentences" in result
    assert "RAG combines retrieval" in result


def test_qa_prompt():
    result = QA_PROMPT.format(
        context="RAG retrieves relevant documents.",
        question="What is RAG?"
    )

    assert "What is RAG?" in result
    assert "RAG retrieves relevant documents." in result