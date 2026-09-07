"""Módulo para exportar los DataFrames procesados a archivos Apache Parquet."""

from pathlib import Path
import pandas as pd


def export_to_parquet(
    repositories: list[dict],
    workflow_files: list[dict],
    workflow_metadata: list[dict],
    output_dir: Path,
) -> None:
    """Convierte las listas de entidades a DataFrames y las guarda como archivos Parquet."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Tabla Repositorios
    df_repos = pd.DataFrame(repositories)
    df_repos.to_parquet(output_dir / "repositories.parquet", engine="pyarrow", index=False)

    # 2. Tabla Archivos Workflow
    df_files = pd.DataFrame(workflow_files)
    df_files.to_parquet(output_dir / "workflow_files.parquet", engine="pyarrow", index=False)

    # 3. Tabla Metadatos del Frontmatter
    df_meta = pd.DataFrame(workflow_metadata)
    df_meta.to_parquet(output_dir / "workflow_metadata.parquet", engine="pyarrow", index=False)