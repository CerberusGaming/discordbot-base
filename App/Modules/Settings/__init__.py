from discord.ext import commands
from sqlalchemy import Column, String


class Settings(commands.Cog, name="Settings"):
    def __init__(self, bot):
        self.bot = bot
        self.storage = bot.get_cog('Storage')
        self.model = self.__gen_model__()
        self.storage.model_base.metadata.create_all()

    def __gen_model__(self):
        class SettingsModel(self.storage.model_base):
            __tablename__ = "settings"
            name = Column(String(64), unique=True, primary_key=True)
            value = Column(String(256))

        return SettingsModel

    def _get_setting(self, name: str):
        name = name.lower()
        ses = self.storage.gen_session()
        query = ses.query(self.model).filter(self.model.name == name)
        if query.count() == 1:
            return query.one().value
        else:
            return None

    def _set_setting(self, name: str, value: str = None):
        name = name.lower()
        ses = self.storage.gen_session()
        query = ses.query(self.model).filter(self.model.name == name)
        if query.count() == 0:
            ses.add(self.model(name=name, value=value))
            ses.commit()
            return value
        else:
            return None

    def _del_setting(self, name: str):
        name = name.lower()
        ses = self.storage.gen_session()
        return ses.query(self.model).filter(self.model.name == name).delete(synchronize_session='fetch')

    def get_setting(self, name: str, default: str = None):
        get = self._get_setting(name)
        if get is None:
            self._del_setting(name)
            self._set_setting(name, default)
            return default
        else:
            return get

    def set_setting(self, name: str, value: str = None):
        return self._set_setting(name, value)

    def update_setting(self, name: str, value: str = None):
        name = name.lower()
        ses = self.storage.gen_session()
        query = ses.query(self.model).filter(self.model.name == name)
        if query.count() == 1:
            query.one().value = value
            ses.commit()
            return value
        else:
            return None
