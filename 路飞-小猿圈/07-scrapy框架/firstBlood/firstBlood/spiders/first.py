# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/17 23:47:02

import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件名称：就是爬虫源文件的一个唯一标识
    name = 'first'
    # 允许的域名：用来限定start_urls列表中哪些url可以进行请求发送，通常不会使用
    # allowed_domains = ['www.baidu.com']
    # 起始的url列表:该列表中存放的URL会被scrapy自动进行请求的发送,可以有多个
    start_urls = ['https://www.baidu.com/', 'https://www.sogou.com']

    # parse用于数据解析：response参数表示就是请求成功后对应的响应对象
    def parse(self, response):
        print(response)
