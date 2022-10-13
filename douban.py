# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/12 22:40:10

import requests
from lxml import etree
import random
import re
import json
import os

vod_douban_id  = input(f'请输入豆瓣ID == > ')

if __name__ == '__main__':
    url = f'https://movie.douban.com/subject/{vod_douban_id}/'
    
    flie_path = f'./douban'
    
    # 创建一个文件夹，保存所有的图片
    if not os.path.exists(flie_path):
        os.mkdir('./douban/')
    
    # 获取文件夹下所有文件名
    file_name_list = os.listdir(flie_path)

    #判读豆瓣ID文件是否存在如果存在，直接读文件，如果不存在爬取数据并保存
    if f'{vod_douban_id}.json' in file_name_list:
        with open(f'{flie_path}/{vod_douban_id}.json', mode='r', encoding='utf-8') as fp:
            json_data = json.load(fp=fp)
        print(json_data)
    else:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
        }
        data = {
            'idsite': 100001,
            'rec': 1,
            'r': 384446,
            'h': 22,
            'm': 38,
            's': 15,
            'url': 'https://search.douban.com/movie/subject_search?search_text=%E7%8B%AC%E8%A1%8C%E6%9C%88%E7%90%83&cat=1002',
            'urlref': 'https://movie.douban.com/',
            '_id': '584fb75590637a4a',
            '_idts': 1665585410,
            '_idvc': 1,
            '_idn': 0,
            '_refts': 1665585410,
            '_viewts': 1665585410,
            '_ref': 'https://movie.douban.com/subject/35183042/',
            'pdf': 1,
            'qt': 0,
            'realp': 0,
            'wma': 0,
            'dir': 0,
            'fla': 0,
            'java': 0,
            'gears': 0,
            'ag': 0,
            'cookie': 1,
            'res': '1920x1080',
            'gt_ms': 376,
        }
        
        page_text = requests.post(url=url, headers=headers, timeout=20)
        
        tree = etree.HTML(page_text.text)
        
        vod_name = tree.xpath('//*[@id="content"]/h1/span[1]/text()')[0]   # 电影名称
        
        try:
            vod_sub = tree.xpath('//span[./text()="又名:"]/following::text()[1]')[0].strip()  # 别名
        except:
            vod_sub = ''
        # https://www.bilibili.com/read/cv18668864
        # https://www.jianshu.com/p/0bab7c92862c/
        # [./text()="制片国家/地区:"]相当于一个判断语句
        # following::text()   以文本作为定位的锚点，跟在后面所有文本信息有1000多个
        # following::text()  [1]就表示排在第一个文本--想要提取的文本 
        
        vod_pic = tree.xpath('//*[@id="mainpic"]/a/img/@src')[0]  # 海报
        
        vod_year = tree.xpath('//*[@id="content"]/h1/span[2]/text()')[0].strip('()')   # 引号中加入删除符号的列表(删除左右大括号和空格)  n.strip('[{}\n]')  # 年代
        
        vod_lang_list = tree.xpath('//span[./text()="语言:"]/following::text()[1]')[0].split("/")        
        try:
            vod_lang = f"{vod_lang_list[0].strip()},{vod_lang_list[1].strip()}"  # 语言
        except:
            vod_lang = tree.xpath('//span[./text()="语言:"]/following::text()[1]')[0].strip()
        
        try:
            vod_class_list = tree.xpath('//span[@property="v:genre"]/text()')
            vod_class = f"{vod_class_list[0]},{vod_class_list[1]}"  # 分类
        except:
            vod_class = tree.xpath('//span[@property="v:genre"]/text()')[0]

        vod_actor_list = tree.xpath('//*[@id="info"]/span[3]/span[2]//text()')
        vod_actor = ''.join(vod_actor_list)
        vod_actor = vod_actor.replace(" / ", ',')  # 主演
        
        vod_content = tree.xpath('//*[@id="link-report"]/span/text()')[0].strip()  # 简介
        
        vod_writer_list = tree.xpath('//*[@id="info"]/span[2]/span[2]/a/text()')
        vod_writer = ','.join(vod_writer_list)  # 编剧
        
        vod_area = tree.xpath('//span[./text()="制片国家/地区:"]/following::text()[1]')[0].strip()  # 国家
        
        if '中国' or '台湾' in vod_area:
            vod_remarks = "高清国语"   # 语言 和总集数
        else:
            vod_remarks = "高清中字"
        
        try:    
            vod_director = tree.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')[0]  #导演
        except:
            vod_director = ''
        
        vod_pubdate = tree.xpath('//*[@id="info"]/span[10]/text()')[0]  # 上映时间    
        
        try:
            vod_total = tree.xpath('//span[./text()="集数:"]/following::text()[1]')[0].strip()  # 集数
        except:
            vod_total = ''
        
        vod_score  = tree.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()')[0]  # 评分
        vod_douban_score  = vod_score   # 豆瓣评分
        
        vod_score_num =  random.randint(100, 1000)
        vod_score_all =  random.randint(200, 500)
        
        try:
            vod_duration = tree.xpath('//*[@id="info"]/span[@property="v:runtime"]/@content')[0]  # 片长
        except:
            vod_duration = tree.xpath('//span[./text()="单集片长:"]/following::text()[1]')[0].strip()
            vod_duration = re.sub('[\u4e00-\u9fa5]', '', vod_duration)    # 去除字符串之中的中文
        
        vod_reurl = url   # 豆瓣地址
        
        vod_data = {
            "vod_name": vod_name,
            "vod_sub": vod_sub,
            "vod_pic": vod_pic,
            "vod_year": vod_year,
            "vod_lang": vod_lang,
            "vod_class": vod_class,
            "vod_actor": vod_actor,
            "vod_content": vod_content,
            "vod_writer": vod_writer,
            "vod_area": vod_area,
            "vod_remarks": vod_remarks,
            "vod_director": vod_director,
            "vod_pubdate": vod_pubdate,
            "vod_total": vod_total,
            "vod_score": vod_score,
            "vod_douban_score": vod_douban_score,
            "vod_score_num": vod_score_num,
            "vod_score_all": vod_score_all,
            "vod_duration": vod_duration,
            "vod_reurl": vod_reurl,
            "vod_douban_id": vod_douban_id,        
        }
        

        with open(f'{flie_path}/{vod_douban_id}.json', mode='w', encoding='utf-8') as fp:
            json.dump(vod_data, fp=fp, ensure_ascii=False, indent=4)
        print(f'{vod_douban_id}  ==> 采集完毕')
        
        # print(
        #     f'"vod_name": "{vod_name}"\n',
        #     f'"vod_sub": "{vod_sub}"\n',
        #     f'"vod_pic": "{vod_pic}"\n',
        #     f'"vod_year": "{vod_year}"\n',
        #     f'"vod_lang": "{vod_lang}"\n',
        #     f'"vod_class": "{vod_class}"\n',
        #     f'"vod_actor": "{vod_actor}"\n',
        #     f'"vod_content": "{vod_content}"\n',
        #     f'"vod_writer": "{vod_writer}"\n',
        #     f'"vod_area": "{vod_area}"\n',
        #     f'"vod_remarks": "{vod_remarks}"\n',
        #     f'"vod_director": "{vod_director}"\n',
        #     f'"vod_pubdate": "{vod_pubdate}"\n',
        #     f'"vod_total": "{vod_total}"\n',
        #     f'"vod_score": "{vod_score}"\n',
        #     f'"vod_douban_score": "{vod_douban_score}"\n',
        #     f'"vod_score_num": "{vod_score_num}"\n',
        #     f'"vod_score_all": "{vod_score_all}"\n',
        #     f'"vod_duration": "{vod_duration}"\n',
        #     f'"vod_reurl": "{vod_reurl}"\n',
        #     f'"vod_douban_id": "{vod_douban_id}"\n',
            
        # )

    
    
    
    

    
