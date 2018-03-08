from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get('https://www.baidu.com')
stop = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(stop).perform()
sleep(3)
driver.find_element_by_link_text('搜索设置').click()
sleep(3)
a = driver.find_element_by_id('nr')
Select(a).select_by_value('50')
sleep(10)
driver.quit()