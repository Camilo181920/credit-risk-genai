import streamlit as st

from src.data import load_data

from src.services.business_metrics import business_summary

st.title("📊 Executive Dashboard")

df = load_data("german_credit.csv")

summary = business_summary(df)

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Clientes",
    int(summary["Clientes"])
)

c2.metric(
    "Monto Promedio",
    f"${summary['Monto Promedio']:,.0f}"
)

c3.metric(
    "Edad Promedio",
    f"{summary['Edad Promedio']:.1f}"
)

c4.metric(
    "Default Rate",
    f"{summary['Tasa Default']:.1%}"
)

st.divider()

st.bar_chart(
    df["credit_risk"].value_counts()
)