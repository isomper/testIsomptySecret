#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：张泽方
#生成日期：
#模块描述：使用授权
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,frameElement,commonFun
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/user/")
from userElement import UserPage


class UseAuth():
    #客户名称
    CUST_NAME = "customerName"
    #系统名称
    SYSTEM_NAME = "systemName"
    #浏览图片按钮
    LOGO_IMAGE = "logoImage"
    #上传图片按钮
    UP_LOGO = "uploadLogo"
    #保存
    SAVE_BUTTON = "save"
    #更新按钮
    UPDATAAUTH = "updateAuth"
    #授权码
    AUTHCODE = "authCode"

    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.dataFile = dataFileName()
        self.frameElem = frameElement(self.driver)
        self.user = UserPage(driver)
    
    #点击保存
    def save_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.SAVE_BUTTON)
        except Exception as e:
            print ("save button error: ") + str(e)
    
    #点击上传按钮
    def up_logo_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.UP_LOGO)
        except Exception as e:
            print ("up logo button error: ") + str(e)
    
    #点击更新按钮
    def click_updateAuth_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.UPDATAAUTH)
        except Exception as e:
            print ("click updateAuth button error: ") + str(e)
    
    #填写授权码
    def add_authcode_name(self,authCode):
        try:
            self.getElem.find_element_wait_and_clear_EC('id',self.AUTHCODE)
            time.sleep(1)
            return self.user.set_common_func(authCode,self.AUTHCODE)
        except Exception as e:
            print ("authCode error: ") + str(e)
        
    #填写客户名称
    def add_customer_name(self,custname):
        return self.user.set_common_func(custname,self.CUST_NAME)
    
    #填写系统名称
    def add_system_name(self,sysname):
        return self.user.set_common_func(sysname,self.SYSTEM_NAME)

    u'''点击浏览图片操作和校验
        parameter:
            index:1代表上传logo,2代表校验浏览图片操作
    '''
    def click_or_check_logo(self,index):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            if index == 1:
                value = "E://testIsompSecret/testData/envelope_image.png"
            elif index == 2:
                value = "E://testIsompSecret/testData/use_of_authorization.xlsx"
            self.getElem.find_element_wait_and_sendkeys('id',self.LOGO_IMAGE,value)
        except Exception as e:
            print ("click  and check up logo button error: ") + str(e)