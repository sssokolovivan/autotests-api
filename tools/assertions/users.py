from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


def assert_user(actual: UserSchema, expected: UserSchema):
    assert_equal(expected.id, actual.id, "id")
    assert_equal(expected.email, actual.email, "email")
    assert_equal(expected.last_name, actual.last_name, "last_name")
    assert_equal(expected.first_name, actual.first_name, "first_name")
    assert_equal(expected.middle_name, actual.middle_name, "middle_name")


def assert_get_user_response(actual: GetUserResponseSchema, expected: CreateUserResponseSchema):
    assert_user(actual.user, expected.user)