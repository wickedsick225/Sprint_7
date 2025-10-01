import allure
import pytest
from api.helpers import login_and_get_id


@allure.feature("Курьер")
class TestLoginCourier:

    @allure.title("Успешный логин курьера")
    def test_successful_login(self, courier):
        courier_id = login_and_get_id(courier["login"], courier["password"])
        assert isinstance(courier_id, int)

    @allure.title("Логин курьера — отсутствуют обязательные поля")
    @pytest.mark.parametrize("login, password", [
        (None, "test"),
        ("test", None),
    ])
    def test_login_missing_fields(self, login, password):
        courier_id = login_and_get_id(login, password)
        assert courier_id is None

    @allure.title("Логин курьера с неверным паролем")
    def test_login_incorrect_password(self, courier):
        courier_id = login_and_get_id(courier["login"], "wrongpassword")
        assert courier_id is None

    @allure.title("Логин несуществующего пользователя")
    def test_login_nonexistent_user(self):
        courier_id = login_and_get_id("notexistlogin", "notexistpass")
        assert courier_id is None
