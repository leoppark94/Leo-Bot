import random
import discord
import os
import openpyxl
import requests
import asyncio
from json import loads
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("Leo Bot(Twitch) 준비완료")
    #파이썬 파일 실행준비시 나올 문구
    game = discord.Game("Leo BOT 열심히 듣는")
    #봇 실행 중 상태표시창에 나올 문구
    await client.change_presence(status=discord.Status.online, activity=game)
    #봇 상태 색상변경


    twitch = "leoppark94"
    name = "레오"
    channel = client.get_channel(297328857567199232)
    a = 0

    while True:
        headers = {'Client-ID': 'uzajzjglke3x3094l7iv5zvacnxeyp'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send(name + "님이 방송중입니다. https://www.twitch.tv/" + twitch)
                a = 1
        except:
            a = 0

        await asyncio.sleep(3)



access_token = os.environ["BOT_TOKEN"]            
client.run(access_token)
