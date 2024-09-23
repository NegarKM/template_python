import dependency_injector.containers as containers
import dependency_injector.providers as providers


class CoreContainers(containers.DeclarativeContainer):
    pass


class RepositoryContainers(containers.DynamicContainer):
    pass


class ServiceContainers(containers.DeclarativeContainer):
    import api_service.resources.build_version.services as build_version_service

    build_version_service = providers.Factory(build_version_service.BuildVersionService)  # type: ignore


class ApplicationContainers(containers.DeclarativeContainer):
    app = providers.Container(CoreContainers)
    repositories = providers.Container(RepositoryContainers)
    services = providers.Container(ServiceContainers)
