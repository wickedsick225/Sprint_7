import allure
import requests
from api.helpers import register_new_courier, delete_courier
from api.urls import URLS
from api.endpoints import Endpoints


@allure.feature("Курьер")
class TestDeleteCourier:

    @allure.title("Успешное удаление курьера")
    def test_delete_courier_success(self):
        courier = register_new_courier()
        response = delete_courier(courier["id"])
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Удаление курьера без id")
    def test_delete_courier_without_id(self):
        url = URLS.BASE_URL + Endpoints.DELETE_COURIER.format(id="")
        response = requests.delete(url, json={})
        assert response.status_code in [400, 404, 500]
        assert "message" in response.json()

    @allure.title("Удаление курьера с несуществующим id")
    def test_delete_courier_nonexistent_id(self):
        url = URLS.BASE_URL + Endpoints.DELETE_COURIER.format(id="9999999")
        response = requests.delete(url, json={"id": 9999999})
        assert response.status_code in [400, 404, 500]
        assert "message" in response.json()
