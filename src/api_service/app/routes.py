from flask_restful import Api, Resource

from api_service.resources.build_version import BuildVersion
from api_service.resources.root import Root
from api_service.resources.user import User


def initialize_route(
    api: Api,
    resource: Resource,
    endpoint: str,
    url: str,
    resource_kwargs: dict,
) -> None:
    api.add_resource(
        resource,
        url,
        resource_class_kwargs=resource_kwargs,
        endpoint=endpoint,
    )


def initialize_routes(api: Api) -> None:
    initialize_route(
        api=api,
        resource=BuildVersion,
        endpoint="version",
        url="/version",
        resource_kwargs={},
    )

    initialize_route(api=api, resource=Root, endpoint="root", url="/", resource_kwargs={})

    initialize_route(
        api=api,
        resource=User,
        endpoint="users",
        url="/users",
        resource_kwargs={},
    )
