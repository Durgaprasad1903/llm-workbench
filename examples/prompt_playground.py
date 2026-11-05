from llm.client_factory import get_llm_client
from llm.prompt_builder import build_prompt

client = get_llm_client("mock")

print("===== LLM PROMPT PLAYGROUND =====")

print("\nChoose a task:")
print("1. Explain a topic")
print("2. Summarize text")
print("3. Answer a question")

choice = input("\nEnter your choice (1-3): ")

try:
    user_input = input("\nEnter your text or question: ")
    prompt = build_prompt(choice, user_input)

except ValueError as error:
    print(error)
    exit()

response = client.generate(prompt)

print("\n===== RESPONSE =====")
print(response)