# -*-coding:utf-8-*-

from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
time.sleep(3)
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector('#kw').send_keys('selenium')
time.sleep(2)
driver.find_element_by_id('su').click()
#driver.implicitly_wait(4)
#driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
#time.sleep(8)
# 参数数字为像素点

#print ('设置浏览器宽480，高800显示')
#driver.set_window_size(480,800)

# 控制浏览器前进后退
'''print ('控制浏览器后退')
driver.back()
time.sleep(5)
print ('控制浏览器前进')
driver.forward()
time.sleep(3)
# 控制浏览器刷新
#print ('控制浏览器刷新')
#driver.refresh()
time.sleep(10)'''

'''print ("查看url位置信息")
location = driver.find_element_by_xpath('//*[@id="4001"]/div[1]/h3/a[1]').size
print (location)
time.sleep(4)
print ('查看url文本信息')
driver.implicitly_wait(3)
text1= driver.find_element_by_xpath('//*[@id="content_left"]/div[1]/div/span/strong').text
print (text1)
driver.implicitly_wait(3)
print ('查看元素属性')
attribute = driver.find_element_by_xpath('//*[@id="4001"]/div[1]/h3/a[1]').get_attribute('type')
print (attribute)
driver.implicitly_wait(3)
print ('查看元素结果是否可见')
result = driver.find_element_by_xpath('//*[@id="content_left"]/div[1]/div/span/strong').is_displayed()
print (result)'''
#print ('查看鼠标悬停')
#定位到要悬停的位置
#float1 = driver.find_element_by_link_text('设置')
#对定位到的元素执行鼠标悬停操作
#ActionChains(driver).move_to_element(float1).perform()
#driver.implicitly_wait(5)
#driver.quit()
# 定位一组元素
texts = driver.find_elements_by_xpath('//div/h3/a')
# 循环遍历出每一条搜索结果
for i in texts:
    print (i.texts)
driver.quit()