from typing import List, Set


def has_agentic_workflow(filenames: List[str]) -> bool:
    """Determina si un conjunto de archivos contiene al menos un par
    'nombre.md' y 'nombre.lock.yml' dentro de .github/workflows/.
    """
    md_bases: Set[str] = {
        f[:-3] for f in filenames if f.endswith(".md") and not f.startswith(".")
    }
    lock_bases: Set[str] = {
        f[:-9]
        for f in filenames
        if f.endswith(".lock.yml") and not f.startswith(".")
    }

    return len(md_bases.intersection(lock_bases)) > 0