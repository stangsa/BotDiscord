import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

## Event
@client.event
async def on_ready():
    print('#################')
    print('###### BOT ######')
    print('### STARTING ###')

@client.event
async def on_member_join(member):
    print(f'{member} has join a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

### Command ###
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)} ms.')
## Chat Command
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason='None'):
    await member.kick(reason=f'AD-Kick_Reason: {reason}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason='None'):
    await member.ban(reason=f'AD-Ban_Reason: {reason}')

@client.command()
async def unban(ctx, *, member):
    Banned_users = await ctx.guild.bans()
    member_name, member_id = member.split('#')
    for ban_entry in Banned_users:
        user = ban_entry.user
        if (user.name, user.id) == (member_name, member_id):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbaned {user.name}#{user.id}')
            return

client.run('NzEwMDA1MDYxMDkwMjc5NDc1.Xrv0FQ.bweVohDi0SsMbg4qkS9iZCcCcxQ')