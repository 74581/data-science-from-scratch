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
"""
map(derivative, xs)报错：
AttributeError: 'numpy.ndarray' object has no attribute 'mask'

原因：
map()在python3中返回generator而不是list

解决办法：
list(map())
"""
plt.plot(xs, list(map(derivative, xs)), 'rx', label='Actual')
plt.plot(xs, list(map(derivative_estimate, xs)), 'b+', label='Estimate')
plt.legend(loc=9)
plt.show()
