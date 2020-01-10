import os
import importlib
from glob import glob
from discord.ext.commands.bot import Bot
from discord.ext.commands import CogMeta, Cog

from .storage import Storage
from .config import DB_URI, BOT_TOKEN, BOT_PREFIX


class DiscordBot(Bot):
    def __init__(self, command_prefix: str = BOT_PREFIX, db_uri: str = DB_URI, **options):
        super().__init__(command_prefix=command_prefix, **options)
        self.add_cog(Storage(db_uri))

    def load_modules(self):
        paths = ['App/Modules', 'Modules']
        modules = []
        for path in paths:
            modules.extend([os.path.normpath(x) for x in glob("{}/*/__init__.py".format(path))])
        for module in modules:
            module = module.replace("\\", "/").replace("//", "/").replace("/__init__.py", '').split('/')
            package = ".".join(module[0:-1])
            module = str(module[-1])
            if not module.startswith("_"):
                impt = importlib.import_module(".{}".format(module), package=package)
                for item in [x for x in dir(impt) if not x.startswith("_")]:
                    cog = getattr(impt, item)
                    if isinstance(cog, Cog) or isinstance(cog, CogMeta):
                        self.add_cog(cog(self))

    def run(self, *args, **kwargs):
        self.load_modules()
        print(self.cogs)
        self.get_cog("Storage").model_base.metadata.create_all()
        super().run(BOT_TOKEN, *args, **kwargs)
