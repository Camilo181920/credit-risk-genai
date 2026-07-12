import streamlit as st

from src.services.genai_service import GenAIService


st.title("🤖 GenAI Credit Analyst")


if "assessment" not in st.session_state:

    st.warning(
        "Primero debe evaluar un cliente en Credit Assessment."
    )

else:

    assessment = st.session_state["assessment"]


    st.subheader(
        "Credit Assessment Summary"
    )


    col1, col2 = st.columns(2)


    col1.metric(
        "Probability",
        f"{assessment.probability:.2%}"
    )


    col2.metric(
        "Risk",
        assessment.risk_level
    )


    st.divider()


    if st.button(
        "Generate Executive Report"
    ):

        service = GenAIService()


        report = (
            service
            .generate_credit_report(
                assessment
            )
        )


        st.subheader(
            "Executive Credit Report"
        )


        st.markdown(
            report
        )