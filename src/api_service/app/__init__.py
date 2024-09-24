import os
from typing import Any, Final

from flasgger import Swagger
from flask import Flask, Response, request
from flask_restful import Api

from api_service.configuration.logger import Logger
import api_service.configuration.containers as containers
import api_service.repositories
import api_service.resources
from api_service.app.routes import initialize_routes
from api_service.configuration.swagger import SWAGGER_CONFIG, SWAGGER_TEMPLATE
from api_service.configuration.config import DBConfig

LOGGER: Final = Logger().configured_logger


def create_application(application_containers: Any = None) -> Flask:
    app = Flask(__name__)

    if not application_containers:
        application_containers = containers.ApplicationContainers()

        application_containers.wire(
            packages=[
                api_service.resources,
                api_service.repositories,
            ]
        )

    app.config.from_object(DBConfig)
    api = Api(
        app,
        prefix=f"/api/{os.getenv('API_VERSION', 'v1')}",
        catch_all_404s=True,
    )

    app.config["SWAGGER"] = SWAGGER_CONFIG
    Swagger(app, template=SWAGGER_TEMPLATE)

    app.database = application_containers.app.database_singleton()
    app.containers = application_containers

    initialize_routes(api)

    app.logger.addHandler(Logger.configure_handler())
    app.debug = False

    return app


application = create_application()


# @application.before_request
# def before_api_request() -> None:
#     log_message = {
#         "flow": "inbound",
#         "method": request.method,
#         "url": request.url,
#         "path": request.path,
#         "body": parse_request_body(request),
#     }
#     LOGGER.info(log_message)
#
#
# @application.after_request
# def after_api_request(resp: Response) -> Response:
#     response_body = json.loads(resp.get_data()) if resp.get_data() else None
#     log_message = {
#         "flow": "outbound",
#         "method": request.method,
#         "url": request.url,
#         "path": request.path,
#         "status": resp.status_code,
#         "body": response_body,
#     }
#     LOGGER.info(log_message)
#     return resp
