import discord,random
from discord.ext import commands, tasks

class Moderation(commands.Cog):
    def __init__(self,client):
        self.client=client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print ('Moderation Ready')

    
    #kick
    @commands.command(name='kick', help='This command kicks members.')
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self,ctx,member : discord.Member,*,reason=None):
        await member.kick(reason=reason)

    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You don't have permission to kick someone.")
        
    #ban
    @commands.command(name='ban', help='This command ban members.')
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self,ctx,member : discord.Member,*,reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @ban.error
    async def ban_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You don't have permission to ban someone.")

    #unban
    @commands.command(help='This command unbans a banned Discord User.')
    @commands.has_guild_permissions(manage_guild=True)
    async def unban(self,ctx,*, member):
        banned_users=await ctx.guild.bans()
        member_name,member_discriminator=member.split('#')

        for ban_entry in banned_users:
            user=ban_entry.user

            if (user.name,user.discriminator)==(member_name,member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return

    @unban.error
    async def unban_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You don't have permission to unban someone.")

    #clear
    @commands.command(aliases=['delete','purge','nuke'],help='This command clear messages.')
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx, amount=2):
        await ctx.channel.purge(limit=amount+1)

    @clear.error
    async def clear_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You don't have permission to clear messages.")

def setup(client):
    client.add_cog(Moderation(client))       
