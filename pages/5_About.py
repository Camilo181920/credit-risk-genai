import streamlit as st


st.title("ℹ️ About the Project")


st.markdown(
"""
# Credit Risk Analytics & GenAI Assistant

## Overview

This project is an end-to-end credit risk analytics platform
that combines Machine Learning, Explainable AI and Generative AI
to support credit decision-making.

The system evaluates customer credit applications, estimates
default probability, identifies the main risk drivers and generates
an executive credit analysis report.

---

## Architecture

The solution follows a modular architecture:
Customer Data
|
v
Data Processing
|
v
Machine Learning Pipeline
|
v
Risk Prediction
|
+----------------+
| |
v v
SHAP Analysis GenAI Report
| |
+----------------+
|
v
Executive Decision Support

---

## Technologies

### Machine Learning

- Python
- Scikit-Learn
- XGBoost
- Pandas
- NumPy

### Explainability

- SHAP

### Generative AI

- OpenAI API
- LLM integration layer

### Application

- Streamlit

### Engineering

- Modular architecture
- Service layer design
- Model registry
- Configuration management

---

## Main Capabilities

### Credit Assessment

Evaluates individual customers and provides:

- Probability of default
- Risk classification
- Main risk factors

---

### Explainable AI

Uses SHAP values to identify the variables
that influence the credit decision.

---

### Generative AI Assistant

Creates executive summaries:

- Risk explanation
- Main concerns
- Credit recommendation

---

## Objective

Provide a decision-support system that helps analysts
understand credit risk while maintaining transparency
and explainability.

"""
)