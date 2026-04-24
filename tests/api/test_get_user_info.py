def test_get_current_user_details(auth_service, auth_token):  # Добавили auth_token в аргументы

    user_info = auth_service.get_current_user_info(auth_token)

    assert user_info.username == "emilys"
