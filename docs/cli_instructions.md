# Instrucciones de Uso de la CLI - Miner

**Miner** es una herramienta en línea de comandos desarrollada con Python y Typer para la detección de repositorios que utilizan GitHub Agentic Workflows (GH-AW) y la extracción de sus componentes en archivos Parquet relacionales.

---

## Requisitos Previos

1. Asegurarse de tener un token de API de GitHub configurado en las variables de entorno:
   ```bash
   export GITHUB_TOKEN="tu_github_token_aqui"
Instalar la herramienta en modo ejecutable:
   
    pip install -e .

Comando: miner extract
Este comando ejecuta el proceso de extracción consumiendo un archivo CSV filtrado, descarga los archivos .md correspondientes a workflows desde GitHub y genera los tres datasets en formato Parquet.

Argumentos y Opciones
input_file (Argumento requerido): Ruta al archivo CSV generado en la fase previa que contiene los repositorios detectados.

--output-dir / -d (Opción opcional): Ruta del directorio de salida donde se guardarán los tres archivos .parquet. Por defecto es ./dataset_parquet.

Ejemplo Completo de Ejecución
1. Extracción de workflows
Ejecuta el comando especificando el CSV de entrada y el directorio de destino:

Bash
miner extract repositorios_ghaw_entrega.csv --output-dir ./dataset_parquet
Salida en consola esperada:

Plaintext
Iniciando extracción de datos desde repositorios_ghaw_entrega.csv hacia dataset_parquet...
 Extracción completada exitosamente. Datasets Parquet guardados en dataset_parquet
2. Archivos Generados
Al finalizar, el directorio ./dataset_parquet contendrá tres archivos:

repositories.parquet

workflow_files.parquet

workflow_metadata.parquet
