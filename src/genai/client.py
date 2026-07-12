import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def get_openai_client():
    """
    Crea un cliente OpenAI.

    Se inicializa solamente cuando
    se necesita.
    """

    api_key = os.getenv(
        "OPENAI_API_KEY"
    )

    if not api_key:
        raise EnvironmentError(
            "OPENAI_API_KEY no está configurada."
        )

    return OpenAI(
        api_key=api_key
    )