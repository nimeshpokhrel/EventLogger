import discord
import datetime
import mdbF

def getGuildPrefix(guild):
	data = mdbF.load_data("prefix")
	guilID = str(guild)
	if guilID in data:
		return data[guilID]

def timedate(req="time"):
	timedate = datetime.datetime.utcnow()
	return timedate

def color():
	return discord.Colour(3773679)
