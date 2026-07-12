import streamlit as st

from src.ui.forms import customer_form

from src.services import CreditService


st.title("🔍 Credit Assessment")


customer = customer_form()


if st.button("Evaluate Customer"):

    service = CreditService()


    assessment = service.evaluate(
        customer
    )

    st.session_state["assessment"] = assessment

    st.session_state[
        "credit_assessment"
    ] = assessment


    col1, col2 = st.columns(2)


    col1.metric(
        "Probability",
        f"{assessment.probability:.2%}"
    )


    col2.metric(
        "Risk",
        assessment.risk_level
    )


    st.subheader(
        "Main Risk Factors"
    )


    for feature in assessment.top_features:

        st.write(
            "•",
            feature
        )