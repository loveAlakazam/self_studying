# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 02:38:14 2019

@author: loveAlakazam
"""

from matplotlib import pyplot as plt

years=[  year for year in range(1950,2020,10)]
gdp=[300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# x축에 연도, y축에 gdp가 있는 선 그래프 그리기
#(x축, y축, 선색깔, 마커표시, 라인스타일)
plt.plot(years,gdp, color='green', marker='o', \
         linestyle='solid') 

# 제목 추가
plt.title("Nominal GDP")

# Y축 레이블 추가
plt.ylabel("Billions of $")
plt.show()
