# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:44:09 2019

@author: loveAlakazam
"""

from matplotlib import pyplot as plt
variance=[(2**i) for i in range(9)]
bias_squared=[(2**i) for i in range(8,-1,-1)]
#print(variance)
#print(bias_squared)

total_error= [ x+y for x, y in zip(variance,bias_squared)]
xs=[i for i, _ in enumerate(variance)]

# 한 차트에 여러개의 series를 그리기 위해
# plt.plot을 여러번 호출할 수 있다.
plt.plot(xs, variance, 'g-', label='variance' ) #초록색 실선
plt.plot(xs, bias_squared, 'r-.', label='bias^2') #붉은색 점선
plt.plot(xs, total_error, 'b:', label='total error') #파란색 점선

# 각 series에 label을 미리 달아 놨기 때문에 
# 범례(legend)는 어렵지 않게 그릴 수 있다.
# 여기서 loc=9는 "top center(위쪽 중앙)"을 의미한다.
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()