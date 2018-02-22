#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""a test mode"""

import random
from functools import partial
import math
from matplotlib import pyplot as plt

__author__ = "74581"

plt.rcParams['font.sans-serif'] = ['Simhei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 梯度下降的思想

def sum_of_squares(v):
    """computes the sum of squared elements in v"""
    return sum(v_i ** 2 for v_i in v)


# 估算梯度

def difference_quotient(f, x, h):
    return (f(x + h) - f(x)) / h


def square(x):
    return x * x


def derivative(x):
    return 2 * x


derivative_estimate = partial(difference_quotient, square, h=0.00001)


# 绘出导入matplotlib.pyplot作为plt的基本相同的形态
# xs = range(-10, 10)
# plt.title("精确的导数值与估计值")
# """
# map(derivative, xs)报错：
# AttributeError: 'numpy.ndarray' object has no attribute 'mask'
#
# 原因：
# map()在python3中返回generator而不是list
#
# 解决办法：
# list(map())
# """
# plt.plot(xs, list(map(derivative, xs)), 'rx', label='Actual')
# plt.plot(xs, list(map(derivative_estimate, xs)), 'b+', label='Estimate')
# plt.legend(loc=9)
# plt.show()


# f为多变量函数时，其他变量保持不便，计算第i个偏导数
def partial_difference_quotient(f, v, i, h):
    """compute the ith partial difference quotient of f at v"""
    w = [v_j + (h if j == i else 0)  # 只对v的第i个元素增加h
         for j, v_j in enumerate(v)]

    return (f(w) - f(v)) / h


# “差商估算法”的缺点是计算代价大
def estimate_gradient(f, v, h=0.00001):
    return [partial_difference_quotient(f, v, i, h)
            for i, _ in enumerate(v)]


# 使用梯度

def step(v, direction, step_size):
    """move step_size in the direction from v"""
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]


def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]


# 选取随机初始值
v = [random.randint(-10, 10) for i in range(3)]

tolerance = 0.0000001


def distance(v, w):
    return math.sqrt(sum((v_i - w_i) ** 2 for v_i, w_i in zip(v, w)))


while True:
    gradient = sum_of_squares_gradient(v)  # 计算v的梯度
    next_v = step(v, gradient, -0.01)  # 取负的梯度步长
    if distance(next_v, v) < tolerance:  # 如果收敛了就停止
        break
    v = next_v  # 如果没汇合就继续

# 选择正确步长

step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]


def safe(f):
    """return a new function that's the same as f,
    except that it outputs infinity whenever f produces an error"""

    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except TypeError:
            return float('inf')

    return safe_f
