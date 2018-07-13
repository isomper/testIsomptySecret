#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：顾亚茹
#生成日期：2018-01-29
#模块描述：运维审计检索功能元素
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
sys.path.append("/testIsompSecret/webElement/audit_management")
from systemLogElement import SystemLogPage
sys.path.append("/testIsompSecret/webElement/user/")
from userElement import UserPage

class AuditLogPage():
    #选择年
    SELECT_YEAR = "fortAuditLogYear"
    #选择月
    SELECT_MOUTH = "fortAuditLogMonth"
    #选择日
    SELECT_DAY = "fortAuditLogDay"
    #选择审计
    SELECT_AUDIT = "showListTypeName"
    #本部门资源本部门人员
    THIS_DEP_RES_PEP = "fontresourcePeople"
    #本部门资源非本部门人员
    THIS_RES_NOT_PEP = "fontresourceNotPeople"
    #本部门人员-非本部门资源
    THIS_PEP_NOT_RES = "fontpeopleNotResource"
    #高级
    HIGH_LEVEL = "btn_qh"
    #运维协议
    OPT_PRO = "operationsProtocol"
    #资源账号
    RES_ACCOUNT = "fortAccountName"
    #用户名称
    USER_NAME = "fortAuditIdOrUser"
    #目标IP/名称
    CLIENT_IP = "fortClientIpOrName"
    #开始时间
    START_TIME = "fortStartTime"
    #结束时间
    END_TIME = "fortEndTime"
    #关键字
    KEY_WORD = "query_key_word"
    #登录IP
    SOURCE_IP = "sourceIP"
    #用户账号
    USER_ACCOUNT = "fortUserAccountName"
    #检索class
    CLICK_QUERY = "retFortAuditLog"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.tableElem = tableElement(self.driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)
        self.systemLog = SystemLogPage(self.driver)
        self.userElem = UserPage(driver)
    
    u'''选择年月日'''
    def select_date(self,dateList):
        date = dateList.split(",")
        if dateList != "":
            self.select_option(self.SELECT_YEAR,date[0])
            self.select_option(self.SELECT_MOUTH,date[1])
            self.select_option(self.SELECT_DAY,date[2])
    
    u'''选择运维协议类型'''
    def select_audit_type(self,proType):
        self.systemLog.set_common_select_elem_by_text(proType,self.OPT_PRO)
    
    u'''点击选择审计'''
    def click_select_audit(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.SELECT_AUDIT)
        except Exception as e:
            print ("Click select audit button error: ") + str(e)
    
    u'''选择三种中的一种审计类型
        parameters:
            - status:选择审计的类型(1:本部门资源非本部门人员,2:本部门人员-非本部门资源)
    '''
    def select_audit(self,status):
        time.sleep(1)
        if status == "1":
            self.getElem.find_element_with_wait_clickable_and_click("id",self.THIS_RES_NOT_PEP)
        elif status == "2":
            self.getElem.find_element_with_wait_clickable_and_click("id",self.THIS_PEP_NOT_RES)
        self.getElem.find_element_with_wait_clickable_and_click("id",self.THIS_DEP_RES_PEP)
    
    u'''点击高级'''
    def click_high_level(self,state):
        try:
            if state == "1":
                self.getElem.find_element_with_wait_clickable_and_click("id",self.HIGH_LEVEL)
        except Exception as e:
            print ("Click high level button error: ") + str(e)
    
    u'''点击检索'''
    def click_search(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.CLICK_QUERY)
            time.sleep(1)
        except Exception as e:
            print ("Click search button error: ") + str(e)
    
    def set_common_func(self,var_text,type,value):
        try:
            revar_text = self.cnEnde.is_float(var_text)
            var_elem =self.getElem.find_element_with_wait_EC(type,value)
            var_elem.clear()
            var_elem.send_keys(revar_text)
        except Exception as e:
            print ("Set audit log common text error: ") + str(revar_text) + str(e)
    
    u'''设置资源账号'''
    def set_res_account(self,resAccount):
        return self.set_common_func(resAccount,"id",self.RES_ACCOUNT)
    
    u'''设置用户名称'''
    def set_user_name(self,userName):
        return self.set_common_func(userName,"id",self.USER_NAME)
    
    u'''设置目标IP/名称'''
    def set_client_ip(self,clientIp):
        return self.set_common_func(clientIp,"id",self.CLIENT_IP)
    
    u'''设置关键字'''
    def set_key_word(self,keyWord):
        return self.set_common_func(keyWord,"id",self.KEY_WORD)
    
    u'''设置登录IP'''
    def set_source_ip(self,sourceIp):
        return self.set_common_func(sourceIp,"id",self.SOURCE_IP)
    
    u'''设置用户账号'''
    def set_user_account(self,userAccount):
        return self.set_common_func(userAccount,"id",self.USER_ACCOUNT)
    
    u'''检查给定的年月日是否存在  
            parameters:
                seleValue : select元素id的value值
    '''
    def select_option(self,seleValue,option):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            selectd_elem = self.getElem.find_element_with_wait_EC("id",seleValue)
            allText = self.selectElem.get_all_option_text(selectd_elem)
            if allText != "请选择" and option in allText:
                self.selectElem.select_element_by_visible_text(selectd_elem,option)
            elif allText == "请选择" or (allText != "请选择" and option not in allText):
                self.selectElem.select_element_by_visible_text(selectd_elem,"请选择")
        except Exception as e :
            print ("Select option error: ") + str(e)
    
    u'''选择部门'''
    def select_depmt(self,deptname):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.getElem.find_element_wait_and_click_EC("id","department_name")
        elem = self.getElem.find_element_with_wait_EC('id','cc_1_switch')
        elem_class = elem.get_attribute('class')
        #点开部门箭头
        if elem_class.split('_')[-1] != "open":
            self.getElem.find_element_wait_and_click_EC('id','cc_1_switch')
        self.userElem.get_tag_by_a(deptname)
    
