from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.youdao.com")

#获得cookie信息
#cookie = driver.get_cookies()

# 打印出cookie信息
#   print(cookie)
# 向cookie的name和value中添加会话信息
driver.add_cookie({'name':'johnson','value':'love'})

# 遍历cookies中name和value信息并打印
for cookie in driver.get_cookies():
    print ("%s : %s"%(cookie['name'],cookie['value']))

driver.quit()

