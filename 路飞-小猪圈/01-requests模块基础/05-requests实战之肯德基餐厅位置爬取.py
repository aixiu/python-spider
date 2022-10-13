#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time: 2022/10/02 16:40:00

import requests
import ast
import json

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    
    # UA伪装：将对应的 User-Agent 封装备到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
    }
    address =  input('请输入要查询的地址： ')
    # 处理url携带的参数：封装到字典中
    param = {
        'op': 'keyword',
        'cname': '',
        'pid': '',
        'keyword': address,  # 查询地点
        'pageIndex': '1',  # 页数
        'pageSize': '10',  # 每页显示的数量
    }
    
    response = requests.get(url=url, headers=headers, params=param)
    
    data_texe = response.text
    filename = f'{address}肯德基地址.json'
    data_json = json.loads(data_texe)  # 字符串转换成字典  json模块
    # data_dict = ast.literal_eval(data_texe)   # 字符串转换成字典  ast模块
    
    for dic in data_json['Table1']:
        storeName = dic['storeName']
        addressDetail = dic['addressDetail']
        pro = dic['pro']
        print(f'餐厅名称：{storeName} 餐厅地址：{addressDetail}')
        
        
    with open(f'./{filename}', mode='w', encoding='utf-8') as fp:
        json.dump(data_json, fp=fp, ensure_ascii=False)
        
    print('over!!!')
    
    
    '''
    常用的方法
        json.load()从json文件中读取数据
        json.loads()将str类型的数据转换为dict类型
        json.dumps()将dict类型的数据转成str
        json.dump()将数据以json的数据类型写入文件中
    '''
    
    
    
