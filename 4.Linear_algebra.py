#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

from functools import partial, reduce
import math

__author__ = '74581'

# plt.rcParams['font.sans-serif'] = ['Simhei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 向量

height_weight_age = [70,  # 英寸
                     170,  # 磅
                     40]  # 岁
grades = [95,  # 考试1
          80,  # 考试2
          75,  # 考试3
          62]  # 考试4


def vector_add(v, w):
    """adds corresponding elements"""
    return [v_i + w_i
            for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [v_i - w_i
            for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    """sums all corresponding elements"""
    result = vectors[0]  # 从第一个向量开始
    for vector in vectors[1:]:  # 之后遍历其他向量
        result = vector_add(result, vector)  # 最后计入总和
    return result


def vector_sum(vectors):
    return reduce(vector_add, vectors)


vector_sum = partial(reduce, vector_add)


def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]


def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the ith elements of the input vectors"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    return sum(v_i * w_i
               for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


def magnitude(v):
    return math.sqrt(sum_of_squares(v))  # math.sqrt是平方根函数


def squared_distance(v, w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2"""
    return sum_of_squares(vector_subtract(v, w))


def distance(v, w):
    return math.sqrt(squared_distance(v, w))


def distance(v, w):
    return magnitude(vector_subtract(v, w))


# 矩阵

A = [[1, 2, 3],  # A有2行3列
     [4, 5, 6]]
B = [[1, 2],  # B有3行2列
     [3, 4],
     [5, 6]]


def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # 第一行中元素的个数
    return num_rows, num_cols


def get_row(A, i):
    return A[i]  # A[i]是第i行


def get_column(A, j):
    return [A_i[j]  # 第A_i行的第j 个元素
            for A_i in A]  # 对每个A_i行


def make_matrix(num_rows, num_cols, entry_fn):
    """return a num_rows x num_cols matrix
    whose (i, j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)  # 根据i创建一个列表
             for j in range(num_cols)]  # [entry_fn(i, 0), ...]
            for i in range(num_rows)]  # 为每一个i创建一个列表


def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0


identity_matrix = make_matrix(5, 5, is_diagonal)
