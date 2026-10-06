from copy import deepcopy
from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client() -> Iterator[TestClient]:
    with TestClient(app_module.app) as test_client:
        yield test_client


@pytest.fixture
def activities(monkeypatch: pytest.MonkeyPatch) -> dict:
    test_activities = deepcopy(app_module.activities)
    monkeypatch.setattr(app_module, "activities", test_activities)
    return test_activities
