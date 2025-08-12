import os


def crear_env(ruta_base):
    env_path = os.path.join(os.path.abspath(ruta_base), ".env")
    if not os.path.exists(env_path):
        with open(env_path, "w", encoding="utf-8") as f:
            f.write(
                """
"""
            )
        print(f"Archivo .env creado en: {env_path}")
