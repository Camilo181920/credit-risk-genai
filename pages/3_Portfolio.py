import streamlit as st

from src.data import load_data

st.title("📈 Portfolio Analysis")

df = load_data("german_credit.csv")

st.dataframe(df.head())

st.bar_chart(
    df["loan_amount"]
)