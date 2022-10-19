# scrapy框架

## 什么是框架

- 就是集成了很多功能，并且具有很强通用性的一个项目模板。

## 如何学习框架

- 专门学习框架封装的各种功能的详细用法。

## 什么是scrapy

- 爬虫中封装好的一个明星框架。
- 功能：高性能的持久化存储，异步数据下载，高性能的数据解析，分布式等常用功能。

## scrapy框架的基本使用

- 环境安装：pip install scrapy
- 安装：pip install pywin32
- pywin32是Python的一个代码库，包装了Windows 系统的 Win32 API，能创建和使用 COM 对象和图形窗口界面。如果你想用Python操控Windows系统，创建窗口、接受键鼠命令，或用到Win32 API，那你就需要它。
- 创建一个工程  scrapy startproject XXXPro
- 一定要先进入XXXPro工程目录
- 在spiders子目录中创一个爬虫文件
  - scrapy genspider spiderName www.xxx.com
- 执行工程
  - scrapy crawl spiderName
  - 工程配置文件：# 显示指定类型的日志信息  LOG_LEVEL = 'ERROR'

## scrapy数据解析

## scrapy持久化存储

- 基于终端指令：
  - 要求：只可以将parse方法的返回值存储到本地的文本文件中
  - 持久化存储对应的文本文件的类型只可以为：'json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle'
  - 指令：scrapy crawl xxx -o filePath
  - 好处：简洁高效便捷
  - 缺点：局限性比较强
    - 数据只可以存储到指定后缀的文本文件中
- 基于管道：
  - 编码流程：
    - 数据解折
    - 在item类中定义相关的属性
    - 将解析的数据封装存储到item类型的对象
    - 将item类型的对象提交给管道进行持久华存储的操作
    - 在管道类的process_item中要将其接收到的item对象中存储的数据进行持久化操作
    - 在配置文件中开启管道
  - 好处：
    - 通用性强。

- 面试题：将爬取到的数据一份存储到本地一份存储到数据库，如何实现？
  - 管道文件中一个管道类对应的是将数据存储到一种平台
  - 爬虫文件提交的item只会给管道文件中第一个被执行的管道类接收
  - process_itme中的 retun item 表示将item传递给下一个即将被执行的管道类

- 基于Spider的全站数据爬取
  - 就是将网站中某版块下的全部页码对应的页面数据进行爬取
  - 需求：爬取校花网中的照片名称
  - 实现方式：
    - 将所有页面的URL添加到start_urls列表（不推荐）
    - 自行手动进行请求发送（）
      - 手动请求发送：
        - scrapy.Request(url, callback)  callback:专门用做于数据解析

- 一个例子：
  - title：如何利用Python爬虫爬取网页中图片(成功实现自动翻页至最后一页)
  - url：<https://blog.csdn.net/weixin_65423581/article/details/122533646>
  - 判断next_url是否存在,若不存在返回None值以便结束循环(需要学习的点)

- 五大核心组件
