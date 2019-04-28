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

# n명의 사람들 점수표
grades=[ random.randrange(0,101) for i in range(n+1)]
print(grades)

decile = lambda grade : grade //10*10
histogram = Counter(decile(grade) for grade in grades)
plt.bar([ x for x in histogram.keys()], #막대 표시
         histogram.values(), #각 막대의 높이를 정한다.
         8) #너비 8
plt.axis([-5, 105, 0, 5]) #x축은 -5부터 105, y축은 0부터 5

plt.xticks([10*i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("# of Students")

plt.title("Distribution of Exam 1 Grades")
plt.show()
