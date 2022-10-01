#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

r = requests.get('http://www.baidu.com')

print(r.request.headers)   # HTTP请求头
print(r.headers)  #HTTP响应头
print(r.status_code)  #HTTP请求的返回状态，比如，200表示成功，404表示失败
print(r.encoding)  #从header中猜测的响应的内容编码方式
print(r.apparent_encoding)  #从内容中分析的编码方式（慢）

print(r.text)  #响应内容的Unicode型的数据
print(r.content)  #响应内容的二进制形式

## 区别：

# resp.text返回的是Unicode型的数据。
# resp.content返回的是bytes型也就是二进制的数据。

    # 也就是说，如果你想取文本，可以通过r.text。
    # 如果想取图片，文件，则可以通过r.content。
    # （resp.json()返回的是json格式数据）


# requests抓取网页的通用框架

import requests

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=20)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'Something Wrong!'


# 本文链接：https://zhuanlan.zhihu.com/p/26681429


# 给出一个图片下载的通用代码片段：

import requests

def get_pic_from_url(url):
    #从url以二进制的格式下载图片数据
    pic_content = requests.get(url,stream=True).content
    open('filename','wb').write(pic_content)

# 本文链接：https://zhuanlan.zhihu.com/p/26786056



# 视频地址：https://www.bilibili.com/video/BV1464y1c7Eq?p=1
# requests安装
    # 安装命令：pip install requests
    
# requests基本使用
    # 1.导入模块
    # 2.发送get请求，获取响应
    # 3.从响应中获取数据
    
import requests

response = requests.get('http://www.baidu.com')   # 一定要加http或https请求协议
print(response)  # 打印响应
print(response.encoding)   # 查看当前返回用于解码response.content的编码。  ISO-8859-1
# response.encoding = 'utf-8'  #设置编码（中文不乱码）
# print(response.text)  # 打印响应内容 按 encoding 指定的编码进行解码
# print(response.content) # 响应体bytes类型

print(response.content.decode()) # 根据对应的编码进行解析  .decode() 解码 .content的二进制内容

'''
知识点：
    text和content方法的区别
    
    r.text 　　　　str 　　　#字符串方式的响应体，会自动根据响应头部的 字符编码进行解码
    r.content 　　 bytes　　#字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩

    requests对象的get和post方法都会返回一个Response对象，这个对象里面存的是服务器返回的所有信息，包括响应头，响应状态码等。其中返回的网页部分会存在.content和.text两个对象中。

    两者区别在于，content中间存的是字节码，而text中存的是Beautifulsoup根据猜测的编码方式将content内容编码成字符串。

    直接输出content，会发现前面存在b'这样的标志，这是字节字符串的标志，而text是，没有前面的b,对于纯ascii码，这两个可以说一模一样，对于其他的文字，需要正确编码才能正常显示。大部分情况建议使用.text，因为显示的是汉字，但有时会显示乱码，这时需要用.content.decode('utf-8')，中文常用utf-8和GBK，GB2312等。这样可以手工选择文字编码方式。

    所以简而言之，.text是现成的字符串，.content还要编码，但是.text不是所有时候显示都正常，这是就需要用.content进行手动编码。
'''