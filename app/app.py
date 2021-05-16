import logging
import os

from cogs.reddit import Reddit
from cogs.twitch import Twitch
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


bot.add_cog(Twitch(bot))
bot.add_cog(Reddit(bot))

logging.info("running bot: %s", bot)
bot.run(os.getenv("DISCORD_TOKEN"))
