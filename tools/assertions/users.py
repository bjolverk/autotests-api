from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
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
    """
    Проверяет соответствие данных двух объектов UserSchema.

    :param actual: Фактические данные пользователя для проверки.
    :param expected: Ожидаемые данные пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, name='id')
    assert_equal(actual.email, expected.email, name='email')
    assert_equal(actual.last_name, expected.last_name, name='last_name')
    assert_equal(actual.first_name, expected.first_name, name='first_name')
    assert_equal(actual.middle_name, expected.middle_name, name='middle_name')


def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    """
    Проверяет, что данные пользователя при GET- запросе совпадают с данными при создании этого пользователя.

    :param get_user_response: Данные пользователя, полученные при запросе.
    :param create_user_response: Данные пользователя, заданные при создании.
    :raises AssertionError: Если данные пользователя не совпадают.
    """
    assert_user(get_user_response, create_user_response)
