import os

from chalice import Blueprint, CognitoUserPoolAuthorizer

app_todo = Blueprint(__name__)

URL_PREFIX = "/todo"
USER_POOL_ARN = os.environ.get("COGNITO_USER_POOL_ARN") or ""

authorizer = CognitoUserPoolAuthorizer(
    name="chalice-otameshi-todo-authorizer",
    provider_arns=[USER_POOL_ARN],
)


@app_todo.route("/", methods=["GET"], authorizer=authorizer)
def index():
    return {"success": True}


# @app_todo.route("/todos", methods=["POST"])
# def add_new_todo():
#     body = app_todo.current_request.json_body
#     return get_app_db().add_item(
#         description=body["description"],
#         metadata=body.get("metadata"),
#     )
