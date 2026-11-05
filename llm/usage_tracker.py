from llm.token_counter import count_tokens
from llm.cost_estimator import estimate_cost


def track_usage(
    prompt: str,
    response: str,
    input_price: float,
    output_price: float
) -> dict:

    input_tokens = count_tokens(prompt)
    output_tokens = count_tokens(response)

    total_cost = estimate_cost(
        input_tokens,
        output_tokens,
        input_price,
        output_price
    )

    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "estimated_cost": total_cost
    }


if __name__ == "__main__":
    usage = track_usage(
        prompt="Explain RAG.",
        response="RAG combines retrieval with language models.",
        input_price=0.15,
        output_price=0.60
    )

    print(usage)