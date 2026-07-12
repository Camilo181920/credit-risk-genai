import streamlit as st

from src.services import GenAIService


st.title("🤖 GenAI Assistant")


if (
    "credit_assessment"
    not in st.session_state
):

    st.warning(
        "Primero evalúe un cliente "
        "en Credit Assessment."
    )

    st.stop()



assessment = st.session_state[
    "credit_assessment"
]


st.subheader(
    "Credit Assessment Summary"
)


st.write(
    f"Risk Level: {assessment.risk_level}"
)


st.write(
    f"Default Probability: "
    f"{assessment.probability:.2%}"
)


st.subheader(
    "Generating Executive Report"
)


if st.button(
    "Generate AI Report"
):

    service = GenAIService()


    report = (
        service
        .generate_credit_report(
            assessment
        )
    )


    st.text_area(
        "Generated Report",
        report,
        height=300
    )