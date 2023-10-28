from tests.helper.aws.cognito_testuser_helper import (
    TEST_USER_NAME,
    create_or_get_testuser,
    delete_testuser,
    get_testuser_id_token,
)


def test_create_testuser():
    delete_testuser(TEST_USER_NAME)
    res = create_or_get_testuser()
    print(res)
    assert res["Username"] == TEST_USER_NAME


def test_get_testuser():
    create_or_get_testuser()
    res = create_or_get_testuser()
    assert res["Username"] == TEST_USER_NAME


def test_get_id_token():
    id_token = get_testuser_id_token()
    assert isinstance(id_token, str)
