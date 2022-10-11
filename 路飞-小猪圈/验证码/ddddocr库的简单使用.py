# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Aixiu
# @Time  : 2022/10/11 22:51:53


# 项目地址：https://github.com/sml2h3/ddddocr
# 安装：pip install ddddocr

'''
    相关文档：
        - https://blog.csdn.net/fun_sn/article/details/125421983
        
        -  import ddddocr
            ocr = ddddocr.DdddOcr()
            with open("test.jpg", 'rb') as f:
                image = f.read()
            res = ocr.classification(image)
            print(res)
'''

import ddddocr

def recognize():
    ocr = ddddocr.DdddOcr()
    with open('./code_img/VerifyCode.png', 'rb') as fp:
        img_bytes = fp.read()
    res = ocr.classification(img_bytes)
    print(res)

recognize()



