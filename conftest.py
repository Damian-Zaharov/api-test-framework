import pytest
from clients.auth_client import AuthClient
from services.auth_service import AuthService
from services.products_service import ProductsService


@pytest.fixture
def auth_client():
    return AuthClient()


@pytest.fixture
def auth_service():
    return AuthService()


@pytest.fixture
def products_service():
    return ProductsService()
