# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 16:51:24 2019

@author: loveAlakazam
"""
import random
from matplotlib import pyplot as plt

# n: the number of students
n=5
 
test_1_grades= [ random.randrange(0,100) for i in range(n)]
test_2_grades= [ random.randrange(0,100) for i in range(n)]


# x축: test_1_grades, y축: test_2_grades
plt.scatter(test_1_grades, test_2_grades)
plt.title("Axes aren't comparable") #공정한 비교 불가
plt.xticks([i*10 for i in range(11)])
plt.yticks([i*10 for i in range(11)])
plt.xlabel("test 1 grades")
plt.ylabel("test 2 grades")
plt.show()
