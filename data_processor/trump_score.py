import json
import csv
import pandas as pd
import numpy as np
file_followed_tweet = json.load(open("/home/niufuqiang/NFQ/Uset_SD/dataset_copy/data/trump_user_follow_tweet_score.json", encoding='utf-8'))

# dict_followed_tweet = {}
# for i in file_followed_tweet:
#     dict_followed_tweet[i] = file_followed_tweet[i]



# num = 0
# csv_reader = pd.read_csv('trump/test.csv', encoding='utf-8')
# csv_reader['followed_tweet'] = 'default_value'
# for i in range(len(csv_reader)):
#     id = str(csv_reader['id'][i])
#     if id in dict_followed_tweet:
#         csv_reader['followed_tweet'][i] = dict_followed_tweet[id]
#         num = num + 1
# print(num)
# csv_reader.to_csv('/home/niufuqiang/NFQ/Uset_SD/dataset_copy/trump/test_add_followed_score.csv', index=False, encoding='utf-8')

# num = 0
# csv_reader = pd.read_csv('trump/train.csv', encoding='utf-8')
# csv_reader['followed_tweet'] = 'default_value'
# for i in range(len(csv_reader)):
#     id = str(csv_reader['id'][i])
#     if id in dict_followed_tweet:
#         csv_reader['followed_tweet'][i] = dict_followed_tweet[id]
#         num = num + 1
# print(num)
# csv_reader.to_csv('/home/niufuqiang/NFQ/Uset_SD/dataset_copy/trump/train_add_followed_score.csv', index=False, encoding='utf-8')

# num = 0
# csv_reader = pd.read_csv('trump/valid.csv', encoding='utf-8')
# csv_reader['followed_tweet'] = 'default_value'
# for i in range(len(csv_reader)):
#     id = str(csv_reader['id'][i])
#     if id in dict_followed_tweet:
#         csv_reader['followed_tweet'][i] = dict_followed_tweet[id]
#         num = num + 1
# print(num)
# csv_reader.to_csv('/home/niufuqiang/NFQ/Uset_SD/dataset_copy/trump/valid_add_followed_score.csv', index=False, encoding='utf-8')

# 统计Trump推文相关性比例
file_tweet_score = json.load(open("/home/niufuqiang/NFQ/Uset_SD/dataset_copy/data/trump_user_follow_tweet_score.json", encoding='utf-8'))
score_1 = 0
score_2 = 0
score_3 = 0
num = 0
for i in file_tweet_score:
    for key, value in file_tweet_score[i][0].items():
        score_1 = score_1 + len(value['1'])
        score_2 = score_2 + len(value['2'])
        score_3 = score_3 + len(value['3'])
num = score_1 + score_2 + score_3
print(num)
print("1:", score_1 / num)
print("2:", score_2 / num)
print("3:", score_3 / num)