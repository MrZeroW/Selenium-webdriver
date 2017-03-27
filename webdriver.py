import time
from selenium import webdriver

#打开百度
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
#窗口最大化
driver.maximize_window()
#设置窗口大小
driver.set_window_size(450, 450)
#窗口位置
driver.set_window_position(1000, 0)
#打印标题
print driver.title
#待机3秒
time.sleep(3)

#打开新闻
driver.find_element_by_css_selector('#u1 > a:nth-child(2)').click()
#后退
driver.back()
#前进
driver.forward()

#回到了新闻页面，清除输入框
driver.find_element_by_css_selector('#ww').clear()
#输入内容
driver.find_element_by_css_selector('#ww').send_keys(u'萨德')
#点击搜索
driver.find_element_by_css_selector('#ww').click()

#打印文本
print driver.find_element_by_css_selector('#u1 > a:nth-child(2)').text

#退出浏览器
driver.quit()
#关闭窗口
driver.close()

#模拟键盘事件
#首先要导入Keys
from selenium.webdriver.common.keys import Keys
#通过调用send_keys()函数模拟键盘动作
send_keys(Keys.TAB)  #Tab
send_keys(Keys.ENTER)  #回车
#组合键
#ctrl + a 全选
send_keys(Keys.CONTROL, 'a')
#ctrl + x 剪切 类似的、

#####重点来了，模拟鼠标事件
#ActionChains类
#	context_click() 右击	
#	double_click() 双击
#	drag_and_drop() 拖动
#move_to_element() 鼠标移动
#这里的用法稍有不同
#导入ActionChains
from selenium.webdriver.common.action_chains import ActionChains
#定位到元素
pp = driver.find_by.....
#右击
ActionChains(driver).context_click(pp).perform()
#双击和右击类似
#下面是拖放
#	先定位原位置和目标位置
element = driver.find_.....
target = driver.find_.....
#		拖放操作
ActionChains(driver).drag_and_drop(element, target).perform()
#鼠标移动
ActionChains(driver).move_to_element(pp).perform()
#之后还有一些操作，目前还用不到，参考文档：https://wenku.baidu.com/view/211fbafecc7931b764ce1550.html
#从28页之后还未仔细学习
