from os import getenv
from discord.ext.commands import Bot
from App.Models import Base
from App.Common.config import get_setting

Base.metadata.create_all()

app = Bot(command_prefix=get_setting("command_prefix", "!"))
TOKEN: str = getenv("TOKEN", "")
