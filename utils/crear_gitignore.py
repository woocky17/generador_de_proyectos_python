import os


def crear_gitignore(ruta_base):
    gitignore_path = os.path.join(os.path.abspath(ruta_base), ".gitignore")
    if not os.path.exists(gitignore_path):
        with open(gitignore_path, "w", encoding="utf-8") as f:
            f.write(
                """
# Ignorar archivos de Python
*.pyc
__pycache__/
# Ignorar entornos virtuales
venv/
# Ignorar archivos de configuración de IDEs
.idea/
.vscode/
# Ignorar archivos de sistema
.DS_Store
# Ignorar archivos de logs
*.log
# Ignorar archivos de caché
*.cache
# Ignorar archivos de configuración de entorno
.env
"""
            )
        print(f"Archivo .gitignore creado en: {gitignore_path}")
