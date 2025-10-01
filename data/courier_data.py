from faker import Faker

fake = Faker()

valid_courier_payload = {
    "login": "test_login",
    "password": "test_password",
    "firstName": "Test"
}

missing_fields_payloads = [
    ({"password": "123"}, 400),                        
    ({"login": "test"}, 400),                          
    ({"login": fake.user_name(), "password": "123"}, 201)
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
