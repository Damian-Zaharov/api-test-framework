import pytest


def test_get_current_user_details(auth_service):
    """
    Тест проверяет получение данных текущего авторизованного пользователя.
    Сценарий:
    1. Авторизуемся и получаем токен.
    2. Отправляем GET запрос на /auth/me с токеном в заголовке.
    3. Проверяем, что данные в ответе соответствуют схеме и пользователю.
    """

    # 1. Получаем токен через сервис (метод, который мы обсуждали ранее)
    token = auth_service.get_auth_token()

    # 2. Используем сервис для получения инфо о себе
    # (Метод get_current_user_info нужно добавить в AuthService, как в примере выше)
    user_info = auth_service.get_current_user_info(token)

    # 3. Проверки
    assert user_info.id is not None
    assert user_info.username == "emilys"

    print(f"\n[УСПЕХ] Данные профиля получены для: {user_info.firstName} {user_info.lastName}")
