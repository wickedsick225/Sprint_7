import allure
import pytest
from api.helpers import register_new_courier, register_courier_with_payload
import requests
from api.urls import URLS
from api.endpoints import Endpoints
from data.courier_data import missing_fields_payloads, generate_courier, invalid_data_login_without_login, invalid_data_login_without_password


@allure.feature("Курьер")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        courier = register_new_courier()
        assert courier["response"].status_code == 201
        assert courier["id"] is not None

    @allure.title("Создание дубликата курьера")
    def test_create_courier_duplicate(self):
        courier = register_new_courier()
        payload = generate_courier()
        payload["login"] = courier["login"]

        response = register_courier_with_payload(payload)
        assert response.status_code == 409
        assert "message" in response.json()


    @allure.title("Проверка ошибки при создании курьера без обязательных полей")
    @allure.description("Отправляем запрос без обязательных полей и проверяем, что возвращается 400 и сообщение об ошибке")
    @pytest.mark.parametrize("courier_data", [
        invalid_data_login_without_login,
        invalid_data_login_without_password
    ])
    def test_courier_registration_without_parameters_failed(self, courier_data):
        with allure.step("Отправляем запрос с неполными данными"):
            response = requests.post(URLS.BASE_URL + Endpoints.CREATE_COURIER, json=courier_data)

        with allure.step("Проверяем, что получаем ошибку 400 и сообщение о нехватке данных"):
            assert response.status_code == 400
            assert "Недостаточно данных для создания учетной записи" in response.text
