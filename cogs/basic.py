import discord
import functionsBOT
from discord.ext import commands, tasks
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get
from functionsBOT import getGuildPrefix


class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client
    # (Always use self in command arguments)

    # Commands
    @commands.command()  # For Commands Header
    async def help(self, ctx):
        embed = discord.Embed(timestamp=functionsBOT.timedate(
        ), description=f"**This is default help menu. Change it in `basic.py`**", colour=discord.Colour(16472409))
        embed.add_field(name="`{}logchannel`".format(functionsBOT.getGuildPrefix(ctx.guild.id)),
                        value="This will change the log channel where all the server and member logs are stored.")
        embed.set_author(name=f"Help Menu")
        embed.set_footer(text="Auto-Generated")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Basic(client))
