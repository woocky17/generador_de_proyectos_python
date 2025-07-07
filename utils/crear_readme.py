import os


def crear_readme(ruta_base):
    readme_path = os.path.join(os.path.abspath(ruta_base), "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(
                """# Proyecto

Este proyecto ha sido generado automáticamente.

## Estructura básica

- src/: Código fuente principal
- config/: Configuración y constantes
- utils/: Utilidades
- data/: Datos

## Primeros pasos

1. Crear entorno virtual:

   ```sh
   python -m venv .venv
   ```

2. Activar entorno virtual:

   ```sh
   .venv\Scripts\activate
   ```

3. Instalar dependencias principales:

   ```sh
   pip install requests
   ```

4. Instalar dependencias del proyecto:

   ```sh
   pip install -r requirements.txt
   ```

5. (Opcional) Actualizar requirements.txt con los paquetes instalados:

   ```sh
   pip freeze > requirements.txt
   ```

"""
            )
        print(f"Archivo README.md creado en: {readme_path}")
