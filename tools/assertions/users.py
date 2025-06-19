from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, name='email')
    assert_equal(response.user.last_name, request.last_name, name='last_name')
    assert_equal(response.user.first_name, request.first_name, name='first_name')
    assert_equal(response.user.middle_name, request.middle_name, name='middle_name')


def assert_user(actual: UserSchema, expected: UserSchema):
    assert_equal(actual.id, expected.id, name='id')
    assert_equal(actual.email, expected.email, name='email')
    assert_equal(actual.last_name, expected.last_name, name='last_name')
    assert_equal(actual.first_name, expected.first_name, name='first_name')
    assert_equal(actual.middle_name, expected.middle_name, name='middle_name')


def assert_get_user_response(get_user_response: UserSchema, create_user_response: UserSchema):
    assert_user(get_user_response, create_user_response)
