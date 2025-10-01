import allure
import pytest
from api.helpers import register_new_courier, register_courier_with_payload
from data.courier_data import missing_fields_payloads, generate_courier


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

    @allure.title("Создание курьера — отсутствие обязательных полей")
    @pytest.mark.parametrize("payload, expected_status", missing_fields_payloads)
    def test_create_courier_missing_fields(self, payload, expected_status):
        response = register_courier_with_payload(payload)
        assert response.status_code == expected_status
        if expected_status == 201:
            assert "id" in response.json()
        else:
            assert "message" in response.json()
