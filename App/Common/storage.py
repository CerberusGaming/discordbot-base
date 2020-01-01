from os import getenv, getcwd
from os.path import normpath
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

Engine = create_engine(getenv("DB_URI", "sqlite:///" + (normpath(getcwd() + "/app.db"))))
Base = declarative_base(bind=Engine)


def Session(engine=Engine):
    return scoped_session(sessionmaker(bind=engine))()
