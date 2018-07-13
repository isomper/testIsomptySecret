#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：
#生成日期：
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

sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

class UserPage():
    #添加按钮class
    ADD_BUTTON = "btn_tj"
    #删除按钮
    DEL_BUTTON = "delete_user"
    #用户部门检索
    SEARCH_DEP = "department_name"
    #账号或名称检索
    SEARCH_ACCOUNT_OR_NAME = "fortUserAccountOrName"
    #角色检索
    SEARCH_ROLE = "fortRoleId"
    #用户状态检索
    SEARCH_USER_STATUS = "fortUserState"
    #点击部门清空
    DEP_CLEAR = "clean_tree_data"
    #检索按钮
    SEARCH_BUTTON = "fort_user"
    #重置按钮
    RESRT_BUTTON = "resetting"
    #用户账号
    USER_ACCOUNT = "fortUserAccount"
    #用户名称
    USER_NAME = "fortUserName"
    #开始时间
    USER_START_TIME = "fortStartTime"
    #结束时间
    USER_END_TIME = "fortEndTime"
    #用户状态
    USER_STATUS = "fortUserState"
    #用户部门
    USER_DEP = "department_name"
    #登录时是否修改
    LOGIN_MODEY = "fortInitializePassword"
    #用户密码
    USER_PWD = "fortUserPassword"
    #确认密码
    USER_RE_PWD = "fortUserPasswordAgain"
    #手机号
    USER_MOBILE = "fortUserMobile"
    #电话
    USER_PHONE = "fortUserPhone"
    #审计查看审批管理员
    IS_APPROVAL = "isDownLoadApproval"
    #邮箱
    USER_EMAIL = "fortUserEmail"
    #地址
    USER_ADDRESS = "fortUserAddress"
    #高级选项
    ADVANCED_OPTIONS = "btn_high"
    #时间规则
    TIME_RULE = "fortRuleTimeId"
    #地址规则
    ADDRESS_RULE = "fortRuleAddressId"
    #认证方式
    AUTH_CODE = "fortAuthenticationCode"
    #域账号
    USER_DOMAIN_ACCOUNT = "fortDomainAccount"
    #radius账号
    USER_RADIUS = "fortRadius"
    #保存按钮
    SAVE_BUTTON = "save_user"
    #点击角色信息
    ROLE_MEG_BUTTON = "//html/body/form[@id='user_form']/div/div[2]/div[1]/a[2]"
    #角色选择框
    ROLE_SELECTD_ELEM = "Roles"
    #角色添加按钮
    ROLE_ADD_BUTTON = "add_roles"
    #全选按钮
    SELECT_ALL_BUTTON = "checkbox"
    #生成证书
    CREATE_CERT = "createCertificate"
    DELETE_CERT = "deleteCertificate"
    #证书名称
    CERT_NAME = "downLoad"
    #没有生成证书之前的名字
    INIT_CERT_NAME = "certificateName"
    #证书序列号
    CERT_SERIAL_NUM = "certificateNum"
    #每页显示
    PAGE_PER_SHOW = "page_select"
    #开关按钮
    SWITCH_STATUS_BUTTON = "btn_qh"
    #返回按钮
    BACK_BUTTON = "history_skip"
    #查询子节点
    QUERY_CHILD_NODE = "query_zijiedian"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.tableElem = tableElement(self.driver)
        self.selectElem = selectElement(driver)
        self.dataFile = dataFileName()
        self.login = loginPage(self.driver)
        self.frameElem = frameElement(self.driver)

    u'''点击添加按钮'''
    def add_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('classname',self.ADD_BUTTON)
        except Exception as e:
            print ("user add button error: ") + str(e)

    u'''点击添加本角色成员按钮'''
    def add_role_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('classname',"btn_tjl")
        except Exception as e:
            print ("user add button error: ") + str(e)

    u'''点击删除按钮'''
    def del_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.DEL_BUTTON)
        except Exception as e:
            print ("Delete button error: ") + str(e)

    '''点击检索按钮'''     
    def click_search_button(self):
        try:
            self.getElem.find_element_wait_and_click_EC('id',self.SEARCH_BUTTON)
            time.sleep(1)
        except Exception as e:
            print ("search button is error: ") + str(e)

    u'''点击重置按钮'''
    def click_reset_button(self):
        try:
            time.sleep(2)
            self.getElem.find_element_with_wait_clickable_and_click('id',self.RESRT_BUTTON)
        except Exception as e:
            print ("click reset button error: ") + str(e)

    u'''每页选择全部'''
    def page_select_all(self):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            
            #选择每页显示全部
            selem = self.getElem.find_element_with_wait_EC('id',self.PAGE_PER_SHOW)
            self.selectElem.select_element_by_value(selem,'2000')
            
        except Exception as e:
            print ("page select all error: ") + str(e)

    u'''获取行数'''
    def get_rows(self):
        try:
            table_xpath = "//table[@id='content_table']"
            rows = self.tableElem.get_table_rows_count(table_xpath)
            return rows
        except Exception as e:
            print ("get tables row error: ") + str(e)

    u'''保存按钮'''
    def save_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.SAVE_BUTTON)
        except Exception as e:
            print ("user save button error: ") + str(e)

    u'''点击全选按钮'''
    def select_all_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.SELECT_ALL_BUTTON)
        except Exception as e:
            print ("select all button error: ") + str(e)

    u'''点击角色信息'''
    def click_role_msg(self):
        try:
            role = self.getElem.find_element_with_wait_EC('xpath',self.ROLE_MEG_BUTTON)
            if role.is_displayed():
                time.sleep(1)
                role.click()
        except Exception as e:
            print ("user role message button error: ") + str(e)

    u'''角色添加按钮'''
    def click_role_add_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.ROLE_ADD_BUTTON)
        except Exception as e:
            print ("role add button error: ") + str(e)

    u'''点击用户操作列对应的按钮
        parameters:
            account : 用户账号
            index : 操作功能按钮对应的input位置
    '''
    def user_operate_list(self,account,index):
        row = self.cmf.find_row_by_name(account, "fortUserAccount")
        update_xpath = "//table[@id='content_table']/tbody/tr[" + str(row) + "]/td[9]/input[" + index + "]"
        time.sleep(1)
        self.getElem.find_element_with_wait_clickable_and_click('xpath',update_xpath)
    
    u'''删除指定的用户
        parameters:
            account:用户账号
    '''
    def del_specified_user(self,account):
        row = self.cmf.find_row_by_name(account, "fortUserAccount")
        update_xpath = "//table[@id='content_table']/tbody/tr[" + str(row) + "]/td[1]/span[1]/input[1]"
        self.getElem.find_element_with_wait_clickable_and_click('xpath',update_xpath)     

    u'''点击用户操作列对应的编辑按钮
        parameters:
            account : 用户账号
    '''
    def operate_edit(self,account):
        try:
            self.user_operate_list(account,"1")
        except Exception:
            print("Click user operation edit button fail")

    u'''点击用户操作列对应的角色按钮
        parameters:
            account : 用户账号
    '''    
    def operate_role(self,account):
        try:
           self.user_operate_list(account,"2")
        except Exception:
            print("Click user operation role button fail")

    u'''点击用户操作列对应的证书按钮
        parameters:
            account : 用户账号
    '''     
    def operate_cert(self,account):
        try:
            self.user_operate_list(account,"2")
        except Exception:
            print("Click user operation cert button fail")

    u'''点击用户操作列对应的删除按钮
        parameters:
            account : 用户账号
    '''     
    def operate_delete(self,account):
        row = self.cmf.find_row_by_name(account, "fortUserAccount")
        opt_xpath = "//table[@id='content_table']/tbody/tr[" + str(row) + "]/td[9]"
        parent_elem = self.getElem.find_element_with_wait_EC("xpath",opt_xpath)
        input_num = str(len(parent_elem.find_elements_by_tag_name("input")))
        try:
            if input_num == "4":
                self.user_operate_list(account,"4")
            else:
                self.user_operate_list(account,"5")
        except Exception:
            print("Click user operation delete button fail")

    u'''改变用户开关状态
        parameters:
            account : 用户账号
            value : 开关状态(switch_on:开,switch_off :关)
    '''  
    def change_user_status_button(self,account,value):
        revalue = self.cnEnde.is_float(value)
        reaccount = self.cnEnde.is_float(account)
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        
        #获取用户行号
        row = self.cmf.find_row_by_name(reaccount,"fortUserAccount")
        button_status_xpath = "//table[@id='content_table']/tbody/tr[" + str(row) + "]/td[8]/input[@id='btn_qh']"        
        try:
            button_status = self.getElem.find_element_with_wait_EC('xpath',button_status_xpath)
            if button_status.get_attribute('class') != revalue:
                button_status.click()
        except Exception as e:
            print ("Change user button status  error: ") + str(e)

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
            print ("set user common text error: ") + str(revar_text) + str(e)

    '''账号或名称检索框
        parameters:
            accountName : 账号或名称
    '''
    def search_accountorname(self,accountName):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            reaccountName = self.cnEnde.is_float(accountName)
            var_elem =self.getElem.find_element_with_wait_EC('id',self.SEARCH_ACCOUNT_OR_NAME)
            var_elem.clear()
            var_elem.send_keys(reaccountName)
        except Exception as e:
            print ("set search user accountOrname  error: ") + str(accountName) + str(e)

    u'''填写用户账号
        parameters:
            account : 用户账号
    '''      
    def set_user_account(self,account):
        return self.set_common_func(account,self.USER_ACCOUNT)

    u'''填写用户名称
        parameters:
            name : 用户名称
    '''     
    def set_user_name(self,name):
        return self.set_common_func(name,self.USER_NAME)

    u'''设置开始时间
        parameters:
            startTime : 开始时间
    '''    
    def set_start_time(self,startTime):
        try:
            start_time_js = "$('input[id=fortStartTime]').attr('readonly',false)"
            self.driver.execute_script(start_time_js)
        except Exception as e:
            print ("start_time js execute error: ") + str(e)
        self.set_common_func(startTime,self.USER_START_TIME)

    u'''设置结束时间
        parameters:
            endTime : 结束时间
    '''      
    def set_end_time(self,endTime):
        try:
            end_time_js = "$('input[id=fortEndTime]').attr('readonly',false)"
            self.driver.execute_script(end_time_js)  
            self.set_common_func(endTime,self.USER_END_TIME)       
        except Exception as e:
            print ("set endTime error: ") + str(e)

    u'''设置用户状态
        parameters:
            value : 0代表锁定,1代表正常
    '''          
    def set_user_status(self,statusValue):
        self.set_common_select_elem(statusValue,self.USER_STATUS)
    
    u'''获取部门箭头的展开状态'''
    def get_element_attribute(self):
        selem = self.getElem.find_element_with_wait_EC('id','tree_1_switch')
        selem_class = selem.get_attribute('class')
        arrow_type = selem_class.split('_')[-1]
        return arrow_type
    
    u'''获取部门a标签
       parameter:
           deptname:部门名称
    '''
    def get_tag_by_a(self, deptname):
        try:
            #获取所有a标签的对象
            elems = self.driver.find_elements_by_tag_name("a")
    
            for elem in elems:
                #获取a标签title
                elemtext = elem.get_attribute("title")
                #获取a标签id
                elemid = elem.get_attribute("id")
    
                if deptname == elemtext:
                    time.sleep(1)
                    self.getElem.find_element_wait_and_click_EC('id',elemid)
                    break
    
        except Exception as e:
            print "Get tag a error:" + str(e)
    
    u'''选择部门公用方法
            parameters : 
                input_id : 部门input框id
                deptname : 部门名称
    '''
    def select_depmt_common(self,input_id,deptname):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.getElem.find_element_wait_and_click_EC("id",input_id)
        time.sleep(1)
        #点开部门箭头
        if self.get_element_attribute() != "open":
            self.getElem.find_element_wait_and_click_EC('id','tree_1_switch')
        time.sleep(2)
        self.get_tag_by_a(deptname)
        
    u'''用户部门'''
    def set_dep(self,deptname):
        try:
            self.select_depmt_common(self.USER_DEP,deptname)
        except Exception as e:
            print ("Set user department error: ") + str(e)
    
    u'''部门查询'''
    def set_query_depmt(self,depmtName):
        try:
            query_dep_js = "$('input[id=department_name]').attr('readonly',false)"
            self.driver.execute_script(query_dep_js)  
            self.set_common_func(depmtName,self.USER_DEP)   
        except Exception as e:
            print ("set query department error: ") + str(e)        
    
    u'''勾选子查询'''
    def click_child_node(self):
        self.getElem.find_element_wait_and_click_EC('id',self.USER_DEP)
        self.click_checkbox(self.QUERY_CHILD_NODE)

    u'''清空部门'''
    def clear_dep(self):
        self.getElem.find_element_with_wait_clickable_and_click("id",self.USER_DEP)
        self.getElem.find_element_with_wait_clickable_and_click("id",self.DEP_CLEAR)

    u'''填写口令
        parameters:
            pwd : 用户口令
    '''  
    def set_user_pwd(self,pwd):
        return self.set_common_func(pwd,self.USER_PWD)

    u'''填写确认口令
        parameters:
            pwd : 确认口令
    '''      
    def set_user_enquire_pwd(self,repwd_):
        return self.set_common_func(repwd_,self.USER_RE_PWD)

    u'''填写手机号
        parameters:
            mobile : 手机
    '''
    def set_user_mobile(self,mobile):
       return self.set_common_func(mobile,self.USER_MOBILE)

    u'''填写电话
        parameters:
            phone : 电话
    '''        
    def set_user_phone(self,phone):
        return self.set_common_func(phone,self.USER_PHONE)

    u'''填写邮箱
        parameters:
            email : 邮箱
    '''      
    def set_user_email(self,email):
        return self.set_common_func(email,self.USER_EMAIL)
    
    u'''填写地址
        parameters:
            address : 地址
    '''        
    def set_user_address(self,address):
        return self.set_common_func(address,self.USER_ADDRESS)

    u'''勾选checkbox
            parameters :
                value : id值
    '''
    def click_checkbox(self,value):
        try:
            time.sleep(2)
            checkbox = self.getElem.find_element_with_wait_EC("id",value)
            if checkbox.is_selected() == False:
                checkbox.click()
        except Exception as e:
            print ("checkbox selected error: ") + str(checkbox) + str(e)
    
    u'''勾选登录时修改'''
    def set_login_selectd(self):
        self.click_checkbox(self.LOGIN_MODEY)

    u'''勾选审计查看审批管理员'''
    def set_audit_admin_selectd(self):
        self.click_checkbox(self.IS_APPROVAL)

    u'''点击高级选项'''
    def click_advanced_option(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.ADVANCED_OPTIONS)
        except Exception as e:
            print ("click advanced options error: ") + str(e)
    
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
    
    u'''select元素通过text选择元素通用方法
            parameter:
                var_text : select元素option选项text的值
                locator : ID值
    '''    
    def set_common_select_elem_by_text(self,var_text,value):
        try:
            revar_text = self.cnEnde.is_float(var_text)
            select_elem = self.getElem.find_element_with_wait_EC('id',value)
            self.selectElem.select_element_by_visible_text(select_elem,str(var_text))
        except Exception as e:
            print ("selected select element option  by visible text error: ") + str(revar_text) + str(e)

    u'''设置用户角色'''
    def set_user_role(self,roleText):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.click_role_msg()
        roleList = roleText.split(',')
        try:
            #判断角色是否为空
            if roleText != "":
                for roleName in roleList:
                    self.set_common_select_elem_by_text(roleName,self.ROLE_SELECTD_ELEM)
        except Exception as e:
            print ("Set user role error: ") + str(e)

    '''用户状态检索
        parameters:
            status : 用户状态
    '''    
    def search_by_user_status(self,status):
        self.set_common_select_elem(status,self.SEARCH_USER_STATUS)

    u'''设置时间访问规则
            parameter:
                timeValue : 时间规则option的value值(-1代表请选择)
    '''
    def set_time_access_rule(self,timeValue):
        return self.set_common_select_elem(timeValue,self.TIME_RULE)

    u'''设置地址访问规则
            parameter:
                addressValue : 地址规则option的value值(-1代表请选择)
    '''    
    def set_address_access_rule(self,addressValue):
        return self.set_common_select_elem(addressValue,self.ADDRESS_RULE)

    u'''设置访问方式
            parameter:
                loginValue : 访问方式option的value值(2代表默认)
    '''    
    def set_auth_method_rule(self,loginValue):
        self.set_common_select_elem(loginValue,self.AUTH_CODE)
        
    u'''填写AD域用户
            parameter:
                adUser : AD域用户名称
    '''        
    def set_ad_name(self,adUser):
        return self.set_common_func(adUser,self.USER_DOMAIN_ACCOUNT)

    u'''填写RADIUS用户
            parameter:
                radiusUser : RADIUS用户名称
    '''        
    def set_radius_name(self,radiusUser):
        return self.set_common_func(radiusUser,self.USER_RADIUS)

    u'''通过用户状态获取行数
            parameters:
                value : 开关value值(switch_on:关,switch_off:开)
    '''
    def search_by_status(self,value):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        
        row = 0
        try:
            
            #获取所有行的用户开关状态
            switchs = self.driver.find_elements_by_id("btn_qh")
            for switch in switchs:
                if switch.get_attribute('class') == value:
                    row = row + 1
            return row
        except Exception as e:
            print ("No users switch status is ") + str(value) + str(e)

    u'''通过用户账号或名称获取行数
            parameters:
                accountName : 查找条件(账号或名称)
    '''    
    def search_direct_by_account_or_name(self,accountName):
        self.frameElem.from_frame_to_otherFrame("mainFrame")

        row = 0
        reName = self.cnEnde.is_float(accountName)
        try:

            #查找name属性为fortUserAccount的所有元素
            account_elems = self.driver.find_elements_by_name("fortUserAccount")
            
            #查找name属性为fortUserName的所有元素
            username_elems = self.driver.find_elements_by_name("fortUserName")

            for index in range(len(account_elems)):
                accountValue_text = account_elems[index].text
                nameValue_text = username_elems[index].text
                
                if (accountName in accountValue_text) or (accountName in nameValue_text):
                    row = row + 1
            return row
        except Exception as e:
            print ("No users accountOrName is ") + str(reName) + str(e)

    u'''通过部门获取行数
            parameters:
                dep : 部门名称
    '''      
    def search_direct_by_dep(self,dep):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        
        row = 0
        redep = self.cnEnde.cnCode(dep)
        try:
            text_list = self.driver.find_elements_by_name("fortDepartmentName")
            for fortDepValue in text_list:
                fortDepValue_text = fortDepValue.text
                if fortDepValue_text == dep:
                    row = row + 1
        except Exception:
            print redep + "is not exsit."
        return row


#----------------------------------证书相关------------------------------------
    u'''生成证书'''
    def create_cert(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.CREATE_CERT)
            time.sleep(3)
            
        except Exception as e:
            print ("click create button error: ") + str(e)

    u'''删除证书'''
    def delete_cert(self):
        try:
            time.sleep(1)
            self.getElem.find_element_with_wait_clickable_and_click("id",self.DELETE_CERT)
            
        except Exception as e:
            print ("click delete cert button error: ") + str(e)
    
    u'''获取证书指定属性的内容
            parameters:
                locator ： ID值
    '''
    def get_cert_var_text(self,value):
        try:
            cert_var_text = self.getElem.find_element_with_wait_EC("id",value).text
            return cert_var_text
        
        except Exception as e:
            print ("Get cert var text error: ") + str(cert_var_text) + str(e)        

    u'''获取生成的证书名字'''
    def get_cert(self):
        return self.get_cert_var_text(self.CERT_NAME)

    u'''获取初始证书名字'''
    def get_init_cert_name(self):
        
        return self.get_cert_var_text(self.INIT_CERT_NAME)

    u'''获取证书序列号'''
    def get_cert_serial_num(self):
        return self.get_cert_var_text(self.CERT_SERIAL_NUM)

    u'''点击返回按钮'''
    def click_back_button(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            back_button = self.getElem.find_element_with_wait_EC('id',self.BACK_BUTTON)
            if back_button.is_displayed():
                time.sleep(1)
                back_button.click()
        except Exception as e:
            print("Click the return button error: ") + str(e)

    u'''填写用户基本信息
            parameters:
                data : 用户列表数据
                roleText : 用户角色
    '''
    def set_user_basic_info(self,data,roleText):
        self.cmf.select_menu(u"运维管理")
        self.cmf.select_menu(u"运维管理",u"用户")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.add_button()
        self.set_user_account(data[2])
        self.set_user_name(data[3])
        self.set_start_time(data[4])
        self.set_end_time(data[5])
        self.set_dep(data[6])
        self.set_user_pwd(data[7])
        self.set_user_enquire_pwd(data[8])
        self.set_user_mobile(data[9])
        self.set_user_phone(data[10])
        self.set_user_email(data[11])
        self.set_user_address(data[12])
        if data[13] != "":
            #点击高级选项
            self.click_advanced_option()
            self.set_auth_method_rule(data[13])
            
            #访问方式不是默认方式
            if int(data[13]) != 2:
                self.set_ad_name(data[14])
        if data[15] != "":
            self.set_user_role(roleText)
            self.click_role_add_button()

        self.save_button()
        self.cmf.click_login_msg_button()
        self.click_back_button()

    u'''用户状态改变为关'''
    def change_user_status_off(self,account):
        off_status = "switch_off"
        self.change_user_status_button(account,off_status)
    
    u'''用户状态改变为开'''
    def change_user_status_on(self,account):
        on_status = "switch_on"
        self.change_user_status_button(account,on_status)