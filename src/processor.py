from pathlib import Path
import pandas as pd
from src.miner import has_agentic_workflow
from src.github_cliente import GitHubClient


class DatasetProcessor:

    def __init__(self, github_client: GitHubClient):
        self.client = github_client

    def process(self, input_path: Path, output_path: Path) -> int:
        df = pd.read_csv(input_path)

        # Detectar el nombre de la columna que contiene 'owner/repo'
        target_col = None
        for col in ["full_name", "name", "repository"]:
            if col in df.columns:
                target_col = col
                break

        if not target_col:
            raise KeyError(
                "El CSV debe contener una columna 'full_name', 'name' o 'repository'."
            )

        uses_gh_aw_flags = []

        for _, row in df.iterrows():
            repo_name = row[target_col]
            filenames = self.client.get_workflow_files(repo_name)
            is_aw = (
                1 if (filenames and has_agentic_workflow(filenames)) else 0
            )
            uses_gh_aw_flags.append(is_aw)

        df["uses_github_agentic_workflows"] = uses_gh_aw_flags

        # Filtrar solo los repositorios positivos
        df_filtered = df[df["uses_github_agentic_workflows"] == 1]
        df_filtered.to_csv(output_path, index=False)

        return len(df_filtered)