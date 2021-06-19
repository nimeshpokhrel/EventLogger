import discord
import functionsBOT
from discord.ext import commands
import random
import mdbF
import datetime
from datetime import timedelta


class main(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def getPrefix(self, gID: int):
        data = mdbF.load_data("prefix")
        guildID = str(gID)
        serverPrefix = data[guildID]
        return serverPrefix

    async def logChannel(self, gID: int):
        data = mdbF.load_data("logschannel")
        guildID = str(gID)
        incID = data[guildID]
        return incID

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        prefix = await self.getPrefix(ctx.guild.id)
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("**Command** Not Found\nPlease Use `{}help` For All **Commands**".format(prefix))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        prefix = await self.getPrefix(message.guild.id)
        if f"<@!{self.client.user.id}>" in message.content:
            await message.channel.send("**My Prefix** Here is `{}`\nPlease Use `{}help` For All **Commands**".format(prefix, prefix))

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        mdbF.save_data(str(guild.id), ".", "prefix")

        mdbF.save_data(str(guild.id), "None", "logschannel")

        spch = self.client.get_channel(765380327731626034)
        embed = discord.Embed(colour=functionsBOT.color(),
                              timestamp=functionsBOT.timedate())
        embed.set_footer(text="Auto-Generated")
        embed.set_author(name="BOT ADDED")
        embed.add_field(
            name='<a:b_yes:764720042817486870> Server Name:', value=guild.name, inline=False)
        embed.add_field(name='<a:b_yes:764720042817486870> Server Owner:',
                        value=guild.owner.mention, inline=False)
        embed.add_field(
            name='<a:b_yes:764720042817486870> Server ID:', value=guild.id, inline=False)
        embed.add_field(name='<a:b_yes:764720042817486870> Server Location:',
                        value=guild.region, inline=False)
        await spch.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        mdbF.remove_data(str(guild.id), "prefix")

        mdbF.remove_data(str(guild.id), "logschannel")

        spch = self.client.get_channel(765495848813461504)
        embed = discord.Embed(colour=functionsBOT.color(),
                              timestamp=functionsBOT.timedate())
        embed.set_footer(text="Auto-Generated")
        embed.set_author(name="BOT REMOVED")
        embed.add_field(
            name='<a:b_no:764720074258120704>  Server Name:', value=guild.name, inline=False)
        embed.add_field(name='<a:b_no:764720074258120704>  Server Owner:',
                        value=guild.owner.mention, inline=False)
        embed.add_field(
            name='<a:b_no:764720074258120704>  Server ID:', value=guild.id, inline=False)
        embed.add_field(name='<a:b_no:764720074258120704>  Server Location:',
                        value=guild.region, inline=False)
        await spch.send(embed=embed)


def setup(client):
    client.add_cog(main(client))
