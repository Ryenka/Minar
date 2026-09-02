from typing import List
import httpx


class GitHubClient:

    def __init__(self, token: str):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        }

    def get_workflow_files(self, repo_full_name: str) -> List[str]:
        url = f"https://api.github.com/repos/{repo_full_name}/contents/.github/workflows"
        with httpx.Client(headers=self.headers, timeout=10.0) as client:
            response = client.get(url)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    return [
                        item["name"]
                        for item in data
                        if item.get("type") == "file"
                    ]
            return []