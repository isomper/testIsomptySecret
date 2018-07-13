#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：张泽方
#生成日期：
#模块描述：密码策略模块
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time

#导入文件
sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/session_configuration/")
from sessionElement import sessionConfig

class PwdStrategy(object):
    #添加密码策略按钮
    ADD_PWD_BUTTON = "add_strategy_password"
    #删除密码策略按钮
    DEL_PWD_BUTTON = "delete_strategy_password"
    #检索按钮
    SEARCH_PWD_BUTTON = "strategy_password__name"
    #重置按钮
    RESRT_BUTTON = "resetting"
    #策略名称
    STRATEGY_NAME = "fortStrategyPasswordName"
    #有效期
    FORT_PERIOD = "fortPeriod"
    #口令最小长度
    LENGTH_MIN = "fortPasswordLengthMin"
    #口令最大长度
    LENGTH_MAX = "fortPasswordLengthMax"
    #小写字母最小长度
    LOWER_CASE_LETER_LENGTH = "fortLowercaseLetterLength"
    #大写字母最小长度
    CAPITA_LETER_LENGTH = "fortCapitalLetterLength"
    #数字最小长度
    DIGITAL_ENGTH = "fortDigitalLength"
    #符号最小长度
    SPECIAL_CHARACTERS_LENGTH = "fortSpecialCharactersLength"
    #禁止使用关键字
    FORBIDDEN_CHARACTER_VALUE= "addForbiddenCharacterValue"
    #禁止使用关键字的添加按钮
    ADD_FORBIDDEN_CHARACTER_BUTTON = "addForbiddenCharacter"
    #全选按钮
    SELECT_ALL_BUTTON = "checkbox"
    #每页显示
    PAGE_PER_SHOW = "page_select"
    #保存按钮
    SAVE_PWD_BUTTON = "save_strategy_password"
    #返回按钮
    RETURN_BUTTON = "history_skip"
    #点击删除成功弹框的确定按钮
    AUI_STATE_HIGHLIGHT = "aui_state_highlight"
    #名称检索框
    SEARCH_NAME = "strategy_password_id"
    #配置密码策略
    PWD_STRATEGY = "fortPasswordStrategyId"
    #用户密码
    USER_PWD = "fortUserPassword"
    USER_PWD_ADIN = "fortUserPasswordAgain"
    #配置全局密码策略
    FORT_STRATEGY_PWD = "fortStrategyPasswordId"
    #资源账号保存按钮
    SAVE_ACCOUNT = "save_account"
    #资源账号名称
    RESOURCE_NAME = "fortAccountName"
    #资源账号密码
    ACCOUNT_PWD = "fortAccountPassword"
    ACCOUNT_PWD_AGIN = "fortAccountPasswordAgain"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cnEnde = cnEncode()
        self.getElem = getElement(driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)
        self.cmF = commonFun(driver)
        self.dataFileName = dataFileName()
        self.session = sessionConfig(driver)

    #点击添加按钮
    def add_pwd_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.ADD_PWD_BUTTON)
        except Exception as e:
            print ("Add password policy error: ") + str(e)
    
    #资源账号编辑页面保存按钮
    def save_account(self):
        try:
            js = "var q=document.getElementById('save_account').click()"
            self.driver.execute_script(js)
            #self.getElem.find_element_with_wait_clickable_and_click('id',self.SAVE_ACCOUNT)
        except Exception as e:
            print ("save button error: ") + str(e)
        
    #点击弹框的确定按钮
    def click_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.AUI_STATE_HIGHLIGHT)
        except Exception as e:
            print ("click button error: ") + str(e)
    
    #点击删除按钮
    def del_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.DEL_PWD_BUTTON)
        except Exception as e:
            print ("Delete button error: ") + str(e)

    #点击检索按钮
    def click_search_button(self):
        try:
            self.getElem.find_element_wait_and_click_EC('id',self.SEARCH_PWD_BUTTON)
            time.sleep(1)
        except Exception as e:
            print ("search button is error: ") + str(e)

    #点击重置按钮
    def click_reset_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.RESRT_BUTTON)
        except Exception as e:
            print ("click reset button error: ") + str(e)
    
    #保存按钮
    def save_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.SAVE_PWD_BUTTON)
        except Exception as e:
            print ("Policy saving error: ") + str(e)
    
    #点击全选按钮
    def select_all_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.SELECT_ALL_BUTTON)
        except Exception as e:
            print ("select all button error: ") + str(e)
    
    #返回按钮
    def return_button(self):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            back_button = self.getElem.find_element_with_wait_EC('id',self.RETURN_BUTTON)
            if back_button.is_displayed():
                time.sleep(1)
                back_button.click() 
        except Exception as e:
            print ("Return error: ") + str(e)
    
    u'''填写变量内容
        parameters:
            var_text : 变量内容
            value : 定位方式值
    '''      
    def set_common_func(self,var_text,value):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            revar_text = self.cnEnde.is_float(var_text)
            time.sleep(2)
            var_elem =self.getElem.find_element_with_wait_EC('id',value)
            var_elem.clear()
            var_elem.send_keys(revar_text)
        except Exception as e:
            print ("Setting up a common text error: ") + str(revar_text) + str(e)

    u'''填写名称
        parameters:
            name : 策略名称
    ''' 
    def set_pwd_name(self,name):
        return self.set_common_func(name,self.STRATEGY_NAME)

    u'''填写有效期
        parameters:
            date : 有效期（天）
    '''     
    def term_of_validity(self,date):
        return self.set_common_func(date,self.FORT_PERIOD)
    
    u'''填写最小口令长度
        parameters:
            min : 口令的最小长度
    '''     
    def password_length_min(self,min):
        return self.set_common_func(min,self.LENGTH_MIN)
    
    u'''填写最大口令长度
        parameters:
            max : 口令的最大长度
    '''     
    def password_length_max(self,max):
        return self.set_common_func(max,self.LENGTH_MAX)
    
    u'''填写小写字母的最小长度
        parameters:
            lowercase : 小写字母的最小长度
    '''     
    def set_lower_case(self,lowercase):
        return self.set_common_func(lowercase,self.LOWER_CASE_LETER_LENGTH)
    
    u'''填写大写字母的最小长度
        parameters:
            capital : 大写字母的最小长度
    '''
    def set_capital(self,capital):
        return self.set_common_func(capital,self.CAPITA_LETER_LENGTH)
    
    u'''填写数字最小长度
        parameters:
            digital : 数字的最小长度
    '''    
    def set_minimum_digital(self,digital):
        return self.set_common_func(digital,self.DIGITAL_ENGTH)
    
    u'''填写字符最小长度
        parameters:
            symbol : 字符的最小长度
    '''
    def set_Minimum_symbol(self,symbol):
        return self.set_common_func(symbol,self.SPECIAL_CHARACTERS_LENGTH)
    
    u'''填写禁止使用关键字
        parameters:
            keywords : 填写的关键字
    '''
    def set_prohibition_of_using_keywords(self,keywords):
        return self.set_common_func(keywords,self.FORBIDDEN_CHARACTER_VALUE)
    
    u'''为资源选择策略
            parameter:
                text : 策略名称
    '''
    def set_resource_strategy(self,text):
        try:
            pwdtext = self.cnEnde.is_float(text)
            pwd_strategy = self.getElem.find_element_with_wait_EC('id', self.FORT_STRATEGY_PWD)
            self.selectElem.select_element_by_visible_text(pwd_strategy, pwdtext)
        except Exception as e:
            print ("Pwd strategy  resource select error:") + str(e)
    
    u'''选择密码策略
            parameter:
                text : 策略名称
    '''    
    def set_pwd_strategy(self, text):
        try:
            pwdtext = self.cnEnde.is_float(text)
            pwd_strategy = self.getElem.find_element_with_wait_EC('id', self.PWD_STRATEGY)
            self.selectElem.select_element_by_visible_text(pwd_strategy, pwdtext)
        except Exception as e:
            print ("Pwd strategy select error:") + str(e)

    #设置用户密码
    def set_pwd(self,pwd):
        return self.set_common_func(pwd,self.USER_PWD)

    #设置用户密码
    def set_pwd_agin(self,pwdagin):
        return self.set_common_func(pwdagin,self.USER_PWD_ADIN)
    
    #设置资源账号名
    def set_resource_account_name(self,name):
        return self.set_common_func(name,self.RESOURCE_NAME)
    
    #设置资源账号密码
    def set_resource_account_pwd(self,pwd):
        return self.set_common_func(pwd,self.ACCOUNT_PWD)
    
    #设置资源账号密码
    def set_resource_account_pwdagin(self,pwdagin):
        return self.set_common_func(pwdagin,self.ACCOUNT_PWD_AGIN)
    
    #关键字添加按钮
    def add_using_keywords_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.ADD_FORBIDDEN_CHARACTER_BUTTON)
        except Exception as e:
            print ("Add keyword errors: ") + str(e)
            
    '''名称检索框
        parameters:
            name :名称
    '''
    def search_name(self,name):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            reaccountName = self.cnEnde.is_float(name)
            var_elem =self.getElem.find_element_with_wait_EC('id',self.SEARCH_NAME)
            var_elem.clear()
            var_elem.send_keys(name)
        except Exception as e:
            print ("set search name  error: ") + str(name) + str(e)
    
    u'''点击密码策略编辑按钮
       Parameters:
          - name:名称
    '''
    def edit(self,name):
        try:
            row = self.cmF.find_row_by_name(name,"fortStrategyPasswordName")
            update_xpath = "html/body/div[1]/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[7]/input[1]"
            self.getElem.find_element_wait_and_click_EC("xpath",update_xpath)
        except Exception:
            print("Click the Edit button to fail")
    
    #点击用户编辑按钮
    def user_edit(self,account):
        try:
            row = self.cmF.find_row_by_name(account,"fortUserAccount")
            update_xpath = "//table[@id='content_table']/tbody/tr[" + str(row) + "]/td[9]//input[1]"
            self.getElem.find_element_wait_and_click_EC("xpath",update_xpath)
        except Exception:
            print("Click the user Edit button to fail")
    
    #点击资源账号管理
    def account_manage(self,name):
        try:
            rename = self.cnEnde.is_float(name)
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            row = self.cmF.find_row_by_name(rename,"fortResourceName")
            update_xpath = "//table[@id='content_table']/tbody/tr[" + str(row) + "]/td[7]//input[1]"
            self.getElem.find_element_wait_and_click_EC("xpath",update_xpath)
        except Exception:
            print("Click account manage button to fail")
    
    #点击资源编辑按钮
    def resource_edit(self,name):
        try:
            row = self.cmF.find_row_by_name(name,"fortResourceName")
            update_xpath = "//table[@id='content_table']/tbody/tr[" + str(row) + "]/td[7]//input[2]"
            self.getElem.find_element_wait_and_click_EC("xpath",update_xpath)
        except Exception:
            print("Click the resource Edit button to fail")
    
    u'''点击密码策略删除按钮
    Parameters:
        - name:名称
    '''
    def del_sing_strategy(self,name):
        try:
            row = self.cmF.find_row_by_name(name,"fortStrategyPasswordName")
            update_xpath = "html/body/div[1]/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[7]/input[2]"
            self.getElem.find_element_wait_and_click_EC("xpath",update_xpath)
        except Exception:
            print("Delete failure")
