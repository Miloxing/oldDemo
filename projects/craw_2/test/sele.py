# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 设置窗口大小
driver.set_window_size(800, 700)

driver.get('http://baidu.com')

# 百度输入框输入 selelnium python 回车
driver.find_element_by_id("kw").send_keys("selenium python\n")

time.sleep(2)
# 向下滚动200个像素
driver.execute_script('window.scrollBy(0,200)')

time.sleep(2)
# 滚动至元素ele可见位置
eles = driver.find_elements_by_css_selector('#rs table tr th a')
ele = eles[0]
driver.execute_script("arguments[0].scrollIntoView();",ele)

time.sleep(2)
# 向右滚动200个像素
driver.execute_script('window.scrollBy(200,0)')

time.sleep(2)
driver.quit()