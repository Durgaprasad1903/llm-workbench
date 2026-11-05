def estimate_cost(
    input_tokens: int,
    output_tokens: int,
    input_price: float,
    output_price: float
) -> float:

    input_cost = (input_tokens / 1_000_000) * input_price
    output_cost = (output_tokens / 1_000_000) * output_price

    return input_cost + output_cost


if __name__ == "__main__":
    cost = estimate_cost(
        input_tokens=1000,
        output_tokens=500,
        input_price=0.15,
        output_price=0.60
    )

    print(f"Estimated API cost: ${cost:.6f}")