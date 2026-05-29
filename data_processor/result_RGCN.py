import csv
import json
import pandas as pd
import numpy as np
import ast
# target = ['biden']
# files = ['RGCN_Model_0', 'RGCN_Model_42', 'RGCN_Model_3047']
# for file_name in files:
#     filename = f'{file_name}.csv'
#     data_path_folder = f'/home/niufuqiang/NFQ/Uset_SD/result/{target[0]}/{filename}'
#     csv_reader = pd.read_csv(data_path_folder, encoding='utf-8')
#     var_name = f'{file_name}_set'
#     locals()[var_name] = set()
#     for i in range(len(csv_reader)):
#         stance = 'stance'
#         predict = 'predict'
#         if csv_reader.at[i, stance] != csv_reader.at[i, predict]:
#             locals()[var_name].add(str(csv_reader.at[i, 'id']))
#     print(file_name, len(locals()[var_name]))
# file_user_stance = json.load(open("/home/niufuqiang/NFQ/Uset_SD/dataset_copy/data/biden_user_real_stance.json", encoding='utf-8'))
# user_stance = {}
# for key, value in file_user_stance.items():
#     user_stance[key] = value
# data_path_folder = f'/home/niufuqiang/NFQ/Uset_SD/result/{target[0]}/RGCN_Model_0.csv'
# num = 0
# with open(data_path_folder, 'r') as f_in, open(f'/home/niufuqiang/NFQ/Uset_SD/dataset_copy/data/{target[0]}_RGCN_Model_0_cmp_stance.csv', 'w', newline='') as f_out:
#     csv_reader = csv.DictReader(f_in)
#     writer = csv.DictWriter(f_out, fieldnames=csv_reader.fieldnames + ['followed_user_stance'])
#     writer.writeheader()  # 写入表头
#     for i, row in enumerate(csv_reader):
#         stance = 'stance'
#         predict = 'predict'
#         if row[stance] != row[predict] and row['id'] in locals()['RGCN_Model_42_set'] and row['id'] in locals()['RGCN_Model_3047_set']:
#             print(row['id'])
#             followed_user_stance = []
#             num = num + 1
#             if len(row['follow']):
#                 user_list = ast.literal_eval(row['follow'])
#                 for user in user_list:
#                     followed_user_stance.append(user_stance[user])
#                 row['followed_user_stance'] = followed_user_stance
#             writer.writerow(row)
# print(num)


target = ['trump']
# target = ['trump']
files = ['RGCN_GFS_Model_0_60']
for file_name in files:
    tweetnumis1 = 0
    dict_user_stance = {}
    data_path_folder = f'/home/niufuqiang/NFQ/Uset_SD/data/数据/follow/{target[0]}/tweet/follow_stance.json'
    file = json.load(open(data_path_folder))
    for i in range(len(file)):
        id = str(file[i]['id'])
        stance = file[i]['manner']
        dict_user_stance[id] = stance
    data_path_folder = f'/home/niufuqiang/NFQ/Uset_SD/data/数据/followed/{target[0]}/tweet-manner/post.json'
    file = json.load(open(data_path_folder))
    for key, value in file.items():
        id = str(value['id'])
        stance = value['manner']
        dict_user_stance[id] = stance

    filename = f'{file_name}.csv'
    data_path_folder = f'/home/niufuqiang/NFQ/Uset_SD/result/{target[0]}/{filename}'
    var_name = f'{file_name}'
    locals()[var_name+'_tweet_num'] = 0
    locals()[var_name+'_user_num'] = 0
    locals()[var_name+'_tweet_len'] = 0
    locals()[var_name+'_follow_user_num'] = 0
    locals()[var_name+'_tweetless15'] = 0
    locals()[var_name+'_followuserstanceopposite'] = 0
    # locals()[var_name+'_followsuerstancedifferent'] = 0
    locals()[var_name+'_usertweetnum1'] = 0
    with open(data_path_folder, 'r') as f:
        csv_reader = csv.DictReader(f)
        for i, row in enumerate(csv_reader):
            stance = 'stance'
            predict = 'predict'
            tweet_list = ast.literal_eval(row['tweets'])
            if len(tweet_list) == 1:
                tweetnumis1 = tweetnumis1 + 1
            if row[stance] != row[predict]:
                word_num = 0
                tweet_num = len(tweet_list)
                if tweet_num == 1:
                    locals()[var_name+'_usertweetnum1'] = locals()[var_name+'_usertweetnum1'] + 1
                # locals()[var_name+'_tweet_num'] = locals()[var_name+'_tweet_num'] + len(tweet_list)
                locals()[var_name+'_user_num'] = locals()[var_name+'_user_num'] + 1
                for j in tweet_list:
                    word_num = word_num + len(j.split())
                if word_num / tweet_num <= 15:
                    locals()[var_name+'_tweetless15'] = locals()[var_name+'_tweetless15'] + 1
                if len(row['follow']):
                    follow_user_stance_set = set()
                    follow_user_stance_set.add(row[stance])
                    follow_user_list = ast.literal_eval(row['follow'])
                    for j in follow_user_list:
                        follow_user_stance_set.add(dict_user_stance[str(j)])
                    if 'against' in follow_user_stance_set and 'favor' in follow_user_stance_set:
                        locals()[var_name+'_followuserstanceopposite'] = locals()[var_name+'_followuserstanceopposite'] + 1

        print(f'{var_name}_user_tweet_num_is_1', tweetnumis1)
        print(f'{var_name}_usertweetnum1', locals()[var_name+'_usertweetnum1'])
        print(f'{var_name}_tweetless15', locals()[var_name+'_tweetless15'])
        print(f'{var_name}_followuserstanceopposite', locals()[var_name+'_followuserstanceopposite'])
        print(f'{var_name}_user_num', locals()[var_name+'_user_num'])

# target = ['trump']
# files = ['RGCN_GFS_Model_0_60']
# for file_name in files:
#     filename = f'{file_name}.csv'
#     data_path_folder = f'/home/niufuqiang/NFQ/Uset_SD/result/{target[0]}/{filename}'
#     var_name = f'{file_name}'
#     locals()[var_name+'_tweet_num'] = 0
#     locals()[var_name+'_user_num'] = 0
#     locals()[var_name+'_tweet_len'] = 0
#     locals()[var_name+'_follow_user_num'] = 0
#     locals()[var_name+'_usertweetnum1'] = 0
#     with open(data_path_folder, 'r') as f:
#         csv_reader = csv.DictReader(f)
#         for i, row in enumerate(csv_reader):
#             stance = 'stance'
#             predict = 'predict'
#             if row[stance] != row[predict]:
#                 tweet_list = ast.literal_eval(row['tweets'])
#                 if len(tweet_list) == 1:
#                     locals()[var_name+'_usertweetnum1'] = locals()[var_name+'_usertweetnum1'] + 1
#                 locals()[var_name+'_tweet_num'] = locals()[var_name+'_tweet_num'] + len(tweet_list)
#                 locals()[var_name+'_user_num'] = locals()[var_name+'_user_num'] + 1
#                 for j in tweet_list:
#                     locals()[var_name+'_tweet_len'] = locals()[var_name+'_tweet_len'] + len(j)
#                 if len(row['follow']):
#                     follow_user_list = ast.literal_eval(row['follow'])
#                     locals()[var_name+'_follow_user_num'] = locals()[var_name+'_follow_user_num'] + len(follow_user_list)
#         print(f'{var_name}_tweet_num', locals()[var_name+'_tweet_num'])
#         print(f'{var_name}_user_num', locals()[var_name+'_user_num'])
#         print(f'{var_name}_tweet_len', locals()[var_name+'_tweet_len'])
#         print(f'{var_name}_follow_user_num', locals()[var_name+'_follow_user_num'])
#         print(f'{var_name}_usertweetnum1', locals()[var_name+'_usertweetnum1'])
# files = ['RGCN_GFS_Model_0_60']
# for file_name in files:
#     filename = f'{file_name}.csv'
#     data_path_folder = f'/home/niufuqiang/NFQ/Uset_SD/result/{target[0]}/{filename}'
#     var_name = f'{file_name}'
#     locals()[var_name+'_tweet_num'] = 0
#     locals()[var_name+'_user_num'] = 0
#     locals()[var_name+'_tweet_len'] = 0
#     locals()[var_name+'_follow_user_num'] = 0
#     with open(data_path_folder, 'r') as f:
#         csv_reader = csv.DictReader(f)
#         for i, row in enumerate(csv_reader):
#             stance = 'stance'
#             predict = 'predict'
#             tweet_list = ast.literal_eval(row['tweets'])
#             locals()[var_name+'_tweet_num'] = locals()[var_name+'_tweet_num'] + len(tweet_list)
#             locals()[var_name+'_user_num'] = locals()[var_name+'_user_num'] + 1
#             for j in tweet_list:
#                 locals()[var_name+'_tweet_len'] = locals()[var_name+'_tweet_len'] + len(j)
#             if len(row['follow']):
#                 follow_user_list = ast.literal_eval(row['follow'])
#                 locals()[var_name+'_follow_user_num'] = locals()[var_name+'_follow_user_num'] + len(follow_user_list)
#         print(f'{var_name}_tweet_num', locals()[var_name+'_tweet_num'])
#         print(f'{var_name}_user_num', locals()[var_name+'_user_num'])
#         print(f'{var_name}_tweet_len', locals()[var_name+'_tweet_len'])
#         print(f'{var_name}_follow_user_num', locals()[var_name+'_follow_user_num'])


# # 统计Biden关注用户推文数量
# import json
# file_tweet = json.load(open("/home/niufuqiang/NFQ/Uset_SD/data/数据/trump/tweet/follow.json", encoding = 'utf-8'))
# num = 0
# a = 0
# against = 0
# none = 0
# favor = 0
# for key, value in file_tweet.items():
#     num = num + len(value['tweets'])
#     for j in value['tweets']:
#         a = a + len(j)
# file_tweet = json.load(open("/home/niufuqiang/NFQ/Uset_SD/data/数据/trump/tweet/follow_stance.json", encoding = 'utf-8'))
# for i in file_tweet:
#     if i['manner'] == 'against':
#         against = against + 1
#     elif i['manner'] == 'none':
#         none = none + 1
#     else:
#         favor = favor + 1
# print("推文总数量", num)
# print("推文平均长度", a / num)
# print("用户平均推文数量", num / len(file_tweet))
# print("against:", against, against / len(file_tweet))
# print("noen:", none, none / len(file_tweet))
# print("favor", favor, favor / len(file_tweet))