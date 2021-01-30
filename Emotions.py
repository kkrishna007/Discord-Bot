import discord,random
from discord.ext import commands, tasks

class Emotions(commands.Cog):
    def __init__(self,client):
        self.client=client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print ('Emotions Ready')
    
    #cry
    @commands.command(name='cry', help='Send a crying GIF!!')
    async def cry(self,ctx):
        import random
        cry_responses = ['https://tenor.com/view/choro-lagrimas-bico-chateada-gif-6165001',
                     'https://tenor.com/view/sad-crying-spiderman-cryface-uglyface-gif-5701170',
                     'https://tenor.com/view/omg-no-why-me-big-baby-ugly-gif-13752527',
                     'https://tenor.com/view/sad-blackish-anthony-anderson-tears-upset-gif-4988274',
                     'https://tenor.com/view/sad-down-gif-5337069',
                     'https://tenor.com/view/tears-sad-crying-cry-gif-3556278',
                     'https://tenor.com/view/crying-gif-3435309',
                     'https://tenor.com/view/boo-cry-monsters-inc-gif-10314257']
        await ctx.send(random.choice(cry_responses))

    #angry
    @commands.command(name='angry', help='Send a angry GIF!!')
    async def angry(self,ctx):
        import random
        angry_responses = ['https://tenor.com/view/mad-mad-face-pissed-frustrated-frustration-gif-15931246',
                     'https://tenor.com/view/rage-gif-4514235',
                     'https://tenor.com/view/you-mad-grumpy-angry-eating-hungry-gif-14536573',
                     'https://tenor.com/view/boss-baby-mad-sad-crying-gif-10842085',
                     'https://tenor.com/view/angry-gif-5902151',
                     'https://tenor.com/view/angry-bubbles-bubbles-fire-furious-mad-gif-12674420',
                     'https://tenor.com/view/angry-mad-rage-candy-gif-10604149']
                     
        await ctx.send(random.choice(angry_responses))

    #laugh
    @commands.command(name='laugh', help='Send a laughing GIF!!')
    async def laugh(self,ctx):
        import random
        laugh_responses = ['https://tenor.com/view/funny-lol-lmao-smile-happy-gif-16457588',
                     'https://tenor.com/view/spit-take-laugh-lmao-gif-9271200',
                     'https://tenor.com/view/baby-toddler-laughing-laugh-toppling-gif-4290934',
                     'https://tenor.com/view/jerry-funny-animal-laughing-gif-13124924',
                     'https://tenor.com/view/shirley-temple-giggle-laughing-black-and-white-movies-gif-3555152',
                     'https://tenor.com/view/puffybear-puffy-cute-lol-happy-gif-12628636',
                     'https://tenor.com/view/funny-smile-best-laugh-thats-funny-gif-8282901',
                     'https://tenor.com/view/laugh-lol-chuckles-funny-gif-5104045',
                     'https://tenor.com/view/minions-lol-laugh-despicable-me-gif-4519855',
                     'https://tenor.com/view/laughing-lmao-chris-evans-rofl-lmfao-gif-15486312']
                     
        await ctx.send(random.choice(laugh_responses))


    
def setup(client):
    client.add_cog(Emotions(client))
