# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/14 16:03:29

'''
下载图片使用第三方模块 aiohttp，请提前安装：pip install aiohttp
'''

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
 