import random
import string
import requests
import allure
from api.urls import URLS
from api.endpoints import Endpoints


def generate_random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


@allure.step("Регистрируем нового курьера")
def register_new_courier():
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()
    payload = {"login": login, "password": password, "firstName": first_name}

    response = requests.post(URLS.BASE_URL + Endpoints.CREATE_COURIER, json=payload)
    courier_id = login_and_get_id(login, password)

    return {
        "login": login,
        "password": password,
        "firstName": first_name,
        "id": courier_id,
        "response": response
    }


@allure.step("Авторизуем курьера и получаем id")
def login_and_get_id(login, password):
    payload = {"login": login, "password": password}
    response = requests.post(URLS.BASE_URL + Endpoints.LOGIN_COURIER, json=payload)
    return response.json().get("id")


@allure.step("Удаляем курьера с id {courier_id}")
def delete_courier(courier_id):
    url = URLS.BASE_URL + Endpoints.DELETE_COURIER.replace(":id", str(courier_id))
    return requests.delete(url, json={"id": courier_id})


@allure.step("Создаем курьера с переданными данными")
def register_courier_with_payload(payload):
    return requests.post(URLS.BASE_URL + Endpoints.CREATE_COURIER, json=payload)


def generate_courier_payload(exclude_field=None):
    payload = {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }
    payload.pop(exclude_field, None)
    return payload

@allure.step("Создаем заказ")
def create_order(first_name, last_name, address, metro_station, phone,
                 rent_time, delivery_date, comment="", color=None):
    payload = {
        "firstName": first_name,
        "lastName": last_name,
        "address": address,
        "metroStation": metro_station,
        "phone": phone,
        "rentTime": rent_time,
        "deliveryDate": delivery_date,
        "comment": comment,
        "color": color or []
    }
    with allure.step(f"Отправляем POST запрос на создание заказа: {payload}"):
        response = requests.post(URLS.BASE_URL + Endpoints.CREATE_ORDER, json=payload)
    return response

@allure.step("Получаем список всех заказов")
def get_orders():
    url = URLS.BASE_URL + Endpoints.GET_ORDERS
    return requests.get(url)

@allure.step("Принять заказ")
def accept_order(order_id, courier_id):
    params = {"courierId": courier_id} if courier_id is not None else {}
    url = f"{URLS.BASE_URL}{Endpoints.ACCEPT_ORDER}{order_id or ''}"
    return requests.put(url, params=params)

@allure.step("Получить заказ по трекинговому номеру")
def get_order_by_track(track_number):
    return requests.get(URLS.BASE_URL + Endpoints.TRACK_ORDER, params={"t": track_number})