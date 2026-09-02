import os
from dotenv import load_dotenv

load_dotenv()


def get_github_token() -> str:
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError(
            "La variable GITHUB_TOKEN no está configurada en el archivo .env"
        )
    return token