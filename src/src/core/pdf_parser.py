"""
PDF text extraction utilities for ResearchFlow AI.
"""

import io
import fitz


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extract text from a PDF provided as bytes.
    """

    document = fitz.open(
        stream=io.BytesIO(file_bytes),
        filetype="pdf"
    )

    pages = []

    for page in document:
        text = page.get_text()

        if text:
            pages.append(text)

    document.close()

    return "\n\n".join(pages)
