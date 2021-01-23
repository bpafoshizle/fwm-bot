import discord
import os
import logging
import requests
import json
from bs4 import BeautifulSoup
import operator

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_word_of_the_day():
    response = requests.get("https://www.merriam-webster.com/word-of-the-day")
    soup = BeautifulSoup(response.text)
    logging.debug("received response from https://www.merriam-webster.com/word-of-the-day")
    word = soup.find("div", class_="word-and-pronunciation").h1.string
    part_of_speech = soup.find("span", class_="main-attr").string
    word_syllables = soup.find("span", class_="word-syllables").string
    definitions = list(map(
        operator.attrgetter("text"),
        soup.find("div", class_="wod-definition-container").find_all('p' ,recursive=False)
    ))

    nl = "\n"
    wod_response = f"""\
Word of the day: {word} [{word_syllables}], {part_of_speech}
Definitions:
{nl.join(definitions)}"""

    return wod_response
    

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    
    if message.content.startswith('$wotd'):
        wod = get_word_of_the_day()
        await message.channel.send(wod)

logging.info(f'running client: {client}')
client.run(os.getenv('TOKEN'))
