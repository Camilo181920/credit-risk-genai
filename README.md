# Credit Risk Analytics & GenAI Assistant

## Overview

Credit Risk Analytics & GenAI Assistant is an end-to-end credit risk
decision-support platform that combines Machine Learning, Explainable AI,
and Generative AI.

The project simulates a financial institution environment where credit
applications are evaluated, risk factors are identified, and executive
reports are generated to support business decisions.

---

# Business Objective

The objective is to build an interpretable credit risk system capable of:

- Predicting customer default probability
- Classifying credit risk level
- Explaining model decisions
- Providing actionable risk insights
- Generating executive credit reports using Generative AI

---

# Main Features

## Credit Risk Prediction

The platform uses Machine Learning models to estimate the probability
of credit default.

Output:

- Default probability
- Risk classification
- Credit decision support


## Explainable AI

SHAP is integrated to explain individual predictions.

The system identifies:

- Main risk drivers
- Variables influencing the decision
- Business-oriented explanations


## Generative AI Assistant

A GenAI layer generates executive credit analysis reports.

The assistant provides:

- Executive summary
- Main risk factors
- Credit recommendation


## Interactive Dashboard

A Streamlit application provides:

- Portfolio overview
- Risk distribution
- Customer assessment
- GenAI reports


---

# Technology Stack

## Data & Machine Learning

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost

## Explainability

- SHAP

## Generative AI

- OpenAI API
- LLM provider abstraction layer

## Application

- Streamlit

## Engineering

- Modular architecture
- Service layer pattern
- Model registry
- Configuration management
- Git version control


---

# System Architecture

                Customer Data
                     |
                     v
             Data Processing
                     |
                     v
          Machine Learning Pipeline
                     |
                     v
            Credit Risk Prediction
                     |
      +--------------+--------------+
      |                             |
      v                             v
SHAP Explainability          GenAI Assistant
      |                             |
      +--------------+--------------+
                     |
                     v
         Executive Decision Support
                     |
                     v
              Streamlit App


---

# Project Structure

credit-risk-genai/

├── app/
│
├── data/
│
├── models/
│
├── notebooks/
│
├── reports/
│
├── sql/
│
├── src/
│ │
│ ├── data/
│ ├── modeling/
│ ├── explainability/
│ ├── genai/
│ ├── services/
│ ├── schemas/
│ └── ui/
│
├── tests/
│
├── README.md
│
└── requirements.txt



---

# Application Workflow

Customer Information

    |
    v

Credit Assessment Service

    |
    +----------------+
    |                |
    v                v

Risk Prediction SHAP Analysis

    |
    v

Credit Assessment Object

    |
    v

GenAI Executive Report

    |
    v

Business Decision Support



---

# Running the Project


## 1. Clone repository


```bash
git clone <repository-url>

cd credit-risk-genai

2. Create virtual environment
python -m venv .venv

source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Train the model
python -m src.train_model
5. Run Streamlit application
streamlit run Home.py
Model Evaluation

The trained model provides:

Accuracy
Precision
Recall
F1 Score
ROC-AUC
Confusion Matrix
Explainability Example

The system can identify risk factors such as:

Low savings level
Existing financial obligations
Account status
High installment ratio

These explanations allow analysts to understand
why a customer was classified as high risk.

Generative AI Example

Generated reports include:

Executive Summary

Customer risk profile explanation.

Main Risk Factors

Identification of the variables contributing
to credit risk.

Recommendation

Suggested actions for credit review.

Future Improvements

Possible extensions:

Model monitoring
Data drift detection
Automated retraining pipeline
Cloud deployment
REST API deployment
Additional LLM providers
Project Status

✅ Machine Learning Pipeline
✅ Credit Risk Prediction
✅ SHAP Explainability
✅ GenAI Integration
✅ Streamlit Dashboard

Project ready for demonstration and further extension.

