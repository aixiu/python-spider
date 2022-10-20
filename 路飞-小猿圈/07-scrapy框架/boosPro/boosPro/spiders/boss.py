import scrapy
from boosPro.items import BoosproItem


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ruyile.com/news/?s=10&fl=10']
    
    # 生成一个通用的url模板
    url = 'https://www.ruyile.com/news/?s=10&fl=10&p={}'
    page_num = 2    
    
    # 回调函数接收item 解析详情页内容
    def parse_detail(self, response):
        item = response.meta['item']
        
        job_desc = response.xpath('//div[@class="nrk"]//text()').extract()
        job_desc = ''.join(job_desc)
        job_desc = job_desc.strip().replace('\n', '')
        # print(job_desc)
        
        item['job_desc'] = job_desc
        
        yield item
        
    # 解析首页中的名称
    def parse(self, response):
        li_list = response.xpath('//div[@class="m1_z"]/div[@class="m2_lb"]')
        for li in li_list:
            item = BoosproItem()
            job_name = li.xpath('./h3/a/text()').extract_first()
            item['job_name'] = job_name
            # print(job_name)
            detail_url = f"https://www.ruyile.com{li.xpath('./h3/a/@href').extract_first()}"
            # print(detail_url)
            # 对详情页发请求获取详情页面源码数据
            # 手动请求的发送
            # 请求传参 meta={'item': item} 可以将matem字典传递给请求对应的回调函数
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item': item})
            
        # 进行分页操作
        if self.page_num <= 3:
            new_url = self.url.format(self.page_num)
            self.page_num +=1
            
            yield scrapy.Request(url=new_url, callback=self.parse)