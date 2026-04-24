import pytest
from clients.auth_client import AuthClient
from services.auth_service import AuthService
from services.products_service import ProductsService

# 1. Сервисы и клиенты (session scope — создаем 1 раз)
@pytest.fixture(scope="session")
def auth_client():
    return AuthClient()

@pytest.fixture(scope="session")
def auth_service():
    return AuthService()

@pytest.fixture(scope="session")
def products_service():
    return ProductsService()

# 2. Токен (зависит от auth_service, поэтому тоже session scope)
@pytest.fixture(scope="session")
def auth_token(auth_service):
    # Логинимся один раз на всю сессию
    token = auth_service.get_auth_token()
    return token
