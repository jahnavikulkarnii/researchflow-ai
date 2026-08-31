from src.core.qa import answer_question


def test_empty_question():

    result = answer_question(
        "This is a research paper.",
        ""
    )

    assert result == "Please enter a question."
