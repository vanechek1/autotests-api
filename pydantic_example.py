from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    # address: Address
    is_active: bool = Field(alias="isActive", default=False)

user_data = {
    'id': 1,
    'name': 'Alice',
    'email': 'alice@example.com',
    'isActive': True
}
user = User(**user_data
            )
# user = User(
#     id="123",
#     name="Alice",
#     email="alice@example.com",
#     address=Address(city="Moscow", zip_code="11111"),
#     is_active=False
# )
print(user.model_dump())  # из объекта модели получить словарь
print(user.model_dump_json(), type(user.model_dump_json()))  # получить json-строку
