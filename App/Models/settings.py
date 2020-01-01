from sqlalchemy import Column, String, Integer
from App.Common.storage import Base


class Settings(Base):
    __tablename__ = "settings"
    name = Column(String(64), unique=True, primary_key=True)
    value = Column(String(256))
