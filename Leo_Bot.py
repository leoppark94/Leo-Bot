import random
import os
import discord
import openpyxl
import requests
import asyncio
from json import loads

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("Leo Bot 준비완료")
    #파이썬 파일 실행준비시 나올 문구
    game = discord.Game("Leo BOT 열심히 듣는")
    #봇 실행 중 상태표시창에 나올 문구
    await client.change_presence(status=discord.Status.online, activity=game)
    #봇 상태 색상변경

# 입장시 자동인사
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send('반가워요 Leo(주형)의 디스코드 채널에 오신걸 환영합니다~~! 저는 레오 봇이에요')

# 퇴장시 자동인사
#@client.event
#async def on_member_remove(member):
#    channel = member.server.get_channel("695053856039764063")
#    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
#    await client.send_message(channel, fmt.format(member, member.server))


@client.event
# 안녕에 대한 응답 등 기본적인 응답
async def on_message(message):
    if message.content.startswith('!안녕'):
        channel = message.channel
        await channel.send('안녕하세요! 어떤것을 도와드릴까요? ' + message.author.display_name + '\n'
        + '사용가능한 명령어를 보기 위해서는 !명령어 를 입력해주세요!')
    if message.content.startswith('!명령어'):
        channel = message.channel
        await channel.send('사용가능한 명령어 리스트에요~!' + '\n'
                           + '모든 명령어 앞에는 !를 붙여주세요' + '\n'
                           + '주사위, 연속주사위, 사진, 공지, 채금, 경고, 팀, 포지션, 그냥팀' + '\n'
                           + '세부적인 명령어 설명을 보려면 !도움 (해당명령어) 를 입력해주세요.' + '\n'
                           + '- 현재 지원하는 게임 : 리그오브레전드, 오버워치')
    if message.content.startswith("!설명"):
        await message.channel.send("해당 봇은 채널의 사용자들의 게이밍 및 채널 관리를 도와줄 수 있는 다기능 무료 봇입니다.이용자들에게 동료들과 팀을 나누고, 불건전한 멤버에게 제제를 가할 수 있습니다.관리자의 일부 권한을 봇에게 나누어 주어 공지사항 등을 멤버들에게 전송할 수 있습니다.간단한 대화식 인터페이스로 되어 있어 사용이 간단하고 쉽습니다.")
    if message.content.startswith("!도움 주사위"):
        await message.channel.send("랜덤으로 주사위를 돌려줘요")
    if message.content.startswith("!도움 연속주사위"):
        await message.channel.send("주사위를 여러번 굴리고 그 합을 구하는 기능이에요 !주사위 (숫자) 를 입력해주세요")
    if message.content.startswith("!도움 사진"):
        await message.channel.send("서버에 업로드 되어있는 사진을 출력시킬수 있어요 현재 !사진 성공회대.png 만 사용가능 추가진은 추후 업데이트")
    if message.content.startswith("!도움 공지"):
        await message.channel.send("공지사항 채널에 특정 메세지를 업로드 할수 있어요. !공지 (공지할 내용) 남용하면 안되요.")
    if message.content.startswith("!도움 채금"):
        await message.channel.send("특정 멤버가 채널에 글을 쓰는걸 막을 수 있어요. !채금 (해당유저의 아이디) 입력하면 되요.")
    if message.content.startswith("!도움 경고"):
        await message.channel.send("특정 멤버에게 경고를 줄수 있어요. 경고 횟수가 3회 누적되면 해당 유저는 채널에서 밴되요.")
    if message.content.startswith("!도움 팀"):
        await message.channel.send("팀원을 양쪽으로 랜덤으로 나누어줘요. 그리고 포지션도 정해줘요. !(게임이름)팀 으로 쓰면되요.")
    if message.content.startswith("!도움 포지션"):
        await message.channel.send("유저들의 포지션만 나누어줘요, 팀은 나누지 않아요. !(게임이름)포지션으로 쓰면되요.")
    if message.content.startswith("!도움 그냥팀"):
        await message.channel.send("팀원을 양쪽으로 랜덤으로 나누어줘요. 포지션은 나누지 않아요. !(게임이름)그냥팀 으로 쓰면되요.")
    if message.content.startswith("안녕"):
        await message.channel.send("반가워요")
    if message.content.startswith("잘가"):
        await message.channel.send("저도 쉬고싶네요.. 하지만 24시간 대기중")
    if message.content.startswith("하이"):
        await message.channel.send("Hello")
    if message.content.startswith("뭐야"):
        await message.channel.send("안녕하세요 저는 레오 봇이에요")

#강화된 주사위 기능 주사위를 여러분 굴리고, 그 합을 구하는 기능
    if message.content.startswith('!연속주사위'):
        channel = message.channel
        count = message.content[7:]
        dice = random.randint(1, 6)
        sum_dice = 0
        for i in range(1, int(count) + 1):
            dice = random.randint(1, 6)
            sum_dice = sum_dice + dice
            await channel.send(str(i) + "번째 주사위는 " + str(dice) +" 입니다")
            dice = 0
        await channel.send("주사위의 총합은 "+ str(sum_dice)+" 입니다")


    if message.content.startswith('!주사위'):
        channel = message.channel
        dice = random.randint(1, 6)
        await channel.send(str(dice))


    if message.content.startswith("!사진"):
#        pic = message.content.split(" ")[1]
        #띄어쓰기를 넣어서 한칸 띄어서 뒤에있는 내용을 받아오도록 함
        await message.channel.send(file=discord.File('성공회대.png'))
        #여러개의 사진을 이용할시 .File(pic) 으로 변경시 파일이름 직접 입력하여 사용가능, pic 앞에있는 # 제거하여야함
        #  await message.channel.send(file=discord.File(pic))


#공지사항 업로드시 사용
    if message.content.startswith("!공지"):
        channel = 697493383568031864
        msg = message.content[4:]
        await client.get_channel(int(channel)).send(msg)




#        def check(m):
#            return m.content == '응' and m.channel == channel
#        msg = await client.wait_for('message', check=check)
#        await channel.send('다행이네요 {.author}!'.format(msg))
#
#        def check(m):
#            return m.content == '아니' and m.channel == channel
#        msg = await client.wait_for('message', check=check)
#        await channel.send('안타깝네요 {.author}!'.format(msg))


#Mute멤버 - 테스트(나중에 자동적으로 금칙어 사용시 채팅금지 멤버로 진행될예정)
    if message.content.startswith("!채금"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="채팅금지")
        await author.add_roles(role)
        await message.channel.send("해당 멤버가 채팅금지 되었습니다.")


#특정 유저에게 경고를 주고 경고가 누적됬을 시 벤을 하는기능
    if message.content.startswith("!경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 3:
                    await message.guild.ban(author)
                    await message.channel.send("경고 3회 누적입니다. 서버에서 추방됩니다.")
                else:
                    await message.channel.send("경고를 1회 받았습니다.")
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(author.id)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                await message.channel.send("경고를 1회 받았습니다.")
                break
            i += 1


#그냥 팀 나누기
    if message.content.startswith("!팀"):
        team = message.content[3:]
        people = team.split(" ")
        teamname = ['"탑솔"', '"정글"', '"미드"', '"원딜"', '"서폿"']
        random.shuffle(people)
        i = 0
        await message.channel.send("```bash\n"
                                   + " ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n"
                                   + "| " + people[i] +" |    " + teamname[i] +  "    | " + people[i+5] + " | \n"
                                   + "| " + people[i+1] +" |    "+ teamname[i+1] +"    | " + people[i+6] + " | \n"
                                   + "| " + people[i+2] + " |    " + teamname[i+2] + "    | " + people[i+7] + " | \n"
                                   + "| " + people[i+3] + " |    " + teamname[i+3] + "    | " + people[i+8] + " | \n"
                                   + "| " + people[i+4] + " |    " + teamname[i+4] + "    | " + people[i+9] + " | \n"
                                   + " ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n"
                                   + "```")


    if message.content.startswith("!그냥팀"):
        team = message.content[5:]
        people = team.split(" ")
        teamname = ['" 1 ----- 2 "', '" 1 ----- 2 "', '" 1 ----- 2 "', '" 1 ----- 2 "', '" 1 ----- 2 "']
        random.shuffle(people)
        i = 0
        await message.channel.send("```bash\n"
                                   + " ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n"
                                   + "| " + people[i] + " |    " + teamname[i] + "    | " + people[i + 5] + " | \n"
                                   + "| " + people[i + 1] + " |    " + teamname[i + 1] + "    | " + people[
                                       i + 6] + " | \n"
                                   + "| " + people[i + 2] + " |    " + teamname[i + 2] + "    | " + people[
                                       i + 7] + " | \n"
                                   + "| " + people[i + 3] + " |    " + teamname[i + 3] + "    | " + people[
                                       i + 8] + " | \n"
                                   + "| " + people[i + 4] + " |    " + teamname[i + 4] + "    | " + people[
                                       i + 9] + " | \n"
                                   + " ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n"
                                   + "```")

    if message.content.startswith("!포지션"):
        team = message.content[5:]
        people = team.split(" ")
        teamname = ['탑    ', '정글', '미드', '원딜', '서폿']
        random.shuffle(teamname)
        for i in range(0, 5):
            await message.channel.send(people[i] + "  ---->  " + teamname[i])
        for i in range(0, 5):
            await message.channel.send(people[i+5] + "  ---->  " + teamname[i])




#롤 팀나누기
    if message.content.startswith("!롤팀"):
        team = message.content[4:]
        people = team.split(" ")
        teamname = ['"탑솔"', '"정글"', '"미드"', '"원딜"', '"서폿"']
        random.shuffle(people)
        i = 0
        await message.channel.send("```bash\n"
                                   + " ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n"
                                   + "| " + people[i] +" |    " + teamname[i] +  "    | " + people[i+5] + " | \n"
                                   + "| " + people[i+1] +" |    "+ teamname[i+1] +"    | " + people[i+6] + " | \n"
                                   + "| " + people[i+2] + " |    " + teamname[i+2] + "    | " + people[i+7] + " | \n"
                                   + "| " + people[i+3] + " |    " + teamname[i+3] + "    | " + people[i+8] + " | \n"
                                   + "| " + people[i+4] + " |    " + teamname[i+4] + "    | " + people[i+9] + " | \n"
                                   + " ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n"
                                   + "```")


    if message.content.startswith("!롤그냥팀"):
        team = message.content[6:]
        people = team.split(" ")
        teamname = ['" 1 ----- 2 "', '" 1 ----- 2 "', '" 1 ----- 2 "', '" 1 ----- 2 "', '" 1 ----- 2 "']
        random.shuffle(people)
        i = 0
        await message.channel.send("```bash\n"
                                   + " ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n"
                                   + "| " + people[i] + " |    " + teamname[i] + "    | " + people[i + 5] + " | \n"
                                   + "| " + people[i + 1] + " |    " + teamname[i + 1] + "    | " + people[
                                       i + 6] + " | \n"
                                   + "| " + people[i + 2] + " |    " + teamname[i + 2] + "    | " + people[
                                       i + 7] + " | \n"
                                   + "| " + people[i + 3] + " |    " + teamname[i + 3] + "    | " + people[
                                       i + 8] + " | \n"
                                   + "| " + people[i + 4] + " |    " + teamname[i + 4] + "    | " + people[
                                       i + 9] + " | \n"
                                   + " ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n"
                                   + "```")

    if message.content.startswith("!롤포지션"):
        team = message.content[6:]
        people = team.split(" ")
        teamname = ['탑    ', '정글', '미드', '원딜', '서폿']
        random.shuffle(teamname)
        for i in range(0, 5):
            await message.channel.send(people[i] + "  ---->  " + teamname[i])
        for i in range(0, 5):
            await message.channel.send(people[i+5] + "  ---->  " + teamname[i])



#오버워치 포지션

    if message.content.startswith("!오버워치팀"):
        team = message.content[7:]
        people = team.split(" ")
        teamname = ['"딜러"', '"딜러"', '"탱커"', '"탱커"', '"서폿"', '"서폿"']
        random.shuffle(people)
        i = 0
        await message.channel.send("```bash\n"
                                   + " ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n"
                                   + "| " + people[i] +" |    " + teamname[i] +  "    | " + people[i+5] + " | \n"
                                   + "| " + people[i+1] +" |    "+ teamname[i+1] +"    | " + people[i+6] + " | \n"
                                   + "| " + people[i+2] + " |    " + teamname[i+2] + "    | " + people[i+7] + " | \n"
                                   + "| " + people[i+3] + " |    " + teamname[i+3] + "    | " + people[i+8] + " | \n"
                                   + "| " + people[i+4] + " |    " + teamname[i+4] + "    | " + people[i+9] + " | \n"
                                   + "| " + people[i+5] + " |    " + teamname[i+5] + "    | " + people[i+10] + " | \n"
                                   + " ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n"
                                   + "```")

    if message.content.startswith("!오버워치그냥팀"):
        team = message.content[9:]
        people = team.split(" ")
        teamname = ['" 1 ----- 2 "', '" 1 ----- 2 "', '" 1 ----- 2 "', '" 1 ----- 2 "', '" 1 ----- 2 "', '" 1 ----- 2 "']
        random.shuffle(people)
        i = 0
        await message.channel.send("```bash\n"
                                   + " ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n"
                                   + "| " + people[i] + " |    " + teamname[i] + "    | " + people[i + 5] + " | \n"
                                   + "| " + people[i + 1] + " |    " + teamname[i + 1] + "    | " + people[
                                       i + 6] + " | \n"
                                   + "| " + people[i + 2] + " |    " + teamname[i + 2] + "    | " + people[
                                       i + 7] + " | \n"
                                   + "| " + people[i + 3] + " |    " + teamname[i + 3] + "    | " + people[
                                       i + 8] + " | \n"
                                   + "| " + people[i + 4] + " |    " + teamname[i + 4] + "    | " + people[
                                       i + 9] + " | \n"
                                   + "| " + people[i + 5] + " |    " + teamname[i + 5] + "    | " + people[
                                       i + 10] + " | \n"
                                   + " ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n"
                                   + "```")

    if message.content.startswith("!오버워치포지션"):
        team = message.content[9:]
        people = team.split(" ")
        teamname = ['딜러', '딜러', '탱커', '탱커', '서폿', '서폿']
        random.shuffle(teamname)
        for i in range(0, 6):
            await message.channel.send(people[i] + "  ---->  " + teamname[i])
        for i in range(0, 6):
            await message.channel.send(people[i+6] + "  ---->  " + teamname[i])

            
access_token = os.environ["BOT_TOKEN"]            
client.run(access_token)
