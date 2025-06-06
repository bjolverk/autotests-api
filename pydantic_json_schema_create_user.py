from clients.authentication.authentication_schema import TokenSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
# Вместо CreateUserRequestDict импортируем CreateUserRequestSchema
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email
import jsonschema

public_users_client = get_public_users_client()

# Вместо CreateUserRequestDict используем CreateUserRequestSchema
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",  # Передаем аргументы в формате snake_case вместо camelCase
    first_name="string",  # Передаем аргументы в формате snake_case вместо camelCase
    middle_name="string"  # Передаем аргументы в формате snake_case вместо camelCase
)
create_user_response = public_users_client.create_user_api(create_user_request)
# print('Create user data:', create_user_response)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
# create_user_response_json = create_user_response.json()
# jsonschema.validate(instance=create_user_response.json(), schema=create_user_response_schema)

validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)

