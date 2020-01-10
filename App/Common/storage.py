from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from discord.ext.commands import Cog


class Storage(Cog):
    def __init__(self, db_uri: str):
        self.engine = create_engine(db_uri)
        self.model_base = declarative_base(bind=self.engine)

    def gen_session(self):
        return scoped_session(sessionmaker(bind=self.engine))()
