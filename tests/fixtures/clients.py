import pytest

from api_service.app import application


@pytest.fixture
def client():
    with application.test_client() as client:
        yield client
