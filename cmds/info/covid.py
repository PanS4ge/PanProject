#{}covid - Get information about that sh*t
import discord
import requests
import json

url = "https://api.covid19api.com/summary"

async def Cmd(language, serverlang, message, client):
    response = requests.get(url)
    data_json = response.json()
    embedVar = discord.Embed(title="Global Covid-19 cases", description="When it will go away :(", color=0x000000)
    embedVar.add_field(name="New Confirmed Cases", value=data_json['Global']['NewConfirmed'], inline=True)
    embedVar.add_field(name="All Confirmed Cases", value=data_json['Global']['TotalConfirmed'], inline=True)
    embedVar.add_field(name="New Deaths", value=data_json['Global']['NewDeaths'], inline=True)
    embedVar.add_field(name="All Deaths", value=data_json['Global']['TotalDeaths'], inline=True)
    embedVar.add_field(name="New Recovered", value=data_json['Global']['NewRecovered'], inline=True)
    embedVar.add_field(name="All Recovered", value=data_json['Global']['TotalRecovered'], inline=True)
    ncs = []
    acs = []
    nd = []
    ad = []
    nr = []
    ar = []
    for x in data_json['Countries']:
        ncs.append(x['NewConfirmed'])
        acs.append(x['TotalConfirmed'])
        nd.append(x['NewDeaths'])
        ad.append(x['TotalDeaths'])
        nr.append(x['NewRecovered'])
        ar.append(x['TotalRecovered'])
    maxncs = max(ncs)
    maxacs = max(acs)
    maxnd = max(nd)
    maxad = max(ad)
    maxnr = max(nr)
    maxar = max(ar)
    embedVar.add_field(name="Leaders in categories", value="This is sad", inline=False)
    embedVar.add_field(name="New Confirmed Cases", value=f"{data_json['Countries'][ncs.index(maxncs)]['Country']} with {maxncs}", inline=False)
    embedVar.add_field(name="All Confirmed Cases", value=f"{data_json['Countries'][acs.index(maxacs)]['Country']} with {maxacs}", inline=False)
    embedVar.add_field(name="New Deaths", value=f"{data_json['Countries'][nd.index(maxnd)]['Country']} with {maxnd}", inline=False)
    embedVar.add_field(name="All Deaths", value=f"{data_json['Countries'][ad.index(maxad)]['Country']} with {maxad}", inline=False)
    embedVar.add_field(name="New Recovered", value=f"{data_json['Countries'][nr.index(maxnr)]['Country']} with {maxnr}", inline=False)
    embedVar.add_field(name="All Recovered", value=f"{data_json['Countries'][ar.index(maxar)]['Country']} with {maxar}", inline=False)
    embedVar.set_footer(text=f"{data_json['Global']['Date']}")
    await message.channel.send(embed=embedVar)