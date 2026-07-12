import streamlit as st


def customer_form():
    """
    Renderiza el formulario de evaluación del cliente
    y devuelve un diccionario con los datos ingresados.
    """

    customer = {}

    customer["status"] = st.selectbox(
        "Status",
        ["A11", "A12", "A13", "A14"]
    )

    customer["loan_duration_months"] = st.slider(
        "Loan Duration (Months)",
        min_value=4,
        max_value=72,
        value=24
    )

    customer["credit_history_status"] = st.selectbox(
        "Credit History",
        ["A30", "A31", "A32", "A33", "A34"]
    )

    customer["purpose"] = st.selectbox(
        "Purpose",
        [
            "A40",
            "A41",
            "A42",
            "A43",
            "A44",
            "A45",
            "A46",
            "A48",
            "A49"
        ]
    )

    customer["loan_amount"] = st.number_input(
        "Loan Amount",
        min_value=250,
        max_value=50000,
        value=5000
    )

    customer["savings"] = st.selectbox(
        "Savings",
        ["A61", "A62", "A63", "A64", "A65"]
    )

    customer["employment_duration"] = st.selectbox(
        "Employment Duration",
        ["A71", "A72", "A73", "A74", "A75"]
    )

    customer["installment_ratio"] = st.slider(
        "Installment Ratio",
        1,
        4,
        2
    )

    customer["personal_status_sex"] = st.selectbox(
        "Personal Status",
        ["A91", "A92", "A93", "A94"]
    )

    customer["other_debtors"] = st.selectbox(
        "Other Debtors",
        ["A101", "A102", "A103"]
    )

    customer["present_residence"] = st.slider(
        "Residence Years",
        1,
        4,
        2
    )

    customer["property"] = st.selectbox(
        "Property",
        ["A121", "A122", "A123", "A124"]
    )

    customer["customer_age"] = st.slider(
        "Customer Age",
        18,
        75,
        35
    )

    customer["other_installment_plans"] = st.selectbox(
        "Other Installment Plans",
        ["A141", "A142", "A143"]
    )

    customer["housing"] = st.selectbox(
        "Housing",
        ["A151", "A152", "A153"]
    )

    customer["number_credits"] = st.slider(
        "Number of Existing Credits",
        1,
        4,
        1
    )

    customer["job"] = st.selectbox(
        "Job",
        ["A171", "A172", "A173", "A174"]
    )

    customer["people_liable"] = st.slider(
        "People Liable",
        1,
        2,
        1
    )

    customer["telephone"] = st.selectbox(
        "Telephone",
        ["A191", "A192"]
    )

    customer["foreign_worker"] = st.selectbox(
        "Foreign Worker",
        ["A201", "A202"]
    )

    return customer