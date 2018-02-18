#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

from __future__ import division
from collections import Counter
from matplotlib import pyplot as plt
import random
import math

__author__ = '74581'

plt.rcParams['font.sans-serif'] = ['Simhei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 描述单个数据集

num_friends = [int(random.random() * 100 % 100)
               for i in range(250)]
friend_counts = Counter(num_friends)
xs = range(101)  # 最大值是100
ys = [friend_counts[x] for x in xs]  # height刚好是朋友的个数
plt.bar(xs, ys)
plt.axis([0, 101, 0, 10])
plt.title("朋友数的直方图")
plt.xlabel("朋友个数")
plt.ylabel("人数")
# plt.show()

num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]


# 中心倾向
# 如果没有从__future__导入division，那就是不对的
def mean(x):
    return sum(x) / len(x)


mean(num_friends)


def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        # 如果是奇数，返回中间值
        return sorted_v[midpoint]
    else:
        # 如果是偶数，返回中间两个值的均值
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


median(num_friends)


def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]


quantile(num_friends, 0.10)
quantile(num_friends, 0.25)
quantile(num_friends, 0.75)
quantile(num_friends, 0.90)


def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
            if count == max_count]


mode(num_friends)


# 离散度
# "range"在Python中已经有特定的含义，所以我们换一个不同的名字
def data_range(x):
    return max(x) - min(x)


data_range(num_friends)


def squares_of_de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [(x_i - x_bar) ** 2 for x_i in x]


def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = squares_of_de_mean(x)
    return sum(deviations) / (n - 1)


variance(num_friends)


def standard_deviation(x):
    return math.sqrt(variance(x))


standard_deviation(num_friends)


def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


interquartile_range(num_friends)


# 相关

def covariance(x, y):
    n = len(x)
    de_mean_x = [x_i - mean(x) for x_i in x]
    de_mean_y = [y_i - mean(y) for y_i in y]
    return sum(x_i * y_i
               for x_i, y_i in zip(de_mean_x, de_mean_y)) / (n - 1)


daily_minutes = []


# covariance(num_friends, daily_minutes)


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0  # 如果没有变动，相关系数为零


# correlation(num_friends, daily_minutes)
outlier = num_friends.index(50)  # outlier的索引，为除去异常值
num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]
daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]
# correlation(num_friends_good, daily_minutes_good)

# 辛普森悖论

# 相关系数其他注意事项

x = [-2, -1, 0, 1, 2]
y = [2, 1, 0, 1, 2]
print(correlation(x, y))  # 0.0
x = [-2, 1, 0, 1, 2]
y = [99.98, 99.99, 100, 100.01, 100.02]
print(correlation(x, y))  # 0.834...

# 相关和因果
