import os
from configparser import ConfigParser


class Config():
    @staticmethod
    def getenv(env, fallback):
        return os.getenv(env, fallback)

    def __init__(self, path: str = None):
        self._cp = ConfigParser()
        if path is None:
            path = os.path.normpath(os.getcwd() + "/config.ini")
            if os.path.isfile(path):
                self._cp.read(path)
            else:
                open(path, 'w').close()
        self.path = path

    def _write(self):
        with open(self.path, 'w') as fp:
            self._cp.write(fp)
            fp.close()

    def init_module(self, module: str, defaults: dict = None):
        if defaults is None:
            defaults = {}

        if not self._cp.has_section(module):
            self._cp.read_dict({module: defaults})
            self._write()
        elif False in [self._cp.has_option(module, x) for x in defaults.keys()]:
            for key, value in defaults.items():
                if not self._cp.has_option(module, key):
                    self._cp.set(module, key, value)
            self._write()
        else:
            return True
        return False

    def get_setting(self, section, option, env, default=""):
        value = self._cp.get(section, option, fallback="")
        if len(value) == 0:
            value = default
        return self.getenv(env, value)
