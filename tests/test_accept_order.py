import pytest
import allure
from api.helpers import login_and_get_id, accept_order


@allure.feature("Заказ")
@allure.story("Принять заказ")
def test_accept_order_success(courier, order):
    courier_id = login_and_get_id(courier["login"], courier["password"])
    response = accept_order(order, courier_id)
    assert response.status_code == 200
    assert response.json()["ok"] is True


@allure.feature("Заказ")
@allure.story("Принять заказ")
def test_accept_order_missing_courier_id(order):
    response = accept_order(order, None)
    assert response.status_code == 400


@allure.feature("Заказ")
@allure.story("Принять заказ")
def test_accept_order_invalid_courier_id(order):
    response = accept_order(order, 999999)
    assert response.status_code == 404


@allure.feature("Заказ")
@allure.story("Принять заказ")
def test_accept_order_missing_order_id(courier):
    courier_id = login_and_get_id(courier["login"], courier["password"])
    response = accept_order(None, courier_id)
    assert response.status_code == 404


@allure.feature("Заказ")
@allure.story("Принять заказ")
def test_accept_order_invalid_order_id(courier):
    courier_id = login_and_get_id(courier["login"], courier["password"])
    response = accept_order(999999, courier_id)
    assert response.status_code == 404
