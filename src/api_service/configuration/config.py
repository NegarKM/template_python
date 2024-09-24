import os
from typing import Final
from urllib.parse import quote_plus


class AppConfig(object):
    TEST_MODE: Final = True if os.environ.get("TEST_MODE") == "True" else False
    BUILD_VERSION: Final = os.environ.get("BUILD_VERSION")


class _DBConfig(object):
    db_driver: Final = os.environ.get("DB_DRIVER")
    db_host: Final = os.environ.get("DB_HOST")
    db_port: Final = os.environ.get("DB_PORT")
    db_name: Final = os.environ.get("DB_NAME")
    db_user: Final = os.environ.get("DB_USER")
    db_password: Final = quote_plus(os.environ.get("DB_PASSWORD", ""))


class DBConfig(object):
    if AppConfig.TEST_MODE:
        SQLALCHEMY_DATABASE_URI = "sqlite://"
    else:
        SQLALCHEMY_DATABASE_URI = f"{_DBConfig.db_driver}://{_DBConfig.db_user}:{_DBConfig.db_password}@{_DBConfig.db_host}:{_DBConfig.db_port}/{_DBConfig.db_name}?charset=utf8mb4"
