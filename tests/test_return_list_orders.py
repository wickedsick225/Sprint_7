import allure
from api.helpers import get_orders


@allure.feature("Заказ")
class TestReturnListOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders_returns_list(self):
        response = get_orders()
        assert response.status_code == 200
        data = response.json()
        assert "availableStations" in data
        assert isinstance(data["availableStations"], list)
