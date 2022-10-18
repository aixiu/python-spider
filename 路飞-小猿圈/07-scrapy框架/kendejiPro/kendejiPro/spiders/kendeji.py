import scrapy
from kendejiPro.items import KendejiproItem


class KendejiSpider(scrapy.Spider):
    name = 'kendeji'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qiuyelou.com/top/goodnum.html']

    # def parse(self, response):
    #     # 解析新闻列表 新闻标题及URL
    #     div_list = response.xpath('//div[@class="toplists"]/dl')
    #     all_data = []  # 存储所有解析到的数据
    #     for index, div in enumerate(div_list):
    #         # xpath返回的是列表，但是列表元素一定是Selector类型的对象
    #         # extract()可以将 Selectror 对象中 data参数存储的字符串提取出来
    #         # 如果列表调用了extract()之后，则表示将列表中每一个Selector 对象中 data 对应的字符串提取了出来，返回的是一个列表
    #         # 可以用 ''.join()拿到列表每一个字符串
    #         # title = div.xpath('./a/text()')[0].extract()
    #         # title = div.xpath('./a/text()').extract_first()  #反回的如果是列表且此列表中第0个拿出来
    #         # link = div.xpath('./a/@href').extract_first()  #反回的如果是列表且此列表中第0个拿出来
    #         if index >= 1:
    #             title = div.xpath('./dt/a[1]/strong/text()')[0].extract()
    #             url = div.xpath('./dt/a[1]/@href')[0].extract()
                
    #             dic = {
    #                 'title': title,
    #                 'url': url
    #             }
    #             all_data.append(dic)
            
    #             # print(title, url)
                
    #     return all_data
    
    
    def parse(self, response):
        # 解析新闻列表 新闻标题及URL
        div_list = response.xpath('//div[@class="toplists"]/dl')
        all_data = []  # 存储所有解析到的数据
        for index, div in enumerate(div_list):
            # xpath返回的是列表，但是列表元素一定是Selector类型的对象
            # extract()可以将 Selectror 对象中 data参数存储的字符串提取出来
            # 如果列表调用了extract()之后，则表示将列表中每一个Selector 对象中 data 对应的字符串提取了出来，返回的是一个列表
            # 可以用 ''.join()拿到列表每一个字符串
            # title = div.xpath('./a/text()')[0].extract()
            # title = div.xpath('./a/text()').extract_first()  #反回的如果是列表且此列表中第0个拿出来
            # link = div.xpath('./a/@href').extract_first()  #反回的如果是列表且此列表中第0个拿出来
            if index >= 1:
                title = div.xpath('./dt/a[1]/strong/text()')[0].extract()
                url = div.xpath('./dt/a[1]/@href')[0].extract()
                
                item = KendejiproItem()
                item['title'] = title
                item['url'] = url
                
                yield item  # 将item提交给了管道
