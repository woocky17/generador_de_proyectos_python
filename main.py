from core.estructura import estructura
from core.inicio import inicio
import os


def main():

    estructura_carpetas, ruta_base = inicio()
    estructura(estructura_carpetas, ruta_base)
    # Cierra la consola automáticamente al finalizar (solo funciona si se ejecuta desde un .bat)
    if os.name == "nt":
        os._exit(0)


if __name__ == "__main__":
    main()
