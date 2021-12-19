#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[6]:


# 10명의 점수와 아이디가 담겨있는 리스트가 들어가야함
def team_spliter(test_data):
    temp_result = []
    team_gap = 500
    for i in range(10):
        random.shuffle(test_data)
        team_1 = test_data[0:5]
        team_2 = test_data[5:10]

        team_1_total = 0
        team_2_total = 0

        for team_1_member in team_1:
            team_1_total = team_1_total + team_1_member[1]

        for team_2_member in team_2:
            team_2_total = team_2_total + team_2_member[1]

        temp_team_gap = abs(team_1_total - team_2_total)

        if team_gap > temp_team_gap:
            team_gap = temp_team_gap
            temp_result = test_data
            
        return temp_result, team_gap

