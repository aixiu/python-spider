# selenium模块

> selenium模块的基本使用  [səˈliːniəm] 斯里扭母
>
> 化妆品生产许可信息管理系统服务平台  <http://scxk.nmpa.gov.cn:81/xk/>  

## selenium模块和爬虫之间具有怎样的关联？

- 便捷的获取网站中的动态加载数据
- 便捷的实现模拟登

## 什么是selenium模块？

- 基于浏览器自动化的一个模块。

## selenium使用流程

- 环境安装：pip install selenium

- 下载一个浏览器的驱动程序
  - python中用Selenium驱动Edge浏览器的方法
  - 在这个网址： <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/>
  - 下载你电脑Microsoft Edge对应的版本的WebDriver。
  - 下载完之后解压压缩包，并把相应的msedgedriver.exe执行文件，复制粘贴到我们电脑python安装位置的scripts目录下即可：
  - <https://blog.csdn.net/Superman980527/article/details/123946723>

- 实例化一个浏览器对象

- 编写基于浏览器自动化的操作代码
  - 发起请求：get(url)
  - 标签定位：find_element()方法
  - 标签交互：send_keys('字符串')
  - 执行JS程序：execute_script('js代码')
  - 前进，后退：back(), forward()
  - 关闭浏览器：quit()

- selenium处理iframe
  - 如果定位的标签存在于iframe标签之中，则必须使用switch_to.frame(id)
  - 动作链（拖动）：from selenium.webdriver import ActionChains
    - 实例化一个动作链对象：action =ActionChains(bro)
    - 长按且点击操作：action.click_and_hold(div)
    - 拖动的方向和像素：move_by_offset(x, y)
    - .perform()让动作链立即执行
    - action.release()释放动作链对象

- 12306模拟登录
