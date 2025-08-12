import os


def crear_main_py(ruta_base):
    main_py_path = os.path.join(os.path.abspath(ruta_base), "main.py")
    if not os.path.exists(main_py_path):
        with open(main_py_path, "w", encoding="utf-8") as f:
            f.write(
                """
from loguru import logger
import sys

def main():
    logger.remove()
    logger.add(sys.stderr, colorize=True, level='INFO',
               format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <magenta>{module}</magenta> | <cyan>{function}:{line}</cyan> | <level>{message}</level>")
    logger.add(".log", rotation='30 days', retention=12, colorize=False, level='INFO',
               format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module} | {function}:{line} | {message}")

    logger.info('Process has started')


    logger.success('Process finished successfully')
if __name__ == \"__main__\":
    main()
"""
            )
        print(f"Archivo main.py creado en: {main_py_path}")
