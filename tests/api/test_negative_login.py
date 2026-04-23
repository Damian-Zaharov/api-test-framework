import pytest
from services.auth_service import AuthService
from core.logger import get_logger


@pytest.fixture
def auth_service():
    return AuthService()


logger = get_logger("TestAuth")


def test_login_invalid_password(auth_service):
    """Тест на вход с неверным паролем (Negative scenario)"""
    username = "emilys"
    password = "wrong_password_123"
    response = auth_service.login_with_invalid_data(username, password)
    assert response.status_code == 400

    error_data = response.json()
    assert "message" in error_data
    assert error_data["message"] == "Invalid credentials"
    print(f"\n[SUCCESS] Сервер корректно отклонил вход: {error_data['message']}")
