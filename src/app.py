import streamlit as st

from core.pdf_parser import extract_text_from_pdf
from core.summarizer import create_research_summary
from core.qa import answer_question


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="ResearchFlow AI",
    page_icon="📚",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📚 ResearchFlow AI")

st.caption(
    "AI-powered research assistant for scientific literature"
)

st.divider()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("ResearchFlow")

    st.markdown(
        """
        ### What can you do?

        📄 Upload a research paper

        🧠 Generate a structured summary

        💬 Ask questions about the paper

        🔬 Compare papers

        📚 Build your research library
        """
    )

    st.divider()

    st.caption(
        "ResearchFlow AI — Research smarter."
    )


# --------------------------------------------------
# PDF UPLOAD
# --------------------------------------------------

st.header("📄 Upload Research Paper")

uploaded_file = st.file_uploader(
    "Choose a scientific paper in PDF format",
    type=["pdf"]
)


# --------------------------------------------------
# PROCESS PDF
# --------------------------------------------------

if uploaded_file is not None:

    with st.spinner(
        "Reading and processing your research paper..."
    ):

        pdf_bytes = uploaded_file.read()

        document_text = extract_text_from_pdf(
            pdf_bytes
        )


    # --------------------------------------------------
    # CHECK EXTRACTION
    # --------------------------------------------------

    if not document_text.strip():

        st.error(
            "No readable text was found in this PDF. "
            "The document may contain scanned images "
            "rather than selectable text."
        )

    else:

        st.success(
            "Research paper successfully processed."
        )


        # --------------------------------------------------
        # DOCUMENT INFORMATION
        # --------------------------------------------------

        word_count = len(
            document_text.split()
        )

        character_count = len(
            document_text
        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Words Extracted",
                f"{word_count:,}"
            )


        with col2:

            st.metric(
                "Characters",
                f"{character_count:,}"
            )


        with col3:

            st.metric(
                "Document",
                uploaded_file.name
            )


        st.divider()


        # --------------------------------------------------
        # SUMMARY
        # --------------------------------------------------

        st.header("🧠 Research Summary")

        summary = create_research_summary(
            document_text
        )


        col1, col2 = st.columns(2)


        with col1:

            st.subheader(
                "Executive Summary"
            )

            st.write(
                summary["executive_summary"]
            )


            st.subheader(
                "Key Findings"
            )

            st.write(
                summary["key_findings"]
            )


        with col2:

            st.subheader(
                "Methodology"
            )

            st.write(
                summary["methodology"]
            )


            st.subheader(
                "Limitations"
            )

            st.write(
                summary["limitations"]
            )


        st.divider()


        # --------------------------------------------------
        # QUESTION ANSWERING
        # --------------------------------------------------

        st.header("💬 Ask the Paper")


        question = st.text_input(
            "Ask a question about the uploaded research paper",
            placeholder=
            "Example: What was the main objective of the study?"
        )


        if st.button(
            "Ask ResearchFlow",
            type="primary"
        ):

            answer = answer_question(
                document_text,
                question
            )

            st.info(answer)
