from core.estructura import estructura
import os

from core.inicio import inicio


def main():
    # Estructura de carpetas por defecto
    estructura_carpetas = [
        "src",
        os.path.join("src", "api"),
        os.path.join("src", "database"),
        os.path.join("src", "core"),
        os.path.join("src", "utils"),
        os.path.join("src", "models"),
        os.path.join("src", "models", "mapper"),
        "config",
        "data",
    ]
    crear_readme = True
    crear_gitignore = True
    estructura_carpetas, ruta_base, crear_readme, crear_gitignore = inicio()
    estructura(estructura_carpetas, ruta_base, crear_readme, crear_gitignore)
    print("\n¡Estructura de proyecto creada en la carpeta actual!")
    if os.name == "nt":
        os._exit(0)


if __name__ == "__main__":
    main()
