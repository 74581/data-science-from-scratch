#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

import csv
import re
from collections import Counter

__author__ = '74581'

# stdin和stdout

"""
三个脚本
egrep.py
line_count.py
most_common_words.py
"""

# 读取文件

# 文本文件基础
"""
'r'意味着只读
file_for_reading = open('reading_file.txt', 'r')

'w'是写入——会破环已存在的文件！
file_for_writing = open('writing_file.txt', 'w')

'a'是添加——加入到文件的末尾
file_for_appending = open('appending_file.txt', 'a')

完成以后别忘了关闭文件
file_for_writing.close()
"""

# 容易忘记关闭文件，应在with程序块里操作，结尾处文件会被自动关闭
"""
with open(filename, 'r') as f:
    data = function_that_gets_data_from(f)

#此时，f已经关闭了，别再试图使用它
process(data)
"""

# 读取完整文本文件，用for语句对文件的行进行迭代
"""
starts_with_hash = 0

with open('input.txt', 'r') as f:
    for line in f:  # 查找文件中的每一行
        if re.match("^#", line):  # 用正则表达式判断它是否以‘#’开头
            starts_with_hash += 1  # 如果是，技术加1
"""


# 正确提取邮件域名的规则有点微妙，近似方案是只取出@后面的部分
# 但joel@mail.datasciencester.com这样的邮件地址，会给出错误答案
def get_domain(email_address):
    """split on '@' and return the last piece"""
    return email_address.lower().split("@")[-1]


"""
with open('email_address.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f
                            if "@" in line)
"""

# 限制的文件
# 文件通常用,分割或者tab分割，以及带有换行符，应使用csv模块或者pandas库
# 因为微软的原因，应用‘rb’，‘wb’的形式用二进制模式处理csv文件
"""
如果文件没有头部，可用csv.reader对每行进行迭代，如：
6/20/2014   AAPL    90.91
6/20/2014   MSFR    41.68
6/20/2014   FB  64.5
6/19/2014   AAPL    91.86
6/19/2014   MSFT    41.51
6/19/2014   FB  64.34

with open('tab_delimited_stock_price.txt', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[0]
        closing_price = float(row[2])
        process(date, symbol, closing_price)
"""

"""
如果文件存在头部：
date:symbol:closing_price
6/20/2014:AAPL:90.91
6/20/2014:MSFR:41.68
6/20/2014:FB:64.5

# 可以跳过头部行（利用read.next()的初始调用），也可以利用csv.DictReader把每行读成字典
with open('colon_delimited_stock_price.txt', 'rb') as f:
    reader = csv.DictReader(f, delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        process(date, symbol, closing_price)

# 即使文件缺少头文件，仍可以通过把关键字作为文件名参数传输来使用DictReader
"""
"""
# 用csv.writer来写限制文件
today_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}

with open('comma_delimited_stock_prices.txt', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])
"""
