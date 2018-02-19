#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""a test mode"""

import random

__author__ = "74581"


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

