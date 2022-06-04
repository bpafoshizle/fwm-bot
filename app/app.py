import logging

from pydiscogs import botbuilder

bot = botbuilder.build_bot("fwm-bot.yaml")

logging.info("running bot: %s", bot)
bot.run(bot.discord_token)
