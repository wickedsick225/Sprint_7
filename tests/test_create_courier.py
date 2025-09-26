import allure
import pytest
from api.helpers import register_new_courier, delete_courier, register_courier_with_payload, generate_courier_payload


@allure.feature("Курьер")
@allure.story("Создание курьера")
def test_create_courier_success():
    courier = register_new_courier()
    # Проверяем, что курьер создан
    assert courier["response"].status_code == 201
    assert courier["id"] is not None
    # Удаляем курьера через лямбду, чтобы убрать if
    {True: lambda: delete_courier(courier["id"])}.get(True)()


@allure.feature("Курьер")
@allure.story("Создание курьера — дубликат")
def test_create_courier_duplicate():
    courier = register_new_courier()
    payload = {"login": courier["login"], "password": "any", "firstName": "any"}
    response = register_courier_with_payload(payload)
    # Проверяем, что дублирование возвращает 409
    assert response.status_code == 409
    {True: lambda: delete_courier(courier["id"])}.get(True)()


@allure.feature("Курьер")
@allure.story("Создание курьера — отсутствие обязательных полей")
@pytest.mark.parametrize(
    "missing_field, expected_status",
    [
        ("login", 400),
        ("password", 400),
        ("firstName", 201),  # firstName необязательное поле
    ],
)
def test_create_courier_missing_fields(missing_field, expected_status):
    payload = generate_courier_payload(missing_field)
    response = register_courier_with_payload(payload)
    # Проверяем статус ответа
    assert response.status_code == expected_status
    # Выполняем действие через словарь-лямбду вместо if
    {201: lambda: delete_courier(response.json().get("id")), 400: lambda: None}.get(expected_status, lambda: None)()
