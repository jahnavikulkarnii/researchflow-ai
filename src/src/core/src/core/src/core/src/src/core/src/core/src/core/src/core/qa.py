"""
Question answering utilities for research papers.
"""


def answer_question(
    document_text: str,
    question: str
) -> str:
    """
    Answer a user's question about a research paper.

    AI integration will be added in the next stage.
    """

    if not question.strip():

        return "Please enter a question."

    if not document_text.strip():

        return "No research paper has been uploaded."

    return (
        "The AI question-answering system "
        "will answer this question using "
        "the uploaded research paper."
    )
