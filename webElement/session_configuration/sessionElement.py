#coding=utf-8
u''' 
#文件名：session
#被测软件版本号：V2.8.1
#作成人：张泽方
#生成日期：2018-1-12
#模块描述：会话配置页面
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入通用方法
sys.path.append("/testIsompSecret/common/")
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

class sessionConfig(object):
    #访问失败次数
    NUMBER_OF_ACCESS_FAILURES = "lockStrategyCount"
    #失败锁定时间
    FAILURES_LOCK_TIME = "lockStrategyTime"
    #web会话超时时间
    SESSION_OUT_TIME = "sessionOutTime"
    #单用户登录方式
    SING_USER_LOGIN = "singleUserLoginType"
    #最大在线数
    MAX_ON_LINE_COUNT = "maxOnLineCount"
    #会话访问失败保存按钮
    SAVE_GLOBAL_BUTTON = "save_globalStrategy"
    #最大在线数保存按钮
    SAVE_SSESSION_BUTTON = "save_sessionConfig"
    
    def __init__ (self,driver):
        self.driver = driver
        self.cnEnde = cnEncode()
        self.log = log()
        self.getElem = getElement(driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)
        self.cmF = commonFun(driver)
        self.tableElem = tableElement(self.driver)
        
    #会话访问失败保存按钮
    def save_global_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.SAVE_GLOBAL_BUTTON)
        except Exception as e:
            print ("failure to save session access: ") + str(e)
        
    #最大在线数保存按钮
    def save_session_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.SAVE_SSESSION_BUTTON)
        except Exception as e:
            print ("maximum number of online number save errors: ") + str(e)

    u'''填写变量内容
        parameters:
            var_text : 变量内容
            value : 定位方式值
    '''     
    def set_common_func(self,var_text,value):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            revar_text = self.cnEnde.is_float(var_text)
            var_elem =self.getElem.find_element_with_wait_EC('id',value)
            var_elem.clear()
            var_elem.send_keys(revar_text)
        except Exception as e:
            print ("Public session strategy configuration error: ") + str(revar_text) + str(e)
    
    u'''添加访问失败次数
        parameters:
            count: 访问失败的次数
    '''  
    def add_session(self,count):
        return self.set_common_func(count,self.NUMBER_OF_ACCESS_FAILURES)

    u'''添加失败锁定时间
        parameters:
            time: 失败锁定的时间
    '''      
    def add_locking_time(self,time):
        return self.set_common_func(time,self.FAILURES_LOCK_TIME)
    
    u'''select元素通过value选择元素通用方法
            parameter:
                var_value : 访问方式value值
                locator : ID值
    '''
    def set_common_select_elem(self,var_value,locator):
        try:
            revar_value = self.cnEnde.is_float(var_value)
            select_elem = self.getElem.find_element_with_wait_EC('id',locator)
            self.selectElem.select_element_by_value(select_elem,str(revar_value))
        except Exception as e:
            print ("selected select element option  by value error: ") + str(revar_value) + str(e)
    
    u'''选择web超时时间
            parameter:
                timeValue : web超时时间option的value值(5代表5分钟)
    '''
    def set_out_time(self,timeValue):
        return self.set_common_select_elem(timeValue,self.SESSION_OUT_TIME)

    u'''选择单用户登录方式
            parameter:
                loginValue : 单用户登录option的value值(0代表无限制)
    '''
    def set_sing_user_login(self,loginValue):
        return self.set_common_select_elem(loginValue,self.SING_USER_LOGIN)
    
    u'''最大在线数
        parameters:
            numValue: 最大在线数
    ''' 
    def max_number_online(self,numValue):
        return self.set_common_func(numValue,self.MAX_ON_LINE_COUNT)
