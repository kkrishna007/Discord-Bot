import discord
from discord.ext import commands, tasks

class Test(commands.Cog):
    def __init__(self,client):
        self.client=client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print ('Test Ready')
    
    #Commands
    @commands.command(name='ping', help='This command returns the latency')
    async def ping(self,ctx):
        await ctx.send(f'**Pong!** {round(self.client.latency*1000)}ms')


    
def setup(client):
    client.add_cog(Test(client))
