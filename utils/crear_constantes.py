import os


def crear_constantes(ruta_base):
    constantes_path = os.path.join(
        os.path.abspath(os.path.join(ruta_base, "config")), "constantes.py")
    if not os.path.exists(constantes_path):
        with open(constantes_path, "w", encoding="utf-8") as f:
            f.write(
                """# Constantes del proyecto
from dotenv import load_dotenv

load_dotenv(override=True)
"""
            )
        print(f"Archivo constantes.py creado en: {constantes_path}")
