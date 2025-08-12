import os


def crear_requirements(ruta_base):
    requirements_path = os.path.join(
        os.path.abspath(ruta_base), "requirements.txt")
    if not os.path.exists(requirements_path):
        with open(requirements_path, "w", encoding="utf-8") as f:
            f.write(
                """
loguru>=0.7.2
sqlalchemy>=2.0.0
pyodbc>=4.0.39
pandas>=2.3.1
dotenv>=0.9.9
"""
            )
        print(f"Archivo requirements.txt creado en: {requirements_path}")
