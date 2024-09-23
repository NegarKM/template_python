import os
from typing import Final

from flasgger import Swagger
from flask import Flask, Response, request
from flask_restful import Api

from api_service.app.routes import initialize_routes
from api_service.configuration.swagger import SWAGGER_CONFIG, SWAGGER_TEMPLATE


def create_application() -> Flask:
    app = Flask(__name__)

    api = Api(
        app,
        prefix=f"/api/{os.getenv('API_VERSION', 'v1')}",
        catch_all_404s=True,
    )
    app.config["SWAGGER"] = SWAGGER_CONFIG

    Swagger(app, template=SWAGGER_TEMPLATE)

    initialize_routes(api)

    return app


application = create_application()
