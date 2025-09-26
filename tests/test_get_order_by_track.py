import pytest
import allure
from api.helpers import create_order, get_order_by_track

@allure.feature("Заказ")
@allure.story("Получить заказ по трек-номеру")
def test_get_order_by_track_success():
    # создаём тестовый заказ
    order_response = create_order(
        first_name="Test",
        last_name="User",
        address="Test Street 1",
        metro_station="1",
        phone="+70000000000",
        rent_time=1,
        delivery_date="2025-10-01",
        comment="Test order",
        color=[]
    )
    track_number = order_response.json()["track"]

    response = get_order_by_track(track_number)
    assert response.status_code == 200
    data = response.json()
    assert "order" in data
    assert data["order"]["track"] == track_number

@allure.feature("Заказ")
@allure.story("Получить заказ по трек-номеру")
def test_get_order_by_track_missing_number():
    response = get_order_by_track(None)
    assert response.status_code == 400
    assert "Недостаточно данных для поиска" in response.text

@allure.feature("Заказ")
@allure.story("Получить заказ по трек-номеру")
def test_get_order_by_track_nonexistent_number():
    response = get_order_by_track(999999999)
    assert response.status_code == 404
    assert "Заказ не найден" in response.text
