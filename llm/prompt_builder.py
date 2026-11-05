def build_prompt(choice: str, user_input: str) -> str:
    user_input = user_input.strip()

    if choice not in ["1", "2", "3"]:
        raise ValueError("Invalid choice")

    if not user_input:
        raise ValueError("Input cannot be empty")

    if choice == "1":
        return f"Explain this topic simply:\n{user_input}"

    elif choice == "2":
        return f"Summarize the following text:\n{user_input}"

    return f"Answer this question:\n{user_input}"