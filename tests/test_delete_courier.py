import allure
import pytest
import requests
from api.helpers import register_new_courier, delete_courier
from api.urls import URLS
from api.endpoints import Endpoints



@allure.feature("Курьер")
@allure.story("Удаление курьера — успешный запрос")
def test_delete_courier_success():
    courier = register_new_courier()
    response = delete_courier(courier["id"])
    assert response.status_code == 200
    assert response.json() == {"ok": True}


@allure.feature("Курьер")
@allure.story("Удаление курьера — без id")
def test_delete_courier_without_id():
    url = URLS.BASE_URL + Endpoints.DELETE_COURIER.replace(":id", "")
    response = requests.delete(url, json={})
    assert response.status_code in [400, 404]  # зависит от API
    assert "message" in response.json()


@allure.feature("Курьер")
@allure.story("Удаление курьера — с несуществующим id")
def test_delete_courier_nonexistent_id():
    url = URLS.BASE_URL + Endpoints.DELETE_COURIER.replace(":id", "9999999")
    response = requests.delete(url, json={"id": 9999999})
    assert response.status_code in [400, 404]
    assert "message" in response.json()
