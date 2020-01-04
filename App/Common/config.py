from App.Common.storage import Session
from sqlalchemy import Column, String
from App.Common.storage import Base


class Settings(Base):
    __tablename__ = "settings"
    name = Column(String(64), unique=True, primary_key=True)
    value = Column(String(256))


Base.metadata.create_all()


def _get_setting(name: str):
    name = name.lower()
    ses = Session()
    query = ses.query(Settings).filter(Settings.name == name)
    if query.count() == 1:
        return query.one().value
    else:
        return None


def _set_setting(name: str, value: str = None):
    name = name.lower()
    ses = Session()
    query = ses.query(Settings).filter(Settings.name == name)
    if query.count() == 0:
        ses.add(Settings(name=name, value=value))
        ses.commit()
        return value
    else:
        return None


def _del_setting(name: str):
    name = name.lower()
    ses = Session()
    return ses.query(Settings).filter(Settings.name == name).delete(synchronize_session='fetch')


def get_setting(name: str, default: str = None):
    get = _get_setting(name)
    if get is None:
        _del_setting(name)
        _set_setting(name, default)
        return default
    else:
        return get


def set_setting(name: str, value: str = None):
    return _set_setting(name, value)


def update_setting(name: str, value: str = None):
    name = name.lower()
    ses = Session()
    query = ses.query(Settings).filter(Settings.name == name)
    if query.count() == 1:
        query.one().value = value
        ses.commit()
        return value
    else:
        return None
