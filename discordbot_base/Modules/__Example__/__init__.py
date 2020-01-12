# This is just a general example on how to structure a bot module.
from discord.ext import commands


class Example(commands.Cog, name="Example"):
    deps = ['A List of all the modules needed for this one to run. This can be missing for no deps.']

    def __init__(self, bot):
        self.bot = bot  # Link bot here if needed, not required
