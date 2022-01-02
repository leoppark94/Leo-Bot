import discord
from discord.ext import commands

# fired when Discord API is ready to be used

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name, '디스코드에 연결됨')
    await client.change_presence(status=discord.Status.online, activity=None)
    print("ready")

# 테스트로만들어본 예제
@client.event
async def on_message(message):
    if message.content.startswith('!안녕'):
        channel = message.channel
        await channel.send('안녕하세요, 살아났어요')

# start the discord bot
client.run("Njk1MDQ1MTYyMDU2OTQxNTg5.XoUdPw.8k2yQ8g2EbSmP3PTKW6CqukLRkw")