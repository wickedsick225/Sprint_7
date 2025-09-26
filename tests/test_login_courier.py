import pytest
import allure
from api.helpers import login_and_get_id, generate_courier_payload, register_courier_with_payload

@allure.feature("Курьер")
@allure.story("Логин курьера")
def test_successful_login(courier):
    courier_id = login_and_get_id(courier["login"], courier["password"])
    assert isinstance(courier_id, int)

@allure.feature("Курьер")
@allure.story("Логин курьера")
@pytest.mark.parametrize("payload", [
    {"password": "test"},
    {"login": "test"}
])
def test_login_missing_fields(payload):
    response = register_courier_with_payload(payload)
    assert response.status_code == 400

@allure.feature("Курьер")
@allure.story("Логин курьера")
def test_login_incorrect_password(courier):
    courier_id = login_and_get_id(courier["login"], "wrongpassword")
    assert courier_id is None

@allure.feature("Курьер")
@allure.story("Логин курьера")
def test_login_nonexistent_user():
    courier_id = login_and_get_id("notexistlogin", "notexistpass")
    assert courier_id is None
