import streamlit as st


def metric_card(title, value):

    st.metric(
        label=title,
        value=value
    )


def section(title):

    st.subheader(title)

    st.divider()