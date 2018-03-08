from selenium import webdriver
from time import sleep

driver =webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('johnson')
driver.find_element_by_id('su').click()

#  截取当前窗口，并指定截图图片的保存位置
driver.get_screenshot_as_png('/johnson')
driver.quit()