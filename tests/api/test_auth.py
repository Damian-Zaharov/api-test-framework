from utils.validators import validate_user_fields


def test_login_success(auth_service):
    # Действие
    user = auth_service.login_with_default_user()

    # Проверка через валидатор
    validate_user_fields(user, "emilys")


def test_login_invalid_password(auth_service):
    # Для негативного теста валидатор статус-кода особенно удобен
    from utils.validators import validate_status_code

    response = auth_service.login_with_invalid_data("emilys", "wrong_pass")

    validate_status_code(response, 400)
    assert response.json()["message"] == "Invalid credentials"
