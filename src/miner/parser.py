"""Módulo para descargar y parsear archivos .md con Frontmatter YAML."""

import json
import yaml
import frontmatter
import httpx


def sanitize_keys(obj):
    """
    Convierte recursivamente todas las claves de un diccionario/lista a tipos nativos seguros.
    """
    if isinstance(obj, dict):
        return {str(k): sanitize_keys(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple, set)):
        return [sanitize_keys(item) for item in obj]
    return obj


def fetch_raw_file_content(client: httpx.Client, repo_full_name: str, file_path: str) -> str:
    """Descarga el contenido crudo de un archivo desde la API de GitHub."""
    clean_path = file_path.lstrip("/")
    url = f"https://raw.githubusercontent.com/{repo_full_name}/main/{clean_path}"
    response = client.get(url)
    
    if response.status_code == 404:
        url = f"https://raw.githubusercontent.com/{repo_full_name}/master/{clean_path}"
        response = client.get(url)
        
    response.raise_for_status()
    return response.text


def parse_workflow_md(raw_content: str) -> tuple[dict, str]:
    """
    Separa el Frontmatter (YAML) y el Body (Markdown) de forma ultrasegura.
    """
    try:
        # Intento de parseo estándar con python-frontmatter
        post = frontmatter.loads(raw_content)
        raw_metadata = dict(post.metadata) if post.metadata else {}
        body = post.content or ""
    except Exception:
        # Fallback defensivo si el Frontmatter YAML tiene un formato inválido
        raw_metadata = {}
        body = raw_content

        if raw_content.startswith("---"):
            parts = raw_content.split("---", 2)
            if len(parts) >= 3:
                try:
                    parsed_yaml = yaml.safe_load(parts[1])
                    if isinstance(parsed_yaml, dict):
                        raw_metadata = parsed_yaml
                    body = parts[2]
                except Exception:
                    pass

    sanitized_metadata = sanitize_keys(raw_metadata)
    return sanitized_metadata, body