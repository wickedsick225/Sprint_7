import allure
import pytest
from api.helpers import create_order
from data.order_data import color_options, valid_order_payload


@allure.feature("Заказ")
class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цвета")
    @pytest.mark.parametrize("color_option, expected_status", color_options)
    def test_create_order_colors(self, color_option, expected_status):
        payload = {**valid_order_payload, "color": color_option}
        response = create_order(**payload)
        assert response.status_code == expected_status
        assert "track" in response.json()
