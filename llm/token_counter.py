import tiktoken


def count_tokens(text: str, model: str = "gpt-4o") -> int:
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)

    return len(tokens)


if __name__ == "__main__":
    prompt = "Explain RAG in simple terms."

    total_tokens = count_tokens(prompt)

    print("Prompt:", prompt)
    print("Token count:", total_tokens)