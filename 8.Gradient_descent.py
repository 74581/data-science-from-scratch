#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""a test mode"""

from functools import partial
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
xs = range(-10, 10)
plt.title("精确的导数值与估计值")
plt.plot(xs, [2 * x for x in xs], 'rx', label='Actual')  # 用 x 表示
plt.plot(xs, [difference_quotient(square, y, 0.00001) for y in xs], 'b+', label='Estimate')  # 用 + 表示
plt.legend(loc=9)
plt.show()
