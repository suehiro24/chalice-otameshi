from chalice import Chalice

from src.otameshi.app_otameshi import URL_PREFIX as OTAMESHI_URL_PREFIX
from src.otameshi.app_otameshi import app_otameshi
from src.todo.app_todo import URL_PREFIX as TODO_URL_PREFIX
from src.todo.app_todo import app_todo

app = Chalice(app_name="chalice-app")

app.register_blueprint(app_otameshi, url_prefix=OTAMESHI_URL_PREFIX)
app.register_blueprint(app_todo, url_prefix=TODO_URL_PREFIX)
