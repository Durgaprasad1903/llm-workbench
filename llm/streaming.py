from typing import Iterator


def stream_response(chunks: Iterator[str]) -> None:
    for chunk in chunks:
        print(chunk, end="", flush=True)

    print()


if __name__ == "__main__":
    mock_chunks = [
        "RAG ",
        "combines ",
        "retrieval ",
        "with ",
        "language models."
    ]

    stream_response(iter(mock_chunks))