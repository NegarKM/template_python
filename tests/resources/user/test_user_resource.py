import os
import json
from http import HTTPStatus
from unittest import TestCase
from datetime import datetime
from sqlalchemy import func

from exceptions import UserAlreadyExists, InvalidInputError, UnauthorizedError
from api_service.models.db_models.user import DBUser
from tests.fixtures.clients import client
from tests.fixtures.session import db_session
from tests.fixtures.configs import TOKEN


class TestUser:
    def test_create_user_ok(self, client, db_session) -> None:
        body = {"email": "myuser@sample.com", "password": "encoded"}
        response = client.post(
            f"/api/{os.getenv('API_VERSION', 'v1')}/users",
            headers={
                "Authorization": f"Bearer {TOKEN}",
                "Content-Type": "application/json",
            },
            json=body
        )

        user = db_session.query(DBUser).filter(func.lower(DBUser.email) == "myuser@sample.com").one_or_none()
        TestCase().assertIsNotNone(user)
        TestCase().assertEqual(user.email, "myuser@sample.com")

        assert response.status_code == HTTPStatus.CREATED
        TestCase().assertDictEqual(
            json.loads(response.data),
            {
                "email": "myuser@sample.com"
            },
        )

    def test_create_user_with_exsisting_email(self, client) -> None:
        body = {"email": "myuser@sample.com", "password": "encoded"}
        client.post(
            f"/api/{os.getenv('API_VERSION', 'v1')}/users",
            headers={
                "Authorization": f"Bearer {TOKEN}",
                "Content-Type": "application/json",
            },
            json=body
        )
        response = client.post(
            f"/api/{os.getenv('API_VERSION', 'v1')}/users",
            headers={
                "Authorization": f"Bearer {TOKEN}",
                "Content-Type": "application/json",
            },
            json=body
        )
        assert response.status_code == HTTPStatus.BAD_REQUEST
        TestCase().assertDictEqual(
            json.loads(response.data),
            {
                "errorCode": UserAlreadyExists.error_code,
                "errorMessage": UserAlreadyExists.description,
                "errorCauses": [],
            },
        )

    def test_create_user_with_invalid_input(self, client) -> None:
        body = {"username": "myuser@sample.com", "password": "encoded"}
        response = client.post(
            f"/api/{os.getenv('API_VERSION', 'v1')}/users",
            headers={
                "Authorization": f"Bearer {TOKEN}",
                "Content-Type": "application/json",
            },
            json=body
        )
        assert response.status_code == InvalidInputError.code
        print(f"response.data: {response.data}")
        TestCase().assertDictEqual(
            json.loads(response.data),
            {
                "errorCode": InvalidInputError.error_code,
                "errorMessage": InvalidInputError.description,
                "errorCauses": {"email": ["Missing data for required field."], "username": ["Unknown field."]}
            },
        )

    def test_create_user_unauthorized(self, client) -> None:
        body = {"email": "myuser@sample.com", "password": "encoded"}
        response = client.post(
            f"/api/{os.getenv('API_VERSION', 'v1')}/users",
            headers={
                "Content-Type": "application/json",
            },
            json=body
        )
        assert response.status_code == UnauthorizedError.code

    def test_get_user_ok(self, client, db_session) -> None:
        body = {"email": "myuser@sample.com", "password": "encoded"}
        client.post(
            f"/api/{os.getenv('API_VERSION', 'v1')}/users",
            headers={
                "Authorization": f"Bearer {TOKEN}",
                "Content-Type": "application/json",
            },
            json=body
        )
        user = db_session.query(DBUser).filter(func.lower(DBUser.email) == "myuser@sample.com").one_or_none()
        TestCase().assertIsNotNone(user)
        TestCase().assertEqual(user.email, "myuser@sample.com")

        get_user_response = client.get(
            f"/api/{os.getenv('API_VERSION', 'v1')}/users?email=myuser@sample.com",
            headers={
                "Authorization": f"Bearer {TOKEN}",
            },
        )

        assert get_user_response.status_code == HTTPStatus.OK
        TestCase().assertDictEqual(
            json.loads(get_user_response.data),
            {
                "email": "myuser@sample.com",
                "created_at": datetime.today().strftime('%Y-%m-%d')
            },
        )

    def test_get_user_not_found(self, client) -> None:
        response = client.get(
            f"/api/{os.getenv('API_VERSION', 'v1')}/users?email=notfoundemail@sample.com",
            headers={
                "Authorization": f"Bearer {TOKEN}",
            },
        )
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_get_user_unauthorized(self, client) -> None:
        response = client.get(f"/api/{os.getenv('API_VERSION', 'v1')}/users?email=myuser@sample.com")
        assert response.status_code == UnauthorizedError.code
