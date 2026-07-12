import streamlit as st

from src.ui.forms import customer_form
from src.services import CreditService
from src.services.genai_service import GenAIService


st.title("🔍 Credit Assessment")


customer = customer_form()


if st.button("Evaluate Customer"):

    try:

        credit_service = CreditService()

        assessment = credit_service.evaluate(
            customer
        )

        st.session_state["assessment"] = assessment

        col1, col2 = st.columns(2)


        col1.metric(
            "Probability Default",
            f"{assessment.probability:.2%}"
        )
        
        st.progress(
            assessment.probability
        )


        col2.metric(
            "Risk Level",
            assessment.risk_level
        )

        if assessment.risk_level == "HIGH":
            st.error("🔴 HIGH RISK")

        elif assessment.risk_level == "MEDIUM":
            st.warning("🟡 MEDIUM RISK")

        else:
            st.success("🟢 LOW RISK")
            

        st.divider()


        st.subheader(
            "🔎 Main Risk Factors"
        )


        for feature in assessment.top_features:

            st.info(
                feature
            )


        st.divider()


        st.subheader(
            "🤖 Executive Credit Report"
        )


        genai_service = GenAIService()


        report = (
            genai_service
            .generate_credit_report(
                assessment
            )
        )


        st.markdown(
            report
        )


    except Exception as e:

        st.error(
            str(e)
        )