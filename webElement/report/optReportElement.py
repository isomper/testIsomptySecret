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
sys.path.append("/testIsompSecret/webElement/report")
from confReportElement import ConfReportPage

class OptReportPage():
    #资源账号
    RES_ACCOUNT_NAME = "fortAccountName"
    #资源名称
    RESOURCE_NAME = "fortResourceName"
    #资源组
    RESOURCE_GROUP = "fortResourceGroup"
    #资源ip
    RESOURCE_IP = "fortResourceIp"
    #勾选全部协议
    RESOURCE_ALL_PROTOCOL = "check_all_protocol"
    #勾选全部资源类型
    ALL_RESTYPE = "check_all_resourceType"
    #勾选全部字段
    SEL_ALL_FIELD = "check_all_field"
    #计划模板
    PLAN_MODULE = "quartzModule"
    #开关
    SWITCH = "onOroff"
    #轮循方式
    CYCLE_TYPE = "types"
    #每月几号
    DATENUM = "typesVal0"
    #执行时间
    EXECTIME = "execute_time"
    #选择邮件接收人
    SEL_EMAIL_USER_BTN = "illegal_command_receive_user"
    #邮件保存
    EMAIL_SAVE_BTN = "quartzSave"
    #邮件返回按钮
    EMAIL_BACK_BTN = "history_skip"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.tableElem = tableElement(self.driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)
        self.confReport = ConfReportPage(self.driver)
    
    u'''切换至运维审计报表'''
    def switch_to_opt_report(self):
        self.frameElem.from_frame_to_otherFrame("leftFrame")
        time.sleep(1)
        self.getElem.find_element_with_wait_clickable_and_click("id","url1")
    
    u'''计划报表开关状态变为开'''
    def set_switch_to_on(self):
        if self.cmf.switch_status("id",self.SWITCH) == 0:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.SWITCH)
    
    u'''计划报表开关状态变为关'''
    def set_switch_to_off(self):
        if self.cmf.switch_status("id",self.SWITCH) == 1:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.SWITCH)        
    
    u'''设置资源账号'''
    def set_res_account(self,resAccount):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        return self.confReport.set_common_func(resAccount,"id",self.RES_ACCOUNT_NAME)
    
    u'''设置资源名称'''
    def set_res_name(self,resName):
        return self.confReport.set_common_func(resName,"id",self.RESOURCE_NAME)
    
    u'''设置资源ip'''
    def set_res_ip(self,resIp):
        return self.confReport.set_common_func(resIp,"id",self.RESOURCE_IP)
    
    u'''选择资源组'''
    def select_res_group(self,resGroup):
        self.confReport.set_common_select_elem_by_text(resGroup,self.RESOURCE_GROUP)
    
    u'''选择轮询方式'''
    def sel_cycle_type(self,cycleType):
       self.confReport.set_common_select_elem_by_text(cycleType,self.CYCLE_TYPE)
    
    u'''选择执行日期'''
    def sel_cycle_date(self,cycleDate):
       self.confReport.set_common_select_elem_by_text(cycleDate,self.DATENUM) 
    
    u'''勾选checkbox'''
    def click_checkbox(self,type,value):
        try:
            elem = self.getElem.find_element_with_wait_EC(type,value)
            if elem.is_selected() == False:
                elem.click()
        except Exception as e:
            print ("checkbox selected error: ") + str(elem) + str(e)
    
    u'''取消勾选checkbox'''
    def quit_click_checkbox(self,type,value):
        try:
            elem = self.getElem.find_element_with_wait_EC(type,value)
            if elem.is_selected():
                elem.click()
        except Exception as e:
            print ("Quit checkbox selected error: ") + str(elem) + str(e)
    
    u'''勾选全部资源协议'''
    def sel_all_protocol(self):
        self.click_checkbox("id",self.RESOURCE_ALL_PROTOCOL)
    
    u'''取消勾选全部资源协议'''
    def unsel_all_protocol(self):
        self.quit_click_checkbox("id",self.RESOURCE_ALL_PROTOCOL)
    
    u'''勾选全部资源类型'''
    def sel_all_restype(self):
        self.click_checkbox("id",self.ALL_RESTYPE)
    
    u'''取消勾选全部资源类型'''
    def unsel_all_restype(self):
        self.quit_click_checkbox("id",self.ALL_RESTYPE)
        
    u'''勾选全部字段'''
    def sel_all_field(self):
        self.click_checkbox("id",self.SEL_ALL_FIELD)
    
    u'''取消勾选全部字段'''
    def unsel_all_field(self):
        self.quit_click_checkbox("id",self.SEL_ALL_FIELD)
    
    u'''否选单一协议类型或者资源类型'''
    def sel_sigle_type(self,valueStr):
        revalue = self.cnEnde.is_float(valueStr)
        typeXpath = "//input[@value=" + revalue + "]"
        if valueStr != "":
            self.click_checkbox("xpath",typeXpath)
        
    u'''设置执行时间
        parameters:
            time : 执行时间
    '''      
    def set_time(self,time):
        try:
            time_js = "$('input[id=execute_time]').attr('readonly',false)"
            self.driver.execute_script(time_js)  
            self.confReport.set_common_func(time,"id",self.EXECTIME)       
        except Exception as e:
            print ("Set time error: ") + str(e)
    
    u'''点击计划模板'''
    def plan_report_btn(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_with_wait_clickable_and_click("id",self.PLAN_MODULE)
        except Exception as e:
            print ("Click plan report button error : ") + str(e)   
    
    u'''点击选择邮件接收人'''
    def sel_email_user_btn(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.SEL_EMAIL_USER_BTN)
        except Exception as e:
            print ("Click select email user button error : ") + str(e)
    
    u'''点击保存'''
    def click_save(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            time.sleep(1)
            self.getElem.find_element_with_wait_clickable_and_click("id",self.EMAIL_SAVE_BTN)
        except Exception as e:
            print ("Click save button error :  ") + str(e)
            
    u'''点击返回'''
    def click_back(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_with_wait_clickable_and_click("id",self.EMAIL_BACK_BTN)
        except Exception as e:
            print ("Click back button error :  ") + str(e)
    
    u'''检查全部报表是否存在即将添加的报表  
            parameters:
                reportName : 报表名字
    '''
    def check_report_is_exist(self,reportName):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        isExsit = True
        try:
            selectd_elem = self.getElem.find_element_with_wait_EC("id","reportModules")
            allText = self.selectElem.get_all_option_text(selectd_elem)
            for num in range(len(allText)):
                if allText[num] == reportName:
                    isExsit = False
                    break
            return isExsit
        except Exception:
            print ("Check report is exist error ")