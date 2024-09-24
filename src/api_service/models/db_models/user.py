from api_service.models.base import BaseDB


class DBUser(BaseDB):
    __tablename__ = "user"
    __table_args__ = {"autoload": True}
    __mapper_args__ = {"confirm_deleted_rows": False}
