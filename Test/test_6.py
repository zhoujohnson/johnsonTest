import time,unittest
from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': '4df10c8e24e65f75',#可有可无
    #'platformVersion': '4.1.1',
    # apk包名
    'appPackage': 'com.xiaoenai.app',
    # apk的launcherActivity
    'appActivity': '.presentation.launcher.LauncherActivity',
    #如果存在activity之间的切换可以用这个
    # 'appWaitActivity':'.MainActivity',
    'unicodeKeyboard': True,
    #隐藏手机中的软键盘
    'resetKeyboard': True,
    # Android 8.0需增加
    #'automationName' : 'UIAutomator2'
    }
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)   #打开小恩爱
driver.implicitly_wait(3)
driver.find_element_by_id('com.xiaoenai.app:id/account_editText').send_keys('4615129016')
driver.implicitly_wait(3)
driver.find_element_by_id('com.xiaoenai.app:id/password_editText').send_keys('123456')
driver.implicitly_wait(3)
driver.find_element_by_id("com.xiaoenai.app:id/login_btn").click()
driver.implicitly_wait(3)
driver.quit()