#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

import math
from collections import Counter

__author__ = '74581'


# 模型

# 最简单的预测模型之一
# 要求：1.某种距离概念；2.接近的点具有相似性质假设
# 其他技术把数据看作整体以学习数据中的模式
# 最近邻法有意忽略大量信息，对每个新数据点预测只依赖少量最接近它的点
# 最近邻法不能帮助理解任意现象的驱动机制
def raw_majority_vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner


def majority_vote(labels):
    """assumes that labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])
    if num_winners == 1:
        return winner  # 唯一的获胜者，返回它的值
    else:
        return majority_vote(labels[:-1])  # 去掉最远的元素，再次尝试


def distance(v, w):
    return math.sqrt(sum((v_i - w_i) ** 2 for v_i, w_i in zip(v, w)))


def knn_classify(k, labeled_points, new_point):
    """each labeled point should be a pair (point, label)"""

    # 把标记好的点按从最近到最远的顺序排序
    by_distance = sorted(labeled_points,
                         key=lambda point_x: distance(point_x[0], new_point))

    # 寻找k个最近邻的标签
    k_nearest_labels = [label for _, label in by_distance[:k]]

    # 然后让它们投票
    return majority_vote(k_nearest_labels)
