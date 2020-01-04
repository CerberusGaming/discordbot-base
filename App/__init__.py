from os import getenv
from discord.ext.commands import Bot
from App.Common.config import get_setting

TOKEN: str = getenv("TOKEN", "")

app = Bot(command_prefix=get_setting("command_prefix", "!"))
