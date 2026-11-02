class PromptTemplate:
    def __init__(self, template: str):
        self.template = template

    def format(self, **kwargs) -> str:
        return self.template.format(**kwargs)


# Summarization prompt
SUMMARY_PROMPT = PromptTemplate(
    "Summarize the following text in {sentences} sentences:\n\n{text}"
)

# Question answering prompt
QA_PROMPT = PromptTemplate(
    "Answer the following question using simple language.\n"
    "Context: {context}\n"
    "Question: {question}"
)


if __name__ == "__main__":
    prompt = SUMMARY_PROMPT.format(
        sentences=3,
        text="RAG combines information retrieval with language models."
    )

    print(prompt)