from typing import Final
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, create_engine

from api_service.configuration.config import DBConfig


class DatabaseManager:
    def __init__(self, echo: bool = False, pool_recycle: int = 1800) -> None:
        self.db_engine: Final = create_engine(
            DBConfig.SQLALCHEMY_DATABASE_URI, echo=echo, pool_recycle=pool_recycle
        )
        self.metadata: Final = MetaData(bind=self.db_engine)
        self.BaseDB: Final = declarative_base(metadata=self.metadata)
