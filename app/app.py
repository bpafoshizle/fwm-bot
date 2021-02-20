import logging
import os

from cogs.inspire import InspireQuote
from cogs.seekingalphanews import SeekingAlhpaNews
from cogs.stocks import StockQuote
from cogs.wotd import WordOfTheDay
from discord.ext import commands

LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()
logging.basicConfig(level=LOGLEVEL)

bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
    logging.info("Logged in as %s", bot.user)


@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


bot.add_cog(WordOfTheDay(bot))
bot.add_cog(InspireQuote(bot))
bot.add_cog(StockQuote(bot))
bot.add_cog(SeekingAlhpaNews(bot))

logging.info("running bot: %s", bot)
bot.run(os.getenv("DISCORD_TOKEN"))
