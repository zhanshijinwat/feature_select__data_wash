import numpy as np 
import pandas as pd 
from glob import glob 
import json

file_list_dir = glob(".\\v7\\*.json")
result_dict = {}
result_dict["real_day"]=["loop", 366, -1]
result_dict["real_hour"]=["loop", 96, -1]
for file_dir in file_list_dir:
    with open(file_dir, 'r', encoding='utf-8') as f:
        dic = json.load(f)
        for k,v in dic.items():
            result_dict[k] = v
            print(k,v)

b = json.dumps(result_dict)
f2 = open("feature_config.json", 'w')
f2.write(b)
f2.close()
