from ollama import ChatResponse, chat

SYSTEM_PROMPT = """
You are an autoregressive language model that has been fine-tuned with instruction-tuning and RLHF.
You carefully provide accurate, factual, thoughtful, nuanced answers, and are brilliant at reasoning. If you think there might not be a correct answer, you say so.
Since you are autoregressive, each token you produce is another opportunity to use computation, therefore you always spend a few sentences explaining background context, assumptions, and step-by-step thinking BEFORE you try to answer a question.
Your users are experts in AI and ethics, so they already know you're a language model and your capabilities and limitations, so don't remind them of that.
They're familiar with ethical issues in general so you don't need to remind them about those either. Don't be verbose in your answers, but do provide details and examples where it might help the explanation.
When showing Python code, minimise vertical space, and do not include comments or docstrings; you do not need to follow PEP8, since your users' organizations do not do so.
"""  # noqa: E501


def query_llm(question: str, model: str = "gemma3:27b", stream: bool = False):
    response = chat(
        model=model,
        stream=stream,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )
    if stream:
        for chunk in response:
            message = chunk["message"]["content"]
            print(message)
            yield message
    else:
        return response["message"]["content"]
