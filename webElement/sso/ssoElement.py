#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：顾亚茹
#生成日期：2017-08-03
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import win32api
import win32con

import os
import time
from selenium.webdriver.common.action_chains import ActionChains

sys.path.append("/testIsomp/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log
from _fileRead import fileRead

sys.path.append("/testIsomp/webElement/sso/")
from keyapi import Command

class SsoPage():
    #IP或名称
    IP_OR_NAME = "query_ip_or_name"
    #sso列表table元素xpath
    TABLE_XPATH = "html/body/div[1]/div[7]/div[2]/div[1]/table[@id='content_table']"
    #mstsc账号
    MSTSC_ACCOUNT = "ssoAccount"
    #mstsc口令
    MSTSC_PWD = "ssoPasswd"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.tableElem = tableElement(self.driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)
        self.command = Command()
        self.action = ActionChains(self.driver)
    
    u'''通过name属性获取所在行数
            parameters : 
                - nameValue : name属性值
                - resName : 资源名字
    '''
    def get_resource_row(self,nameValue,resName):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        reName = self.cnEnde.is_float(resName)
        row = 0
        try:
            text_list = self.driver.find_elements_by_name(nameValue)
            for fortNameValue in text_list:
                row = row + 1
                if fortNameValue.text == reName:
                    break
        except Exception:
            print nameValue + "is not exsit."
        return row
    
    u'''选择账号
            parameters:
                - resName:资源名称
                - account:账号
    '''
    def select_account(self,resName,seAccount):
        reaccount = self.cnEnde.is_float(seAccount)
        row = self.get_resource_row("fortResourceName",resName)
        selectXpath = "//table[@id='content_table']/tbody/tr[" + str(2*row-1) + "]/td[6]/select"
        time.sleep(1)
        seElem = self.getElem.find_element_with_wait_EC("xpath",selectXpath)
        self.selectElem.select_element_by_visible_text(seElem,reaccount)
    
    u'''选择登录图标
            parameters:
                - resName:资源名称
                - iconName:图标名称
    '''    
    def select_sso_icon(self,resName,iconName):
        reiconName = "'%s'"%eval('iconName')
        row = self.get_resource_row("fortResourceName",resName)
        #资源名称路径
        resname_xpath = "//table[@id='content_table']/tbody/tr[" + str(2*row-1) + \
        "]/td[2]"
        #resElem = self.getElem.find_element_with_wait_EC("xpath",resname_xpath)
        self.getElem.find_element_wait_and_click_EC("xpath",resname_xpath)
        #self.action.click_and_hold(resElem)
        img_xpath = "/html/body/div[1]/div[7]/div[2]/div/table[@id='content_table'] \
        /tbody/tr[" + str(2*row) + "]/td[@id='open01']/div/table/tbody/tr/td[2]/a[@alt=" + reiconName + "]/img"
        self.getElem.find_element_wait_and_click_EC("xpath",img_xpath)
    
    u'''选择登录协议
            parameters :
                protocol : 协议类型
    '''
    def select_protocol(self,protocol):
        self.frameElem.from_frame_to_otherFrame("artIframe")
        seProtocol = self.getElem.find_element_with_wait_EC("id","select_protocol")
        self.selectElem.select_element_by_visible_text(seProtocol,protocol)
        self.cmf.click_login_msg_button()
    
    u'''按下chrome启动应用'''
    def execute_chrome_key(self):
        time.sleep(1)
        self.command.peration_key("left_arrow")
        time.sleep(1)
        self.command.peration_key("enter")
        time.sleep(2)
    
    u'''在呼起的应用里面执行命令
            parameters:
                exePath : au3可执行文件路径
                iconType : 图标class
                username : 账号
                pwd : 密码
                cmdList : 命令集
    '''
    def opt_cmd(self,exePath,iconType,username,pwd,cmdList):
        reiconType = self.cnEnde.is_float(iconType)
        rename = self.cnEnde.is_float(username)
        rePwd = self.cnEnde.is_float(pwd)
        recmdList = self.cnEnde.is_float(cmdList)
        reList = str(recmdList)
        os.popen(exePath + " " + iconType + " " + username + " " + pwd + " " \
        + reList)
    
    u'''根据浏览器类型进行单点登录'''
    def choice_browser(self,iconType,username,pwd,cmdList):
        fileList = fileRead().get_ip_address()
        browserType = fileList[1].strip('\n')
        if browserType == '1':
            self.execute_chrome_key()
        elif browserType != '0' or browserType != '1' :
            self.opt_cmd("\\testIsomp\\webElement\\sso\\sso_firefox.exe","", \
            "","","")        
        self.opt_cmd("\\testIsomp\\webElement\\sso\\sso_client.exe",iconType, \
        username,pwd,cmdList)
        
#-----------------------------------RDP相关-----------------------------------
    u'''填写不代填用户和密码类型的账号'''
    def set_mstsc_account(self,account):
        reaccount = self.cnEnde.is_float(account)
        self.frameElem.from_frame_to_otherFrame("artIframe")
        self.getElem.find_element_wait_and_sendkeys("id",self.MSTSC_ACCOUNT,reaccount)
    
    u'''填写不代填用户和密码类型的密码'''
    def set_mstsc_pwd(self,pwd):
        repwd = self.cnEnde.is_float(pwd)
        self.frameElem.from_frame_to_otherFrame("artIframe")
        self.getElem.find_element_wait_and_sendkeys("id",self.MSTSC_PWD,repwd)
        
#-----------------------------------数据库相关--------------------------------
    u'''选择应用发布'''
    def select_app(self,resName,appName):
        reName = self.cnEnde.is_float(appName)
        row = self.get_resource_row("fortResourceName",resName)
        selectXpath = "//table[@id='content_table']/tbody/tr[" + str(2*row) + \
        "]/td[@id='open01']/div/table/tbody/tr/td[1]/select"
        seElem = self.getElem.find_element_with_wait_EC("xpath",selectXpath)
        self.selectElem.select_element_by_visible_text(seElem,reName)
    
    u'''选择应用发布和登录图标
            parameters:
                - resName:资源名称
                - iconName:图标名称
                - appName : 应用发布名称
    '''    
    def select_app_and_sso_icon(self,resName,appName,iconName):
        reiconName = "'%s'"%eval('iconName')
        row = self.get_resource_row("fortResourceName",resName)
        #资源名称路径
        resname_xpath = "//table[@id='content_table']/tbody/tr[" + str(2*row-1) + \
        "]/td[3]"
        self.getElem.find_element_wait_and_click_EC("xpath",resname_xpath)
        self.select_app(resName,appName)
        img_xpath = "/html/body/div[1]/div[7]/div[2]/div/table[@id='content_table']/tbody/tr[" \
         + str(2*row) + "]/td[@id='open01']/div/table/tbody/tr/td[4]/a[@alt=" \
        + reiconName + "]/img"
        self.getElem.find_element_wait_and_click_EC("xpath",img_xpath)
    
            
            
        
        
        
 
            
        
        


 
        
    

        
        
        
        