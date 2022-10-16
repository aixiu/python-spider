# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/09 23:59:02

'''
    实例化etree对象

    etree.parse('filename'):将本地html文档加载到该对象中
    etree.HTML(pate_text):网络获取的页面数据加载到该对象
    
    # 使用lxml.etree.parse()解析html文件，该方法默认使用的是“XML”解析器，所以如果碰到不规范的html文件时就会解析错误
    # 避免报错 自己创建html解析器，增加parser参数
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse('test.html', parser=parser)
    
    标签定位

    最左侧的 / :如果xpath表达式最左侧是以/开头，则该xpath表达式一定要从根标签开始定位指定的标签 (此方式并不常用)
    tree.xpath('/html/head/meta')  # 定位meta

    非最左侧的 / :表示一个层级
    tree.xpath('/html//meta')  # 定位meta

    最左侧的 // ：xpath表达式可以从任意位置进行标签定位
    tree.xpath('//mate')  # 定位meta

    属性定位：tageName[@attrName="value"]

    # 定位到class为song的div下面的所有的p
    tree.xpath('//div[@class="song"]/p')
    # 打印:[<Element p at 0x256b1982e00>, <Element p at 0x256b1982e40>, <Element p at 0x256b1982e80>, <Element p at 0x256b1982ec0>]


    索引定位：tag[index] (索引是从1开始的)

    # 定位到class为song的div下面的第二个的p
    tree.xpath('//div[@class="song"]/p[2]')
    # 打印：[<Element p at 0x1f4a62a2e00>]

    还有不常用的定位方式： 模糊匹配等

    取文本

    /text()：直系文本内容
    //text()：所有的文本内容
    tree.xpath('//div[@class="song"]/p[2]/text()')
    #打印 ['王安石']


    取属性：/@attName

    tree.xpath('//a[@id="feng"]/@href')
    # 打印 ['http://www.haha.com']

    tree.xpath('//a[@id="feng"]/@id')
    # 打印 ['feng']

    
    原文链接：https://blog.csdn.net/tao5090694/article/details/120425637
'''

from lxml import etree

if __name__ == '__main__':
    # 实例化好了一个 etree 对象，且将被解析的源码加载到了该对象中
    parser = etree.HTMLParser(encoding="utf-8")
    tree = etree.parse('./test.html', parser=parser)
    # r = tree.xpath('/html/head/title')
    # r = tree.xpath('/html/body/div')
    # r = tree.xpath('/html//div')
    # r = tree.xpath('//div')
    
    # r = tree.xpath("//div[@class='song']")
    # r = tree.xpath("//div[@class='song']/p")
    # r = tree.xpath("//div[@class='song']/p[2]")    # 这里索引是从1开始的  验证方法，如果是0，则为空
    
    # r = tree.xpath("//div[@class='tang']//li[5]/a/text()")  # 取到的是一个列表  ['杜牧']
    # r = tree.xpath("//div[@class='tang']//li[5]/a/text()")[0]  # 列表的索引才能拿到字符串内容
    
    
    # r = tree.xpath("//li[7]//text()")[0]  # /text()：直系文本内容  //text()：所有的文本内容
    # r = tree.xpath("//div[@class='tang']//text()")
    
    r =tree.xpath("//div[@class='song']/img/@src")   # 取属性：/@attName
    
    print(r)
