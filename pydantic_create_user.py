from pydantic import BaseModel, EmailStr, Field, computed_field, ConfigDict, ValidationError
from pydantic.alias_generators import to_camel
import uuid


class UserSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    email: EmailStr
    last_mame: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def username(self) -> str:
        return f"{self.first_name} {self.last_mame}"


class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr
    password: str
    last_mame: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    user: UserSchema


create_user_request = CreateUserRequestSchema(
    email="test@example.com",
    password="string",
    lastName="Bond",
    firstName="Zara",
    middleName="Alice"
)
print('Create user request:', create_user_request)

create_user_response_json = """
{
  "user": {
    "id": "string",
    "email": "user@example.com",
    "lastName": "Bond",
    "firstName": "Zara",
    "middleName": "Alice"
  }
}
"""
user_json_model = CreateUserResponseSchema.model_validate_json(create_user_response_json)
print('User JSON model:', user_json_model)
print(user_json_model.model_dump(by_alias=True))
print(user_json_model.model_dump_json(by_alias=True))

print(user_json_model.user.username)


user_dict = {
    "user": {
        "id": "string",
        "email": "user@example.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "Alice"
    }
}
user_dict_model = CreateUserResponseSchema(**user_dict)
print("User dict model", user_dict_model)

try:
    UserSchema(
        id=123, # int
        email="test@example.com",
        lastName="Bond",
        firstName="Zara",
        middleName="Alice"
    )
except ValidationError as error:
    print(error.errors())

