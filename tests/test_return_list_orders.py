import pytest
import allure
from api.helpers import get_orders


@allure.feature("Заказ")
@allure.story("Получение списка заказов")
def test_get_orders_returns_list():
    response = get_orders()
    assert response.status_code == 200
    orders = response.json()["availableStations"]
    assert isinstance(orders, list)
