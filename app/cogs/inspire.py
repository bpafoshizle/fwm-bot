import json

import requests
from discord.ext import commands


class InspireQuote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def inspire(self, ctx):
        await ctx.send(self.get_quote())

    def get_quote(self):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]["q"] + " -" + json_data[0]["a"]
        return quote
