# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/05 09:34:53

from bs4 import BeautifulSoup
if __name__=="__main__":
    #将本地的html文档中的数据加载到该对象中，所以参数一得是一个文件描述符，是一个被赋值成功的fp
    fp = open('./test.html','r',encoding='utf-8') #这里是读取，所以第二个参数是r
    soup = BeautifulSoup(fp,'lxml') #soup就是实例化好的对象，已经将本地存储的一个html文件的数据进行了加载
    print(soup)
    print('-'*40)

    # soup.tagName返回的是html中第一次出现的tagName标签
    print(soup.a)  #soup.tagName返回的是html中第一次出现的tagName标签，在这里是打印出第一次出现的a标签
    print('-' * 40)

    print(soup.div)
    print('-' * 40)

    '''
    soup.find():返回的是单个符合要求的标签
                -soup.find('tagName'):等价于soup.tagName
                -属性定位：通过特定的属性定位到该属性对应的标签，如soup.find('div',class_/id/attr='song')
    '''
    print(soup.find('div'))#返回的是第一次出现的标签，=print(soup.div)
    print('-' * 40)

    #属性定位：定位第二个div，通过特定的属性定位到该属性对应的标签
    print(soup.find('div', class_='song')) #class_表示参数名称，如果不加下划线则表示关键字而不是参数名称
    print(soup.find('div', attrs={'class': 'song'})) # 上边内容的另一种写法
    # print(soup.find('div', class_/id/attr='song')) # 属性名还可以是 id attr等
    print('-' * 40)

    '''
    soup.findall():返回的是一个列表，包括符合标准的所有标签
                -soup.find_all('tagName'):以列表形式返回符合要求的所有tagName标签
                -属性定位：与find函数类似，如soup.find_all('div',class_/id/attr='song')
    '''
    print(soup.find_all('a'))
    print('-' * 40)

    '''
    soup.select():
                -select方法用于选择，参数中可以放置选择器，比如想要定位到"tang"这个属性值所在的div，'tang'是class属性值，
                    所以可以使用类选择器'.tang' , '.'表示的就是class；同样也可以使用id选择器、标签选择器等等。返回的是一个列表，包含满足条件的标签。
                -层级选择器：
                    -soup.select('.tang > ul >li > a')：'>'表示的是一个层级，先通过class选择器定位到最外层的div标签，然后用层级分隔符'>'，
                        转到下一层，其中ul用的是标签选择器。注意如果想拿到li标签中的第一个a标签，这种形式soup.select('.tang > ul >li[1]')是不被支持的，
                        所以只能先定位到所有的a标签，因为select返回的是包含满足条件的标签的列表，所以可以从返回的列表中获取第一个a标签，如下：
                        soup.select('.tang > ul >li > a')[0]。
                    -soup.select('.tang > ul a')[0]:空格表示的是多个层级，>表示的是单个层级，
    '''
    print(soup.select('.tang'))
    print('-' * 40)

    #一个层级
    print(soup.select('.tang > ul >li > a')[0]) #>表示层级选择
    print('-' * 40)

    '''
    -获取标签之间的文本数据：
                -soup.a.text/string/get_text():text属性和get_text()方法可以获取某一个标签中所有的文本内容，直系非直系都可以
                                               string属性只能获取该标签下面直系的文本内容
    -获取标签中的属性值：
                -soup.a['src']:标签后面直接跟属性名称,如soup.select('.tang > ul a')[0]['href']
                -li.a就可以获取li标签中的a标签
    '''

    #多个层级：如ul和a之间不是直系子标签,可以用空格表示多个层级
    print(soup.select('.tang > ul a')[0].text)
    print('-' * 40)

    print(soup.select('.tang > ul a')[0].string)
    print('-' * 40)

    print(soup.select('.tang > ul a')[0].get_text())
    print('-' * 40)

    #text和string的区别：text可以返回这个标签下的所有内容，而string只能返回直系的文本内容
    print(soup.find('div', class_='song').string)
    print('-'*40)

    print(soup.find('div', class_='song').text)
    print('-' * 40)

    print(soup.select('.tang > ul a')[0]['href'])
    print('-' * 40)

    print(soup.select('.tang > ul a')[0])  #f返回<a href="http://www.baidu.com" title="qing">清明时节雨纷纷，路上行人欲断魂
