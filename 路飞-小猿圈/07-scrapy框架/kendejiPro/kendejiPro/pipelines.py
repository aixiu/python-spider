# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class KendejiproPipeline:
    fp = None
    # 重写父类的一个方法：该方法只在开始爬虫的进起被调用一次
    def open_spider(self, spider):
        print('开始爬虫。。。')
        self.fp = open('./kedeji.txe', mode='w', encoding='utf-8')
    # 专门用来处理item类型对象
    # 该方法可以接收爬虫文件提交过来的item对象
    # 该方法每接收到一个item就会被调用一次
    def process_item(self, item, spider):
        title = item['title']
        url = item['url']
        
        self.fp.write(f"{title}: {url}\n")
        
        return item  # 就会传递给下一个即将被执行的管道类
    
    def close_spider(self, spider):
        print('结束爬虫')
        self.fp.close()
 
# 管道文件中一个管道类对应一组数据存储到一个平台或者载体中       
class mysqPileLine:
    conn = None  # 数据库链接对象
    cursor =None # 数据库游标对，用来执行数据库语句
    def open_spider(self, spider):
        self.conn = sqlite3.connect('./kendeji.db')
    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()  # 通过连接对象去创建游标对象
        try:
            self.cursor.execute(f'inisert into kendeji values("{item["title"]}", {item["url"]})')  # 执行sql语句
        except Exception as e :
            print(e)
            self.conn.rollback()
            
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        
# 爬虫文件提交的item类型的对象最终会提交给哪一个管道类？
    # 先执行的管道类
