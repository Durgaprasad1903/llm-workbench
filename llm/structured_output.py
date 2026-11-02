import json
from pydantic import BaseModel
def parse_structured_response(
    response: str,
    model_class: type[BaseModel]
) -> BaseModel:
    data = parse_json_response(response)
    return model_class.model_validate(data)


def parse_json_response(response: str) -> dict:
    try:
        return json.loads(response)
    except json.JSONDecodeError as error:
        raise ValueError("Invalid JSON response") from error


if __name__ == "__main__":
    mock_response = """
    {
        "topic": "RAG",
        "difficulty": "Beginner",
        "summary": "RAG combines retrieval with language models."
    }
    """

    result = parse_json_response(mock_response)

    print(result)
    print(result["topic"])