#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""a test mode"""

import random
import math
from collections import Counter

from matplotlib import pyplot as plt

__author__ = "74581"

plt.rcParams['font.sans-serif'] = ['Simhei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 不独立和独立

# 条件概率
def random_kid():
    return random.choice(["boy", "girl"])


both_girls = 0
older_girls = 0
either_girls = 0

random.seed(0)
for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girls += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girls += 1
print("P(both | older):", both_girls / older_girls)  # ~ 1/2
print("P(both | either):", both_girls / either_girls)  # ~ 1/3


# 贝叶斯定理

# P(E|F)=P(E,F)/P(F)=P(F|E)P(E)/P(F)
# P(F)=P(F,E)+P(F,~E) # ~等于非
# P(E|F)=P(E,F)/P(F)=P(F|E)P(E)/[P(F|E)P(E)+P(F|~E)P(~E)]

# 随机变量

# 连续分布

# 均匀分布的密度函数
def uniform_pdf(x):  # 概率密度函数(probability density function, pdf)
    return 1 if 0 <= x < 1 else 0


# 均匀分布的累积分布函数
def uniform_cdf(x):  # 累计分布函数(cumulative distribution function, cdf)
    """returns the probability that a uniform random variable is <= x"""
    if x < 0:
        return 0  # 均匀分布的随机变量不会小于0
    elif x < 1:
        return x  # e.g. P(X <= 0.4) = 0.4
    else:
        return 1  # 均匀分布的随机变量总是小于1


# 正态分布

def normal_pdf(x, mu=0, sigma=1.0):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma)


# xs = [x / 10.0 for x in range(-50, 50)]
# plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
# plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
# plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
# plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')
# plt.legend()
# plt.title("多个正态分布的概率密度函数")
# # plt.show()

def normal_cdf(x, mu=0, sigma=1.0):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


# xs = [x / 10.0 for x in range(-50, 50)]
# plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
# plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
# plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
# plt.plot(xs, [normal_cdf(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')
# plt.legend(loc=4)  # 底部右边
# plt.title("多个正态分布的累积分布函数")
# plt.show()


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


# 中心极限定理

def bernoulli_trial(p):
    return 1 if random.random() < p else 0


def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))


def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]

    # 用条形图绘出实际的二项式样本
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')

    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # 用线型图绘出正态近似
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
          for i in xs]
    plt.plot(xs, ys)
    plt.title("二项分布与正态近似")
    plt.show()


make_hist(0.75, 100, 10000)
