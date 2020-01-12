from discord.ext import commands
from sqlalchemy import Column, String, Integer


class Settings(commands.Cog, name="Settings"):
    deps = ['Storage']

    def __init__(self, bot):
        self.bot = bot
        self.storage = bot.get_cog('Storage')
        self.model = self.__gen_model__()
        self.storage.model_base.metadata.create_all()

    def __gen_model__(self):
        class SettingsModel(self.storage.model_base):
            __tablename__ = "settings"
            id = Column(Integer, primary_key=True, autoincrement=True)
            module = Column(String(64))
            setting = Column(String(64))
            value = Column(String(4096))

        return SettingsModel

    def get(self, module: str, setting: str = None):
        ses = self.storage.gen_session()
        value = ses.query(self.model).filter(self.model.module == module)
        value = value.filter(self.model.setting == setting) if setting is not None else value
        value = value.all() if value.count() > 0 else None
        return value

    def set(self, module: str, setting: str, value: str):
        value = str(value)
        ses = self.storage.gen_session()
        check = ses.query(self.model).filter(self.model.module == module).filter(self.model.setting == setting)
        if check.count() == 0:
            ses.add(self.model(module=module, setting=setting, value=value))
            ses.commit()
            return True
        if check.count() == 1:
            check.one().value = value
            ses.commit()
            return True
        else:
            return False

    def rem(self, module, setting):
        ses = self.storage.gen_session()
        check = ses.query(self.model).filter(self.model.module == module).filter(self.model.setting == setting)
        records = check.delete(synchronize_session='fetch')
        ses.commit()
        return records
