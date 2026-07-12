import streamlit as st
import matplotlib.pyplot as plt

from src.data import load_data
from src.services.business_metrics import business_summary


st.title("📊 Executive Risk Dashboard")


@st.cache_data
def get_data():

    return load_data(
        "german_credit.csv"
    )


df = get_data()


summary = business_summary(
    df
)


# =====================
# KPI SECTION
# =====================

st.subheader(
    "Portfolio Overview"
)


c1, c2, c3, c4 = st.columns(4)


c1.metric(
    "Customers",
    int(summary["Clientes"])
)


c2.metric(
    "Average Loan",
    f"${summary['Monto Promedio']:,.0f}"
)


c3.metric(
    "Average Age",
    f"{summary['Edad Promedio']:.1f}"
)


c4.metric(
    "Default Rate",
    f"{summary['Tasa Default']:.1%}"
)



st.divider()


# =====================
# RISK DISTRIBUTION
# =====================

st.subheader(
    "Credit Risk Distribution"
)


risk_counts = (
    df["credit_risk"]
    .value_counts()
)


st.bar_chart(
    risk_counts
)



st.divider()


# =====================
# LOAN ANALYSIS
# =====================

col1, col2 = st.columns(2)


with col1:

    st.subheader(
        "Loan Amount Distribution"
    )


    st.bar_chart(
        df["amount"]
        .head(100)
    )


with col2:

    st.subheader(
        "Age Distribution"
    )


    st.bar_chart(
        df["age"]
        .value_counts()
        .sort_index()
    )



st.divider()


# =====================
# BUSINESS INSIGHTS
# =====================

st.subheader(
    "Portfolio Insights"
)


default_rate = summary[
    "Tasa Default"
]


if default_rate > 0.30:

    st.error(
        "High default exposure detected."
    )

elif default_rate > 0.15:

    st.warning(
        "Moderate credit risk exposure."
    )

else:

    st.success(
        "Portfolio risk level is controlled."
    )