from os import getenv as _getenv
from os import getcwd as _getcwd
from os.path import normpath as _normpath
from os.path import isfile as _isfile
from configparser import ConfigParser as _CP

_configfile = _CP()
_path = _normpath(_getcwd() + "/config.ini")
if _isfile(_path):
    _configfile.read(_path)
else:
    _configfile.add_section('db')
    _configfile.add_section('bot')
    _configfile.set('bot', 'prefix', '')
    _configfile.set('bot', 'token', '')
    _configfile.set('db', 'uri', '')
    with open(_path, 'w') as fp:
        _configfile.write(fp)
        fp.close()
    exit()


def _setting(section, option, env, default=""):
    value = _configfile.get(section, option, fallback="")
    if len(value) == 0:
        value = default
    return _getenv(env, value)


# SQLA DB URI
DB_URI = _setting('db', 'uri', 'DB_URI', "sqlite:///" + (_normpath(_getcwd() + "/app.db")))

# Bot Command Prefix: ! -> "!Command <option>"
BOT_PREFIX = _setting('bot', 'prefix', 'BOT_PREFIX', '!')

# Discord Bot API Token
BOT_TOKEN = _setting('bot', 'token', 'BOT_TOKEN', '')
