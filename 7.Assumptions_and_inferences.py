#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""a test mode"""

import math
import random

__author__ = "74581"


# 统计假设检验

# 案例：掷硬币

def normal_approximation_to_binomial(n, p):
    """finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


def normal_cdf(x, mu=0.0, sigma=1.0):  # 用到的第六章函数
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


# 正态cdf是一个变量在一个阈值以下的概率
normal_probability_below = normal_cdf


# 如果它不在阈值以下，就在阈值以上
def normal_probability_above(lo, mu=0.0, sigma=1.0):
    return 1 - normal_cdf(lo, mu, sigma)


# 如果它小于hi但不必lo小，那么它在区间之内
def normal_probability_between(lo, hi, mu=0.0, sigma=1.0):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


# 如果不在区间之内，那么就在区间之外
def normal_probability_outside(lo, hi, mu=0.0, sigma=1.0):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def inverse_normal_cdf(p, mu=0.0, sigma=1.0, tolerance=0.00001):  # 用到的第六章函数
    """find approximate inverse using binary search"""
    # 如果非标准型，先调整单位使之服从标准型
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0, 0  # normal_cdf(-10)是(非常接近)0
    hi_z, hi_p = 10.0, 1  # normal_cdf(10)是(非常接近)1
    mid_z = (low_z + hi_z) / 2
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


def normal_upper_bound(probability, mu=0.0, sigma=1.0):
    """return the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability, mu=0.0, sigma=1.0):
    """return the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bound(probability, mu=0.0, sigma=1.0):
    """return the symmetric (about the mean) bounds
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2

    # 上界应有在它之上的tail_probability
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # 下界应有在它之下的tail_probability
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound


mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

normal_two_sided_bound(0.95, mu_0, sigma_0)  # ~(469, 531)

# 基于假设p是0.5时95%的边界
lo, hi = normal_two_sided_bound(0.95, mu_0, sigma_0)

# 基于p = 0.55的真实mu和sigma
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# 第2类错误意味着我们没有拒绝原假设
# 这会在x仍然在最初的区间时发生
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability  # 0.887

hi = normal_upper_bound(0.95, mu_0, sigma_0)  # 是526（<531，因为我们在上尾需要更多的概率）
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability  # 0.936


# 另一种检验方式
def two_sided_p_value(x, mu=0.0, sigma=1.0):
    if x >= mu:
        # 如果x大于均值，tail表示比x大多少
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # 如果x比均值小，tail表示比x小多少
        return 2 * normal_probability_below(x, mu, sigma)


two_sided_p_value(529.5, mu_0, sigma_0)  # 530次正面朝上~0.062

# 验证模拟
extreme_value_count = 0
for _ in range(100000):
    num_heads = sum(1 if random.random() < 0.5 else 0  # 正面朝上的计数
                    for _ in range(1000))  # 在1000次抛掷中
    if num_heads >= 530 or num_heads <= 470:  # 并计算达到极值的概率
        extreme_value_count += 1  # 极值的频率
print(extreme_value_count / 100000)  # 0.062 > 5%

two_sided_p_value(531.5, mu_0, sigma_0)  # 532次正面朝上，相应的p值为0.0463 < 5%

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

upper_p_value(524.5, mu_0, sigma_0)  # 0.061
upper_p_value(526.5, mu_0, sigma_0)  # 0.047
# 计算p值前需要确定数据大致上服从正态分布，可以用绘图进行检验

# 置信区间

p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt((p_hat * (1 - p_hat) / 1000))  # 0.0158
normal_two_sided_bound(0.95, mu, sigma)  # [0.4940, 0.5560]在置信区间内

p_hat = 540 / 1000
mu = p_hat
sigma = math.sqrt((p_hat * (1 - p_hat) / 1000))  # 0.0158
normal_two_sided_bound(0.95, mu, sigma)  # [0.5091, 0.5709]在置信区间外


# P-hacking

def run_experiment():
    """flip a fair coin 1000 times, True = heads, False = tails"""
    return [random.random() < 0.5 for _ in range(1000)]


def reject_fairness(experiment):
    """using the 5% significance levels"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531


random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment
                      for experiment in experiments
                      if reject_fairness(experiment)])
print(num_rejections)  # 46
# p值不应该靠直觉得出，替代方案有下文的“贝叶斯推断”
