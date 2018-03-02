from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# 获得当前窗口下钉句柄
now_handle = driver.current_window_handle
print (now_handle)
driver.find_element_by_link_text('登录').click()
driver.implicitly_wait(5)
driver.find_element_by_link_text('立即注册').click()
driver.implicitly_wait(3)
# 获得所有窗口的句柄到到当前会话
all_handle = driver.window_handles
for a in all_handle:
    if a != now_handle:
        driver.switch_to_window(a)
print ('切换为下一个窗口，进行注册操作')
driver.implicitly_wait(3)
driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys('强哥哥是猛男')
time.sleep(10)
driver.quit()