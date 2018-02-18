#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

from matplotlib import pyplot as plt
from collections import Counter

__author__ = '74581'

plt.rcParams['font.sans-serif'] = ['Simhei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# matplotlib

# years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
# gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
# # 创建一幅线图，x轴是年份，y轴是gdp
# plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
# # 添加一个标题
# plt.title("GDP")
# # 给y轴加标记
# plt.ylabel("Billion dollars")
# plt.show()

# 条形图

# movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
# num_oscars = [5, 11, 3, 8, 10]
# xs = [i for i, _ in enumerate(movies)]
# # 使用左侧x坐标[xs]和高度[num_oscars]画条形图
# plt.bar(xs, num_oscars)
# plt.ylabel("The Academy Awards received")
# plt.title("My Favorite Movies")
# # 使用电影的名字标记x轴，位置在x轴上条形的中心
# plt.xticks([i for i, _ in enumerate(movies)], movies)
# plt.show()

# grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
#
#
# def decile(grade):
#     return grade // 10 * 10
#
#
# histogram = Counter(decile(grade) for grade in grades)
# plt.bar([x for x in histogram.keys()], histogram.values(), 8)  # 每个条形的宽度设置为8
# plt.axis([-5, 105, 0, 5])  # x轴取值从-5到105，y轴取值0到5
# plt.xticks([10 * i for i in range(11)])  # x轴标记为0,10,...,100
# plt.xlabel("10 range")
# plt.ylabel("Number of students")
# plt.title("Examination score distribution")
# plt.show()

# mentions = [500, 505]
# years = [2013, 2014]
# plt.bar(years, mentions, 0.8)
# plt.xticks(years)
# plt.ylabel("Numbers")
# plt.axis([2012.5, 2014.5, 0, 550])
# plt.title("Not huge increasing!")
# plt.show()

# 线图

# variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
# bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
# total_error = [x + y for x, y in zip(variance, bias_squared)]
# xs = [i for i, _ in enumerate(variance)]
# # 可以多次调用plt.plot以便在同一个图上显示多个序列
# plt.plot(xs, variance, 'g-', label='variance')  # 绿色实线
# plt.plot(xs, bias_squared, 'r-.', label='bias^2')  # 红色点虚线
# plt.plot(xs, total_error, 'b:', label='total error')  # 蓝色点线
# # 因为已经对每个序列都指派了标记所以可以自由地布置图例，loc=9指的是“顶部中央”
# plt.legend(loc=9)
# plt.xlabel("模型复杂度")
# plt.title("偏差-方差权衡图")
# plt.show()

# 散点图

# friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
# minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# plt.scatter(friends, minutes)
# # 每个点加标记
# for label, friend_count, minute_count in zip(labels, friends, minutes):
#     plt.annotate(label,
#                  xy=(friend_count, minute_count),  # 把标记放在对应的点上，但要有轻微偏移
#                  xytext=(5, -5),
#                  textcoords='offset points')
# plt.title("日分钟数与朋友数")
# plt.xlabel("朋友数")
# plt.ylabel("花在网站上的日分钟数")
# plt.show()

test_1_grades = [99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]
plt.scatter(test_1_grades, test_2_grades)
plt.title("可比较的轴")  # xy刻度便于比较
plt.xlabel("测试1的分数")
plt.ylabel("测试2的分数")
plt.axis("equal")
plt.show()
