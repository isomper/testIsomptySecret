#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：顾亚茹
#生成日期：2018-01-29
#模块描述：配置审计检索功能元素
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

class SystemLogPage():
    #选择年
    SELECT_YEAR = "fortLogYear"
    #选择月
    SELECT_MOUTH = "fortLogMonth"
    #选择日
    SELECT_DAY = "fortLogDay"
    #日志类型
    SYSTEM_LOG_TYPE = "fortSystemLogTypeId"
    #检索class
    CLICK_QUERY = "js_btn"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.tableElem = tableElement(self.driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)
    
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
    
    u'''选择年月日'''
    def select_date(self,dateList):
        date = dateList.split(',')
        self.select_option(self.SELECT_YEAR,date[0])
        self.select_option(self.SELECT_MOUTH,date[1])
        self.select_option(self.SELECT_DAY,date[2])
        
    u'''选择日志类型'''
    def select_system_log_type(self,logType):
        self.set_common_select_elem_by_text(logType,self.SYSTEM_LOG_TYPE)
    
    u'''点击检索'''
    def click_query(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("classname",self.CLICK_QUERY)
            time.sleep(1)
        except Exception as e:
            print ("Click query button error: ") + str(e)
    
    u'''获取表格行数'''
    def get_table_count(self):
        table_xpath = "//table[@id='content_table']"
        count  = self.tableElem.get_table_rows_count(table_xpath)
        return count
    
    u'''检查给定的年月日是否存在  
            parameters:
                seleValue : select元素id的value值
    '''
    def select_option(self,seleValue,option):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            selectd_elem = self.getElem.find_element_with_wait_EC("id",seleValue)
            allText = self.selectElem.get_all_option_text(selectd_elem)
            if allText != "请选择" and option == "":
                self.selectElem.select_element_by_index(selectd_elem,1)
            elif option != "" or allText == "请选择":
                self.selectElem.select_element_by_visible_text(selectd_elem,"请选择")
        except Exception as e :
            print ("Select option error: ") + str(e)