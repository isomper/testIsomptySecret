#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time 
#导入驱动
sys.path.append("/testSimp/common/")
from _initDriver import *
#导入登录
sys.path.append("/testSimp/testCase/")
from test_login import *
#导入定位
sys.path.append("/testSimp/testCase/position")
from position_frame import *

class test_single:
    
    #点击账号按钮
    def set_button_user(self,browser):
        positionButtonUser = browser.find_element_by_css_selector("input[value=\"" +("账号").decode("utf-8")+ "\"]")
        positionButtonUser.click()
    
    #点击Crt
    def set_button_crt(self,browser):
        positionButtonCrt = browser.find_element_by_css_selector("img[alt=\"SecureCRT\"]")
        count = 50
        #循环点击50次CRT图标
        for i in range(count):            
            positionButtonCrt.click()

#打开驱动
starttime=datetime.datetime.now()
browser = initDriver().open_driver()

#登录
test_login().login_denglu(browser)
#定位
position_frame().leave_frame(browser)
position_frame().position_main(browser)

#点击账号按钮
test_single().set_button_user(browser)

counts = 1000
#循环1000次点击50次CRT的操作
for i in range(counts):
    
    #点击Crt
    test_single().set_button_crt(browser)

    time.sleep(4)
    #关闭所有CRT的进程
    command ='taskkill /f /im SecureCRT.exe'
    os.system(command)

#计算并打印耗时时间
endtime=datetime.datetime.now()
time = endtime-starttime
print time
