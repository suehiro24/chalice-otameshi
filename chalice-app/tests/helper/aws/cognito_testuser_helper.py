import os

import boto3

# AWS Config
SSO_PROFILE_NAME = "chalice-otameshi"
USER_POOL_ID = os.environ.get("COGNITO_USER_POOL_ID", "")
USER_POOL_CLIENT_ID = os.environ.get("COGNITO_USER_POOL_TEST_CLIENT_ID", "")
# Test user attributes
TEST_USER_NAME = os.environ.get("TEST_USER_NAME", "")
TEST_USER_EMAIL = os.environ.get("TEST_USER_EMAIL", "")
TEST_USER_TEMP_PASSWORD = os.environ.get("TEST_USER_TEMP_PASSWORD", "")
TEST_USER_PASSWORD = os.environ.get("TEST_USER_PASSWORD", "")

boto3.setup_default_session(profile_name=SSO_PROFILE_NAME)

client = boto3.client(service_name="cognito-idp", region_name="ap-northeast-1")


def create_or_get_testuser():
    """Create or get that the test user in the Cognito user pool.

    Returns:
        dict: A dictionary containing the user attributes of the created or updated user.
    Raises:
        Exception: If any exception occurs while creating the test user.
    """
    try:
        # Fetch existing user
        res_get_user = client.admin_get_user(
            UserPoolId=USER_POOL_ID,
            Username=TEST_USER_NAME,
        )
        # Ensure existing user is fulfilled requirements then return.
        if _check_testuser_has_required_attrs(res_get_user):
            return res_get_user
        else:
            raise Exception("The existing test user does not have the required attributes.")
    except client.exceptions.UserNotFoundException:
        # Create test user if not exist
        return _create_testuser()
    except Exception as e:
        raise e


def delete_testuser(userName):
    try:
        client.admin_delete_user(UserPoolId=USER_POOL_ID, Username=userName)
    except client.exceptions.UserNotFoundException:
        pass
    except Exception as e:
        raise e


def get_testuser_id_token() -> str:
    response = client.admin_initiate_auth(
        UserPoolId=USER_POOL_ID,
        ClientId=USER_POOL_CLIENT_ID,
        AuthFlow="ADMIN_NO_SRP_AUTH",
        AuthParameters={
            "USERNAME": TEST_USER_NAME,
            "PASSWORD": TEST_USER_PASSWORD,
        },
    )
    return response["AuthenticationResult"]["IdToken"]


def _create_testuser():
    res = client.admin_create_user(
        UserPoolId=USER_POOL_ID,
        Username=TEST_USER_NAME,
        UserAttributes=[
            {"Name": "name", "Value": TEST_USER_NAME},
            {"Name": "email", "Value": TEST_USER_EMAIL},
            {"Name": "email_verified", "Value": "True"},
            {"Name": "preferred_username", "Value": TEST_USER_NAME},
        ],
        TemporaryPassword=TEST_USER_TEMP_PASSWORD,
        # ForceAliasCreation=True | False,
        # MessageAction="RESEND" | "SUPPRESS"
        DesiredDeliveryMediums=[
            "EMAIL",  # | "SMS"
        ],
        # ClientMetadata={"string": "string"},
    )
    client.admin_set_user_password(
        UserPoolId=USER_POOL_ID,
        Username=TEST_USER_NAME,
        Password=TEST_USER_PASSWORD,
        Permanent=True,
    )
    return res["User"]


def _check_testuser_has_required_attrs(user):
    """Check if the test user has the required attributes.

    Args:
        user (dict): A dictionary containing the user attributes of the test user.

    Returns:
        bool: True if the test user has the required attributes, False otherwise.
    """
    if user["Username"] != TEST_USER_NAME:
        return False

    for attr in user["UserAttributes"]:
        if attr["Name"] == "email":
            if attr["Value"] != TEST_USER_EMAIL:
                return False
        if attr["Name"] == "email_verified":
            if attr["Value"] != "True":
                return False

    return True
