#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

import math
import random
from collections import Counter

from matplotlib import pyplot as plt

__author__ = '74581'

plt.rcParams['font.sans-serif'] = ['Simhei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 探索你的数据

# 探索一维数据
def bucketize(point, bucket_size):
    """floor the point to the next lower multiple of bucket_size"""
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points, bucket_size):
    """buckets the points and counts how many in each bucket"""
    return Counter(bucketize(point, bucket_size) for point in points)


def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()


random.seed(0)

# -100到100之间均匀抽取
uniform = [200 * random.random() - 100 for _ in range(10000)]


def normal_cdf(x, mu=0, sigma=1.0):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""
    # 如果非标准型，先调整单位使之服从标准型
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0, 0  # normal_cdf(-10)是(非常接近)0
    hi_z, hi_p = 10.0, 1  # normal_cdf(10)是(非常接近)1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # 考虑中点
        mid_p = normal_cdf(mid_z)  # 和cdf在那里的值
        if mid_p < p:
            # midpoint仍然太低，搜索比它大的值
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint仍然太高，搜索比它小的值
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z


# 均值为0标准差为57的正态分布
normal = [57 * inverse_normal_cdf(random.random())  # 使用第六章的两个函数
          for _ in range(10000)]

plot_histogram(uniform, 10, "均匀分布的直方图")
plot_histogram(normal, 10, "正态分布的直方图")
