import json
from pathlib import Path
import typer
import pandas as pd

from miner.config import get_github_token
from miner.github_cliente import GitHubClient
from miner.processor import DatasetProcessor
from miner.parser import fetch_raw_file_content, parse_workflow_md
from miner.exporter import export_to_parquet

app = typer.Typer(
    help="Miner: herramienta para identificar y procesar repositorios con GitHub Agentic Workflows."
)


# === TAREA 2: Detección de repositorios GH-AW ===
@app.command()
def process(
    input_file: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        help="Archivo CSV de entrada.",
    ),
    output: Path = typer.Option(
        Path("repositorios_ghaw.csv"),
        "--output",
        "-o",
        help="Ruta del archivo CSV de salida.",
    ),
):
    """Procesa un CSV con repositorios candidatos e identifica cuáles usan GH-AW."""
    try:
        token = get_github_token()
        client = GitHubClient(token=token)
        processor = DatasetProcessor(github_client=client)

        typer.echo(f"Procesando archivo: {input_file}...")
        total_found = processor.process(input_file, output)

        typer.secho(
            f" Proceso completado exitosamente.\n"
            f"Se encontraron {total_found} repositorios con GH-AW.\n"
            f"Archivo resultante guardado en: {output}",
            fg=typer.colors.GREEN,
        )
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)


# === TAREA 3: Extracción de workflows y generación de archivos Parquet ===
@app.command()
def extract(
    input_file: Path = typer.Argument(
        ...,
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        help="CSV con los repositorios que usan GH-AW (salida de Tarea 2).",
    ),
    output_dir: Path = typer.Option(
        Path("./dataset_parquet"),
        "--output-dir",
        "-d",
        help="Directorio donde se guardarán los archivos Parquet.",
    ),
):
    """Extrae el Frontmatter y Body de los archivos .md y genera el dataset Parquet."""
    try:
        typer.echo(
            f"Iniciando extracción de datos desde {input_file} hacia {output_dir}..."
        )
        token = get_github_token()
        df_input = pd.read_csv(input_file)

        repositories = []
        workflow_files = []
        workflow_metadata = []

        client = GitHubClient(token=token)
        for idx, row in df_input.iterrows():
                repo_full_name = row["name"]
                owner, repo_name = repo_full_name.split("/")
                repo_id = idx + 1

                repositories.append(
                    {
                        "repository_id": repo_id,
                        "owner": owner,
                        "name": repo_name,
                        "full_name": repo_full_name,
                    }
                )

                try:
                    workflows = client.get_workflow_md_files(repo_full_name)
                    for file_info in workflows:
                        file_path = file_info["path"]
                        file_name = file_info["name"]
                        file_id = f"{repo_id}_{file_name}"

                        raw_content = fetch_raw_file_content(
                            client.client, repo_full_name, file_path
                        )
                        metadata_dict, body_md = parse_workflow_md(raw_content)

                        workflow_files.append(
                            {
                                "file_id": file_id,
                                "repository_id": repo_id,
                                "file_name": file_name,
                                "file_path": file_path,
                                "body_markdown": body_md,
                            }
                        )

                        workflow_metadata.append(
                            {
                                "metadata_id": f"meta_{file_id}",
                                "file_id": file_id,
                                "name": str(metadata_dict.get("name", "")),
                                "description": str(
                                    metadata_dict.get("description", "")
                                ),
                                "tools": json.dumps(
                                    metadata_dict.get("tools", [])
                                ),
                                "raw_frontmatter_json": json.dumps(
                                    metadata_dict
                                ),
                            }
                        )
                except Exception as ex:
                    typer.secho(
                        f"Advertencia en {repo_full_name}: {ex}",
                        fg=typer.colors.YELLOW,
                    )

        export_to_parquet(
            repositories, workflow_files, workflow_metadata, output_dir
        )
        typer.secho(
            f" Extracción completada exitosamente. Datasets Parquet guardados en {output_dir}",
            fg=typer.colors.GREEN,
        )
    except Exception as e:
        typer.secho(f"Error en extracción: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()