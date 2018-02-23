#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

# line_count.py
import sys

__author__ = '74581'

# 9/stdin和stdout

count = 0
for line in sys.stdin:
    count += 1

# 输出去向 sys.stdout
print(count)

# "|"运算符是管道字符，意思是“使用左边命令的输出作为右边命令的输入”
# type SomeFile.txt | python egrep.py "[0-9]" | python line_count.py
# type SomeFile.txt | egrep.py "[0-9]" | line_count.py
