from os import getenv as _getenv
from os import getcwd as _getcwd
from os.path import normpath as _normpath

TOKEN: str = _getenv("TOKEN", "")
DB_URI: str = _getenv("DB_URI", "sqlite:///" + (_normpath(_getcwd() + "/app.db")))

PREFIX: str = _getenv("PREFIX", "!")
