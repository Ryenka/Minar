# Diccionario de Datos

Este documento describe las tablas, columnas, tipos de datos y restricciones de integridad relacional del dataset en formato Parquet generado por Miner.

---

## Tabla: `repositories`
Almacena la información de identificación de los repositorios procesados.

| Columna | Tipo de Dato | Clave | Descripción |
| :--- | :--- | :--- | :--- |
| `repository_id` | `INTEGER` | **PK** | Identificador único numérico del repositorio. |
| `owner` | `STRING` | - | Nombre del usuario u organización propietaria en GitHub. |
| `name` | `STRING` | - | Nombre del repositorio. |
| `full_name` | `STRING` | - | Nombre completo en formato `owner/name`. |

---

## Tabla: `workflow_files`
Contiene la ubicación y el contenido principal (body) de los archivos `.md` de workflows encontrados.

| Columna | Tipo de Dato | Clave | Descripción |
| :--- | :--- | :--- | :--- |
| `file_id` | `STRING` | **PK** | Identificador único del archivo (`{repository_id}_{file_name}`). |
| `repository_id` | `INTEGER` | **FK** | Clave foránea que referencia a `repositories.repository_id`. |
| `file_name` | `STRING` | - | Nombre del archivo `.md`. |
| `file_path` | `STRING` | - | Ruta relativa del archivo dentro del repositorio. |
| `body_markdown` | `STRING` | - | Contenido principal del archivo Markdown (excluyendo Frontmatter). |

---

## Tabla: `workflow_metadata`
Almacena los metadatos extraídos del bloque Frontmatter (YAML) de cada archivo de workflow.

| Columna | Tipo de Dato | Clave | Descripción |
| :--- | :--- | :--- | :--- |
| `metadata_id` | `STRING` | **PK** | Identificador único del metadato (`meta_{file_id}`). |
| `file_id` | `STRING` | **FK** | Clave foránea que referencia a `workflow_files.file_id`. |
| `name` | `STRING` | - | Nombre asignado al workflow en el Frontmatter. |
| `description` | `STRING` | - | Descripción del workflow. |
| `tools` | `STRING` (JSON) | - | Cadena JSON con la lista de herramientas/tools declaradas. |
| `raw_frontmatter_json` | `STRING` (JSON) | - | Objeto JSON completo con todos los campos crudos del Frontmatter. |