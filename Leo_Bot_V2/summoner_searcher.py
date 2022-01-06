#!/usr/bin/env python
# coding: utf-8

# In[65]:


import requests
from bs4 import BeautifulSoup
import re


# In[58]:


# OP.GG 를 크롤링하여 솔로랭크와, 자유랭크 점수를 가져옴
def searching_op_gg(summoner_name):
    
    try:
        # 결과를 담을 변수
        result_score = 0
        # 헤더 추가 필요(op.gg 의 경우 requests를 막아둠)
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
        # 아이디가 입력되면 op.gg에 입력하여 검색
        test = requests.get('https://www.op.gg/summoner/userName='+summoner_name, headers=header).text

        # 티어가 있는 CSS 선택자를 가져와서 공백문자 제거
        soup = BeautifulSoup(test, 'html.parser')
        solo_rank_tier = soup.select_one('.TierRank').text.strip()
        team_rank_tier = soup.select_one('.sub-tier__rank-tier').text.strip()
        
        # 솔로랭크와 자유랭크 티어를 수치화
        # 솔로랭크의 경우 1티어 정도의 가산점을 더함
        solo_int = tier_2_int(solo_rank_tier) + 5
        team_int = tier_2_int(team_rank_tier)
        
        # 결과값 반환
        result_score = result_score + solo_int
        result_score = result_score + team_int
            
        return [summoner_name, result_score]
        
    except Exception as e:
        
        print("OP.GG 크롤링 에러발생, 아이디를 확인해주세요 :"+str(e))
        return 0


# In[89]:


# 티어를 int 로 변환하는 함수
def tier_2_int(rank_name_str):

    result = 0

    unranked = re.findall("Unranked", rank_name_str)
    iron = re.findall("Iron (\d)", rank_name_str)
    bronze = re.findall("Bronze (\d)", rank_name_str)
    silver = re.findall("Silver (\d)", rank_name_str)
    gold = re.findall("Gold (\d)", rank_name_str)
    platinum = re.findall("Platinum (\d)", rank_name_str)    
    diamond = re.findall("Diamond (\d)", rank_name_str)
    master = re.findall("Master", rank_name_str)
    grandmaster = re.findall("Grandmaster", rank_name_str)
    challenger = re.findall("Challenger", rank_name_str)

    if unranked != []:
        result = result + 5

    if iron != []:
        temp = 5 - int(iron[0])
        result = result + temp

    if bronze != []:
        temp = 5 - int(bronze[0])
        result = result + temp + 5

    if silver != []:
        temp = 5 - int(silver[0])
        result = result + temp + 10

    if gold != []:
        temp = 5 - int(gold[0])
        result = result + temp + 15

    if platinum != []:
        temp = 5 - int(platinum[0])
        result = result + temp + 20

    if diamond != []:
        temp = 5 - int(diamond[0])
        result = result + temp + 25

    if master != []:
        result = result + 30

    if grandmaster != []:
        result = result + 35

    if challenger != []:
        result = result + 40

    return result


# In[ ]:




