#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：顾亚茹
#生成日期：2018-01-24
#模块描述：配置审计报表元素
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import time

sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

class ConfReportPage():
    #表单模板名称
    MODULE_NAME = "moduleName"
    #添加模板按钮
    ADD_MODULE_BTN = "addModule"
    #选择表单模板
    SELECT_REPORT = "reportModules"
    #删除模板
    DEL_MODULE = "delModule"
    #用户账号
    USER_ACCOUNT = "fortUserAccount"
    #用户名称
    USER_NAME = "fortUserName"
    #用户组
    USER_GROUP = "fortUserGroup"
    #模块
    SELECT_MODULE = "fortModule"
    #全选
    CHECK_ALL = "check_all"
    #查询报表
    QUERY_REPORT = "queryReport"

    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.tableElem = tableElement(self.driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)
    
    u'''填写变量内容
        parameters:
            var_text : 变量内容
            type : 定位方式
            value : 定位方式对应的值
    '''      
    def set_common_func(self,var_text,type,value):
        try:
            revar_text = self.cnEnde.is_float(var_text)
            var_elem =self.getElem.find_element_with_wait_EC(type,value)
            var_elem.clear()
            var_elem.send_keys(revar_text)
        except Exception as e:
            print ("Set report config common text error: ") + str(revar_text) + str(e)    
    
    u'''设置表单名称'''
    def set_module_name(self,moduleName):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        time.sleep(1)
        return self.set_common_func(moduleName,"id",self.MODULE_NAME)
    
    u'''填写用户账号'''
    def set_user_account(self,userAccount):
        return self.set_common_func(userAccount,"id",self.USER_ACCOUNT)
    
    u'''填写用户名称'''
    def set_user_name(self,userName):
        return self.set_common_func(userName,"id",self.USER_NAME)
    
    u'''勾选字段'''
    def click_field(self):
        try:
            selem = self.getElem.find_element_with_wait_EC("id",self.CHECK_ALL)
            if selem.is_selected() == False:
                selem.click()
        except Exception as e:
            print ("Click field error: ") + str(e)
    
    u'''取消勾选字段'''
    def quit_click_field(self):
        try:
            selem = self.getElem.find_element_with_wait_EC("id",self.CHECK_ALL)
            if selem.is_selected():
                selem.click()
        except Exception as e:
            print ("Click field error: ") + str(e)
    
    u'''点击添加模板'''
    def click_add_module(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.ADD_MODULE_BTN)
        except Exception as e:
            print ("Click add module error: ") + str(e)
    
    u'''点击删除模板'''
    def click_del_module(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.DEL_MODULE)
        except Exception as e:
            print ("Click del module error: ") + str(e)
    
    u'''点击查询报表'''
    def click_query_report(self):
        try:
            time.sleep(1)
            self.getElem.find_element_with_wait_clickable_and_click("id",self.QUERY_REPORT)
        except Exception as e:
            print ("Click query report error: ") + str(e)     
    
    u'''select元素通过text选择元素通用方法
            parameter:
                var_text : select元素option选项text的值
                value : ID值
    '''    
    def set_common_select_elem_by_text(self,var_text,value):
        try:
            revar_text = self.cnEnde.is_float(var_text)
            select_elem = self.getElem.find_element_with_wait_EC('id',value)
            self.selectElem.select_element_by_visible_text(select_elem,str(var_text))
        except Exception as e:
            print ("selected select element option  by visible text error: ") + str(revar_text) + str(e)
    
    u'''选择模板名称'''
    def select_report(self,reportName):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        self.set_common_select_elem_by_text(reportName,self.SELECT_REPORT)
    
    u'''选择用户组'''
    def select_group(self,userGroup):
        self.set_common_select_elem_by_text(userGroup,self.USER_GROUP)
    
    u'''选择模块'''
    def select_module(self,moduleName):
        self.set_common_select_elem_by_text(moduleName,self.SELECT_MODULE)
    
    u'''切换至配置报表'''
    def switch_to_conf_report(self):
        self.frameElem.from_frame_to_otherFrame("leftFrame")
        time.sleep(1)
        self.getElem.find_element_with_wait_clickable_and_click("id","url0")
            