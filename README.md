# Miner

**Miner** es una aplicación de línea de comandos (CLI) desarrollada en Python para automatizar la identificación de repositorios 
en GitHub que han adoptado **GitHub Agentic Workflows (GH-AW)**. 

---

## ¿Qué problema resuelve Miner?

Con el lanzamiento de GitHub Agentic Workflows el 13 de febrero de 2026, resulta relevante analizar qué proyectos comenzaron a 
utilizar esta tecnología. Determinar esto de forma manual analizando miles de repositorios es ineficiente y propenso a errores.

Miner resuelve este problema procesando de forma automatizada un conjunto de datos de repositorios candidatos (obtenidos 
mediante herramientas como SEART). La herramienta consulta la API de GitHub para inspeccionar el directorio `.github/workflows/` 
de cada repositorio y valida si cumple con el criterio de adopción de GH-AW: la presencia de al menos un par de archivos 
compuestos por un archivo Markdown (`nombre.md`) y su respectivo archivo compilado (`nombre.lock.yml`) con el mismo nombre base.

Como resultado, la aplicación genera un archivo CSV limpio y filtrado que conserva únicamente los repositorios confirmados como 
usuarios de GitHub Agentic Workflows.

---

## 1. Preparación del Entorno Python

Miner requiere **Python 3.10** o superior. Se recomienda utilizar un entorno virtual aislado para gestionar la instalación del 
proyecto.

### Opción A: Utilizando `uv` (Recomendado)
Si tienes instalado `uv`, crea y activa el entorno virtual ejecutando:

#### bash
uv venv
source .venv/bin/activate    / En Linux / macOS
.venv\Scripts\activate      / En Windows (PowerShell/CMD)


### Opción B: Utilizando venv (Estándar de Python)
También puedes usar el módulo nativo venv:Bashpython -m venv .venv
source .venv/bin/activate    # En Linux / macOS
.venv\Scripts\activate      # En Windows (PowerShell/CMD)

---


## 2. Instalación de Dependencias
Una vez activado el entorno virtual, instala las dependencias del 
proyecto ejecutando:

Bashpip install -e .
Si deseas instalar también las herramientas de desarrollo para ejecutar 
las pruebas automatizadas (pytest), utiliza:Bashpip install -e ".[dev]"

---

## 3. Configuración del Archivo .env y GITHUB_TOKEN
Para realizar consultas a la API de GitHub sin sufrir bloqueos de
límite de peticiones (rate limiting), Miner requiere un Token de Acceso
Personal (PAT) de GitHub.

---


## Paso 3.1: Crear el archivo .env
Copia el archivo de plantilla .env.example para generar tu archivo de configuración local .env:Bashcp .env.example .env
Nota de seguridad: El archivo .env está incluido en el .gitignore del proyecto y nunca debe ser subido al repositorio.

## Paso 3.2: Generar y configurar tu GITHUB_TOKEN
Ingresa a tu cuenta de GitHub y ve a Settings -> Developer Settings -> Personal access tokens -> Tokens (classic).Haz clic en Generate new token (classic).Asigna un nombre al token y selecciona el alcance (scope) repo o acceso de lectura pública.Copia el token generado.Abre el archivo .env creado en tu proyecto y pega tu token:[Token_Github]

---

## 4. Ejemplo de Ejecución de Miner/Minar
Miner se ejecuta desde la consola a través de la interfaz CLI creada con Typer.Sintaxis básica:Bashminer <archivo_entrada.csv> --output <archivo_salida.csv>
Ejemplo de ejecución real:Bashminer repositorios_candidatos.csv --output repositorios_ghaw.csv

---

## 5. Archivos de Entrada y Salida
Archivo de Entrada (<archivo_entrada.csv>)
° Descripción: Es el CSV que contiene el listado de repositorios 
candidatos a analizar.
°Estructura requerida: Debe ser un archivo CSV bien formado que contenga una columna identificadora del repositorio con el formato propietario/nombre-repositorio (la columna puede llamarse full_name, name o repository).Archivo de Salida (<archivo_salida.csv>)Descripción: Es el CSV generado automáticamente por Miner tras completar el análisis.Estructura resultante: Conserva la estructura y metadatos del archivo de entrada original, agregando la nueva columna binaria uses_github_agentic_workflows (donde el valor es 1). El archivo es filtrado para conservar únicamente las filas de repositorios que cumplen las condiciones de uso de GH-AW.

---

## 6. Ejecución de Pruebas Automatizadas
Para verificar la lógica de detección de GitHub Agentic Workflows a través de los tests unitarios con pytest, ejecuta:Bashpytest