#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time: 2022/10/01 23:45:13

import requests
import json

if __name__ == '__main__':
    # 1.指定URL
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.UA伪装：将对应的 User-Agent 封装备到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    # 3.post 请求参数处理（同get请求一致）
    word = input('enter a word: ')
    data = {
        'kw': word
    }
    # 4.进行请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5.获取响应数据: json()返回的是一个OBJ对象，如果确认响应数据是json类型的，才可以使用json方法
    dic_obj = response.json()
    
    # 6.持久化存储
    with open(f'./{word}.json', mode='w', encoding='utf-8') as fp:
        json.dump(dic_obj, fp=fp, ensure_ascii=False, indent=4)
    
    print('over!!!')
    
    '''        
    参数	        描述	                                                      默认值
    skipkeys	   是否跳过无法被JSON序列化的key（包括str, int, float, bool, None）	False
    sort_keys	   是否对数据按照key进行排序	                                   False
    ensure_ascii   输出保证将所有输入的非 ASCII 字符转义	                       True
    allow_nan	   是否允许JSON规范外的float数据(nan, inf, -inf)	               True
    default	       是一个函数, 当某个value无法被序列化时, 对其调用该函数	        None
    indent	       是一个正整数,  代表序列化后的缩进	                           None
    separator	   是一个格式为 (item_separator, key_separator) 的元组, 默认取值为 (', ', ': ')	None
    check_circular  是否检查循环引用	                                          True
    
    '''
        

    
