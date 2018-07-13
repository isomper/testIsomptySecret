#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：
#生成日期：
#模块描述：告警策略模块
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
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

#导入用户元素类
sys.path.append("/testIsompSecret/webElement/user/")
from userElement import UserPage

class AlarmPage():
    u'''高危运维'''
    #高危运维默认告警级别
    COMMON_ALARM_LEVEL = "commandAlarmLevel"
    #勾选syslog
    SYSLOG_CHECK = "alarmTypeSyslogCheck"
    #勾选邮件
    MAIL_CHECK = "alarmTypeMailCheck"
    #选择邮件接收人添加按钮
    COMMAND_RECEIVE_USER = "illegal_command_receive_user"
    u'''运行状态告警'''
    #内存百分比
    MEM_SELECT = "memoryAlarmSelect"
    #硬盘百分比
    DISK_SELECT = "diskAlarmSelect"
    #CPU百分比
    CPU_SELECT = "cpuAlarmSelect"
    #运行状态告警默认告警级别
    DEF_ALR_LEVEL_SELECT = "defaultAlarmLevelSelect"
    #勾选syslog
    RUN_SYSLOG_CHECK = "runStateAlarmTypeSyslogCheck"
    #勾选邮件
    RUN_MAIL_CHECK = "runStateAlarmTypeMailCheck"
    #选择邮件接收人添加按钮
    SYSTEM_STATE_RECEIVE_USER = "system_state_receive_user"
    #周期检测
    TEST_SELECT = "testCycleSelect"
    #事件是否升级开关
    SWTICH_BUTTON = "btn_sj"
    #重复发生事件次数
    TIME_SELECT = "repeatTimesSelect"
    #事件升级告警级别
    DEF_UPDATE_SELECT = "defaultAlarmUpdateSelect"
    u'''认证异常'''
    #默认告警级别
    AUTH_ALARM_LEVEL = "authAlarmLevel"
    #勾选syslog
    AUTH_SYSLOG_CHECK = "authAlarmTypeSyslogCheck"
    #勾选邮件
    AUTH_MAIL_CHECK = "authAlarmTypeMailCheck"
    #选择邮件接收人添加按钮
    AUTH_EXCEPTIN_RECEIVE_USER = "auth_exception_receive_user"

    u'''告警归纳'''
    #类型检索
    FORT_SYSTEM_ALARM_TYPEID = "fortSystemAlarmTypeId"
    #等级检索
    FORT_ALARM_LEVEL = "fortAlarmLevel"
    #检索按钮
    SEARCH_BUTTON = "js_btn"
    #重置按钮
    REST_BUTTON = "resetting"
    
    #保存按钮
    SAVE_BUTTON = "saveAlarmConfig"
    #选择邮件接收人检索按钮
    RECEIVE_USER_BUTTON = "quick_user"
    #选择邮件接收页面确定按钮
    OK_BUTTON = "okButton"
    #选择邮件接收页面返回按钮
    RETURN_BUTTON = "cancelButton"
    #勾全选
    CHECK_ALL_BUTTON = "user_check_all"
    #填写邮箱
    USER_MAIL = "fortUserEmail"
    #个人信息维护
    MESSAGE = "message"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.tableElem = tableElement(self.driver)
        self.selectElem = selectElement(driver)
        self.dataFile = dataFileName()
        self.frameElem = frameElement(self.driver)
        self.user = UserPage(driver)
        
    u'''点击保存按钮'''
    def save_button(self):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.SAVE_BUTTON)
        except Exception as e:
            print ("Save policy error: ") + str(e)
    
    u'''点击添加邮件接收人公用方法
            parameters :
                type : 定位方式
                value : 值
    '''
    def click_button_common(self,type,value):
        var_button = self.getElem.find_element_with_wait_EC(type,value)
        if var_button.is_displayed():
            var_button.click()
    
    u'''选择邮件接收人检索按钮'''
    def click_receive_user(self):
        try:
            self.click_button_common('id',self.RECEIVE_USER_BUTTON)
        except Exception as e:
            print ("Select the mail recipient error : ") + str(e)
    
    u'''点击确定按钮'''
    def ok_button(self):
        self.frameElem.switch_to_content()
        try:
            self.getElem.find_element_wait_and_click_EC('id',self.OK_BUTTON)
        except Exception as e:
            print ("Determine error: ") + str(e)
    
    u'''点击返回按钮'''
    def return_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.RETURN_BUTTON)
        except Exception as e:
            print ("return error: ") + str(e)
    
    u'''勾选全选按钮'''
    def check_all_button(self):
        try:
            self.click_button_common('id',self.CHECK_ALL_BUTTON)
        except Exception as e:
            print("Click checkall button error: ") + str(e)
            
    u'''左边框点击告警配置'''
    def click_left_config_test(self):
        self.frameElem.from_frame_to_otherFrame("leftFrame")
        self.getElem.find_element_wait_and_click_EC("id", "url1")
   
    u'''左边框点击告警归纳'''
    def click_left_Induce_test(self):
        self.frameElem.from_frame_to_otherFrame("leftFrame")
        self.getElem.find_element_wait_and_click_EC("id", "url0")
    
    u'''填写变量内容
        parameters:
            var_text : 变量内容
            value : 定位方式值
    '''
    def set_common_func(self,var_text,value):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        try:
            revar_text = self.cnEnde.is_float(var_text)
            var_elem =self.getElem.find_element_with_wait_EC('id',value)
            var_elem.clear()
            var_elem.send_keys(revar_text)
        except Exception as e:
            print ("set common text error: ") + str(revar_text) + str(e)
    
    #取消高危运维syslog，邮件配置
    def del_command_config(self):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            self.click_left_config_test()
            self.click_command_alarm_menu()
            self.syslog_check()
            self.mail_check()
            self.save_button()
            self.frameElem.switch_to_content()
            self.cmf.click_msg_button(1)
        except Exception as e:
            print ("del command config: ") + str(e)
            
    #取消运行状态告警syslog，邮件配置
    def del_default_config(self):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            self.click_left_config_test()
            self.click_default_alarm_menu()
            self.run_syslog_check()
            self.run_mail_check()
            self.change_switch_status()
            self.save_button()
            self.frameElem.switch_to_content()
            self.cmf.click_msg_button(1)
        except Exception as e:
            print ("del default config: ") + str(e)
    
    #取消认证异常syslog，邮件配置
    def del_auth_config(self):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            self.click_left_config_test()
            self.auth_default_alarm_menu()
            self.auth_syslog_check()
            self.auth_mail_check()
            self.save_button()
            self.frameElem.switch_to_content()
            self.cmf.click_msg_button(1)
        except Exception as e:
            print ("del auth config: ") + str(e)
    
    #取消绕行告警syslog，邮件配置
    def del_ip_config(self):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            self.click_left_config_test()
            self.ip_default_alarm_menu()
            self.ip_syslog_check()
            self.ip_mail_check()
            self.del_ip_select()
            self.save_button()
            self.frameElem.switch_to_content()
            self.cmf.click_msg_button(1)
        except Exception as e:
            print ("del ip config: ") + str(e)

#---------------------------------高危运维--------------------------------------------------
    #点击高危运维模块
    def click_command_alarm_menu(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_with_wait_clickable_and_click('link',"高危运维")
        except Exception as e:
            print ("commmand alarm menu error: ") + str(e)
    
    u'''高危运维默认告警级别
            parameter:
                commandValue : 告警级别option的value值(5代表等级：5)
    '''
    def command_alarm_level(self,commandValue):
        return self.user.set_common_select_elem(commandValue,self.COMMON_ALARM_LEVEL)
    
    u'''勾选syslog按钮'''
    def syslog_check(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.SYSLOG_CHECK)
        except Exception as e:
            print ("Check syslog error: ") + str(e)
            
    u'''勾选mail按钮'''
    def mail_check(self):
        try:
            time.sleep(2)
            self.getElem.find_element_with_wait_clickable_and_click('id',self.MAIL_CHECK)
            time.sleep(2)
        except Exception as e:
            print ("mail mail error: ") + str(e)
    
    u'''点击邮件添加按钮'''
    def click_illegal_command_receive_user(self):
        try:
            time.sleep(2)
            self.getElem.find_element_with_wait_clickable_and_click('id',self.COMMAND_RECEIVE_USER)
        except Exception as e:
            print ("click mail recipient error: ") + str(e)
    
    
#---------------------------------运维状态告警--------------------------------------------------
    #点击运行状态告警模块
    def click_default_alarm_menu(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_with_wait_clickable_and_click('link',"运行状态告警")
        except Exception as e:
            print ("default alarm menu error: ") + str(e)

    u'''内存设置百分比
            parameter:
                memoryValue : mem百分比option的value值(5代表50%)
    '''    
    def memory_alarm_select(self,memoryValue):
        time.sleep(2)
        return self.user.set_common_select_elem(memoryValue,self.MEM_SELECT)
    
    u'''磁盘设置百分比
            parameter:
                diskValue : disk百分比option的value值(5代表50%)
    '''    
    def disk_alarm_select(self,diskValue):
        time.sleep(1)
        return self.user.set_common_select_elem(diskValue,self.DISK_SELECT)
    
    u'''cpu设置百分比
            parameter:
                cpuValue : cpu百分比option的value值(5代表50%)
    '''    
    def cpu_alarm_select(self,cpuValue):
        time.sleep(1)
        return self.user.set_common_select_elem(cpuValue,self.CPU_SELECT)
    
    u'''检测周期
            parameter:
                testValue : 检测周期option的value值(5代表5秒)
    '''    
    def test_cycle_select(self,testValue):
        time.sleep(2)
        return self.user.set_common_select_elem(testValue,self.TEST_SELECT)
    
    u'''默认告警级别
            parameter:
                defaultValue : 默认告警级别option的value值(5代表级别5)
    '''    
    def default_alarm_level_select(self,defaultValue):
        time.sleep(2)
        return self.user.set_common_select_elem(defaultValue,self.DEF_ALR_LEVEL_SELECT)
   
    u'''勾选syslog按钮'''
    def run_syslog_check(self):
        try:
            time.sleep(2)
            self.getElem.find_element_with_wait_clickable_and_click('id',self.RUN_SYSLOG_CHECK)
        except Exception as e:
            print ("Check syslog run error: ") + str(e)
            
    u'''勾选mail按钮'''
    def run_mail_check(self):
        try:
            time.sleep(2)
            self.getElem.find_element_with_wait_clickable_and_click('id',self.RUN_MAIL_CHECK)
        except Exception as e:
            print ("Check mail run error: ") + str(e)
    
    u'''选择邮件接收人添加按钮'''
    def system_state_receive_user(self):
        try:
            time.sleep(2)
            self.getElem.find_element_with_wait_clickable_and_click('id',self.SYSTEM_STATE_RECEIVE_USER)
        except Exception as e:
            print ("Select the system mail recipient error: ") + str(e)
    
    u'''改变开关状态'''
    def change_switch_status(self):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        try:
            button_elem = self.getElem.find_element_with_wait_EC("id",self.SWTICH_BUTTON)
            class_attr = button_elem.get_attribute("class")
            off_status = "switch_off"
            on_status = "switch_on"
            if class_attr == on_status:
                self.click_default_alarm_menu()
                self.frameElem.from_frame_to_otherFrame("rigthFrame")
                button_elem = self.getElem.find_element_with_wait_EC("id",self.SWTICH_BUTTON)
                button_elem.click()
                button_elem.click()
            else:
                button_elem.click()
        except Exception as e:
            print ("Change button status error: ") + str(e)

    u'''重复事件
            parameter:
                repeatValue : 重复事件option的value值(10代表10次)
                    '''
    def repeat_times_select(self,repeatValue):
        time.sleep(2)
        return self.user.set_common_select_elem(repeatValue,self.TIME_SELECT)
    
    u'''升级事件告警级别
            parameter:
                updateValue : 升级告警级别option的value值(6代表等级6)
                    '''
    def defaultA_alarm_update_elect(self,updateValue):
        time.sleep(2)
        return self.user.set_common_select_elem(updateValue,self.DEF_UPDATE_SELECT)
    
#---------------------------------认证异常--------------------------------------------------
    #点击认证异常模块
    def auth_default_alarm_menu(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_with_wait_clickable_and_click('link',"认证异常")
        except Exception as e:
            print ("auth alarm menu error: ") + str(e)
    
    u'''默认告警级别
            parameter:
                authValue : 告警级别option的value值(5代表等级：5)
    '''    
    def auth_alarm_level(self,authValue):
        return self.user.set_common_select_elem(authValue,self.AUTH_ALARM_LEVEL)
    
    u'''勾选syslog按钮'''
    def auth_syslog_check(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.AUTH_SYSLOG_CHECK)
        except Exception as e:
            print ("Check auth syslog error: ") + str(e)
            
    u'''勾选mail按钮'''
    def auth_mail_check(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.AUTH_MAIL_CHECK)
        except Exception as e:
            print ("mail auth mail error: ") + str(e)
    
    u'''选择邮件接收人添加按钮'''
    def auth_exception_receive_user(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.AUTH_EXCEPTIN_RECEIVE_USER)
        except Exception as e:
            print ("Select the auth mail recipient error: ") + str(e)
    
#---------------------------------告警归纳--------------------------------------------------
    u'''点击检索按钮'''
    def search_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('classname',self.SEARCH_BUTTON)
            time.sleep(1)
        except Exception as e:
            print ("Retrieval strategy error: ") + str(e)
    
    u'''点击重置按钮'''
    def rest_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.REST_BUTTON)
        except Exception as e:
            print ("reset error: ") + str(e)
    
    u'''类型检索
            parameter:
                text : 告警类型检索的text值
    '''    
    def search_type(self,text):
        try:
            searchtext = self.cnEnde.is_float(text)
            search_type = self.getElem.find_element_with_wait_EC('id', self.FORT_SYSTEM_ALARM_TYPEID)
            self.selectElem.select_element_by_visible_text(search_type, searchtext)
        except Exception as e:
            print ("search type select error:") + str(e)
    
    u'''级别检索
            parameter:
                text : 告警级别检索的text值
    '''    
    def search_level(self,text):
        try:
            searchtext = self.cnEnde.is_float(text)
            search_level = self.getElem.find_element_with_wait_EC('id', self.FORT_ALARM_LEVEL)
            self.selectElem.select_element_by_visible_text(search_level, searchtext)
        except Exception as e:
            print ("search level select error:") + str(e)
#---------------------------------填写邮箱--------------------------------------------------

    #点击个人维护
    def click_user_message_menu(self):
        self.frameElem.from_frame_to_otherFrame("topFrame")
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.MESSAGE)
        except Exception as e:
            print ("click user message menu error: ") + str(e)
    
    #填写邮箱
    def set_user_mail(self,usermail):
        return self.user.set_common_func(usermail,self.USER_MAIL)
    
    #点击保存
    def click_save_button(self):
        return self.user.save_button()