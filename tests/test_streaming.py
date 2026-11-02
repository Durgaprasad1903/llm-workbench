from io import StringIO
from unittest.mock import patch

from llm.streaming import stream_response


def test_stream_response():
    chunks = iter(["RAG ", "combines ", "retrieval."])

    output = StringIO()

    with patch("sys.stdout", output):
        stream_response(chunks)

    assert output.getvalue() == "RAG combines retrieval.\n"