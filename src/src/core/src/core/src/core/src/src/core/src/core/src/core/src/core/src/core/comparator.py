"""
Research paper comparison utilities.
"""


def compare_papers(
    paper_a: str,
    paper_b: str
) -> dict:
    """
    Compare two research papers.

    AI-powered comparison will be implemented
    in a future version.
    """

    if not paper_a.strip() or not paper_b.strip():

        return {
            "objective":
                "Two research papers are required.",

            "methodology":
                "Two research papers are required.",

            "findings":
                "Two research papers are required.",

            "limitations":
                "Two research papers are required."
        }

    return {
        "objective":
            "The AI will compare the objectives of both papers.",

        "methodology":
            "The AI will identify methodological similarities and differences.",

        "findings":
            "The AI will compare the major findings.",

        "limitations":
            "The AI will compare the limitations of both studies."
    }
