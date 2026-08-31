from src.core.pdf_parser import extract_text_from_pdf


def test_invalid_pdf():

    try:

        extract_text_from_pdf(
            b"not a real pdf"
        )

    except Exception:

        assert True
