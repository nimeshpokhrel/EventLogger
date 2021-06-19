import discord
import functionsBOT
from discord.ext import commands
import random
import mdbF
import datetime
from datetime import timedelta


class moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def logChannel(self, gID: int):
        data = mdbF.load_data("logschannel")
        guildID = str(gID)
        incID = data[guildID]
        return incID

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        slogC = mdbF.load_data("logschannel")
        if str(guild.id) in slogC:
            logcID = await self.logChannel(guild.id)
            logc = discord.utils.get(self.client.get_all_channels(), id=logcID)
            cnum = random.randint(1, 9999)
            when = datetime.datetime.utcnow()
            before = when + timedelta(minutes=1)
            after = when - timedelta(minutes=1)
            entry = await guild.audit_logs(action=discord.AuditLogAction.ban, before=before, after=after).find(lambda e: e.target.id == user.id and after < e.created_at < before)
            embed = discord.Embed(timestamp=functionsBOT.timedate(
            ), description=f"**Offender:** {user.name} `{user.id}`\n**Responsible Moderator:** {entry.user.mention} `{entry.user.id}`\n**Reason:** {entry.reason}", colour=discord.Colour(16472409))
            embed.set_author(name=f"user banned | case {cnum}")
            embed.set_footer(text="Auto-Generated")
            await logc.send(embed=embed)
        else:
            pass

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        slogC = mdbF.load_data("logschannel")
        if str(guild.id) in slogC:
            logcID = await self.logChannel(guild.id)
            logc = discord.utils.get(self.client.get_all_channels(), id=logcID)
            cnum = random.randint(1, 9999)
            when = datetime.datetime.utcnow()
            before = when + timedelta(minutes=1)
            after = when - timedelta(minutes=1)
            entry = await guild.audit_logs(action=discord.AuditLogAction.unban, before=before, after=after).find(lambda e: e.target.id == user.id and after < e.created_at < before)
            embed = discord.Embed(timestamp=functionsBOT.timedate(
            ), description=f"**Offender:** {user.name} `{user.id}`\n**Responsible Moderator:** {entry.user.mention} `{entry.user.id}`", colour=discord.Colour(16472409))
            embed.set_author(name=f"user unbanned | case {cnum}")
            embed.set_footer(text="Auto-Generated")
            await logc.send(embed=embed)
        else:
            pass


def setup(client):
    client.add_cog(moderation(client))
