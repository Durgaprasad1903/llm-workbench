from llm.client_factory import get_llm_client


# Select provider
client = get_llm_client("mock")

# Generate response
prompt = "Explain Retrieval Augmented Generation."

response = client.generate(prompt)

print("Response:", response)