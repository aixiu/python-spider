import scrapy


class KendejiSpider(scrapy.Spider):
    name = 'kendeji'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.kfc.com.cn/kfccda/news.aspx']

    def parse(self, response):
        # 解析新闻列表 新闻标题及URL
        div_list = response.xpath('//div[@id="list"]/ul/li')
        for div in div_list:
            # xpath返回的是列表，但是列表元素一定是Selector类型的对象
            # extract()可以将 Selectror 对象中 data参数存储的字符串提取出来
            # 如果列表调用了extract()之后，则表示将列表中每一个Selector 对象中 data 对应的字符串提取了出来，返回的是一个列表
            # 可以用 ''.join()拿到列表每一个字符串
            # title = div.xpath('./a/text()')[0].extract()
            title = div.xpath('./a/text()').extract_first()  #反回的如果是列表且此列表中第0个拿出来
            
            print(title)
