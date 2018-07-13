#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：顾亚茹
#生成日期：2017-08-02
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
from selenium.webdriver.common.action_chains import ActionChains

sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

class ClientPage():
    #添加按钮
    ADD_BUTTON = "addClient"
    #资源类型选择框
    RES_TYPE_QUERY = "resource_type_name"
    #检索按钮
    QUERY_BUTTON = "select_client"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.actions = ActionChains(self.driver)
        self.tableElem = tableElement(self.driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)
    
    u'''点击按钮公用部分
            parameters :
                type : 定位方式
                value : 值
    '''
    def click_button_common(self,type,value):
        var_button = self.getElem.find_element_with_wait_EC(type,value)
        if var_button.is_displayed():
            var_button.click()
    
    u'''点击添加按钮'''
    def add_button(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            time.sleep(1)
            self.click_button_common('id',self.ADD_BUTTON)
        except Exception as e:
            print ("Click client add button error: ") + str(e)

    u'''点击资源类型选择框'''
    def click_res_type(self):
        try:
            time.sleep(1)
            self.click_button_common('id',self.RES_TYPE_QUERY)
        except Exception as e:
            print ("Resource type select error: ") + str(e)
    
    u'''点击检索按钮'''
    def click_query_button(self):
        try:
            time.sleep(1)
            self.click_button_common('id',self.QUERY_BUTTON)
        except Exception as e:
            print("Click query button error: ") + str(e)
    
    u'''选择资源类型
       parameter:
            resType:资源名称
    '''
    def select_res_type_common(self,value,resType,end):
        try:
            parent_elem = self.getElem.find_element_with_wait_EC('id',value)
            #获取所有a标签的对象
            elems = parent_elem.find_elements_by_tag_name("a")
    
            for elem in elems:
                #获取a标签title
                elemtext = elem.get_attribute("title")
                #获取a标签id
                elemid = elem.get_attribute("id")
                var_id = elemid[:-1] + str(end)
    
                if resType == elemtext:
                    time.sleep(1)
                    self.getElem.find_element_wait_and_click_EC('id',var_id)
                    break
    
        except Exception as e:
            print "Select res type error:" + str(e)
        
    u'''选择检索资源类型'''
    def select_query_res_type(self,parentType,resType):
        self.click_res_type()
        if parentType != "":
            self.select_res_type_common("resource_type",parentType,"switch")
        self.select_res_type_common("resource_type",resType,"span")
    
    u'''设置客户端名称'''
    def set_client_name(self,clientName):
        reName = self.cnEnde.is_float(clientName)
        try:
            name_xpath = "//input[@editinput='name']"
            name_elem = self.getElem.find_element_with_wait_EC('xpath',name_xpath)
            name_elem.clear()
            name_elem.send_keys(reName)
    
        except Exception as e:
            print("Set client name error: ") + str(e) 
    
    u'''设置动作流'''
    def set_action_stream(self,actionStream):
        reName = self.cnEnde.is_float(actionStream)
        
        try:
            stream_xpath = "//textarea[@editinput='script']"
            stream_elem = self.getElem.find_element_with_wait_EC('xpath',stream_xpath)
            stream_elem.clear()
            stream_elem.send_keys(reName)
        except Exception as e:
            print("Set action stream error: ") + str(e)
    
    u'''选择添加的资源类型'''
    def set_database_res_type(self,parentType,resType):        
        try:
            res_xpath = "//input[@editinput='resourceType']"
            res_elem = self.getElem.find_element_wait_and_click_EC('xpath',res_xpath)
            if parentType != "":
                self.select_res_type_common("resource_type_add",parentType,"switch")
            self.select_res_type_common("resource_type_add",resType,'span')
            
        except Exception as e:
            print("Set database resource type error: ") + str(e)
    
    u'''添加保存按钮'''
    def save_button(self):
        try:
            save_xpath = "//input[@saveinput='save_add']"
            save_elem = self.getElem.find_element_wait_and_click_EC('xpath',save_xpath)
        except Exception as e:
            print("Click save button error: ") + str(e)
    
    u'''新添加的客户端编辑保存按钮'''
    def edit_save_button(self):
        try:
            save_xpath = "//input[@saveinput='save_edit']"
            save_elem = self.getElem.find_element_wait_and_click_EC('xpath',save_xpath)
        except Exception as e:
            print("Click edit save button error: ") + str(e)
    
    u'''默认客户端编辑保存按钮'''
    def default_client_save_button(self):
        try:
            save_xpath = "//input[@saveinput='save_resource_action_stream']"
            save_elem = self.getElem.find_element_wait_and_click_EC('xpath',save_xpath)
        except Exception as e:
            print("Click default client edit save button error: ") + str(e)
        
    u'''添加取消按钮'''
    def quit_button(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            quit_xpath = "//input[@cancelinput='cancel_add']"
            time.sleep(1)
            quit_elem = self.getElem.find_element_wait_and_click_EC('xpath',quit_xpath)
        except Exception as e:
            print("Click quit button error: ") + str(e)
    
    u'''新添加的客户端编辑取消按钮'''
    def edit_quit_button(self):
        try:
            quit_xpath = "//input[@cancelinput='cancel_edit']"
            quit_elem = self.getElem.find_element_wait_and_click_EC('xpath',quit_xpath)
        except Exception as e:
            print("Click quit button error: ") + str(e)
    
    u'''默认客户端编辑取消按钮'''
    def default_client_edit_quit_button(self):
        try:
            quit_xpath = "//input[@cancelinput='resource_action_stream']"
            quit_elem = self.getElem.find_element_wait_and_click_EC('xpath',quit_xpath)
        except Exception as e:
            print("Click quit button error: ") + str(e)
    
    u'''获取客户端行数'''
    def get_clien_num(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        table_xpath = "//table[@id='listTable']"
        rows = self.tableElem.get_table_rows_count(table_xpath)
        return rows    
        
    u'''通过客户端名称获取所在行数
            parameters : 
                clientName : 客户端名称
    '''
    def get_row_by_account(self,clientName):
        table_xpath = "//table[@id='listTable']"
        reName = self.cnEnde.is_float(clientName)
        table_num = self.get_clien_num()
        for row in range(table_num):
            if row != 0:
                cell_text = self.tableElem.get_table_cell_text(table_xpath,row,1)[0]
                if cell_text == reName:
                    return row+1
    
    u'''点击操作列对应的操作
            parameters : 
                clientName : 客户端名称
                index : input位置
    '''    
    def select_operation(self,clientName,index):
        reindex = self.cnEnde.is_float(index)
        try:
            row = self.get_row_by_account(clientName)
            index_xpath = "//table[@id='listTable']/tbody/tr[" + str(row) + "]/td[5]/input[@class='cz_btn'][" + reindex + "]"
            time.sleep(1)
            edit_elem = self.getElem.find_element_with_wait_EC('xpath',index_xpath)
            edit_elem.click()
        except Exception as e:
            print ("Click operation button error: ") + str(e)
    
    u'''点击编辑'''
    def edit_operation(self,clientName):
        self.select_operation(clientName,"1")
    
    u'''点击删除按钮'''
    def del_operation(self,clientName):
        self.select_operation(clientName,"2")