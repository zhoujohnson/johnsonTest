from selenium import webdriver
import os
#找到HTML文件打开
driver= webdriver.Chrome()
# 要使用file协议的格式：file:///
file_path = "file:///work/johnsonTest"+os.path.abspath('upfile.html')
driver.get(file_path)

#定位上传按钮，添加本地文件
driver.find_element_by_name('file').send_keys('/work/johnsonTest/test.txt')
