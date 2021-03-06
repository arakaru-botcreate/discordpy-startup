import discord
import os

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
CANNEL_ID = 748986561131053198


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "start":
        await message.cnannel.send("ここにリアクションを付ける")

@client.event
async def on_raw_reaction_add(payload):

    if payload.message_id == 785335000580751390:

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
    if payload.message_id == 785335000580751390:
        print(payload.emoji.name)

        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        role = discord.utils.find(lambda r: r.name == payload.emoji.name, guild.roles)

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            await member.remove_roles(role)
            print("done")

async def greet():
    channnel = client.get_channel(CANNEL_ID)
    await channel.send('起動')

@client.event
async def on_ready():
    print("Botは正常に起動しました！")
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')
    await client.change_presence(activity=discord.Game(name="役職を管理！1"))
    await greet()

client.run(token)
