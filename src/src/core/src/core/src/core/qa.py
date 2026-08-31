"""
Question answering utilities for research papers.
"""


def answer_question(
    document_text: str,
    question: str
) -> str:

    if not question.strip():
        return "Please enter a question."

    return (
        "AI-powered document question answering "
        "will be connected here."
    )
