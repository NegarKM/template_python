import dependency_injector.containers as containers
import dependency_injector.providers as providers


class CoreContainers(containers.DeclarativeContainer):
    import api_service.settings.database_manager as database_manager

    database_singleton = providers.Singleton(database_manager.DatabaseManager, echo=False, pool_recycle=1800)


class RepositoryContainers(containers.DynamicContainer):
    import api_service.repositories.repository.user_repository as user_repository

    user_repository = providers.Factory(user_repository.UserTableRepository)


class ServiceContainers(containers.DeclarativeContainer):
    import api_service.resources.build_version.services as build_version_service
    import api_service.resources.user.services as user_service

    build_version_service = providers.Factory(build_version_service.BuildVersionService)
    user_service = providers.Factory(user_service.UserService)


class ApplicationContainers(containers.DeclarativeContainer):
    app = providers.Container(CoreContainers)
    repositories = providers.Container(RepositoryContainers)
    services = providers.Container(ServiceContainers)
