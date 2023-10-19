from chalice import Chalice
from chalicelib.otameshi.app_otameshi import app_otameshi, url_prefix_otameshi
from chalicelib.todo.app_todo import app_todo, url_prefix_todo

app = Chalice(app_name="chalice-app")

app.register_blueprint(app_otameshi, url_prefix=url_prefix_otameshi)
app.register_blueprint(app_todo, url_prefix=url_prefix_todo)
