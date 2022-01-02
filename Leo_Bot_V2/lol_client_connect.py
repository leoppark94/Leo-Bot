import lcu_driver
import re
import summoner_searcher as SS
import team_spliter as TS




connector = lcu_driver.Connector()


# fired when LCU API is ready to be used
@connector.ready
async def connect(connection):
    print('LCU API is ready to be used.')

# fired when League Client is closed (or disconnected from websocket)
@connector.close
async def disconnect(_):
    print('The client have been closed!')
    await connector.stop()

# '/lol-lobby/v2/lobby/members' can access who entered in lobby
@connector.ws.register('/lol-lobby/v2/lobby/members')
async def player_score(connection, event):
    # 반환되는 내용 그 자체 내용
    raw_data_lobby = str(event.data)
    summoner_list = re.findall("'isSpectator': False.*?summonerInternalName': '(.*?)'", raw_data_lobby)
    # summoner_name
    print(raw_data_lobby)
    print(summoner_list)
    if len(summoner_list) == 10:
        player_score = []
        for summoner_name in summoner_list:
            # op.gg 에 아이디를 검색한 뒤 해당 아이디의 점수를 추출
            player_score.append(SS.searching_op_gg(summoner_name))

        team_result, team_gap = TS.team_spliter(player_score)
        print("-------------")
        print("1팀")
        print(team_result[0:5])
        print("-------------")
        print("2팀")
        print(team_result[5:])
        print("-------------")
        print("점수차이 : ", team_gap)

# starts the connector
connector.start()
