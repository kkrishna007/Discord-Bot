import discord
from discord.ext import commands, tasks

class Games(commands.Cog):
    def __init__(self,client):
        self.client=client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print ('Games Ready')
    
    #8ball Game
    @commands.command(aliases=['8ball'],help='This command answers any Yes/No Question')
    async def _8ball(self,ctx,*,question):
        import random
        responses = ['It is certain',
                  'Bhai mujhe nhi pata',
                  'Haa ji zarur',
                  'It is decidedly so',
                  'Without a doubt',
                  'Yes – definitely',
                  'You may rely on it',
                  'As I see it, yes',
                  'Most likely',
                  'Outlook good',
                  'Yes Signs point to yes',
                  'Reply hazy',
                  'Ask again later',
                  'Better not tell you now',
                  'Cannot predict now',
                  'Concentrate and ask again',
                  'Dont count on it',
                  'My reply is no',
                  'My sources say no',
                  'Outlook not so good',
                  'Very doubtful']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


    
def setup(client):
    client.add_cog(Games(client))