import os
import json
from http import HTTPStatus

from tests.fixtures.clients import client


class TestBuildVersion:
    def test_get_version(self, client) -> None:
        response = client.get(f"/api/{os.getenv('API_VERSION', 'v1')}/version")
        response_data = json.loads(response.data)

        assert response.status_code == HTTPStatus.OK
        assert "build_version" in response_data
