import json
from http import HTTPStatus

from flasgger import SwaggerView
from flask import Response


class Root(SwaggerView):
    def get(self) -> Response:
        return Response(
            response=json.dumps("OK"),
            content_type="application/json",
            status=HTTPStatus.OK.value,
        )
