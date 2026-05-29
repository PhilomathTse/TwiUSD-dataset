import csv
import pandas as pd
import numpy as np
target = ['trump']
files = ['bert_Model_0', 'BERTGCN_0', 'llama3', 'RGCN_Model_0', 'Roberta_Model_0', 'TAN_0']
for file_name in files:
    filename = f'{file_name}.csv'
    data_path_folder = f'/home/niufuqiang/NFQ/Uset_SD/result/{target[0]}/{filename}'
    csv_reader = pd.read_csv(data_path_folder, encoding='utf-8')
    var_name = f'{file_name}_set'
    locals()[var_name] = set()
    for i in range(len(csv_reader)):
        if file_name == 'BERTGCN_0':
            stance = 'stance'
            predict = 'Predict'
        else:
            stance = 'stance'
            predict = 'predict'
        if csv_reader.at[i, stance] != csv_reader.at[i, predict]:
            locals()[var_name].add(csv_reader.at[i, 'id'])
    print(file_name, len(locals()[var_name]))

for i in locals()['BERTGCN_0_set']:
    num = 0
    if i in locals()['RGCN_Model_0_set']:
        continue
    for file_name in files:
        var_name = f'{file_name}_set'
        if i in locals()[var_name]:
            num = num + 1
    if num == len(files) - 1:
        print(i)

"""
biden:id
1216167347943329792
1455176358749999104
14293348
37764633
703640251378618369
27397922
"""