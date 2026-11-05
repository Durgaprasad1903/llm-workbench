from llm.usage_tracker import track_usage


def test_track_usage():
    result = track_usage(
        prompt="Explain RAG.",
        response="RAG combines retrieval with language models.",
        input_price=0.15,
        output_price=0.60
    )

    assert result["input_tokens"] > 0
    assert result["output_tokens"] > 0
    assert result["total_tokens"] == (
        result["input_tokens"] + result["output_tokens"]
    )
    assert result["estimated_cost"] > 0