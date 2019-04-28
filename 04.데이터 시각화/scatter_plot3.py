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
plt.title("The Axes are comparable")

# x, y 축 시작점을 같게한다.
# test2에서 대부분의 편차가 발생했다는 사실을 알 수 있다.
plt.axis('equal')

plt.xlabel("test 1 grades")
plt.ylabel("test 2 grades")
plt.show()
