
from loguru import logger
import sys

def main():
    logger.remove()
    logger.add(sys.stderr, colorize=True, level='INFO',
               format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <magenta>{module}</magenta> | <cyan>{function}:{line}</cyan> | <level>{message}</level>")
    logger.add(".log", rotation='30 days', retention=12, colorize=False, level='INFO',
               format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module} | {function}:{line} | {message}")

    logger.info('Process has started')

    # Aquí puedes añadir el código principal de tu aplicación

    logger.success('Process finished successfully')
if __name__ == "__main__":
    main()
