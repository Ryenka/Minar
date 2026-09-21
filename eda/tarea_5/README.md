# Tarea 5: Análisis Exploratorio de la Evolución de GH-AW

Este directorio contiene la implementación de la **Tarea 5**, enfocada en el análisis evolutivo e histórico de versiones de los archivos Markdown de GitHub Agentic Workflows utilizando el dataset de historial **GHAW-H**.

---

## 1. Origen y Obtención de los Datos

* **Dataset Utilizado**: Dataset histórico **GHAW-H**.
* **Ubicación de Entrada**: Los archivos Parquet del dataset GHAW-H (`repository.parquet`, `source_markdown_file_history.parquet`, `source_markdown_file_version.parquet`, `source_markdown_file_snapshot.parquet`) deben ubicarse en `./data/raw/` o en la ruta correspondiente a tu entorno local.
* **Ubicación de Salida Procesada**: `./eda/tarea_5/data/processed/`

---

## 2. Requisitos y Entorno Python

Para esta tarea se requiere la librería **PyYAML** para parsear los encabezados Frontmatter YAML de las versiones.


# Activar el entorno virtual
source .venv/bin/activate  # En Linux/macOS
.\.venv\Scripts\Activate.ps1  # En Windows

# Instalar PyYAML y asegurar dependencias de visualización
python -m pip install pyyaml pandas pyarrow matplotlib seaborn jupyterlab ipykernel
3. Instrucciones y Orden de Ejecución
Iniciar JupyterLab desde la raíz del proyecto:

jupyter lab
Asegurar que el Kernel seleccionado sea el del entorno virtual del proyecto (Python (miner-venv)).

Ejecutar los notebooks en orden estricto:

01_preparacion_y_agregaciones.ipynb:

Procesa y relaciona las 4 tablas históricas.

Reconstruye las secuencias de versiones consecutivas y calcula las medidas de cambio.

Agrupa datos por archivo y por mes.

Exporta 4 tablas procesadas en eda/tarea_5/data/processed/.

02_boxplots_y_evolucion.ipynb:

Carga las tablas generadas en el primer notebook.

Genera gráficos Boxplot con Seaborn y tablas de resumen de cuartiles (IQR, Q1, Q3, Mediana).

Inspecciona casos puntuales de cambios en body y frontmatter.

Detalla hallazgos y limitaciones.

4. Archivos Procesados Generados
Al finalizar el Notebook 1, la carpeta eda/tarea_5/data/processed/ contendrá:

version_measures.parquet: Medidas a nivel de versión individual.

transitions.parquet: Comparaciones y deltas entre versiones consecutivas.

file_summary.parquet: Agregación consolidada por historia de archivo.

monthly_file_summary.parquet: Agregación de transiciones por archivo y mes.