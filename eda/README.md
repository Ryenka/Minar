Markdown
# Tarea 4: Análisis Exploratorio de Datos (EDA) - GitHub Agentic Workflows

Este directorio contiene el análisis exploratorio de datos sobre los repositorios y archivos Markdown de GitHub Agentic Workflows (GH-AW) extraídos mediante la herramienta **Miner**.

---

## 1. Origen de los Datos
* **Dataset en Hugging Face**: [Tu-Usuario/github-agentic-workflows-dataset](https://huggingface.co/datasets/Tu-Usuario/github-agentic-workflows-dataset)
* **Ubicación local recomendada de los archivos Parquet**:
  * Archivos crudos (Entrada Tarea 3): `./dataset_parquet/`
  * Archivos procesados (Salida Notebook 1): `./eda/data/processed/`

---

## 2. Instalación y Configuración del Entorno

Asegúrate de activar el entorno virtual del proyecto Python e instalar las dependencias requeridas para ejecutar el análisis:

bash
# Activar entorno virtual (PowerShell en Windows)
.\.venv\Scripts\Activate.ps1

# Activar entorno virtual (Bash/Linux/macOS)
source .venv/bin/activate

# Instalar dependencias para JupyterLab, manipulación de datos y visualización
python -m pip install jupyterlab ipykernel pandas pyarrow matplotlib seaborn

# Registrar el Entorno en Jupyter
Para asegurarte de que JupyterLab reconozca y utilice el entorno virtual del proyecto:

En Bash:

python -m ipykernel install --user --name=miner-venv --display-name "Python (miner-venv)"

---

## 3. Instrucciones y Orden de Ejecución
### Iniciar JupyterLab desde la raíz del proyecto:

En Bash:

jupyter lab

Al abrir los notebooks, verifica que el kernel seleccionado en la esquina superior derecha sea "Python (miner-venv)".

### Orden estricto de ejecución:

eda/01_descripcion_y_calidad.ipynb: Carga las tablas relacionales Parquet originales, evalúa la integridad y calidad de los datos, aplica transformaciones de limpieza y guarda las tablas procesadas en eda/data/processed/.

eda/02_exploracion_y_hallazgos.ipynb: Carga los datos limpios desde eda/data/processed/, analiza las distribuciones del body y frontmatter, responde preguntas exploratorias cruzando tablas y sintetiza los hallazgos principales.