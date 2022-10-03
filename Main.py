from Data import Data
import discord
from discord.ext import commands
from discord.utils import get

f = open("DC_DOUHAN_TOKEN", "r")

TOKEN = f.read()

intents = discord.Intents.default()
client = commands.Bot(command_prefix='&', intents=intents)

x = Data()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('My Anime List!'))
    print(f'{client.user} is ready for game!!')




