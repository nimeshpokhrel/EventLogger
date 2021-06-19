import discord
import os
from discord.ext import commands, tasks
import mdbF


def get_prefix(client, message):
    data = mdbF.load_data("prefix")
    guildID = str(message.guild.id)
    serverPrefix = data[guildID]
    return serverPrefix


intents = discord.Intents.all()
client = commands.Bot(command_prefix=get_prefix, intents=intents)
client.remove_command("help")

# BOT STATUS AREA START
svnum = str(len(client.guilds))


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name=f".help | EventLogger | SVs: {svnum}"))
    print('BOT IS ONLINE')
    print("UserName: ", client.user.name)
    print("UserID: ", client.user.id)
    countSV.start()


@tasks.loop(seconds=60)
async def countSV():
    svnum = len(client.guilds)
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name=f".help | EventLogger | SVs: {svnum}"))
# BOT STATUS AREA END

# COGS AREA START
for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
# COGS AREA END

client.run('')
