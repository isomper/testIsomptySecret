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

import os
import time
import win32api
import win32con
import win32gui

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log
sys.path.append("/testIsompSecret/webElement/department/")
from test_dptm_ment import Department

class AppPage():
    #应用发布
    APP_MODULE = "url4"
    #名称检索框
    NAME_QUERY = "txtApplicationReleaseId"
    #检索
    QUERY_BUTTON = "btnApplicationReleaseName"
    #重置
    RESET = "resetting"
    #添加class
    ADD_BUTTON = "btn_tj"
    #删除
    DEL_BUTTON = "btnDelApplicationRelease"
    #名称
    APP_NAME = "fortApplicationReleaseServerName"
    #IP
    APP_IP = "fortApplicationReleaseServerIp"
    #ip检测
    IP_IS_EXIST = "ip_succ"
    #端口
    APP_PORT = "fortApplicationReleaseServerPort"
    #port检测
    PORT_IS_EXIST = "port_succ"
    #连接用户名
    APP_ACCOUNT = "fortApplicationReleaseServerAccount"
    #口令
    PWD = "fortApplicationReleaseServerPassword"
    #确认口令
    REPWD = "fortApplicationReleaseServerPassword2"
    #描述
    DEPICT = "fortDescription"
    #保存
    SAVE_BUTTON = "save_application_release"
    #返回
    BACK_BUTTON = "history_skip"
    #账号删除
    ACCOUNT_DEL = "btnDelApplicationReleaseAccount"
    #账号名称
    ACCOUNT_NAME = "fortAccountName"
    #账号口令
    ACCOUNT_PWD = "fortApplicationReleaseServerAccountPassword"
    #账号确认口令
    ACCOUNT_REPWD = "fortApplicationReleaseServerAccountPassword2"
    #选择绑定用户
    BOUND_USER_BUTTON = "btn_tjyh"
    #账号/用户名
    ACCOUNT_OR_NAME = "fort_user_account"
    #检索
    USER_QUERY = "quick_user"
    #确认
    CONFIRM_BUTTON = "okButton"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.actions = ActionChains(self.driver)
        self.tableElem = tableElement(self.driver)
        self.selectElem = selectElement(driver)
        self.dptment = Department(self.driver)
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
    
    u'''点击应用发布按钮'''
    def app_module_button(self):
        self.frameElem.from_frame_to_otherFrame("leftFrame")
        try:
            time.sleep(1)
            self.click_button_common('id',self.APP_MODULE)
            time.sleep(1)
        except Exception as e:
            print ("Click app module button error: ") + str(e)
    
    u'''填写变量内容
        parameters:
            var_text : 变量内容
            type : 定位方式
            value : 定位方式对应的值
    '''      
    def set_common_func(self,var_text,type,value):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        try:
            revar_text = self.cnEnde.is_float(var_text)
            var_elem =self.getElem.find_element_with_wait_EC(type,value)
            var_elem.clear()
            var_elem.send_keys(revar_text)
        except Exception as e:
            print ("Set application common text error: ") + str(revar_text) + str(e)    
    
    u'''应用发布名称检索'''
    def set_app_query_name(self,name):
        try:
            self.set_common_func(name,'id',self.NAME_QUERY)
        except Exception as e:
            print ("Set name query condition error: ") + str(e)
    
    u'''点击检索按钮'''
    def click_query_button(self):
        try:
            self.click_button_common('id',self.QUERY_BUTTON)
        except Exception as e:
            print("Click query button error: ") + str(e)
    
    u'''点击重置按钮'''
    def click_reset_button(self):
        try:
            time.sleep(2)
            self.click_button_common('id',self.RESET)
        except Exception as e:
            print ("Click reset button error: ") + str(e)
    
    u'''点击添加'''
    def click_add_button(self):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        try:
            self.click_button_common('classname',self.ADD_BUTTON)
        except Exception as e:
            print ("Click add button error: ") + str(e)
    
    u'''点击删除'''
    def click_del_button(self):
        try:
            self.click_button_common('id',self.DEL_BUTTON)
        except Exception as e:
            print ("Click delete button error: ") + str(e)
    
    u'''勾选全删按钮'''
    def click_check_all(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            time.sleep(1)
            self.getElem.find_element_wait_and_click_EC("id", "checkbox")
        except Exception:
            print("Select the check box failure")

    u'''全删'''
    def del_all(self):
        self.click_check_all()
        self.click_del_button()
    
    u'''查询已存在名称位于第几行
       Parameters:
          - namevalue:传入的要被查询名称
          - name:表格列的name属性
       return：定位该名称位于第几行
    '''
    def find_row_by_name(self, namevalue, name):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        row = 0
        try:
            text_list = self.driver.find_elements_by_name(name)
            for fortNameValue in text_list:
                row = row + 1
                fortNameValue_text = fortNameValue.text
                if fortNameValue_text == namevalue:
                    break
        except Exception:
            print namevalue + " is not exsit."
        return row
            
    u'''点击应用发布操作列对应的按钮
        parameters:
            name : 应用发布名称
            index : 操作功能按钮对应的input位置
    '''
    def app_operate_list(self,name,nameValue,index):
        rename = self.cnEnde.is_float(name)
        row = self.find_row_by_name(rename,nameValue)
        update_xpath = "//table[@id='content_table']/tbody/tr[" + str(row) + "]/td[5]/input[" + index + "]"
        self.click_button_common('xpath',update_xpath)
    
    u'''点击编辑'''
    def operate_edit(self,name):
        try:
            self.app_operate_list(name,self.APP_NAME,"1")
        except Exception as e:
            print("Click application operation edit button fail") + str(e)
    
    u'''点击删除'''
    def operate_del(self,name):
        try:
            self.app_operate_list(name,self.APP_NAME,"2")
        except Exception as e:
            print("Click application operation edit button fail") + str(e)
    
    u'''点击账号管理'''
    def operate_account_manage(self,name):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        try:
            self.app_operate_list(name,self.APP_NAME,"3")
        except Exception as e:
            print("Click application operation account button fail") + str(e)
    
    u'''设置应用发布名称'''
    def set_name(self,name):
        try:
            self.set_common_func(name,'id',self.APP_NAME)
        except Exception as e:
            print ("Set application name error: ") + str(e)
        
    u'''设置应用发布IP'''
    def set_ip(self,ip):
        try:
            self.set_common_func(ip,'id',self.APP_IP)
        except Exception as e:
            print ("Set application ip error: ") + str(e)
    
    u'''ip_succ ip不可达  ip可达 port_succ 端口不可达 端口可达'''
    def get_elem_title(self,type,value):
        self.driver.implicitly_wait(2)
        selem = self.getElem.find_element_with_wait_EC(type,value)
        title_text = selem.get_attribute("title")
        
    u'''IP是否可达'''
    def ip_is_succ(self):
        try:
            selem = self.getElem.find_element_with_wait_EC("classname",self.IP_IS_EXIST)
        except Exception as e:
            print("Ip is not visibility") + str(e)
    
    u'''PORT是否可达'''    
    def port_is_exist(self):
        try:
            selem = self.getElem.find_element_with_wait_EC("classname",self.PORT_IS_EXIST)
        except Exception as e:
            print("Port is not visibility") + str(e)
    
    u'''设置应用发布端口'''
    def set_port(self,port):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        try:
            self.set_common_func(port,'id',self.APP_PORT)
        except Exception as e:
            print ("Set application port error: ") + str(e)
    
    u'''设置连接用户名'''
    def set_app_account(self,account):
        try:
            self.set_common_func(account,'id',self.APP_ACCOUNT)
        except Exception as e:
            print ("Set application account error: ") + str(e)
    
    def click_app_port(self):
        self.getElem.find_element_wait_and_click_EC('id',self.APP_PORT)
    
    def click_app_account(self):
        self.getElem.find_element_wait_and_click_EC('id',self.APP_ACCOUNT)
    
    u'''设置密码'''
    def set_pwd(self,pwd):
        try:
            self.set_common_func(pwd,'id',self.PWD)
        except Exception as e:
            print ("Set application pwd error: ") + str(e)
    
    u'''设置确认口令'''
    def set_repwd(self,repwd):
        try:
            self.set_common_func(repwd,'id',self.REPWD)
        except Exception as e:
            print ("Set application repwd error: ") + str(e)
    
    u'''设置描述'''
    def set_desp(self,desp):
        try:
            self.set_common_func(desp,'id',self.DEPICT)
        except Exception as e:
            print ("Set application descript error: ") + str(e)
    
    u'''点击应用发布保存'''
    def click_save_button(self):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        try:
            time.sleep(1)
            self.getElem.find_element_wait_and_click_EC('id',self.SAVE_BUTTON)
        except Exception as e:
            print("Click save button error: ") + str(e)
    
    u'''判断是否是有ip可用性校验'''
    def is_pop_up(self):
        xpath = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        flag = self.getElem.find_element_wait_and_compare_text("xpath", xpath, [0, "ip可用性校验失败！"])
        if flag:
            self.cmf.click_login_msg_button()
    
    u'''应用发布返回'''
    def click_back_button(self):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        try:
            time.sleep(1)
            self.getElem.find_element_wait_and_click_EC('id',self.BACK_BUTTON)
        except Exception as e:
            print("Click back button error: ") + str(e)
            
#---------------------------------应用发布账号------------------------------
    u'''资源账号删除'''
    def account_del(self):
        try:
            self.getElem.find_element_wait_and_click_EC('id',self.ACCOUNT_DEL)
        except Exception as e:
            print("Click account del button error: ") + str(e)
    
    u'''账号'''
    def set_account(self,account):
        try:
            self.set_common_func(account,'id',self.ACCOUNT_NAME)
        except Exception as e:
            print ("Set application account error: ") + str(e)
    
    u'''密码'''
    def set_account_pwd(self,pwd):
        try:
            self.set_common_func(pwd,'id',self.ACCOUNT_PWD)
        except Exception as e:
            print ("Set account pwd error: ") + str(e)
    
    u'''确认密码'''
    def set_account_repwd(self,repwd):
        try:
            self.set_common_func(repwd,'id',self.ACCOUNT_REPWD)
        except Exception as e:
            print ("Set account repwd error: ") + str(e)
    
    u'''选择绑定用户按钮'''
    def click_bound_user(self):
        try:
            self.getElem.find_element_wait_and_click_EC('id',self.BOUND_USER_BUTTON)
        except Exception as e:
            print ("Click bound user button error: ") + str(e)
    
    u'''账号/用户名检索框'''
    def set_account_or_name(self,userName):
        reName = self.cnEnde.is_float(userName)
        self.frameElem.switch_to_artIframe()
        try:
            self.getElem.find_element_with_wait_EC('id',self.ACCOUNT_OR_NAME).send_keys(reName)
        except Exception as e:
            print ("Set account or name condition error: ") + str(e)
        
    u'''用户检索按钮'''
    def user_query_button(self):
        try:
            self.getElem.find_element_wait_and_click_EC('id',self.USER_QUERY)
        except Exception as e:
            print ("User query button error: ") + str(e)
    
    u'''通过账号获取用户所在行数
            parameters : 
                column_index :用户账号所在的列序号(从0开始)
                account : 勾选的账号
    '''
    def get_row_by_account(self,account):
        self.frameElem.switch_to_artIframe()
        try:
            table_xpath = "//table[@id='user_table']"
            table_num = self.tableElem.get_table_rows_count(table_xpath)
            for row in range(table_num):
                cell_text = self.tableElem.get_table_cell_text(table_xpath,row,1)[0]
                if cell_text == account:
                    return row+1
                    break
        
        except Exception as e:
            print ("Get row number error: ") + str(e)
    
    u'''勾选用户账号对应的checkbox
            parameters : 
                account : 勾选的账号
    '''    
    def select_user_checkbox(self,account):
        reaccount = self.cnEnde.is_float(account)
        row = self.get_row_by_account(account)
        index_xpath = "//table[@id='user_table']/tbody/tr[" + str(row) + "]/td[1]/li/input[1]"
        if self.getElem.is_element_exsit('xpath',index_xpath):
            elem = self.getElem.find_element_with_wait_EC('xpath',index_xpath)
            elem.click()
            self.confirm_button()
        else:
            self.user_back_button()
    
    u'''点击确认按钮'''
    def confirm_button(self):
        self.frameElem.switch_to_content()
        try:
            self.getElem.find_element_wait_and_click_EC('id',self.CONFIRM_BUTTON)
        except Exception as e:
            print ("Click confirm button error: ") + str(e)
    
    def user_back_button(self):
        self.frameElem.switch_to_content()
        self.getElem.find_element_wait_and_click_EC('id','cancelButton')
    
    u'''点击账号编辑'''
    def operate_account_edit(self,name):
        try:
            self.app_operate_list(name,"fortAccountName","1")
        except Exception as e:
            print("Click operation account edit button fail") + str(e)
    
    u'''点击账号删除'''
    def operate_account_del(self,name):
        try:
            self.app_operate_list(name,"fortAccountName","2")
        except Exception as e:
            print("Click operation account del button fail") + str(e)