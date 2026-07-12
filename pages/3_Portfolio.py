import streamlit as st

from src.data import load_data


st.title("📈 Portfolio Analysis")


@st.cache_data
def get_data():

    return load_data(
        "german_credit.csv"
    )


df = get_data()


# =========================
# DATA PREVIEW
# =========================

st.subheader(
    "Customer Portfolio"
)


st.dataframe(
    df.head(20),
    use_container_width=True
)



st.divider()



# =========================
# RISK SEGMENTATION
# =========================

st.subheader(
    "Risk Segmentation"
)


risk_distribution = (
    df["credit_risk"]
    .value_counts()
)


st.bar_chart(
    risk_distribution
)



st.divider()



# =========================
# CREDIT AMOUNT
# =========================

st.subheader(
    "Credit Amount Distribution"
)


st.bar_chart(
    df["amount"]
)



st.divider()



# =========================
# CREDIT DURATION
# =========================

col1, col2 = st.columns(2)


with col1:

    st.subheader(
        "Loan Duration"
    )

    st.bar_chart(
        df["duration"]
        .value_counts()
        .sort_index()
    )



with col2:

    st.subheader(
        "Customer Age"
    )

    st.bar_chart(
        df["age"]
        .value_counts()
        .sort_index()
    )



st.divider()



# =========================
# SUMMARY
# =========================

st.subheader(
    "Portfolio Summary"
)


good_clients = (
    (df["credit_risk"] == 0)
    .sum()
)


bad_clients = (
    (df["credit_risk"] == 1)
    .sum()
)


c1, c2 = st.columns(2)


c1.metric(
    "Good Credit Customers",
    good_clients
)


c2.metric(
    "High Risk Customers",
    bad_clients
)