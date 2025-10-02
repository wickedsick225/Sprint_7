from faker import Faker

fake = Faker("ru_RU")

valid_courier_payload = {
    "login": "test_login",
    "password": "test_password",
    "firstName": "Test"
}

invalid_data_login_without_login = {
    "login": "",
    "firstName": fake.first_name(),
    "password": fake.password()
}

invalid_data_login_without_password = {
    "login": fake.user_name(),
    "firstName": fake.first_name(),
    "password": ""
}

missing_fields_payloads = [
    ({"password": "123"}, 400),   
    ({"login": "test"}, 400), 
]


def generate_courier(login_only=False, password_only=False):
    if login_only:
        return {"login": fake.user_name()}
    if password_only:
        return {"password": "123"}
    return {
        "login": fake.user_name(),
        "password": "123",
        "firstName": fake.first_name()
    }
