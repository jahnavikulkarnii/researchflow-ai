"""
PDF text extraction utilities for ResearchFlow AI.
"""

import io
import fitz


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extract all readable text from a PDF.

    Parameters
    ----------
    file_bytes:
        PDF file represented as bytes.

    Returns
    -------
    str
        Extracted text from the PDF.
    """

    document = fitz.open(
        stream=file_bytes,
        filetype="pdf"
    )

    pages = []

    for page in document:

        text = page.get_text()

        if text:
            pages.append(text)

    document.close()

    return "\n\n".join(pages)
