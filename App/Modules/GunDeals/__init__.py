from discord.ext import commands
import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from .reddit import Reddit


class GunDeals(commands.Cog):
    deps = ['Storage', 'Settings']

    def __init__(self, bot):
        self.bot = bot
        self.name = "gundeals"
        self.storage = bot.get_cog('Storage')
        self.settings = bot.get_cog('Settings')
        self.feeds = self.__gen_feed_model__()
        self.storage.model_base.metadata.create_all()

    def __gen_feed_model__(self):
        class Model(self.storage.model_base):
            __tablename__ = "feed_entries"
            id = Column(Integer, primary_key=True, autoincrement=True)
            subreddit = Column(String(24))
            post_id = Column(String(24), unique=True)
            title = Column(String(2048))
            author = Column(String(2048))
            post = Column(String(2048))
            posted_on = Column(DateTime, default=datetime.datetime.utcnow())
            text = Column(String(4096))
            link = Column(String(2048))
            flair = Column(String(2048))
            thumb = Column(String(2048))
            sticky = Column(Boolean, default=False)
            nsfw = Column(Boolean, default=False)
            posted = Column(Boolean, default=False)

        return Model

    # def store_entries(self):
    #     ses = self.storage.gen_session()
    #     for setting in self.settings.get(self.name)
    #     reddit = Reddit("gundeals")
        # entries = reddit.get_posts(FEED_LIMIT)
        # for entry in entries:
        #     exists = ses.query(FeedEntry).filter(FeedEntry.post_id == entry.id).count() > 0
        #     if not exists and not entry.sticky:
        #         print("Stored: {}".format(entry))
        #         ses.add(FeedEntry(post_id=entry.id,
        #                           title=entry.title,
        #                           author=entry.author,
        #                           post=entry.post,
        #                           posted_on=entry.posted_on,
        #                           text=entry.text,
        #                           link=entry.link,
        #                           thumb=entry.thumb,
        #                           sticky=entry.sticky,
        #                           nsfw=entry.nsfw,
        #                           flair=entry.flair,
        #                           posted=False))
        #         ses.commit()
        # ses.close()
