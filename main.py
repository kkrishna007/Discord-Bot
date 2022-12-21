import discord,youtube_dl,random,asyncio,os,praw
from discord.ext import commands, tasks
from itertools import cycle
from async_timeout import timeout
from discord.ext import commands
from discord.voice_client import VoiceClient

status=cycle(['Guitar','Sitaar','Piano','PUBG','Ukulele','Saxophone','Violin','Tabla'])
client=commands.Bot(command_prefix='.')


reddit = praw.Reddit(client_id='mCkzcpUAFjwilA',
                     client_secret='DlqfAQijHt6wTKeVOcqEweVhTRE',
                     user_agent='discord bot by u/KKRISHNA007')

#on ready
@client.event
async def on_ready():
    change_status.start()
    print ("Tansen Babu Tayyar Hai.")

#cogs
@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('C:\\Users\\Kkrishna\\OneDrive\\Desktop\\DESKTOP\\DISCORD BOT\\cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


#responding to some words
@client.event
async def on_message(message):

        if message.author == client.user:
            return

        if message.author.bot: 
            return

        if 'tansen' in message.content.lower():
            await message.channel.send('Kya hua ji? Mera naam liya kisi ne ???')

        elif 'ram ram' in message.content.lower():
            await message.channel.send(random.choice(['Jai Mata Di','Jai Shree Ram','Siyavar Ram Chandra Ki Jai']))

        elif 'nigga' in message.content.lower():
            await message.channel.send("Don't use the N-word")  
        
        elif 'sex' in message.content.lower():
            await message.channel.send('Behave!')   

        elif 'fuck' in message.content.lower():
            await message.channel.send("Don't abuse in the GC") 

        elif 'rasode mai kon tha' in message.content.lower():
            await message.channel.send('Rashi Ben')
            await message.channel.send('https://tenor.com/view/rashi-bahu-rasude-gif-18250889')      

        elif 'help' in message.content.lower():
            await message.channel.send('I am always there to help you.....')
            
        await client.process_commands(message)   
        

#hey
@client.command(help= 'This Command is used to introduce Tansen Himself and about his creator.')
async def hey(ctx):
    await ctx.send(f'Namaste, I am Tansen. I was created by'+ ' <@629655903913771046>' +'.\nI am his first test project.\nI can do Moderations and some fun stuff too.')

#on command errors
@client.event
async def on_command_error(ctx,error):
    if isinstance (error,commands.CommandNotFound):
        await ctx.send("Invalid Command used. Get some help bruh.\nNashe kam kara kar :smoking:")

#status
@tasks.loop(seconds=7)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#dank
@client.command(aliases=['dankmemes'], help="Get high quality Dank Memes from Reddit")
async def dank(ctx):
    memes_submissions = reddit.subreddit('dankmemes').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@client.command(aliases=['reddit'],help="Get high quality hot posts from desired subreddit")
async def red(ctx,*,sr):
    red_submissions = reddit.subreddit(sr).hot()
    red_to_pick=random.randint(1,20)
    for i in range(0, red_to_pick):
        sub = next(x for x in red_submissions if not x.stickied)

    await ctx.send(sub.url)

#hello
@client.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    import random
    hello_response = ['***grumble*** Why did you wake me up?',
                      'Top of the morning to you lad!',
                      'Hello, how are you?',
                      'Hi',
                      '**Wasssuup!**',
                      'Bhai apni Bandi ke ghar pe akela tha\nKyu bula liya?\nKya kaam hai?']
    await ctx.send(random.choice(hello_response))

#die
@client.command(name='die', help='This command returns a random last words')
async def die(ctx):
    import random
    die_responses = ['why have you brought my short life to an end',
                     'i could have done so much more',
                     'i have a family, kill them instead',
                     'Mera badla lene koi zarur ayega.',
                     'Hume maarke galat kiye. Pachtaoge ab']
    await ctx.send(random.choice(die_responses))

#youtube
youtube_dl.utils.bug_reports_message = lambda: ''

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
@client.command(name='join', help='This command makes the bot join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

@client.command(name='queue', help='This command adds a song to the queue')
async def queue_(ctx, url):
    global queue

    queue.append(url)
    await ctx.send(f'`{url}` added to queue!')

@client.command(name='remove', help='This command removes an item from the list')
async def remove(ctx, number):
    global queue

    try:
        del(queue[int(number)])
        await ctx.send(f'Your queue is now `{queue}!`')
    
    except:
        await ctx.send('Your queue is either **empty** or the index is **out of range**')
        
@client.command(name='play', help='This command plays songs')
async def play(ctx):
    global queue

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(queue[0], loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))
    del(queue[0])

@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()

@client.command(name='resume', help='This command resumes the song!')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()

@client.command(name='view', help='This command shows the queue')
async def view(ctx):
    await ctx.send(f'Your queue is now `{queue}!`')

@client.command(name='leave', help='This command stops makes the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@client.command(name='stop', help='This command stops the song!')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()




    
'''
queue = [ ]
youtube_dl.utils.bug_reports_message = lambda: ''

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

@client.command(name='join', help='This command makes the bot join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return    
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(name='queue', help='This command adds a song to the queue')
async def queue_(ctx, url):
    global queue

    queue.append(url)
    await ctx.send(f'`{url}` added to queue!')

@client.command(name='remove', help='This command removes an item from the list')
async def remove(ctx, number):
    global queue

    try:
        del(queue[int(number)])
        await ctx.send(f'Your queue is now `{queue}!`')
    
    except:
        await ctx.send('Your queue is either **empty** or the index is **out of range**')
        
@client.command(name='view', help='This command shows the queue')
async def view(ctx):
    await ctx.send(f'Your queue is now `{queue}!`')

@client.command(name='leave', help='This command stops makes the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@client.command(name='play',aliases=['p','bajao'], help='This command plays music')
async def play(ctx,*,url):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice_client
    
    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send(f':thumbsup: Joined VC')
    await ctx.send('Searching :mag_right: ')
    await ctx.send('**Now Playing :notes:: ** ***{}***'.format(player.title))

@client.command(name='stop', help='This command stops the music and makes the bot leave the voice channel')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
'''

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')
    
client.run('TOKEN')
