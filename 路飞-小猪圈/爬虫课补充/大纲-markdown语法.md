# 协程 & asyncio & 异步编程

## 视频地址

- <https://www.bilibili.com/video/BV1Yh411o7Sz/?p=83&vd_source=20f7c1f5f32f90ae92d9428e45039d9b>

- p80~p100 爬虫课补充

## 协程

> 协程不是计算机提供的，是人为创造的。

协程（Coroutine），也可以被称为微线程，是一种用户态内的上下文切换技术。简而言之，其实就是通过一个线程实现代码块相互切换执行。例如：

```python
def func1():
    print(1)
    ...
    print(2)

def func2():
    print(3)
    ...
    print(4)

func1()
func2()
```

## 实现协程有这么几种方法

- greenlet，早期模块
- yield关键字
- asyncio装饰器(python3.4)
- async、await关键字(python3.5) 【推荐】

### greenlent 实现协程

> pip install greenlet

```python
from greenlet import greenlet

def func1():
    print(1)       # 第2步：输出 1
    gr2.switch()   # 第3步：切换到 func2 函数
    print(2)       # 第6步：输出 2
    gr2.switch()   # 第7步：切换到 func2 函数，从上一次执行的位置继续向后执行

def func2():
    print(3)       # 第4步：输出 3
    gr1.switch()   # 第5步：切换到 func1 函数，从上一次执行的位置继续向后执行
    print(4)       # 第8步：输出 4

gr1 = greenlet(func1)
gr2 = greenlet(func2)

gr1.switch()   # 第1步：去执行 func1 函数
```

### yield关键字(了解即可)

```python
def func1():
    yield 1
    yield from func2()
    yield 2

def func2():
    yield 3
    yield 4

f1 = func1()
for item in f1:
    print(item)
```

### asyncio模块

> 在 python3.4及之后的版本才可用。

```python
import asyncio

@asyncio.coroutine
def func1():
    print(1)
    yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到 tasks 中其他任务
    print(2)

@asyncio.coroutine
def func2():
    print(3)
    yield from asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到 tasks 中其他任务
    print(4)

tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
```

注意：遇到IO阻塞自动切换

### async & await关键字

> 在 python3.5及之后的版本。

```python
import asyncio

async def func1():
    print(1)
    await asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到 tasks 中其他任务
    print(2)

async def func2():
    print(3)
    await asyncio.sleep(2)  # 遇到IO耗时操作，自动化切换到 tasks 中其他任务
    print(4)

tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
```

## 协程的意义

在一个线程中，如果遇到IO等待时间，线程不会傻傻等，利用空闲时间再去干点其它的事。

案例：去下载三张图片（网络IO）

### 普通方法（同步）

```python
pip install requests

import requests

def download_image(url):
    print('开始下载：', url)
    # 发送网络请求，下载图片
    response = requests.get(url)
    print('下载完成')
    # 图片保存到本地文件
    file_name = url.rsplit('/')[-1]
    with open(file_name, mode='wb') as fp:
        fp.write(response.content)

if __name__ == '__main__':
    url_list = [
        'http://image2.pearvideo.com/cont/20221012/13293812-170223-1.png',
        'http://image2.pearvideo.com/cont/20200729/cont-1688740-12438860.png',
        'http://image.pearvideo.com/cont/20210723/cont-1736170-12605892.png'
    ]

    for item in url_list:
        download_image(item)
```

### 协程方式（异步）

```python
import aiohttp
import asyncio

async def fetch(session, url):
    print('发送请求：', url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit('/')[-1]
        with open(file_name, mode='wb') as fp:
            fp.write(content)
        print('下载完成: ', url)
            
async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'http://image2.pearvideo.com/cont/20221012/13293812-170223-1.png',
            'http://image2.pearvideo.com/cont/20200729/cont-1688740-12438860.png',
            'http://image.pearvideo.com/cont/20210723/cont-1736170-12605892.png'
        ]
        
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        
        await asyncio.wait(tasks)
        
if __name__ == '__main__':
    asyncio.run(main())
```

## 异步编程

### 事件循环

理解成为一个死循环。去检测并执行某些代码。

```python
# 伪代码

任务列表 = ['任务1', '任务2', '任务3', ...]

while True:
    可执行的任务列表，已完成的任务列表 = 去任务列表中检查所有的任伤，将“可执行”和“已完成”的任务返回。

    for 就绪任务 in 可执行的任务列表:
        执行已就绪任务

    for 已完成的任务 in 已完成的任务列表:
        在任务列表中移除 已完成的任务

    如果 任务列表 中的任务都已完成，则终止循环
```

```python
import asyncio

# 去生成或获取一个事件循环
loop = asyncio.get_event_loop()

# 将任务放到 “任务列表”
loop.run_until_complete(任务)
```

### 快速上手

协程函数，定义函数的时候   async def 函数名
协程对象，执行 协程函数() 得到的就是协程对象

```python
async def fun():
    pass

result = func()

```

注意：执行协程函数创建协程对象，函数内部代码不会执行。
如果想要运行协程函数内部代码，必须要将协程对象交给事件循环来处理。

```python
import asyncio

async def func():
    print('快来搞我吧')

result = func()

# 去生成或获取一个事件循环
# loop = asyncio.get_event_loop()

# 将任务放到 “任务列表”
# loop.run_until_complete(result)

asyncio.run(result)   # python3.7 可以用这一行代替上边的两行
```

### await

await + 可等待的对象（协程对象, Future, Task对象）可以理解为 IO等待

#### 示例1

```python
import asyncio

async def func():
    print('来玩呀')
    response = await asyncio.sleep(2)   # 理解为网络IO请求
    print('结束', response)

asyncio.run(func())
```

#### 示例2

```python
import asyncio

async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '返回值'

async def func():
    print('执行协程函数内部代码')
    
    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行，当前协程挂机时，事件循环可以去执行其他协程（任务）。
    response = await others()
    print('IO请求结束，结果为：', response)
    
asyncio.run(func())
```

#### 示例3

一个协程函数里可有以多个 await 关键字  

```python
import asyncio

async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '返回值'

async def func():
    print('执行协程函数内部代码')
    
    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行，当前协程挂机时，事件循环可以去执行其他协程（任务）。
    response1 = await others()   
    print('IO请求结束，结果为：', response1)
    
    response2 = await others()
    print('IO请求结束，结果为：', response2)

asyncio.run(func())

```

注意： await就是等待对象的值得到结果之后再继续向下走。

await 关键字
await 关键字等待三种类型：协程对象、task 对象、future 对象(官网原话)。
await 是一个只能在协程函数中使用的关键字，用于遇到 IO 操作时挂起当前任务。
当前任务挂起过程后，事件循环可以去执行其他的任务。
当前协程 IO 处理完成时，可以再次切换回来执行 await 之后的代码。

[原文链接](https://blog.csdn.net/m0_51180924/article/details/124612674)

#### Task对象

- 在程序想要创建多个任务对象，需要使用 task 对象来实现。

- task 是用来调度协程并发执行的，也就是说事件循环中有多个 task 才能有并发的效果。

> 官网：<https://docs.python.org/3/library/asyncio-task.html>
>
> Tasks are used to schedule coroutines concurrently.
When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon。

本质上，asyncio.create_task() 是将协程对象封装成task对象，并立即加入事件循环，同时追踪协程的状态。

白话:在事件循环中添加多个任务的。
Tasks用于并发调度协程，通过 asyncio.create_task(协程对象)的方式创建Task对象，这样可以让协程加入事件循环中等待被调度执行。除了使用  asyncio.create_task() 函数以外，还可以用低层级 loop.create_task() 或 ensure_future() 函数。不建议手动实列化 Task 对象。

## Markdown 常用格式

```markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题

两个空格换行
分隔线：---
~~删除线~~
> 区块引用
换行：<br>
使用反斜杠转义特殊字符

*斜体文本*
**粗体文本**
***粗斜体文本***

A链接：
[文松博客](https://www.huwensong.com)
<https://www.huwensong.com>
[文松博客][1]
[1]: https://www.huwensong.com

img图片：
![文松博客图标](https://www.huwensong.com/favicon.ico)
<img src="https://www.huwensong.com/favicon.ico" width="50%">

list列表：
- 第一项
- 第二项
- 第三项

1. 第一项
2. 第二项
3. 第三项

table表格:
|  表头   | 表头  |
|  ----  | ----  |
| 单元格  | 单元格 |
| 单元格  | 单元格 |

值得一提的是，Markdown可以设置表格的对齐方式，语法示范如下：
-: 设置内容和标题栏居右对齐。
:- 设置内容和标题栏居左对齐。
:-: 设置内容和标题栏居中对齐。
可以自行进行尝试。
```
