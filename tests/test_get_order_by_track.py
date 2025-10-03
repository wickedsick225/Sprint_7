import allure
from api.helpers import create_order, get_order_by_track
from data.order_data import valid_order_payload


@allure.feature("Заказ")
class TestGetOrderByTrack:

    @allure.title("Успешное получение заказа по трек-номеру")
    def test_get_order_by_track_success(self):
        order_response = create_order(**valid_order_payload)
        track_number = order_response.json()["track"]

        response = get_order_by_track(track_number)
        assert response.status_code == 200
        data = response.json()
        assert "order" in data
        assert data["order"]["track"] == track_number

    @allure.title("Получение заказа без номера")
    def test_get_order_by_track_missing_number(self):
        response = get_order_by_track(None)
        assert response.status_code == 400
        assert "Недостаточно данных для поиска" in response.text

    @allure.title("Получение заказа с несуществующим номером")
    def test_get_order_by_track_nonexistent_number(self):
        response = get_order_by_track(999999999)
        assert response.status_code == 404
        assert "Заказ не найден" in response.text
