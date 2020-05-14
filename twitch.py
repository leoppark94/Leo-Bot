import random
import discord
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
    game = discord.Game("새로운 봇 제작중")
    #봇 실행 중 상태표시창에 나올 문구
    await client.change_presence(status=discord.Status.online, activity=game)
    #봇 상태 색상변경


    twitch_a = "green_teaa_"
    name_a = "동네건강원"
    a = 0
    twitch_b = "marucun"
    name_b = "히나마루"
    b = 0
    twitch_c = "dueeet"
    name_c = "Duet"
    c = 0
    twitch_d = "leoppark94"
    name_d = "레오"
    d = 0
    channel = client.get_channel(297328857567199232)

    while True:
        headers = {'Client-ID': 'uzajzjglke3x3094l7iv5zvacnxeyp'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch_a, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send(name_a + "님이 방송중입니다. https://www.twitch.tv/" + twitch_a)
                a = 1
        except:
            a = 0

        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch_b, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and b == 0:
                await channel.send(name_b + "님이 방송중입니다. https://www.twitch.tv/" + twitch_b)
                b = 1
        except:
            b = 0

        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch_c, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and c == 0:
                await channel.send(name_c + "님이 방송중입니다. https://www.twitch.tv/" + twitch_c)
                c = 1
        except:
            c = 0

        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch_d, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and d == 0:
                await channel.send(name_d + "님이 방송중입니다. https://www.twitch.tv/" + twitch_d)
                d = 1
        except:
            d = 0

        await asyncio.sleep(5)

client.run("Njk1MDQ1MTYyMDU2OTQxNTg5.XoUeUg.UkvyKR153UbtnQG6CDnYWMhx1wc")