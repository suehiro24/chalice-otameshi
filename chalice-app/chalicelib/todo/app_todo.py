from chalice import Blueprint, CognitoUserPoolAuthorizer

app_todo = Blueprint(__name__)

URL_PREFIX = "/todo"
