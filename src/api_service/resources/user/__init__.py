from http import HTTPStatus
from typing import Any, Dict

from flask import Response, request
from flasgger import SwaggerView
from marshmallow import ValidationError

from api_service.common.constants.content_types import ContentTypes
from api_service.resources.user.schemas import UsersPOSTRequest, UserGETResponse
from exceptions import InvalidInputError
from api_service.configuration.resource_decorators import validate_authorization_token

from dependency_injector.wiring import Provide, inject


class BaseUser(SwaggerView):
    @inject
    def __init__(self, service: Any = Provide["services.user_service"]) -> None:
        self.service = service


class User(BaseUser):
    definitions: Dict[str, Any] = {
        "UsersPOSTRequest": UsersPOSTRequest,
        "UserGETResponse": UserGETResponse,
    }

    @validate_authorization_token
    def post(self) -> Response:
        try:
            input_details = UsersPOSTRequest().load(request.get_json())
        except ValidationError as err:
            raise InvalidInputError(err.messages)
        user = self.service.create_user(input_details)

        return Response(
            response=UserGETResponse().dumps(user) if user else {},
            content_type=ContentTypes.JSON,
            status=HTTPStatus.CREATED.value,
        )

    @validate_authorization_token
    def get(self) -> Response:
        query_params = dict(request.args)
        response = self.service.get_user(query_params.pop("email"))

        return Response(
            response=UserGETResponse().dumps(response),
            content_type=ContentTypes.JSON,
            status=HTTPStatus.OK.value,
        )
