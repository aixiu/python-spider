import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ruyile.com/news/?s=10&fl=15']
    
    def parse_detail(self, response):
        job_desc = response.xpath('//div[@class="nrk"]//text()').extract()
        job_desc = ''.join(job_desc)
        print(job_desc)

    def parse(self, response):
        li_list = response.xpath('//div[@class="m1_z"]/div[@class="m2_lb"]')
        for li in li_list:
            job_name = li.xpath('./h3/a/text()').extract_first()
            print(job_name)
            detail_url = f"https://www.ruyile.com{li.xpath('./h3/a/@href').extract_first()}"
            print(detail_url)
            # 对详情页发请求获取详情页面源码数据
            # 手动请求的发送
            yield scrapy.Request(detail_url, callback=self.parse_detail)