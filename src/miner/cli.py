from pathlib import Path
import typer
from miner.config import get_github_token
from miner.github_cliente import GitHubClient
from miner.processor import DatasetProcessor

app = typer.Typer(
    help="Miner: herramienta para identificar repositorios con GitHub Agentic Workflows."
)


@app.command()
def main(
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


if __name__ == "__main__":
    app()