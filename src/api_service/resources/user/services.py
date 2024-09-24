from typing import Any
from dependency_injector.wiring import Provide, inject
from exceptions import UserNotFound, UserAlreadyExists


class UserService:
    @inject
    def __init__(self, user_repository: Any = Provide["repositories.user_repository"]):
        self.user_repository = user_repository

    def create_user(self, input_details) -> dict:
        user = self.user_repository.get_user_by_email(input_details["email"])
        if user:
            raise UserAlreadyExists()
        user = self.user_repository.create_user(input_details["email"], input_details["password"])
        if not user:
            raise UserNotFound()
        return {"email": user.email}

    def get_user(self, email) -> dict:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise UserNotFound()
        return {"email": user.email, "created_at": user.created_at}
