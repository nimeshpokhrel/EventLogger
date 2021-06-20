import discord
import functionsBOT
from discord.ext import commands
import random
import mdbF
import datetime
from datetime import timedelta


class extras(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def logChannel(self, gID: int):
        data = mdbF.load_data("logschannel")
        guildID = str(gID)
        incID = data[guildID]
        return incID

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not before.author.bot:
            slogC = mdbF.load_data("logschannel")
            if str(before.author.guild.id) in slogC:
                logcID = await self.logChannel(before.author.guild.id)
                logc = discord.utils.get(
                    self.client.get_all_channels(), id=logcID)
                cnum = random.randint(1, 9999)
                embed = discord.Embed(timestamp=functionsBOT.timedate(
                ), description=f"**Before:** {before.content}\n**After:** {after.content}\n**Message ID:** `{before.id}`\n**Channel:** {before.channel.mention} `{before.channel.id}`\n**User:** {before.author.mention} `{before.author.id}`", colour=discord.Colour(15116805))
                embed.set_author(name=f"message edited | case {cnum}")
                embed.set_footer(text="Auto-Generated")
                await logc.send(embed=embed)
            else:
                pass
        else:
            return

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            slogC = mdbF.load_data("logschannel")
            if str(message.author.guild.id) in slogC:
                logcID = await self.logChannel(message.author.guild.id)
                logc = discord.utils.get(
                    self.client.get_all_channels(), id=logcID)
                cnum = random.randint(1, 9999)
                embed = discord.Embed(timestamp=functionsBOT.timedate(
                ), description=f"**Message:** {message.content}\n**Message ID:** `{message.id}`\n**Channel:** {message.channel.mention} `{message.channel.id}`\n**User:** {message.author.mention} `{message.author.id}`", colour=discord.Colour(16472409))
                embed.set_author(name=f"message deleted | case {cnum}")
                embed.set_footer(text="Auto-Generated")
                await logc.send(embed=embed)
            else:
                pass
        else:
            return

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.member, before, after):
        if not member.bot:
            slogC = mdbF.load_data("logschannel")
            if str(member.guild.id) in slogC:
                if before.channel == None:
                    logcID = await self.logChannel(member.guild.id)
                    logc = discord.utils.get(
                        self.client.get_all_channels(), id=logcID)
                    cnum = random.randint(1, 9999)
                    embed = discord.Embed(timestamp=functionsBOT.timedate(
                    ), description=f"**Channel:** {after.channel.name} `{after.channel.id}`\n**User:** {member.mention} `{member.id}`", colour=discord.Colour(1892359))
                    embed.set_author(name=f"channel joined | case {cnum}")
                    embed.set_footer(text="Auto-Generated")
                    await logc.send(embed=embed)
                elif before.channel != None and after.channel != None and before.channel != after.channel:
                    logcID = await self.logChannel(member.guild.id)
                    logc = discord.utils.get(
                        self.client.get_all_channels(), id=logcID)
                    cnum = random.randint(1, 9999)
                    embed = discord.Embed(timestamp=functionsBOT.timedate(
                    ), description=f"**Before:** {before.channel.name} `{before.channel.id}`\n**After:** {after.channel.name} `{after.channel.id}`\n**User:** {member.mention} `{member.id}`", colour=discord.Colour(15116805))
                    embed.set_author(name=f"channel changed | case {cnum}")
                    embed.set_footer(text="Auto-Generated")
                    await logc.send(embed=embed)
                elif before.channel != None and after.channel == None:
                    logcID = await self.logChannel(member.guild.id)
                    logc = discord.utils.get(
                        self.client.get_all_channels(), id=logcID)
                    cnum = random.randint(1, 9999)
                    embed = discord.Embed(timestamp=functionsBOT.timedate(
                    ), description=f"**Channel:** {before.channel.name} `{before.channel.id}`\n**User:** {member.mention} `{member.id}`", colour=discord.Colour(16472409))
                    embed.set_author(name=f"channel left | case {cnum}")
                    embed.set_footer(text="Auto-Generated")
                    await logc.send(embed=embed)
            else:
                pass
        else:
            return

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        slogC = mdbF.load_data("logschannel")
        if str(invite.guild.id) in slogC:
            logcID = await self.logChannel(invite.guild.id)
            logc = discord.utils.get(self.client.get_all_channels(), id=logcID)
            cnum = random.randint(1, 9999)
            if invite.max_uses == 0 and invite.max_age != 0:
                embed = discord.Embed(timestamp=functionsBOT.timedate(
                ), description=f"**Code:** {invite.code}\n**Channel:** {invite.channel}\n**Expires:** {invite.max_age / 3600} hour/s\n**Uses:** Unlimited\n**User:** {invite.inviter.mention} `{invite.inviter.id}`", colour=discord.Colour(15116805))
                embed.set_author(name=f"invite created | case {cnum}")
                embed.set_footer(text="Auto-Generated")
                await logc.send(embed=embed)
            elif invite.max_uses != 0 and invite.max_age == 0:
                embed = discord.Embed(timestamp=functionsBOT.timedate(
                ), description=f"**Code:** {invite.code}\n**Channel:** {invite.channel}\n**Expires:** Never\n**Uses:** {invite.max_uses}\n**User:** {invite.inviter.mention} `{invite.inviter.id}`", colour=discord.Colour(15116805))
                embed.set_author(name=f"invite created | case {cnum}")
                embed.set_footer(text="Auto-Generated")
                await logc.send(embed=embed)
            elif invite.max_uses == 0 and invite.max_age == 0:
                embed = discord.Embed(timestamp=functionsBOT.timedate(
                ), description=f"**Code:** {invite.code}\n**Channel:** {invite.channel}\n**Expires:** Never\n**Uses:** Unlimited\n**User:** {invite.inviter.mention} `{invite.inviter.id}`", colour=discord.Colour(15116805))
                embed.set_author(name=f"invite created | case {cnum}")
                embed.set_footer(text="Auto-Generated")
                await logc.send(embed=embed)
            else:
                embed = discord.Embed(timestamp=functionsBOT.timedate(
                ), description=f"**Code:** {invite.code}\n**Channel:** {invite.channel}\n**Expires:** {invite.max_age / 3600} hour/s\n**Uses:** {invite.max_uses}\n**User:** {invite.inviter} `<@{invite.inviter.id}>`", colour=discord.Colour(15116805))
                embed.set_author(name=f"invite created | case {cnum}")
                embed.set_footer(text="Auto-Generated")
                await logc.send(embed=embed)
        else:
            pass

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        # if before.roles != after.roles:
        #     bID = []
        #     aID = []
        #     for x in before.roles:
        #         bID.append(x.id)
        #     for x in after.roles:
        #         aID.append(x.id)
        #     slogC = mdbF.load_data("logschannel")
        #     if str(before.guild.id) in slogC:
        #         logcID = await self.logChannel(before.guild.id)
        #         logc = discord.utils.get(self.client.get_all_channels(), id=logcID)
        #         cnum = random.randint(1, 9999)
        #         embed = discord.Embed(timestamp=functionsBOT.timedate(), description=f"**Before:** {bID} \n**After:** {aID}", colour=discord.Colour(15116805))
        #         embed.set_author(name=f"role updated | case {cnum}")
        #         embed.set_footer(text="Auto-Generated")
        #         await logc.send(embed=embed)
        #     else:
        #         pass
        if before.nick != after.nick:
            slogC = mdbF.load_data("logschannel")
            if str(before.guild.id) in slogC:
                logcID = await self.logChannel(before.guild.id)
                logc = discord.utils.get(
                    self.client.get_all_channels(), id=logcID)
                cnum = random.randint(1, 9999)
                embed = discord.Embed(timestamp=functionsBOT.timedate(
                ), description=f"**Before:** {before.nick} \n**After:** {after.nick}\n**User:** {before.mention} `{before.id}`", colour=discord.Colour(15116805))
                embed.set_author(name=f"nickname updated | case {cnum}")
                embed.set_footer(text="Auto-Generated")
                await logc.send(embed=embed)
            else:
                pass
        else:
            pass


def setup(client):
    client.add_cog(extras(client))
