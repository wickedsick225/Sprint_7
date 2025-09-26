import pytest
from api.helpers import register_new_courier, delete_courier, create_order


@pytest.fixture
def courier():
    courier_data = register_new_courier()
    yield courier_data
    delete_courier(courier_data["id"])

@pytest.fixture
def order():
    response = create_order(
        first_name="Test",
        last_name="User",
        address="Test street 1",
        metro_station="1",
        phone="+70000000000",
        rent_time=1,
        delivery_date="2025-10-01"
    )
    return response.json()["track"]