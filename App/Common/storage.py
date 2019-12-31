from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from App.Common.config import DB_URI

Engine = create_engine(DB_URI)
Base = declarative_base(bind=Engine)


def Session(engine=Engine):
    return scoped_session(sessionmaker(bind=engine))()
