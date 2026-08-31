"""
Research paper summarization utilities.
"""


def create_research_summary(text: str) -> dict:
    """
    Create a structured research summary.

    The current version provides the structure.
    AI generation will be connected in the next step.
    """

    if not text.strip():

        return {
            "executive_summary":
                "No research text was provided.",

            "key_findings":
                "No findings could be extracted.",

            "methodology":
                "No methodology could be identified.",

            "limitations":
                "No limitations could be identified.",

            "future_work":
                "No future research directions could be identified."
        }

    return {
        "executive_summary":
            "This section will contain an AI-generated summary of the research paper.",

        "key_findings":
            "This section will contain the major findings identified by the AI.",

        "methodology":
            "This section will contain a summary of the research methodology.",

        "limitations":
            "This section will contain limitations identified from the paper.",

        "future_work":
            "This section will contain suggested future research directions."
    }
