import os
from discord.ext.commands.bot import Bot
from .storage import Storage


class DiscordBot(Bot):
    def __init__(self,
                 command_prefix: str = os.getenv("COMMAND_PREFIX", "!"),
                 db_uri: str = os.getenv("DB_URI", "sqlite:///" + (os.path.normpath(os.getcwd() + "/app.db"))),
                 **options):
        super().__init__(command_prefix=command_prefix, **options)
        self.add_cog(Storage(db_uri))
