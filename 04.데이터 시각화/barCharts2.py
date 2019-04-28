# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 03:04:28 2019

@author: loveAlakazam
"""
from matplotlib import pyplot as plt
import random
from collections import Counter

# 0~100사이의 수를 랜덤
n=10 #people

# n명의 사람들 점수표(귀찮아서 랜덤으로함)
grades=[ random.randrange(0,101) for i in range(n+1)]
print(grades)

#lambda함수를 이용하여 사용자 정의 함수 decile 를 정의
decile = lambda grade : grade //10*10

# 히스토그램
# grades=[56, 87, 33 ] 이라 가정하면
# 1) grade = 56 ==> decile(56) = (56//10) * 10 = 50
# 2) grade = 87 ==> decile(87) = (87//10) * 10 = 80
# 3) grade = 33 ==> decile(33) = (33//10) * 10 = 30
# Counter(decile(grade) for grade in grades) = ({80: 1, 50:1, 30: 1 }) 을 출력
histogram = Counter(decile(grade) for grade in grades)
plt.bar([ x for x in histogram.keys()], #막대 표시
         histogram.values(), #각 막대의 높이를 정한다.
         8) #너비 8
plt.axis([-5, 105, 0, n]) #x축은 -5부터 105, y축은 0부터 n

plt.xticks([10*i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")

plt.title("Distribution of Exam 1 Grades")
plt.show()
