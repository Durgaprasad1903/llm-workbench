# LLM Workbench

A hands-on LLM engineering project covering reusable LLM clients, prompt templates, structured outputs, streaming, token counting, cost estimation, provider switching, and interactive prompt applications.

Built using Python, OpenAI API, Google Gemini API, Pydantic, and pytest.

## Overview

LLM Workbench is a collection of reusable components for working with Large Language Models (LLMs).

The project focuses on building practical LLM engineering foundations before moving towards advanced applications such as RAG systems and Agentic AI.

## Features

### 1. LLM Clients

* OpenAI client integration.
* Google Gemini client integration.
* Mock LLM client for local testing.
* Reusable client methods.

### 2. Prompt Engineering

* Reusable prompt templates.
* Dynamic prompt formatting.
* Summary and question-answering templates.

### 3. Structured Output

* JSON response parsing.
* Pydantic model validation.
* Structured response handling.
* Invalid JSON error handling.

### 4. Streaming Responses

* OpenAI streaming support.
* Gemini streaming support.
* Display responses incrementally.
* Mock streaming implementation.

### 5. Token & Cost Management

* Token counting using tiktoken.
* Input and output token tracking.
* API cost estimation.
* Usage tracking.

### 6. Reusable LLM Interface

* Common abstract LLM interface.
* Mock, OpenAI, and Gemini implementations.
* Provider factory.
* Provider switching without changing application logic.

### 7. Prompt Playground

* Interactive command-line application.
* Explain a topic.
* Summarize text.
* Answer questions.
* Input validation.
* Reusable prompt-building logic.

## Tech Stack

| Technology        | Purpose                         |
| ----------------- | ------------------------------- |
| Python 3.12       | Core programming language       |
| OpenAI SDK        | OpenAI integration              |
| Google Gen AI SDK | Gemini integration              |
| Pydantic          | Structured output validation    |
| tiktoken          | Token counting                  |
| python-dotenv     | Environment variable management |
| pytest            | Automated testing               |

## Project Structure

```text
llm-workbench/
│
├── examples/
│   ├── openai_demo.py
│   ├── provider_switching.py
│   └── prompt_playground.py
│
├── llm/
│   ├── __init__.py
│   ├── base_client.py
│   ├── mock_client.py
│   ├── openai_client.py
│   ├── gemini_client.py
│   ├── client_factory.py
│   ├── prompt_templates.py
│   ├── prompt_builder.py
│   ├── structured_output.py
│   ├── response_models.py
│   ├── streaming.py
│   ├── token_counter.py
│   ├── cost_estimator.py
│   └── usage_tracker.py
│
├── tests/
│   ├── test_base_client.py
│   ├── test_openai_client.py
│   ├── test_gemini_client.py
│   ├── test_prompt_templates.py
│   ├── test_structured_output.py
│   ├── test_response_models.py
│   ├── test_streaming.py
│   ├── test_openai_streaming.py
│   ├── test_gemini_streaming.py
│   ├── test_usage_tracker.py
│   └── test_prompt_playground.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Durgaprasad1903/llm-workbench.git
```

### 2. Navigate to the project

```bash
cd llm-workbench
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
```

Never upload your `.env` file or expose API keys on GitHub.

**Note:** API keys and API credits are required for actual OpenAI and Gemini requests. The Mock client can be used without API keys or credits.

## Usage

### 1. Mock LLM Client

Run:

```bash
python -m llm.mock_client
```

Example:

```python
from llm.mock_client import MockLLMClient

client = MockLLMClient()

response = client.generate("Explain RAG.")

print(response)
```

### 2. Provider Switching

Select an LLM provider using the client factory.

```python
from llm.client_factory import get_llm_client

client = get_llm_client("mock")

response = client.generate("Explain RAG.")

print(response)
```

Supported providers:

* `mock`
* `openai`
* `gemini`

### 3. Prompt Playground

Run:

```bash
python -m examples.prompt_playground
```

Available tasks:

1. Explain a topic.
2. Summarize text.
3. Answer a question.

### 4. Token Counting

```python
from llm.token_counter import count_tokens

tokens = count_tokens("Explain RAG in simple terms.")

print(tokens)
```

### 5. Cost Estimation

```python
from llm.cost_estimator import estimate_cost

cost = estimate_cost(
    input_tokens=1000,
    output_tokens=500,
    input_price=0.15,
    output_price=0.60
)

print(cost)
```

The prices above are illustrative inputs, not current provider pricing.

## Testing

The project uses pytest for automated testing.

Run all tests:

```bash
python -m pytest
```

Current test coverage includes:

* LLM client implementations.
* Provider interface.
* Provider factory.
* Prompt templates.
* Structured output.
* Pydantic validation.
* Streaming.
* Token usage and cost tracking.
* Prompt-building logic.
* Input validation.

**Current status: 24 tests passing.**

Provider integrations are tested using mocks, so running the test suite does not require API credits.

## Learning Progress

| Day   | Implementation                              | Status    |
| ----- | ------------------------------------------- | --------- |
| Day 1 | OpenAI and Gemini clients                   | Completed |
| Day 2 | Reusable prompt templates                   | Completed |
| Day 3 | Structured JSON output                      | Completed |
| Day 4 | Streaming responses                         | Completed |
| Day 5 | Token counting and cost estimation          | Completed |
| Day 6 | Common LLM interface and provider switching | Completed |
| Day 7 | Interactive Prompt Playground               | Completed |

## Future Improvements

Potential extensions:

* Add more provider integrations.
* Add conversation memory.
* Add retry and error-handling mechanisms.
* Add logging and monitoring.
* Build a web-based Prompt Playground.

## Key Learnings

Through this project, I gained practical experience with:

* Integrating LLM providers using Python SDKs.
* Designing reusable LLM components.
* Creating structured LLM outputs.
* Handling streaming responses.
* Tracking token usage and estimating costs.
* Designing provider-independent interfaces.
* Writing automated tests using pytest.

## Author

**Durga Prasad**

GitHub: [@Durgaprasad1903](https://github.com/Durgaprasad1903)

---

*Part of my AI Engineering learning roadmap.*
