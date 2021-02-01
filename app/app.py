import json
import logging
import operator
import os

# import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands#, tasks

bot = commands.Bot(command_prefix=".")


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return quote


def get_word_of_the_day():
    response = requests.get("https://www.merriam-webster.com/word-of-the-day")
    soup = BeautifulSoup(response.text)
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


def format_wod_response_text(word, word_syllables, part_of_speech, definitions):
    nln = "\n"
    wod_response = f"""\
Word of the day: {word} [{word_syllables}], {part_of_speech}
Definitions:
{nln.join(definitions)}"""
    return wod_response


def format_wod_response_embed(word, word_syllables, part_of_speech, definitions):
    pass


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


@bot.command()
async def inspire(ctx):
    await ctx.send(get_quote())


@bot.command()
async def wotd(ctx):
    wod = format_wod_response_text(*get_word_of_the_day())
    await ctx.send(wod)


logging.info("running bot: %s", bot)
bot.run(os.getenv("DISCORD_TOKEN"))
