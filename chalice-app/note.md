## Poetry

### Add library

common: `poetry add chalice`

dev only: `poetry add --group dev pytest`

vscode ユーザの DevContainer 内では sudo じゃないと `/usr/local/bin/python` にインストールできない. 以下実行後に `poetry add` すればおｋ.

`sudo poetry config virtualenvs.create false`

### Export dependences

common: `poetry export -o requirements.txt`

dev only: `poetry export --with dev -o requirements-dev.txt`
