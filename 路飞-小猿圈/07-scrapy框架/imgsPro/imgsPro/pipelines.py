# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class ImgsproPipeline:
#     def process_item(self, item, spider):
#         return item

from scrapy.pipelines.images import ImagesPipeline  # 导入ImagesPipeline类
import scrapy

# 新类继承ImagesPipeline类，专门用于文件下载的管道类，下载过程支持异步和多线程
class imgsPileLine(ImagesPipeline):  
    
    # 就是可以根据图片地址进行图片数据的请求，重写父类的方法
    # 对item中的图片进行请求操作
    def get_media_requests(self, item, info):
        #手动向管道itme中的url发送请求
        yield scrapy.Request(item['src'])
        
    #指定图片存储的路径
    def file_path(self, request, response=None, info=None):
        #根据URL来生成图片的名称
        imgName = request.url.split('/')[-1]
        return imgName

    def item_completed(self, results, item, info):
        return item #返回给下一个即将被执行的管道类，如果有别的管道
