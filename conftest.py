import pytest

@pytest.fixture(scope="session")
def base_headers():
    return{
        "Content-Type": "application/json"
    }