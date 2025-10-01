import allure
from api.helpers import login_and_get_id, accept_order


@allure.feature("Заказ")
class TestAcceptOrder:

    @allure.title("Успешное принятие заказа")
    def test_accept_order_success(self, courier, order):
        courier_id = login_and_get_id(courier["login"], courier["password"])
        response = accept_order(order, courier_id)
        assert response.status_code == 200
        assert response.json().get("ok") is True

    @allure.title("Принятие заказа без courier_id")
    def test_accept_order_missing_courier_id(self, order):
        response = accept_order(order, None)
        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Принятие заказа с неверным courier_id")
    def test_accept_order_invalid_courier_id(self, order):
        response = accept_order(order, 999999)
        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Принятие заказа без order_id")
    def test_accept_order_missing_order_id(self, courier):
        courier_id = login_and_get_id(courier["login"], courier["password"])
        response = accept_order(None, courier_id)
        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Принятие заказа с неверным order_id")
    def test_accept_order_invalid_order_id(self, courier):
        courier_id = login_and_get_id(courier["login"], courier["password"])
        response = accept_order(999999, courier_id)
        assert response.status_code == 404
        assert "message" in response.json()
