def assert_status_code(response, expected_code=200):
    """Универсальная проверка статус-кода с понятным сообщением"""
    assert response.status_code == expected_code, \
        f"Ожидали {expected_code}, но получили {response.status_code}. Ответ: {response.text}"

def assert_user_data(user, expected_name):
    """Проверка основных полей пользователя"""
    assert user.username == expected_name
    assert user.id is not None
    assert "@" in user.email

def validate_status_code(response, expected_code=200):
    """Проверяет статус-код и выводит детальную ошибку при несовпадении"""
    assert response.status_code == expected_code, \
        f"Ожидали код {expected_code}, но получили {response.status_code}. Ответ сервера: {response.text}"

def validate_user_fields(user, expected_username):
    """Комплексная проверка полей пользователя (Pydantic объект)"""
    assert user.id is not None, "ID пользователя не должен быть пустым"
    assert user.username == expected_username, f"Ожидали username {expected_username}, получили {user.username}"
    assert "@" in user.email, f"Некорректный формат email: {user.email}"
