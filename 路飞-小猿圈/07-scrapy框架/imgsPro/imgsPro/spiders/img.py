import scrapy


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//div[@data-waterfall="true"]/div')
        for div in div_list:
            # src = 'https://sc.chinaz.com{}'.format(div.xpath('./div[@class="bot-div"]/a/@href'))
            img_name = div.xpath('./div/a/text()').extract_first()
            src = div.xpath('./img/@src').extract_first()
            print(f'{img_name} ==> {src}')
            

