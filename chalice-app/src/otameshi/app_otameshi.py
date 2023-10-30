import requests
from chalice import Blueprint

app_otameshi = Blueprint(__name__)

URL_PREFIX = "/otameshi"


@app_otameshi.route("/")
def index():
    return {"hello": "world"}


@app_otameshi.route("/jsonplaceholder/posts")
def get_placeholder_posts():
    """Get a post from an External API (JsonPlaceholder)
    see: https://jsonplaceholder.typicode.com/
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.ok:
        return response.json()
    else:
        return None


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# See the README documentation for more examples.
#


@app_otameshi.route("/hello/{name}")
def hello_name(name):
    # '/hello/james' -> {"hello": "james"}
    return {"hello": name}


@app_otameshi.route("/users", methods=["POST"])
def create_user():
    # This is the JSON body the user sent in their POST request.
    user_as_json = app_otameshi.current_request.json_body
    # We'll echo the json body back to the user in a 'user' key.
    return {"user": user_as_json}
