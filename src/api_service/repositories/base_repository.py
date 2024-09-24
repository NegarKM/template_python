from dependency_injector.wiring import Provide, inject
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import Select
from typing import Any, Callable, Dict, List

from exceptions import RepositoryException


class BaseRepository:
    @inject
    def __init__(self, session: Any) -> None:
        self.session = session
        # self.is_batch_write = False

    def set_batch_write(self, session: Session = None) -> None:
        # self.is_batch_write = True
        if session:
            self.session = session

    def rollback(self) -> None:
        self.session.rollback()
        self.session.close()

    def commit(self) -> None:
        self.session.commit()
        self.session.close()

    def _read_entities(self, stmt: Select, option: str) -> Any:
        try:
            return getattr(self.session.execute(stmt), option)()
        except OperationalError:
            raise
        except Exception:
            raise RepositoryException()
        finally:
            # if not self.is_batch_write:
            self.session.close()

    def _write_entities(self, action: Callable, option: str) -> Any:
        try:
            action(option)
            self.session.flush()
            # if not self.is_batch_write:
            self.session.commit()

            if action == self.session.add:
                return option.id if (option and hasattr(option, "id")) else 0  # type: ignore
        except OperationalError:
            raise
        except Exception:
            self.session.rollback()
            raise RepositoryException()
        finally:
            # if not self.is_batch_write:
            self.session.close()

    def get_all_entities(self, stmt: Select) -> List:
        return self._read_entities(stmt, "all")

    def get_entity(self, stmt: Select) -> Dict:
        return self._read_entities(stmt, "one")

    def get_entity_if_exist(self, stmt: Select) -> Dict:
        return self._read_entities(stmt, "one_or_none")

    def get_first_entity(self, stmt: Select) -> Dict:
        return self._read_entities(stmt, "first")

    def count_all_entities(self, stmt: Select) -> int:
        return len(self._read_entities(stmt, "all"))

    def add_entity(self, entity: Any) -> int:
        return self._write_entities(self.session.add, entity)

    def merge_entity(self, entity: Any) -> None:
        self._write_entities(self.session.merge, entity)

    def delete_entity(self, stmt: Select) -> None:
        self._write_entities(self.session.execute, stmt)

    def update_entity(self, stmt: Select, synchronize_session: str = "fetch") -> None:
        self._write_entities(
            self.session.execute,
            stmt.execution_options(synchronize_session=synchronize_session)
        )
