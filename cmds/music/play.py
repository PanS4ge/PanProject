#{}play (url) - Plays music from URL
import asyncio

import discord
from discord import FFmpegPCMAudio
from discord.utils import get
import youtube_dl
import os

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

def Get_Connected_VC(message):
    for x in message.guild.voice_channels:
        if(message.author in x.members):
            return x.id
    return 2137

async def Cmd(language, serverlang, message, client):
    try:
        channel = Get_Connected_VC(message)
        wok = await message.channel.send("Working on this...")
        if(Get_Connected_VC(wok) == 2137):
            await client.get_channel(channel).connect()
        if(channel != 2137):
            try:
                url = message.content.split(" ")[1]
            except:
                await message.channel.send("Bro put url after command.")
            '''
            song_there = os.path.isfile("song.mp3")
            try:
                if song_there:
                    os.remove("song.mp3")
            except PermissionError:
                await message.channel.send("Wait for the current playing music end or use the 'stop' command")
                return
            await message.channel.send("Getting everything ready, playing audio soon")
            guild = message.guild
            vcli = get(client.voice_clients, guild=message.guild)
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '128',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, 'song.mp3')
            vcli.play(discord.FFmpegPCMAudio("song.mp3"))
            '''
            guild = message.guild
            vcli = get(client.voice_clients, guild=message.guild)
            player = await YTDLSource.from_url(url, stream=True)
            vcli.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
            await message.channel.send('Now playing: {}'.format(player.title))
        else:
            await message.channel.send("Join VC idot, or join me with join cmd")
    except:
        await message.channel.send("Maybe send valid youtube video, or maybe someone already took me to play music.")