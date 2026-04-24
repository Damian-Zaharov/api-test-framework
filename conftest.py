import pytest
from clients.auth_client import AuthClient
from services.auth_service import AuthService
from services.products_service import ProductsService


@pytest.fixture(scope="session")
def auth_client():
    return AuthClient()


@pytest.fixture(scope="session")
def auth_service():
    return AuthService()


@pytest.fixture(scope="session")
def products_service():
    return ProductsService()


@pytest.fixture(scope="session")
def auth_token(auth_service):
    token = auth_service.get_auth_token()
    return token
