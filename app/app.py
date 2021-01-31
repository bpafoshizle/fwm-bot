import json
import logging
import operator
import os

import discord
import requests
from bs4 import BeautifulSoup

client = discord.Client()


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


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    if message.content.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith("$wotd"):
        wod = format_wod_response_text(*get_word_of_the_day())
        await message.channel.send(wod)


logging.info("running client: %s", client)
client.run(os.getenv("DISCORD_TOKEN"))
