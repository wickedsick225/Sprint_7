import allure
import pytest
from api.helpers import create_order


@allure.feature("Заказ")
@allure.story("Создание заказа с разными цветами")
@pytest.mark.parametrize(
    "color_option",
    [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]
)
def test_create_order_colors(color_option):
    response = create_order(
        first_name="Test",
        last_name="User",
        address="Test Street 1",
        metro_station="1",
        phone="+70000000000",
        rent_time=1,
        delivery_date="2025-10-01",
        comment="Test order",
        color=color_option
    )
    assert response.status_code == 201
    assert "track" in response.json()
