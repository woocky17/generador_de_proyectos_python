import os


def crear_conection_db(ruta_base):
    conection_path = os.path.join(
        os.path.abspath(os.path.join(ruta_base, "src/database")), "conection_db.py")
    if not os.path.exists(conection_path):
        with open(conection_path, "w", encoding="utf-8") as f:
            f.write(
                """
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.exc import SQLAlchemyError, OperationalError
from loguru import logger


def open_db(db_info: str):
    try:
        odbc_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={db_info[0]};DATABASE={db_info[1]};UID={db_info[2]};PWD={db_info[3]}"

        connection_url = URL.create(
            \"mssql+pyodbc\",
            query={\"odbc_connect\": odbc_str}
        )
        engine = create_engine(connection_url)
        with engine.connect() as conn:
            conn.execute(text(\"SELECT 1\"))

        return engine

    except OperationalError as oe:
        return {
            \"error\": True,
            \"message\": f\"OperationalError during connection {str(oe)}\",
        }
    except SQLAlchemyError as se:
        return {
            \"error\": True,
            \"message\": f\"SQLAlchemyError during connection {str(se)}\",
        }
    except Exception as e:
        return {
            \"error\": True,
            \"message\": f\"Unexpected error {str(e)}\",
        }


class DatabaseConnection:
    def __init__(self, db_info: str):
        self.db_info = db_info
        self.engine = None

    def __enter__(self):
        self.engine = open_db(self.db_info)
        if isinstance(self.engine, dict) and 'error' in self.engine:
            return self.engine
        logger.success(\"Database connection established\")
        return self.engine

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if self.engine:
                self.engine.dispose()
                logger.success(\"Database connection closed\")
        except Exception as e:
            self.engine = None
            return False
"""
            )
        print(f"Archivo conection_db.py creado en: {conection_path}")
