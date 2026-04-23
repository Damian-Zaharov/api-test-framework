import pytest
from services.auth_service import AuthService
from core.logger import get_logger


@pytest.fixture
def auth_service():
    return AuthService()

logger = get_logger("TestAuth")

def test_login_and_check_token(auth_service):
    # Теперь user — это объект, а не словарь!
    user = auth_service.login_with_default_user()
    logger.info(f"RECEIVED TOKEN: {user.accessToken}")
    # Теперь работает автодополнение через точку:
    assert user.id == 1
    assert user.username == "emilys"
    assert "@" in user.email
    assert user.accessToken is not None

    # Если сервер пришлет вместо id строку или битый URL,
    # тест упадет еще на этапе валидации в сервисе с понятной ошибкой.

