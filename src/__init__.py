"""Paquete para la detección automatizada de GitHub Agentic Workflows."""

from src.miner import has_agentic_workflow
from src.github_cliente import GitHubClient
from src.processor import DatasetProcessor

__version__ = "0.1.0"

__all__ = [
    "has_agentic_workflow",
    "GitHubClient",
    "DatasetProcessor",
    "__version__",
]