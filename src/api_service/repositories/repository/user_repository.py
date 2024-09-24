from dependency_injector.wiring import Provide, inject
from sqlalchemy import func
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.sql.expression import select, update
from typing import Any, Dict

from api_service.repositories.base_repository import BaseRepository


class UserTableRepository(BaseRepository):
    @inject
    def __init__(self, database: Any = Provide["app.database_singleton"]) -> None:
        from api_service.models.db_models.user import DBUser

        self.user = DBUser
        self.session = scoped_session(sessionmaker(bind=database.db_engine))()
        super().__init__(session=self.session)

    def get_user_by_email(self, email: str) -> Dict:
        return super().get_entity_if_exist(
            (
                select(*[getattr(self.user, col) for col in self.user.__table__.columns.keys()]).where(
                    func.lower(self.user.email) == email.lower()
                )
            )
        )

    def create_user(self, email: str, password: str) -> Dict:
        new_user = self.user(email=email.lower(), password=password)
        super().add_entity(new_user)
        return self.get_user_by_email(email)

    def change_email(self, old_email: str, new_email: str) -> None:
        super().update_entity(
            (update(self.user).where(func.lower(self.user.email) == old_email.lower()).values(email=new_email.lower()))
        )
