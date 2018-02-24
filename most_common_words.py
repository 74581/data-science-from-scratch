#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

# most_common_words.py
import sys
from collections import Counter

__author__ = '74581'

# 9/stdin和stdout

# 传递单词的个数作为第一个参数
try:
    num_words = int(sys.argv[1])
except TypeError:
    print("usage: most_common_words.py num_words")
    sys.exit(1)  # 非零的exit代码表明有错误

counter = Counter(word.lower()
                  for line in sys.stdin  # 小写的单词
                  for word in line.strip().split()  # 用空格划分
                  if word)  # 跳过空的‘words’

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")

# type the_bible.txt | python most_common_words.py 10
