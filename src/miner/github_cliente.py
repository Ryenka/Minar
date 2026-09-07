from typing import List, Dict, Any
import httpx


class GitHubClient:

    def __init__(self, token: str):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        }
        # Cliente httpx persistente para usar en la CLI y parser
        self.client = httpx.Client(headers=self.headers, timeout=10.0)

    def get_workflow_files(self, repo_full_name: str) -> List[str]:
        """Obtiene todos los nombres de archivo en .github/workflows/."""
        url = f"https://api.github.com/repos/{repo_full_name}/contents/.github/workflows"
        response = self.client.get(url)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                return [
                    item["name"]
                    for item in data
                    if item.get("type") == "file"
                ]
        return []

    def get_workflow_md_files(self, repo_full_name: str) -> List[Dict[str, Any]]:
        """Obtiene la lista de archivos .md dentro de .github/workflows/."""
        url = f"https://api.github.com/repos/{repo_full_name}/contents/.github/workflows"
        response = self.client.get(url)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                return [
                    {
                        "name": item["name"],
                        "path": item["path"],
                        "download_url": item.get("download_url", ""),
                    }
                    for item in data
                    if item.get("type") == "file" and item["name"].endswith(".md")
                ]
        return []

    def close(self):
        """Cierra la conexión del cliente HTTP."""
        self.client.close()