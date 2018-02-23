#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

# egrep.py
import sys, re

__author__ = '74581'

# 9/stdin和stdout

# sys.argv是命令行参数的列表
# sys.argv[0]是程序自己的名字
# sys.argv[1]会是在命令行上指定的正则表达式
regex = sys.argv[1]

# 对传递到这个脚本中的每一个行
for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)
