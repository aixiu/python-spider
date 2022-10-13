#!/usr/bin/env pythonrequests
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time: 2022/10/02 16:03:18

import requests
import json


if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list"
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '1',  # 从库中的第几部电影去取
        'limit': '20',  # 一次请求取出的个数
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    response = requests.get(url=url, params=param, headers=headers)
    
    list_data = response.json()
    
    with open('./douban.json', mode='w', encoding='utf-8') as fp:
        json.dump(list_data, fp=fp, ensure_ascii=False)
    print('over!!!')
