from clients.auth_client import AuthClient
from config.config import config
from schemas.user_schema import UserLoginResponse, UserMeResponse


class AuthService:
    def __init__(self):
        self.client = AuthClient()

    def login_with_default_user(self):
        """Бизнес-логика: авторизация с данными из config.py"""
        response = self.client.login(
            username=config.USER_NAME,
            password=config.USER_PASSWORD
        )
        response.raise_for_status()  # Убедимся, что запрос прошел успешно

        # Валидируем JSON через Pydantic
        return UserLoginResponse(**response.json())

    def get_auth_token(self):
        """Метод для получения токена"""
        user = self.login_with_default_user()
        return user.accessToken

    def get_current_user_info(self, token: str) -> UserMeResponse:
        """Метод для получения данных пользователя"""
        response = self.client.get_me(token)
        response.raise_for_status()
        return UserMeResponse(**response.json())

    def login_with_invalid_data(self, username, password):
        """Метод для попытки входа с неверными данными"""
        return self.client.login(username=username, password=password)

