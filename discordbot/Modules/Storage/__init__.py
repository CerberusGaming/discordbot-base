import os

from discord.ext import commands
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


class Storage(commands.Cog):
    def __init__(self, bot):
        config = bot.config
        config.init_module('storage', defaults={'uri': ''})

        default = "sqlite:///{}".format(os.path.normpath(os.getcwd() + "/app.db"))
        self.engine = create_engine(config.get_setting('db', 'uri', 'DB_URI', default))
        self.model_base = declarative_base(bind=self.engine)

    def gen_session(self):
        return scoped_session(sessionmaker(bind=self.engine))()
