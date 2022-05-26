import os
import logging
from discord.ext import commands

logger = logging.getLogger(__name__)

class MyClass(commands.Cog):
    def __init__(self, bot, guild_ids):
        self.bot = bot
        self.guild_ids = guild_ids
        bot.slash_command(guild_ids=guild_ids)(self.my_command_method)

    async def my_command_method(self, ctx, dorukyumParam="https://github.com/Pycord-Development/pycord/issues/1342"):
        logger.debug(f"reason for the dorukyumParam: {dorukyumParam}")
        await ctx.respond(f"Hello from my_command_method!")


if __name__ == "__main__":
    bot = commands.Bot()
    bot.add_cog(MyClass(bot, [os.getenv("DISCORD_GUILD_ID")]))
    bot.run(os.getenv('DISCORD_TOKEN'))