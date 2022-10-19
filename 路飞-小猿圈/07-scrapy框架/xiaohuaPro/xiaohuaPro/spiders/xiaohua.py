# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/19 12:06:18

# 目标URL：https://www.ruyile.com/nice/?f=2&p=1
# 或是：https://pic.netbian.com/4kmeinv/
# 或是：https://mm.enterdesk.com/
import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ruyile.com/nice/?f=2']
    
    # 生成一个通用的url模板
    page_num = 2
    url = 'https://www.ruyile.com/nice/?f=2&p={}'
    def parse(self, response):
        tp_list = response.xpath('//div[@class="m3_xhtp"]/div[@class="tp_list"]')
        for tp in tp_list:
            img_name = tp.xpath('./div[2]/a/text()').extract_first()
            img_url = f"https://www.ruyile.com{tp.xpath('./div[1]/a/@href').extract_first()}"
            
            print(f'{img_name} == > {img_url}')
        
        if self.page_num <= 6:
            new_url = self.url.format(self.page_num)
            self.page_num += 1
            # 手动请求发送: callback回调函数是专门用作于数据解析，递归调用
            yield scrapy.Request(url=new_url, callback=self.parse)
