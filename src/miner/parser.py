"""Módulo para descargar y parsear archivos .md con Frontmatter YAML."""

import json
import frontmatter
import httpx


def fetch_raw_file_content(client: httpx.Client, repo_full_name: str, file_path: str) -> str:
    """Descarga el contenido crudo de un archivo desde GitHub API."""
    url = f"https://raw.githubusercontent.com/{repo_full_name}/main/{file_path}"
    response = client.get(url)
    
    # Si la rama principal no es 'mai', intenta con 'master'
    if response.status_code == 404:
        url = f"https://raw.githubusercontent.com/{repo_full_name}/master/{file_path}"
        response = client.get(url)
        
    response.raise_for_status()
    return response.text


def parse_workflow_md(raw_content: str) -> tuple[dict, str]:
    """
    Separa el Frontmatter (YAML) y el Body (Markdown).
    Retorna:
        tuple[dict, str]: (metadatos_frontmatter, contenido_markdown_body)
    """
    post = frontmatter.loads(raw_content)
    metadata = dict(post.metadata)
    body = post.content
    return metadata, body