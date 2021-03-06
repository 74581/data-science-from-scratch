#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

from __future__ import division
from collections import Counter
from collections import defaultdict

__author__ = '74581'

# 寻找关键联系人

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []
for i, j in friendships:
    users[i]["friends"].append(users[j])  # 把i加为j的朋友
    users[j]["friends"].append(users[i])  # 把j加为i的朋友


def number_of_friends(user):
    """how many friends does _user_have?"""
    return len(user["friends"])  # 返回朋友数


total_connections = sum(number_of_friends(user)
                        for user in users)
print(total_connections)  # 总朋友数:24

num_users = len(users)
avg_connections = total_connections / num_users
print(avg_connections)  # 平均朋友数:2.4

num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]  # 创建表(user_id, number_of_friends)
num_friends_by_friends = sorted(num_friends_by_id,
                                key=lambda x: x[1],
                                reverse=True)
print(num_friends_by_friends)  # 按朋友数从大到小排序


# 你可能知道的数据科学家

def friends_of_friend_ids_bad(user):
    # foaf是“朋友的朋友”的英文简写
    return [foaf["id"]
            for friend in user["friends"]  # 对每一位用户的朋友
            for foaf in friend["friends"]]  # 得到他们的朋友


print(friends_of_friend_ids_bad(users[0]))  # (Hero)[0, 2, 3, 0, 1, 3]
print([friend["id"] for friend in users[0]["friends"]])  # [1, 2]
print([friend["id"] for friend in users[1]["friends"]])  # [0, 2, 3]
print([friend["id"] for friend in users[2]["friends"]])  # [0, 2, 3]


def not_the_same(user, other_user):
    """two users are not the same if they have different ids"""
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    """other_user is not a friend if he's not in user["friends"];
    that is, if he's not_the_same as all the people in user["friends"]"""
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]  # 对我的每一位朋友
                   for foaf in friend["friends"]  # 计数他们的朋友
                   if not_the_same(user, foaf)  # 既不是我
                   and not_friends(user, foaf))  # 也不是我的朋友


print(friends_of_friend_ids(users[3]))  # Counter({0: 2, 5: 1})即3和0有两个共同的朋友，和5有一个共同的朋友

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]


print(data_scientists_who_like("Python"))  # 找出喜欢Python的人：2，3，5

user_ids_by_interest = defaultdict(list)  # 键是interest，值是带有这个interest的user_id的列表
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
interests_by_user_id = defaultdict(list)  # 键是user_id，值是对那些user_id的interest的列表
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)


def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])


print(most_common_interests_with(users[0]))  # 和0（id）拥有共同兴趣的user_id按从共同兴趣数量从大到小排序

# 工资与工作年限

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# 键是year，值是对每一个tenure的salary的列表
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
# 键是year，每个值是相应tenure的平均salary
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
    }
print(average_salary_by_tenure)


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


# 键是tenure bucket，值是相应bucket的salary的列表
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
# 键是tenure bucket，值是对那个bucket的average salary
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
    }
print(average_salary_by_bucket)

# 付费账户

years_experience = [(0.7, "paid"),
                    (1.9, "unpaid"),
                    (2.5, "paid"),
                    (4.2, "unpaid"),
                    (6, "unpaid"),
                    (6.5, "unpaid"),
                    (7.5, "unpaid"),
                    (8.1, "unpaid"),
                    (8.7, "paid"),
                    (10, "paid")
                    ]


def predict_paid_or_unpaid(years_experience):  # 根据工作年限简单预测是否付费
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


# 兴趣主题

words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())
for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
