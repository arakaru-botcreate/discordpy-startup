from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@client.event
async def on_raw_reaction_add(payload):

    if payload.message_id == ID:

        print(payload.emoji.name)
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        role = discord.utils.find(lambda r: r.name == payload.emoji.name, guild.roles)

        if role is not None:
            print(role.name + " was found!")
            print(role.id)
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            await member.add_roles(role)
            print("done")


@client.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == ID:
        print(payload.emoji.name)

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        role = discord.utils.find(lambda r: r.name == payload.emoji.name, guild.roles)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
            print("done")


@client.event
async def on_ready():
    print("Botは正常に起動しました！")
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')
    await client.change_presence(activity=discord.Game(name="役職を管理！"))
    
    
bot.run(token)
client.run("TOKEN")
