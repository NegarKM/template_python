from http import HTTPStatus
from typing import Any

from flask import Response
from flask_restful import Resource

from api_service.common.constants.content_types import ContentTypes
from api_service.resources.build_version.schemas import BuildVersionGETResponse

from dependency_injector.wiring import Provide, inject


class BuildVersion(Resource):
    @inject
    def __init__(self, service: Any = Provide["services.build_version_service"]) -> None:
        self.service = service

    def get(self) -> Response:
        response_json: str = BuildVersionGETResponse().dumps(
            {"build_version": self.service.get_build_version()},
        )

        return Response(
            response=response_json,
            content_type=ContentTypes.JSON,
            status=HTTPStatus.OK.value,
        )
