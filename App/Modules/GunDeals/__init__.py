from discord.ext import commands
from App import app


class GunDeals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Loaded Gundeals Module")
        super().__init__()

    @commands.command()
    def test(self, ctx):
        print(ctx)


app.add_cog(GunDeals(app))
