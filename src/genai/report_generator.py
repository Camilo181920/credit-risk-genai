from src.genai.client import get_openai_client
from src.prompts import analyst_prompt
from src.llm.mock_provider import MockLLM


def generate_report(
    assessment,
):
    """
    Genera reporte crediticio con IA.
    Usa OpenAI si existe una clave válida,
    si no usa proveedor local.
    """

    prompt = analyst_prompt(
        assessment
    )


    try:

        client = get_openai_client()


        response = client.chat.completions.create(

            model="gpt-4.1-mini",

            messages=[

                {
                    "role": "system",
                    "content":
                    (
                        "You are a banking "
                        "credit analyst."
                    ),
                },

                {
                    "role": "user",
                    "content": prompt,
                },

            ],

        )


        return (
            response
            .choices[0]
            .message
            .content
        )


    except Exception:

        mock = MockLLM()

        return mock.generate(
            prompt
        )