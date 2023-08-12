from fastapi.testclient import TestClient
from cafe.api import api # noqa
import pytest


@pytest.fixture(scope="function", name="api")
def _api():
    return api


@pytest.fixture(scope="function")
def api_client(api):
    return TestClient(api)
