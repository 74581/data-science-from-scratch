#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""
from __future__ import division
import re
import re as regex
from collections import defaultdict, Counter
import random
from functools import partial, reduce

__author__ = '74581'

# 空白形式

for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
    print(i)
    print("done looping")
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]
two_plus_three = 2 + \
                 3

# 模块

my_regx = re.compile("[0-9]+", re.I)
my_regx = regex.compile("[0-9]+", regex.I)
lookup = defaultdict(int)
my_counter = Counter()


# 函数

def double(x):
    """this is where you put an optional docstring
    that explains what the function does.
    for example, this function multiplies its input by 2"""
    return x * 2


def apply_to_one(f):
    """calls the function f with 1 as its argument"""
    return f(1)


my_double = double
x = apply_to_one(my_double)
print(x)  # 等于2
y = apply_to_one(lambda x: x + 4)
print(y)  # 等于5


def my_print(message="my default message"):
    print(message)


my_print("hello")  # 打印"hello"
my_print()  # 打印"my default message"


def subtract(a=0, b=0):
    return a - b


subtract(10, 5)  # 返回5
subtract(0, 5)  # 返回-5
subtract(b=5)  # 和前一句一样

# 字符串

single_quoted_string = 'data science'
double_quoted_string = "data science"
tab_string = "\t"  # 表示tab字符
len(tab_string)  # 是1
not_tab_string = r"\t"  # 表示字符'\'和't'
len(not_tab_string)  # 是2
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""
print(multi_line_string)

# 异常

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

# 列表

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists_second = [integer_list, heterogeneous_list, []]
list_length = len(integer_list)  # 等于3
list_sum = sum(integer_list)  # 等于6
x = range(10)  # 是列表[0, 1, ..., 9]
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zero = x[0]  # 等于0，列表是0-索引的
one = x[1]  # 等于1
nine = x[-1]  # 等于9，最后一个元素的Python惯用法
eight = x[-2]  # 等于8，倒是第二个元素的Python惯用法
x[0] = -1  # 现在是[-1, 1, 2, 3, ..., 9]
first_three = x[:3]  # [-1, 1, 2]
three_to_end = x[3:]  # [3, 4, ..., 9]
one_to_four = x[1:5]  # [1, 2, 3, 4]
last_three = x[-3:]  # [7, 8, 9]
without_first_and_last = x[1:-1]  # [1, 2, ..., 8]
copy_of_x = x[:]  # [-1, 1, 2, ..., 9]
print(1 in [1, 2, 3])  # True
print(0 in [1, 2, 3])  # False
x = [1, 2, 3]
x.extend([4, 5, 6])  # x现在是[1, 2, 3, 4, 5, 6]
x = [1, 2, 3]
y = x + [4, 5, 6]  # y是[1, 2, 3, 4, 5, 6];x是不变的
x.append(0)  # x现在是[1, 2, 3, 0]
y = x[-1]  # 等于0
z = len(x)  # 等于4
x, y = [1, 2]  # 现在x是1，y是2
_, y = [1, 2]  # 现在y==2，不用关心第一个元素是什么

# 元组

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3  # my_list现在是[1, 3]
try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")


def sum_and_product(x, y):
    return (x + y), (x * y)


sp = sum_and_product(2, 3)  # 等于(5, 6)
s, p = sum_and_product(5, 10)  # s是15，p是50
x, y = 1, 2  # 现在x是1，y是2
x, y = y, x  # Python风格的互换变量，现在x是2，y是1

# 字典

empty_dict = {}  # Python风格
empty_dict2 = dict()  # 更少的Python风格
grades = {"Joel": 80, "Tim": 95}
joels_grade = grades["Joel"]  # 等于80
try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")
joel_has_grade = "Joel" in grades  # 正确
kate_has_grade = "Kate" in grades  # 错误
joels_grade = grades.get("Joel", 0)  # 等于80
kates_grade = grades.get("Kate", 0)  # 等于0
no_ones_grade = grades.get("No One")  # 默认的默认值为None
grades["Tim"] = 99  # 替换了旧的值
grades["Kate"] = 100  # 增加了第三个记录
num_students = len(grades)  # 等于3
tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}
tweet_keys = tweet.keys()  # 键的列表
tweet_values = tweet.values()  # 值的列表
tweet_items = tweet.items()  # （键，值）元组的列表
"user" in tweet_keys  # True, 使用慢速的列表
"user" in tweet  # 更符合Python惯用法，使用快速的字典
"joelgrus" in tweet_values  # True

# defaultdict
word_counts = {}
document = ["a", "b", "b"]
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1
word_counts = defaultdict(int)  # int()生成0
for word in document:
    word_counts[word] += 1
dd_list = defaultdict(list)  # list()生成一个空列表
dd_list[2].append(1)  # 现在dd_list包含{2:[1]}
dd_list = defaultdict(dict)  # dict()产生一个新字典
dd_list["Joel"]["City"] = "Seattle"  # {"Joel": {"City": "Seattle"}}
dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1  # 现在dd_pair包含{2: [0,1]}

# Counter
c = Counter([0, 1, 2, 0])  # c是（基本的）{0: 2, 1: 1, 2: 1}
word_counts = Counter(document)
# 打印10个最常见的词和它们的计数
for word, count in word_counts.most_common(10):
    print(word, count)

# 集合

s = set()
s.add(1)  # s现在是1
s.add(2)  # s现在是{1, 2}
s.add(2)  # s还是{1，2}
x = len(s)  # 等于2
y = 2 in s  # 等于True
z = 3 in s  # 等于False
hundreds_of_other_words = []
stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list  # False，但需要检查每个元素
stopwords_set = set(stopwords_list)
"zip" in stopwords_set  # 非常快地检查
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)  # 6
item_set = set(item_list)  # {1, 2, 3}
num_distinct_items = len(item_set)  # 3
distinct_item_list = list(item_set)  # [1, 2, 3]

# 控制流

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"
parity = "even" if x % 2 == 0 else "odd"
x = 0
while x < 10:
    print(x, "is less than 10")
    x += 1
for x in range(10):
    print(x, "is less than 10")
for x in range(10):
    if x == 3:
        continue  # 直接进入下次迭代
    if x == 5:
        break  # 完全退出循环
    print(x)

# 真和假

one_is_less_than_two = 1 < 2  # 等于True
true_equals_false = True == False  # 等于False
x = None
print(x == None)  # 打印True，但这并非Python的惯用法
print(x is None)  # 打印True，符合Python的惯用法


def some_function_that_returns_a_string():
    return ""


s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""
first_char = s and s[0]
safe_x = x or 0
all([True, 1, {3}])  # True
all([True, 1, {}])  # False,{}为假
any([True, 1, {}])  # True
all([])  # True，列表里没有假的元素
any([])  # False，列表里没有真的元素

# 排序

x = [4, 1, 2, 3]
y = sorted(x)  # 结果是[1, 2, 3, 4]，但x没有变
x.sort()  # x变为[1, 2, 3, 4]
# 通过绝对值对列表元素从最大到最小排血
x = sorted([-4, 1, -2, 3], key=abs, reverse=True)  # 是[-4, 3, -2, 1]
# 从最高数到最低数排序单词和计数
wc = sorted(word_counts.items(),
            key=lambda x: x[1],
            reverse=True)

# 列表解析

even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
squares = [x * x for x in range(5)]  # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]  # [0, 4, 16]
square_dict = {x: x * x for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}
square_set = {x * x for x in [1, -1]}  # {1}
zeroes = [0 for _ in even_numbers]  # 和even_numbers有相同的长度
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]  # 100个对(0,0)(0,1)...(9,8)(9,9)
increasing_pairs = [(x, y)  # 只考虑x < y的对
                    for x in range(10)  # range(lo, hi)与之相等
                    for y in range(x + 1, 10)]  # [lo, lo + 1, ..., hi - 1]


# 生成器和迭代器

def lazy_range(n):
    """a lazy version of range"""
    i = 0
    while i < n:
        yield i
        i += 1


def do_something_with(x, y=0):
    pass


for i in lazy_range(10):
    do_something_with(i)


def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1


lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)

# 随机性

# random.random()生成在0-1之间均匀分布的随机数，是最常用的随机函数
four_uniform_randoms = [random.random() for _ in range(4)]
random.seed(10)  # 设置随机数种子为10
print(random.random())  # 0.5714025946899135
random.seed(10)  # 重设随机数种子为10
print(random.random())  # 再次得到0.5714025946899135
random.randrange(10)  # 从range(10) = [0, 1, ..., 9]中随机选取
random.randrange(3, 6)  # 从range(3, 6) = [3, 4, 5]中随机选取
up_to_ten = []
for i in range(10):
    up_to_ten.append(i)
random.shuffle(up_to_ten)
print(up_to_ten)
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
four_with_replacement = [random.choice(range(10))
                         for _ in range(4)]

# 正则表达式

print(all([  # 所有这些语句都为true，因为
    not re.match("a", "cat"),  # *'cat'不以'a'开头
    re.search("a", "cat"),  # *'cat'里有一个字符'a'
    not re.search("c", "dog"),  # *'dog'里没有字符'c'
    3 == len(re.split("[ab]", "carbs")),  # *分割掉a,b，剩余长度为3
    "R-D-" == re.sub("[0-9]", "-", "R2D2")  # 用虚线进行位的替换
]))  # 打印True


# 面向对象的编程

# 按惯例，我们给下面的类起个PascalCase的名字
class Set:
    # 这些是成员函数
    # 每个函数都取第一个参数"self"（另一种惯例）
    # 它表示所用到的特别的集合对象
    def __init__(self, values=None):
        """This is the constructor.
        It gets called when you create a new Set.
        You would use it like
        s1 = Set()  # 空集合
        s2 = Set([1, 2, 2, 3])  # 用值初始化"""
        self.dict = {}  # Set的每一个实例都有自己的dict属性，我们会用这个属性来追踪成员关系
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        """this is the string representation of a Set object
        if you type it at the Python prompt of pass it to str()"""
        return "Set: " + str(self.dict.keys())

    # 通过成为self.__dict__中对应值为True的键，来表示成员关系
    def add(self, value):
        self.dict[value] = True

    # 如果它在字典中是一个键，那么在集合中就是一个值
    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]


s = Set([1, 2, 3])
s.add(4)
print(s.contains(4))  # True
s.remove(3)
print(s.contains(3))  # False


# 函数式工具

def exp(base, power):
    return base ** power


def two_to_the(power):
    return exp(2, power)


two_to_the = partial(exp, 2)  # 现在是一个包含一个变量的函数
print(two_to_the(3))
square_of = partial(exp, power=2)
print(square_of(3))  # 9


def double(x):
    return 2 * x


xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]  # [2, 4, 6, 8]
twice_xs = map(double, xs)  # 和上面一样
list_doubler = partial(map, double)  # double了一个列表的*function*
twice_xs = list_doubler(xs)  # 同样是[2, 4, 6, 8]


def multiply(x, y):
    return x * y


products = map(multiply, [1, 2], [4, 5])  # [1 * 4, 2 * 5] = [4, 10]


def is_even(x):
    """True if x is even, False if x is odd"""
    return x % 2 == 0


x_evens = [x for x in xs if is_even(x)]  # [2, 4]
x_evens = filter(is_even, xs)  # 和上面一样
list_evener = partial(filter, is_even)  # filter了一个列表的*function*
x_evens = list_evener(xs)  # 同样是[2, 4]

x_product = reduce(multiply, xs)  # = 1 * 2 * 3 * 4 = 24
list_product = partial(reduce, multiply)
x_product = list_product(xs)  # 同样是24

# 枚举

# 非Python用法
for i in range(len(document)):
    documents = document[i]
    do_something_with(i, document)
# 也非Python用法
i = 0
for document in documents:
    do_something_with(i, document)
    i += 1
for i, document in enumerate(documents):
    do_something_with(i, documents)
for i in range(len(documents)):
    do_something_with(i)  # 非Python用法
for i, _ in enumerate(documents):
    do_something_with(i)  # Python用法

# 压缩和参数拆分

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2)  # 是[('a', 1), ('b', 2), ('c', 3)]
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
zip(('a', 1), ('b', 2), ('c', 3))  # [('a', 'b', 'c'), ('1', '2', '3')]


def add(a, b):
    return a + b


add(1, 2)  # 返回3
add(*[1, 2])  # 返回3


# args和kwargs

def doubler(f):
    def g(x):
        return 2 * f(x)

    return g


def f1(x):
    return x + 1


g = doubler(f1)
print(g(3))  # 8(== (3 + 1) * 2)
print(g(-1))  # 0(== (-1 + 1) * 2)


def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)


magic(1, 2, key="word", key2="word2")


def other_way_magic(x, y, z):
    return x + y + z


x_y_list = [1, 2]
z_dict = {"z": 3}
print(other_way_magic(*x_y_list, **z_dict))  # 6


def doubler_correct(f):
    """works no matter what kind of inputs f expects"""

    def g(*args, **kwargs):
        """whatever arguments g is supplied, pass them through to f"""
        return 2 * f(*args, **kwargs)

    return g


def f2(x, y):
    return x + y


g = doubler_correct(f2)
print(g(1, 2))  # 6
