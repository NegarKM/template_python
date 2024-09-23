from dependency_injector.wiring import Provide, inject
from api_service.configuration.config import AppConfig


class BuildVersionService:
    @inject
    def __init__(self):
        pass

    def get_build_version(self) -> str:
        """
        returns current build version.

        Returns:
        - String representation of current build version
        """
        version = AppConfig.BUILD_VERSION

        return version
