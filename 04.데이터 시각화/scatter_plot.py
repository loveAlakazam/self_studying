# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:08:22 2019

@author: loveAlakazam
"""
from matplotlib import pyplot as plt
import random

# n: uesr_num 
n=9

# 사용자의 친구 수
friends=[ random.randrange(10,100) for i in range(n)]

# 매일 사이트에서 체류하는 시간
times=[ random.randrange(100,200) for i in range(n)]

# 각 포인트 라벨
labels=[chr(i) for i in range(97,97+n)]

#x축: friends,  y축: times 
plt.scatter(friends, times)

#각 포인트에 라벨을 단다.
for label, friends_cnt, times_cnt in zip(labels, friends, times):
    plt.annotate(label,
                 xy=(friends_cnt, times_cnt),   #라벨을 데이터 포인트 근처에 둔다.
                 xytext=(5, -5),                # 약간 떨어져있게한다. 
                 textcoords='offset points')
plt.title('Daily Minutes vs, Number of Friends')
plt.xlabel('# of friends')
plt.ylabel('daily minutes spent on the site')
plt.show()
