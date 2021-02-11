import logging
import operator
import os

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands, tasks

from cogs.utils.timing import calc_tomorrow_6am, wait_until


class WordOfTheDay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # pylint: disable=no-member
        self.wotd_task.start()

    @commands.command()
    async def wotd(self, ctx):
        wod = self.format_wod_response_embed(*self.get_word_of_the_day())
        await ctx.send(embed=wod)

    @tasks.loop(hours=24)
    async def wotd_task(self):
        logging.info("channel id %s", os.getenv("DSCRD_CHNL_GENERAL"))
        chnl = self.bot.get_channel(int(os.getenv("DSCRD_CHNL_GENERAL")))
        logging.info("Got channel %s", chnl)
        await chnl.send(
            embed=self.format_wod_response_embed(*self.get_word_of_the_day())
        )

    @wotd_task.before_loop
    async def before(self):
        await self.bot.wait_until_ready()
        logging.info("wotd_task_before_loop: bot ready")
        tmrw_6am = calc_tomorrow_6am()
        logging.info("wotd_task_before_loop: waiting until: %s", tmrw_6am)
        await wait_until(tmrw_6am)
        logging.info("wotd_task_before_loop: waited until 6am")

    def get_word_of_the_day(self):
        response = requests.get("https://www.merriam-webster.com/word-of-the-day")
        soup = BeautifulSoup(response.text, features="html.parser")
        logging.debug(
            "received response from https://www.merriam-webster.com/word-of-the-day"
        )
        word = soup.find("div", class_="word-and-pronunciation").h1.string
        part_of_speech = soup.find("span", class_="main-attr").string
        word_syllables = soup.find("span", class_="word-syllables").string
        definitions = list(
            map(
                operator.attrgetter("text"),
                soup.find("div", class_="wod-definition-container").find_all(
                    "p", recursive=False
                ),
            )
        )

        return word, word_syllables, part_of_speech, definitions

    def format_wod_response_embed(
        self, word, word_syllables, part_of_speech, definitions
    ):
        embed = discord.Embed(
            title="Word of the Day Post", description="The word du jour", color=0x9D2235
        )
        embed.add_field(name="Today's Word", value=word, inline=False)
        embed.add_field(name="Part of Speech", value=part_of_speech)
        embed.add_field(name="Syllables", value=word_syllables, inline=False)
        embed.add_field(name="Definition(s)", value=definitions)
        return embed
