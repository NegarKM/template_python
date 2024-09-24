import os

from sqlalchemy.engine import Engine
from sqlalchemy.sql import text

# isort: off
# fmt: off
# from api_service.configuration.config import DBConfig
#
# DBConfig.SQLALCHEMY_DATABASE_URI = "sqlite://"

from api_service.app import application
# fmt: on
# isort: on

database = application.database
db_engine = database.db_engine


def execute_command(engine: Engine, command: str) -> None:
    try:
        engine.execute(text(command.replace("AUTO_INCREMENT", "")))
    except Exception as e:
        raise Exception(f"Error in executing sql command: {sql_command} - {e}")


init_sql_file = os.environ.get("DB_INIT_FILE")
with open(init_sql_file, "r") as sql_file:
    sql_command = ""

    for line in sql_file:
        if not line.startswith("--") and not line.startswith("USE") and line.strip("\n"):
            # Append line to the command string
            sql_command += line.strip("\n")

            # If the command string ends with ';', it is a full statement
            if sql_command.endswith(";"):
                try:
                    execute_command(db_engine, sql_command)
                finally:
                    sql_command = ""
                    db = ""
