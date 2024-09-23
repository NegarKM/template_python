import os
from typing import Any, Final

from flasgger import Swagger
from flask import Flask, Response, request
from flask_restful import Api

import api_service.configuration.containers as containers
import api_service.resources
from api_service.app.routes import initialize_routes
from api_service.configuration.swagger import SWAGGER_CONFIG, SWAGGER_TEMPLATE


def create_application(application_containers: Any = None) -> Flask:
    app = Flask(__name__)

    if not application_containers:
        application_containers = containers.ApplicationContainers()

        application_containers.wire(
            packages=[
                api_service.resources,
            ]
        )

    api = Api(
        app,
        prefix=f"/api/{os.getenv('API_VERSION', 'v1')}",
        catch_all_404s=True,
    )

    app.config["SWAGGER"] = SWAGGER_CONFIG
    Swagger(app, template=SWAGGER_TEMPLATE)

    app.containers = application_containers

    initialize_routes(api)

    return app


application = create_application()
