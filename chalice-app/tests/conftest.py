import pytest

from tests.helper.aws.cognito_testuser_helper import get_testuser_id_token


@pytest.fixture(scope="session")
def testuser_id_token():
    return get_testuser_id_token()
