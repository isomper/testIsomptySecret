#coding=utf-8
u''' 
#文件名：login
#被测软件版本号：V2.8.1
#作成人：顾亚茹
#生成日期：2017-06-10
#模块描述：登录页面
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time

sys.path.append("/testIsompSecret/common/")
from _icommon import getElement,selectElement,frameElement,commonFun
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName


class loginPage(object):
    #登录方式
    LOGIN_METHOD = "loginMethod"
    #用户名(ad+口令)
    LOGIN_USERNAME = "username"
    #AD域方式用户名
    LOGIN_LDAP_USERNAME = "ldapUsername"
    #口令(ad+口令)
    LOGIN_PWD = "pwd"
    #AD域方式口令
    LOGIN_LDAP_PWD = "ldapPwd"
    #radius+口令登录方式口令
    LOGIN_RADIUS_PWD = "radiusPwd"
    #登录按钮
    LOGIN_BUTTON = "do_login"
    #系统名称
    LOGIN_SYSTEM_NAME = "systemName"
    #帮助与控件下载
    LOGIN_DOWNLOAD = "/html/body/div[2]/div[5]/a"
    #版权所有
    LOGIN_COPYRIGHT = "/html/body/div[2]/div[5]/text()[2]"
    #访问失败次数
    ACCESS_MAX_ACCOUNT = "lockStrategyCount"
    #会话策略保存按钮
    STRATEGY_SAVE_BUTTON = "save_globalStrategy"
    #退出
    QUIT = "logout"

    def __init__(self,driver):

        self.driver = driver
        self.getElem = getElement(self.driver)
        self.dataFile = dataFileName()
        self.selectElem = selectElement(self.driver)
        self.frameElem = frameElement(self.driver)
        self.commElem = commonFun(self.driver)
        self.cmf = commonFun(self.driver)
        self.cnEnde = cnEncode()
        self.log = log()

    u'''获取登录方式'''
    def get_login_method(self):
        loginMethod = self.getElem.find_element_with_wait_EC('id',self.LOGIN_METHOD)
        return self.selectElem.get_option_text(loginMethod,0)
        
    u'''设定登录方式
            parameters : 
                value : 登录方式value值
    '''
    def set_login_method(self,value): 
        revalue = self.cnEnde.is_float(value)
        loginMethod = self.getElem.find_element_with_wait_EC('id', self.LOGIN_METHOD)
        try:
            self.selectElem.select_element_by_value(loginMethod,str(revalue))
        except Exception as e:
            self.log.error_detail("login type error",e)

    u'''填写变量内容
        parameters:
            var_text : 变量内容
            locator : 定位方式对应的属性值
    '''       
    def set_common_var_text(self,var_text,value):
        try:
            revar_text = self.cnEnde.is_float(var_text)
            var_elem = self.getElem.find_element_with_wait_EC('id',value)
            var_elem.clear()
            var_elem.send_keys(revar_text)
        except Exception as e:
            print ("set login var text error: ") + str(revar_text) + str(e)
        
    u'''填写用户账号
        parameters:
            account : 用户账号
    '''       
    def set_login_username(self,account):
        return self.set_common_var_text(account,self.LOGIN_USERNAME)
            
    u'''填写AD域用户名
        parameters:
            account : AD域用户账号
    '''
    def set_ad_login_username(self,adUsername):
        return self.set_common_var_text(adUsername,self.LOGIN_LDAP_USERNAME)
        
    u'''填写口令
        parameters:
            account : 口令
    '''
    def set_login_pwd(self,pwd):
        return self.set_common_var_text(pwd,self.LOGIN_PWD)
            
    u'''填写填写AD域密码
        parameters:
            account : AD域密码
    '''
    def set_ad_login_pwd(self,adPwd):
        return self.set_common_var_text(adPwd,self.LOGIN_LDAP_PWD)
            
    u'''填写填写RADIUS密码
        parameters:
            account : RADIUS密码
    '''    
    def set_radius_login_pwd(self,radiusPwd):
        return self.set_common_var_text(radiusPwd,self.LOGIN_RADIUS_PWD)
        
    u'''点击登录按钮'''
    def click_login_button(self):
        try:
            time.sleep(1)
            self.getElem.find_element_wait_and_click_EC('tagname','body')
            self.getElem.find_element_with_wait_clickable_and_click('id',self.LOGIN_BUTTON)

        except Exception as e:
            self.log.error_detail("click login button error",e)

        pass
        
    u'''用户名口令认证登录
            parameters:
                list : 登录用户列表信息
    '''
    def login(self,list):
        time.sleep(2)
        self.frameElem.switch_to_content()
        self.set_login_method(list[2])
        self.set_login_username(list[3])
        self.set_login_pwd(list[4])
        self.click_login_button()
    
    u'''判断是否登陆成功'''
    def is_login_success(self):
        success = False
        try:
            self.frameElem.from_frame_to_otherFrame('topFrame')
            text = self.getElem.find_element_wait_and_get_text("id","message",10)
        except Exception as e:
            text = ""
        
        if text == "个人信息维护":
            success = True

        return success
        
    u'''AD域认证登录
            parameters:
                list : 登录用户列表信息
    '''    
    def ad_login(self,list):
        self.frameElem.switch_to_content()
        self.set_login_method(int(list[2]))
        self.set_ad_login_username(list[3])
        self.set_ad_login_pwd(list[5])
        self.click_login_button()
        
    u'''AD域+口令认证登录
            parameters:
                list : 登录用户列表信息
    '''   
    def ad_pwd_login(self,list):
        self.frameElem.switch_to_content()
        self.set_login_method(int(list[2]))
        self.set_login_username(list[3])
        self.set_login_pwd(list[4])
        self.set_ad_login_pwd(list[5])
        self.click_login_button()
    
    u'''Radius认证登录
            parameters:
                list : 登录用户列表信息
    '''
    def radius_pwd_login(self,list):
        self.frameElem.switch_to_content()
        self.set_login_method(list[2])
        self.set_login_username(list[3])
        self.set_login_pwd(list[4])
        self.set_radius_login_pwd(list[5])
        self.click_login_button()
        
    #证书认证登录
    def cert_login(self,list):
        brower_name = self.driver.capabilities['browserName']
        
    u'''设置访问失败最大次数
            parameters:
                roleName : 角色名称
    '''
    def set_max_login_count(self):
        
        self.frameElem.from_frame_to_otherFrame('topFrame')

        self.commElem.select_menu(u"策略配置",u"会话配置")
        
        self.frameElem.from_frame_to_otherFrame('mainFrame')

        #选择密码策略默认配置
        strategy_option = self.getElem.find_element_with_wait_EC('id','fortPasswordStrategyId')
        self.selectElem.select_element_by_value(strategy_option, "1000000000001")
        
        #设置最大登录数
        self.set_common_var_text(3,self.ACCESS_MAX_ACCOUNT)

        #设定锁定时间
        self.set_common_var_text(1,"lockStrategyTime")
        
        #点击保存按钮
        self.getElem.find_element_with_wait_clickable_and_click('id',self.STRATEGY_SAVE_BUTTON)
        self.commElem.click_login_msg_button()

    u'''点击退出'''
    def quit(self):
        self.frameElem.from_frame_to_otherFrame('topFrame')
        try:
            login_elem = self.getElem.find_element_with_wait_EC('id',self.QUIT)
            if login_elem.is_displayed():
                time.sleep(1)
                login_elem.click()
        except Exception as e:
            print ("Click quit button error: ") + str(e)
