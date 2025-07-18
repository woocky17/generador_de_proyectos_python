import os


def crear_error_utils(ruta_base):
    error_utils_path = os.path.join(
        os.path.abspath(os.path.join(ruta_base, "src/utils")), "error_utils.py")
    if not os.path.exists(error_utils_path):
        with open(error_utils_path, "w", encoding="utf-8") as f:
            f.write(
                """
import sys
from loguru import logger


def error_message_with_finisher(error, message: str = "An error occurred"):
    if isinstance(error, dict) and error.get('error'):
        logger.error(
            f"{message}: {error['message']} - {error['exception'] if 'exception' in error else 'No exception provided'}"
        )
        logger.info('Process finished with errors')
        sys.exit(1)


def error_message_without_finisher(error, message: str = "An error occurred"):
    if isinstance(error, dict) and error.get('error'):
        logger.error(
            f"{message}: {error['message']} - {error['exception'] if 'exception' in error else 'No exception provided'}"
        )
"""
            )
        print(f"Archivo error_utils.py creado en: {error_utils_path}")

