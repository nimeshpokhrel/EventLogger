import discord
import functionsBOT
import random
import mdbF
import datetime
from datetime import timedelta
from discord.ext import commands


class events(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def logChannel(self, gID: int):
        data = mdbF.load_data("logschannel")
        guildID = str(gID)
        if guildID in data:
            logID = data[guildID]
        else:
            logID = None
        return logID

    @commands.Cog.listener()
    async def on_member_join(self, member):
        incID = await self.logChannel(member.guild.id)
        if (incID != None):
            inc = discord.utils.get(self.client.get_all_channels(), id=incID)
            if(inc != None):
                await inc.send(f"Hey {member.mention}, welcome to **{member.guild.name}**!")
        defrolID = await self.getdefrole(member.guild.id)
        defrol = discord.utils.get(member.guild.roles, id=defrolID)
        if(defrol != None):
            await member.add_roles(defrol)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        outcID = await self.logChannel(member.guild.id)
        if (outcID != None):
            outc = discord.utils.get(self.client.get_all_channels(), id=outcID)
            if(outc != None):
                await outc.send(f"**{member}**, just left the server!")
        roledata = mdbF.load_data("temproleholder")
        guildID = str(member.guild.id)
        if guildID in roledata:
            memberID = member.id
            allRoles = member.roles
            print(allRoles)
            for x in allRoles:
                if x.id == int(guildID):
                    allRoles.remove(x)
                if roledata[guildID]["blacklist-roles"] != None:
                    if str(x.id) in roledata[guildID]["blacklist-roles"]:
                        allRoles.remove(x)

            print(allRoles)
            allRoles.reverse()
            print(allRoles)
            if allRoles != None:
                for x in allRoles:
                    mdbF.save_data("{}.{}.{}".format(
                        guildID, memberID, x.id), x.name, "temproleholder")

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        slogC = mdbF.load_data("logschannel")
        if str(channel.guild.id) in slogC:
            when = datetime.datetime.utcnow()
            before = when + timedelta(minutes=1)
            after = when - timedelta(minutes=1)
            entry = await channel.guild.audit_logs(action=discord.AuditLogAction.channel_delete, before=before,
                                                   after=after).find(
                lambda e: e.target.id == channel.id and after < e.created_at < before)
            logcID = await self.logChannel(channel.guild.id)
            logc = discord.utils.get(self.client.get_all_channels(), id=logcID)
            cnum = random.randint(1, 9999)
            embed = discord.Embed(timestamp=functionsBOT.timedate(
            ), description=f"**Type:** {channel.type}\n**Channel:** {channel.name} `<#{channel.id}>`\n**Category:** {channel.category} `{channel.category.id}`\n**Responsible Moderator:** {entry.user} `<@{entry.user.id}>`", colour=discord.Colour(16472409))
            embed.set_author(name=f"channel deleted | case {cnum}")
            embed.set_footer(text="Auto-Generated")
            await logc.send(embed=embed)
        else:
            pass

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        slogC = mdbF.load_data("logschannel")
        if str(channel.guild.id) in slogC:
            when = datetime.datetime.utcnow()
            before = when + timedelta(minutes=1)
            after = when - timedelta(minutes=1)
            entry = await channel.guild.audit_logs(action=discord.AuditLogAction.channel_create, before=before,
                                                   after=after).find(
                lambda e: e.target.id == channel.id and after < e.created_at < before)
            logcID = await self.logChannel(channel.guild.id)
            logc = discord.utils.get(self.client.get_all_channels(), id=logcID)
            cnum = random.randint(1, 9999)
            embed = discord.Embed(timestamp=functionsBOT.timedate(
            ), description=f"**Type:** {channel.type}\n**Channel:** {channel.name} `<#{channel.id}>`\n**Category:** {channel.category} `{channel.category.id}`\n**Responsible Moderator:** {entry.user} `<@{entry.user.id}>`", colour=discord.Colour(1892359))
            embed.set_author(name=f"channel created | case {cnum}")
            embed.set_footer(text="Auto-Generated")
            await logc.send(embed=embed)
        else:
            pass

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        slogC = mdbF.load_data("logschannel")
        if str(role.guild.id) in slogC:
            logcID = await self.logChannel(role.guild.id)
            logc = discord.utils.get(self.client.get_all_channels(), id=logcID)
            cnum = random.randint(1, 9999)
            when = datetime.datetime.utcnow()
            before = when + timedelta(minutes=1)
            after = when - timedelta(minutes=1)
            entry = await role.guild.audit_logs(action=discord.AuditLogAction.role_create, before=before, after=after).find(lambda e: e.target.id == role.id and after < e.created_at < before)
            embed = discord.Embed(timestamp=functionsBOT.timedate(
            ), description=f"**Role:** {role.name} `<@&{role.id}>`\n**Responsible Moderator:** {entry.user} `<@{entry.user.id}>`", colour=discord.Colour(15116805))
            embed.set_author(name=f"role created | case {cnum}")
            embed.set_footer(text="Auto-Generated")
            await logc.send(embed=embed)
        else:
            pass

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        slogC = mdbF.load_data("logschannel")
        if str(role.guild.id) in slogC:
            logcID = await self.logChannel(role.guild.id)
            logc = discord.utils.get(self.client.get_all_channels(), id=logcID)
            cnum = random.randint(1, 9999)
            when = datetime.datetime.utcnow()
            before = when + timedelta(minutes=1)
            after = when - timedelta(minutes=1)
            entry = await role.guild.audit_logs(action=discord.AuditLogAction.role_delete, before=before, after=after).find(lambda e: e.target.id == role.id and after < e.created_at < before)
            embed = discord.Embed(timestamp=functionsBOT.timedate(
            ), description=f"**Role:** {role.name} `<@&{role.id}>`\n**Responsible Moderator:** {entry.user} `<@{entry.user.id}>`", colour=discord.Colour(16472409))
            embed.set_author(name=f"role deleted | case {cnum}")
            embed.set_footer(text="Auto-Generated")
            await logc.send(embed=embed)
        else:
            pass

    @commands.Cog.listener()
    async def on_guild_role_update(self, bef, aft):
        slogC = mdbF.load_data("logschannel")
        if str(bef.guild.id) in slogC:
            logcID = await self.logChannel(bef.guild.id)
            logc = discord.utils.get(self.client.get_all_channels(), id=logcID)
            if bef.name != aft.name:
                cnum = random.randint(1, 9999)
                when = datetime.datetime.utcnow()
                before = when + timedelta(minutes=1)
                after = when - timedelta(minutes=1)
                entry = await bef.guild.audit_logs(action=discord.AuditLogAction.role_update, before=before, after=after).find(lambda e: e.target.id == bef.id and after < e.created_at < before)
                embed = discord.Embed(timestamp=functionsBOT.timedate(
                ), description=f"**Before:** {bef.name} `<@&{bef.id}>`\n**After:** {aft.name} `<@&{aft.id}>`\n**Responsible Moderator:** {entry.user} `<@{entry.user.id}>`", colour=discord.Colour(15116805))
                embed.set_author(name=f"role updated | case {cnum}")
                embed.set_footer(text="Auto-Generated")
                await logc.send(embed=embed)
        else:
            pass


def setup(client):
    client.add_cog(events(client))
