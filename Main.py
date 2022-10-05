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

@client.command()
async def search(ctx, txt):
    a = x.search(txt)
    await ctx.send(a)

@client.command()
async def info(ctx,txt):
    txt = txt.replace('_',' ')
    a = x.info(txt)
    img = a['main_picture']['large']
    embed = discord.Embed(
        title= a['title'],
        description= a['synopsis'],
        color= 0x1abc9
    )
    embed.set_image(url=img)

    await ctx.send(embed= embed)

@client.commanf()
async def suggest(ctx, typ):
    a= x.suggest(typ)

    embed = discord.Embed(
        title= a['title'],
        description= a['synopsis'],
        color= 0x1abc9
    )
    embed.set_image(url=a['main_picture']['large'])

    await ctx.send(embed= embed)

client.run(TOKEN)
