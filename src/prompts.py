from __future__ import annotations


def analyst_prompt(
    assessment,
):
    """
    Construye el prompt para el analista
    crediticio basado en IA Generativa.
    """

    if isinstance(
        assessment,
        dict,
    ):

        probability = assessment.get(
            "probability",
            0,
        )

        risk_level = assessment.get(
            "risk_level",
            "Unknown",
        )

        top_features = assessment.get(
            "top_features",
            [],
        )

    else:

        probability = assessment.probability

        risk_level = assessment.risk_level

        top_features = assessment.top_features


    return f"""
You are a Senior Credit Risk Analyst.

Produce a professional executive summary.

Probability of default:

{probability:.2%}

Risk Level:

{risk_level}

Most Important Variables:

{", ".join(top_features)}

The response must contain:

1. Executive Summary

2. Main Risk Factors

3. Recommendation

Maximum 150 words.
"""