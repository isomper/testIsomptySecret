#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
#导入驱动
sys.path.append("/testIsompSecret/common/")
from _icommon import getElement,selectElement,frameElement,commonFun
from _initDriver import initDriver
from _globalVal import globalValue
from _fileRead import fileRead

sys.path.append("/testIsompSecret/webElement/auth_method/")
from authMethodElement import AuthMethodPage

sys.path.append("/testIsompSecret/webElement/role/")
from test_roledf import Role

#导入登录
sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/user/")
from userElement import UserPage

sys.path.append("/testIsompSecret/webElement/department/")
from test_dptm_ment import Department

sys.path.append("/testIsompSecret/webElement/resource/")
from test_resource_common import Resource
from test_windows_ment import WindowsResource
from databaseElement import DatabaseResource
from test_resource_accountmgr_ment import Accountmgr
sys.path.append("/testIsompSecret/webElement/group/")
from test_regroup_ment import Regroup
from test_usergroup_ment import Usergroup
sys.path.append("/testIsompSecret/webElement/client_conf")
from clientConfElement import ClientPage
sys.path.append("/testIsompSecret/webElement/rule")
from test_command_rule_ment import CommandRule
sys.path.append("/testIsompSecret/webElement/ass_service")
from ntpElement import NtpService
sys.path.append("/testIsompSecret/webElement/mail")
from test_mail_ment import MailPage

sys.path.append("/testIsompSecret/webElement/passwd_envelope")
from test_passwd_envelope_ment import EnvelopePage

sys.path.append("/testIsompSecret/webElement/sso")
from ssoElement import SsoPage
#导入告警配置
sys.path.append("/testIsompSecret/webElement/alarm_configuration")
from alarmElement import AlarmPage

#导入应用发布
sys.path.append("/testIsompSecret/webElement/application")
from appConfElement import AppPage
sys.path.append("/testIsompSecret/webElement/authorization")
from authrizationElement import AuthorizationPage
sys.path.append("/testIsompSecret/testCase/authorization/")
from test_authorization import testAuthorization
sys.path.append("/testIsompSecret/webElement/ass_service/")
from syslogElement import Syslog
sys.path.append("/testIsompSecret/webElement/password_strategy/")
from pwdStrategyElement import PwdStrategy

class setDriver():
   
    u'''本地驱动'''
    def set_local_driver(self):
        driver = initDriver().open_driver()
        return driver

    u'''远程驱动'''
    def set_remote_driver(self):
        driver_lists = globalValue().get_value()
        driver = initDriver().remote_open_driver(driver_lists[0],driver_lists[1])
        
#        driver = initDriver().remote_open_driver("http://172.16.10.21:5555/wd/hub","firefox")
        return driver

    #获取驱动
    def set_driver(self):
         #读取test.conf文件内容
        fileList = fileRead().get_ip_address()
        #读取开关字符，0代表本地登录，1代表远程登录
        ipAdd = fileList[3].strip('\n')
        if ipAdd == '0':
            return self.set_local_driver()
        elif ipAdd == '1':
            return self.set_remote_driver()

class CommonSuiteData():
    
    def __init__(self,driver):
        self.driver = driver
        self.dataFile = dataFileName()
        self.cmf = commonFun(self.driver)
        self.initDriver = initDriver()
        self.loginElem = loginPage(self.driver)
        self.roleElem = Role(self.driver)
        self.userElem = UserPage(self.driver)
        self.frameElem = frameElement(self.driver)
        self.authElem = AuthMethodPage(self.driver)
        self.dptment = Department(self.driver)
        self.resource = Resource(self.driver)
        self.account = Accountmgr(self.driver)
        self.windowsElem = WindowsResource(self.driver)
        self.databaseElem = DatabaseResource(self.driver)
        self.usergroup = Usergroup(self.driver)
        self.regroup = Regroup(self.driver)
        self.appElem = AppPage(self.driver)
        self.authorizationElem = AuthorizationPage(self.driver)
        self.testAutho = testAuthorization(self.driver)
        self.clientElem = ClientPage(self.driver)
        self.command = CommandRule(self.driver)
        self.ntp = NtpService(self.driver)
        self.mail = MailPage(self.driver)
        self.syslog = Syslog(driver)
        self.ssoElem = SsoPage(self.driver)
        self.alarm = AlarmPage(self.driver)
        self.PwdStr = PwdStrategy(self.driver)
        self.passwdenvelope = EnvelopePage(self.driver)

    u'''切换模块
            parameter:
                levelText1 : 一级模块名称
                levelText2 : 二级模块名称
    '''     
    def switch_to_moudle(self,levelText1,levelText2):
        time.sleep(2)
        self.frameElem.from_frame_to_otherFrame("topFrame")
        
        self.cmf.select_menu(levelText1)
        self.cmf.select_menu(levelText1,levelText2)

#----------------------------------------用户相关------------------------------  
    
    u'''填写用户信息
            parameters:
                data[1] : 用户名称
                data[3] : 用户账号
                data[4] : 用户密码
                data[5] : 确认密码
                data[6] : 开始时间
                data[7] : 访问方式
                data[8] : AD域账号
                roleText : 用户角色
    '''
    def set_user_basic_info(self,data,roleText,status='no'):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        if status != 'no':
            self.userElem.add_role_button()
        else:
            self.userElem.add_button()
        self.userElem.set_user_account(data[3])
        self.userElem.set_user_name(data[1])
        self.userElem.set_user_pwd(data[4])
        self.userElem.set_user_enquire_pwd(data[5])
        self.userElem.set_start_time(data[6])
        if data[12] != "":
            self.userElem.set_user_email(data[12])
        if data[10] != "":
            self.userElem.set_dep(data[10])
        if data[7] !="":
            #设置访问方式
            self.userElem.click_advanced_option()
            self.userElem.set_auth_method_rule(data[7])
            
            #访问方式不是默认方式
            if int(data[7]) != 2:
                self.userElem.set_ad_name(data[8])
        if data[9] != "":
            self.userElem.set_user_role(roleText)
            self.userElem.click_role_add_button()
        self.userElem.save_button()
        self.cmf.click_login_msg_button()

    u'''删除用户'''
    def del_user(self):
        self.switch_to_moudle(u"运维管理",u"用户")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.userElem.select_all_button()
        self.userElem.del_button()
        self.frameElem.switch_to_content()
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()
    
    u'''用户退出'''
    def user_quit(self):
        self.loginElem.quit()
    
#-----------------------------部门--------------------------------------------
    u'''填写部门名称
            parameters :
                data[0] : 部门名称
                data[1] : 操作类型(添加：0)
                data[2] : 添加的部门名称
    '''
    def set_dep(self,data):
        self.switch_to_moudle(u"运维管理",u"组织定义")
        self.dptment.click_left_department()
        #点击展开按钮
        self.dptment.click_dept_switch()
        self.dptment.click_basic_operation(data[0], int(data[1]))
        self.dptment.popup_sendkey(data[2])
        self.dptment.click_ok_button()
        self.cmf.click_login_msg_button()
    
    def set_del_dep(self,data):
        self.switch_to_moudle(u"运维管理",u"组织定义")
        self.dptment.click_left_department()
        self.dptment.click_dept_switch()
        self.dptment.click_basic_operation(data[0],int(data[1]))
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()
        
#-----------------------------用户组------------------------------------------    
    u'''添加用户到用户组'''
    def set_user_to_group(self,data):
#        self.usergroup.click_left_usergroup()
#        self.usergroup.click_usergroup_switch()
        self.usergroup.click_usergroup_add_user(data[3], data[4])
        self.regroup.check_depart(data[5])
        self.usergroup.click_usergroup_add_user_query()
        self.regroup.check_all_resource()
        self.regroup.click_resource_okbutton()
        self.cmf.click_login_msg_button()
    
    u'''填写用户组信息
            parameters:
                data[0] : 操作类型(添加：0)
                data[1] : 部门名称
                data[2] : 编辑的用户组名称
                data[3] : 添加的用户组名称
    '''
    def set_add_user_group(self,data):
        self.switch_to_moudle(u"运维管理",u"组织定义")
        self.usergroup.click_left_usergroup()
        self.usergroup.click_usergroup_switch()
        self.usergroup.usergroup_click_basic_operation(int(data[0]), data[1], data[2])
        self.dptment.popup_sendkey(data[3])
        self.dptment.click_ok_button()
        self.cmf.click_login_msg_button()
        if data[4] != "":
            self.set_user_to_group(data)
    
    u'''删除用户组
            parameters :
                data[0] : 操作类型(删除:4)
                data[1] : 部门名称
                data[2] : 删除的用户组名称
    '''
    def set_del_user_group(self,data):
        self.switch_to_moudle(u"运维管理",u"组织定义")
        self.usergroup.click_left_usergroup()
        self.usergroup.click_usergroup_switch()
        self.usergroup.usergroup_click_basic_operation(int(data[0]), data[1], data[2])
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()
        
#-----------------------------资源组------------------------------------------    
    u'''添加资源到资源组'''
    def set_res_to_group(self,data):
        self.regroup.click_regroup_add_resouce(data[3], data[4])
        self.regroup.check_depart(data[5])
        self.regroup.click_regroup_add_resouce_query()
        self.regroup.check_all_resource()
        self.regroup.click_resource_okbutton()
        time.sleep(1)
        self.cmf.click_login_msg_button()
    
    u'''填写资源组信息
            parameters:
                data[0] : 操作类型(添加：0)
                data[1] : 部门名称
                data[2] : 编辑的资源组名称
                data[3] : 添加的资源组名称
    '''    
    def set_add_res_group(self,data):
        self.switch_to_moudle(u"运维管理",u"组织定义")
        self.regroup.click_left_regroup()
        self.regroup.click_regroup_switch()
        self.regroup.regroup_click_basic_operation(int(data[0]), data[1], data[2])
        self.dptment.popup_sendkey(data[3])
        self.dptment.click_ok_button()
        self.cmf.click_login_msg_button()
        if data[4] != "":
            self.set_res_to_group(data)
    
    u'''删除资源组
            parameters :
                data[0] : 操作类型(删除:4)
                data[1] : 部门名称
                data[2] : 删除的资源组名称
    '''
    def set_del_res_group(self,data):
        self.switch_to_moudle(u"运维管理",u"组织定义")
        self.regroup.click_left_regroup()
        self.regroup.click_regroup_switch()
        self.regroup.regroup_click_basic_operation(int(data[0]), data[1], data[2])
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()
    

#-----------------------------资源--------------------------------------------
    u'''填写资源基本信息
            parameters : 
                data[0]:资源类型
                data[1]:资源名称
                data[2]:资源IP
                data[3]:部门
    '''
    def set_resource_info(self,data):
        time.sleep(2)
        self.switch_to_moudle(u"运维管理",u"资源")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.resource.click_add_edit_button()
        self.resource.select_resource_type(data[0])
        time.sleep(2)
        self.resource.set_resource_name(data[1])
        self.resource.set_resource_ip(data[2])
        if data[3] != 'no':
            time.sleep(5)
            self.resource.set_depart(data[3])
        #选择协议
        if data[4] != "":
            self.resource.select_agreement(data[4])
        if data[5] != "":
            self.resource.click_account_sync()
            self.resource.set_admin_account(data[5])
            self.resource.set_admin_pwd(data[6])
            self.resource.set_confirm_pwd(data[7])
        #提权口令
        if data[8] != "":
            self.resource.click_up_super()
            self.resource.set_super_pwd(data[8])
            self.resource.set_super_confirm_pwd(data[9])
        #填写域名
        if data[10] != "":
            self.databaseElem.set_domain_name(data[10])
        #账号分类
        if data[11] != "":
            self.resource.click_account_sync()
            self.windowsElem.select_account_type(data[11])
        #归属域控主机
        if data[12] != "":
            self.windowsElem.select_attach_domian(data[12])
        #主机名
        if data[13] != "":
            self.databaseElem.set_host_name(data[13])
        
        self.resource.click_save_button()
        self.cmf.click_login_msg_button()
        time.sleep(3)
        self.cmf.back()
    
    u'''填写数据库基本信息'''
    def set_database_res_info(self,data):
        self.switch_to_moudle(u"运维管理",u"资源")
        self.frameElem.from_frame_to_otherFrame("mainFrame")        
        self.resource.click_add_edit_button()
        self.resource.select_resource_type(data[2])
        self.databaseElem.add_edit_database_resource(data)
        self.cmf.click_login_msg_button()
        time.sleep(3)
        self.cmf.back()
        
    u'''填写资源账号基本信息
            parameters: 
                data[1]:资源名称
                data[4] : 账号编辑方式
                data[5] : 账号名称
                data[6] : 口令
                data[7] : 确认口令
    '''
    def set_res_account(self,data):
        self.switch_to_moudle(u"运维管理",u"资源")
        self.account.click_account_manage_button(data[0])
        time.sleep(1)
        self.account.click_account_add_edit_button(data[2])
        self.account.select_edit_way(data[1])
        if data[2] != "no":
            self.account.set_account_name(data[2])
        self.account.set_account_pwd(data[3])
        self.account.set_account_confirm_pwd(data[4])
        self.account.set_authorize()
        self.account.click_save_account()
        self.cmf.click_login_msg_button()

#-----------------------------授权----------------------------------------
    u'''填写授权基本信息
            parameters:
                data[1]:授权名称
                data[2]:部门名称
                data[3]:状态
    '''
    def set_authorization(self, data):
        self.switch_to_moudle(u'运维管理', u'授权')
        self.authorizationElem.add_button()
        self.authorizationElem.set_auth_name(data[1])
        self.authorizationElem.set_dep(data[2], data[3])
        self.authorizationElem.click_add_user()
        self.authorizationElem.set_select_user_search_button()
        self.authorizationElem.set_user_check_all_button()
        self.authorizationElem.set_ok_button()
        #添加资源
        self.authorizationElem.click_add_res()
        self.authorizationElem.set_select_res_search_button()
        self.authorizationElem.set_res_check_all_button()
        self.authorizationElem.set_ok_button()
        self.authorizationElem.save_button()
        self.cmf.click_login_msg_button()
        self.cmf.back()
#---------------------------------填写应用发布信息----------------------------
    u'''填写应用发布信息'''
    def set_application_info(self,data):
        self.switch_to_moudle(u"系统配置",u"关联服务")
        self.appElem.app_module_button()
        self.appElem.click_add_button()
        self.appElem.set_name(data[0])
        self.appElem.set_ip(data[1])
        self.appElem.set_app_account(data[3])
        self.appElem.set_pwd(data[4])
        self.appElem.set_repwd(data[5])
        self.appElem.ip_is_succ()
        self.appElem.click_save_button()
        self.cmf.click_login_msg_button()
    
    u'''删除应用发布'''
    def del_application(self,rowList):
        self.switch_to_moudle(u"系统配置",u"关联服务")
        self.appElem.app_module_button()
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        app_data = self.get_table_data("add_application")
        for dataRow in rowList:
            data = app_data[dataRow]
            if dataRow != 0:
                self.appElem.operate_del(data[0])
                self.cmf.click_login_msg_button()
                self.cmf.click_login_msg_button()    

#-------------------------------------客户端-----------------------------------
    u'''填写客户端基本信息'''
    def set_client_info(self,data):
        #self.switch_to_moudle(u"系统配置",u"客户端配置")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.clientElem.add_button()
        self.clientElem.set_client_name(data[2])
        self.clientElem.set_action_stream(data[3])
        self.clientElem.set_database_res_type(data[0],data[1])
        self.clientElem.save_button()
    
    u'''删除客户端'''
    def set_delete_client_info(self,data):
        #self.switch_to_moudle(u"系统配置",u"客户端配置")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.clientElem.select_query_res_type(data[0],data[1])
        self.clientElem.click_query_button()
        self.clientElem.del_operation(data[2])
        self.cmf.click_login_msg_button()
    
#------------------------------资源账号授权------------------------------------
    u'''添加用户和资源账号类型的授权'''
    def set_authorization_info(self,data):
        self.switch_to_moudle(u"运维管理",u"授权")
        self.testAutho.common_part(data)
        self.testAutho.add_user(data)
        self.authorizationElem.click_add_res_account()
        self.authorizationElem.set_select_res_ip(data[6])
        self.authorizationElem.set_select_res_account(data[8])
        self.authorizationElem.set_select_res_search_button()
        self.authorizationElem.set_res_check_all_button()
        self.authorizationElem.set_ok_button()
        self.authorizationElem.res_account_status()
        self.authorizationElem.save_button()
        self.cmf.click_login_msg_button()

    u'''删除授权'''
    def del_authorization(self):
        self.switch_to_moudle(u"运维管理", u"授权")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.authorizationElem.check_all()
        self.authorizationElem.del_button()
        self.cmf.click_login_msg_button()
        self.cmf.click_login_msg_button()

        
#-----------------------------数据----------------------------------------
    u'''获取数据
        Parameters:
            - sheetname:sheet名称
            return：表格数据
    '''
    def get_table_data(self,sheetname):
        filePath = self.dataFile.get_common_suite_test_data_url()
        fileData = self.dataFile.get_data(filePath,sheetname)
        return fileData
    
    u'''添加应用发布'''
    def add_application(self,rowList):
        app_data = self.get_table_data('add_application')
        for dataRow in rowList:
            data = app_data[dataRow]
            if dataRow != 0:
                self.set_application_info(data)

    u'''初始化用户登录'''
    def isomper_login(self):
        login_data = self.get_table_data('add_user')
        logindata = login_data[4]
        self.loginElem.login(logindata)
    
    u'''添加用户数据模板'''
    def add_user_data_module(self,rowList):
        time.sleep(2)
        self.switch_to_moudle(u"运维管理",u"用户")
        user_data = self.get_table_data("add_user")
        for dataRow in rowList:
            data = user_data[dataRow]
            if dataRow != 0:
                self.set_user_basic_info(data,data[9],data[13])
                self.userElem.click_back_button()
        
    u'''添加系统管理员和部门管理员的用户'''
    def add_user_with_role(self):
        rowList = [1]
        self.add_user_data_module(rowList)
        
    u'''登录并切换至角色公用方法
            parameters: 
                login_status ：'no'(登录状态：没有登录)
    '''
    def login_and_switch_to_common(self,login_status='no'):
        login_data = self.get_table_data("add_user")
        logindata = login_data[1]
        if login_status == 'no':
            self.loginElem.login(logindata)
        
        #获取角色
        roleList = logindata[9].split(',')
        return roleList

    u'''使用系统管理员登录系统'''
    def login_sysadmin(self):
        login_data = self.get_table_data('add_user')
        logindata = login_data[1]
        self.loginElem.login(logindata)

    u'''使用安全保密管理员登录系统'''
    def login_secadmin(self):
        login_data = self.get_table_data('add_user')
        logindata = login_data[2]
        self.loginElem.login(logindata)

    u'''使用安全审计员登录系统'''
    def login_sysaudit(self):
        login_data = self.get_table_data('add_user')
        logindata = login_data[3]
        self.loginElem.login(logindata)

    u'''用户登录系统'''
    def login_user(self, row):
        login_data = self.get_table_data('add_user')
        logindata = login_data[int(row)]
        self.loginElem.login(logindata)

    u'''切换至运维操作员'''
    def switch_to_operation(self):
        self.cmf.select_role_by_text(u"运维操作员")
    
    #使用新添加的用户登录
    def use_new_user_login(self):
        login_data = self.get_table_data("add_user")
        logindata = login_data[1]
        time.sleep(2)
        self.loginElem.login(logindata)
    
    u'''运维管理员登录'''
    def sso_user_login(self,rowList):
        login_data = self.get_table_data("add_user")
        logindata = login_data[rowList]
        time.sleep(1)
        self.loginElem.login(logindata)
    
    u'''运维管理员AD域方式登录'''
    def sso_user_ad_login(self,rowList):
        login_data = self.get_table_data("add_user")
        logindata = login_data[rowList]
        self.frameElem.switch_to_content()
        self.loginElem.set_login_method(logindata[2])
        self.loginElem.set_ad_login_username(logindata[3])
        self.loginElem.set_ad_login_pwd(logindata[11])
        time.sleep(1)
        self.loginElem.click_login_button()
        
    u'''添加认证配置'''
    def add_meth_method(self):
        meth_data = self.get_table_data("meth_method")
        methData = meth_data[1]
        
        self.switch_to_moudle(u"策略配置",u"认证强度")
        
        self.authElem.select_all_auth(methData)
    
    u'''会话配置,设置最大登录数'''
    def set_login_max_num(self):
        self.loginElem.set_max_login_count()
    
    u'''添加登录测试数据'''
    def add_login_data(self):
        rowList = [2,3,4,5,6,7]
        self.add_user_data_module(rowList)
    
    u'''添加授权用户'''
    def add_authorization_user(self):
        rowList = [8,9,10,11,12]
        self.add_user_data_module(rowList)
    
    u'''添加应用发布用户'''
    def add_app_user(self):
        rowList = [3]
        self.add_user_data_module(rowList)
    
    u'''添加单点登录用户'''
    def add_sso_user(self):
        rowList = [6,8,9,10,11,13]
        self.add_user_data_module(rowList)
        
    u'''添加部门'''
    def add_dep(self, rowList):
        dep_data = self.get_table_data("add_dep")
        for dataRow in rowList:
            data = dep_data[dataRow]
            if dataRow != 0:
                self.set_dep(data)
    
    u'''删除部门'''
    def del_dep(self, rowList):
        dep_data = self.get_table_data("del_dep")
        for dataRow in rowList:
            data = dep_data[dataRow]
            if dataRow != 0:
                self.set_del_dep(data)
    
    u'''增加资源数据模板'''
    def add_resource_modele(self,rowList):
        res_data = self.get_table_data("add_res")
        for dataRow in rowList:
            data = res_data[dataRow]
            if dataRow != 0:
                self.set_resource_info(data)
    
    u'''添加授权资源'''
    def add_resource(self):
        rowList = [1,2]
        self.add_resource_modele(rowList)
    
    u'''添加sso资源'''
    def add_sso_resource(self):
        #rowList = [1,2,3,4,5,7,8]
        rowList = [1,3,4,5]
        self.add_resource_modele(rowList)
    
    u'''添加依附操作系统'''
    def add_database_resource(self):
        rowList = [2]
        self.add_resource_modele(rowList)
    
    u'''添加资源账号数据模板'''
    def add_res_account_module(self,rowList):
        account_data = self.get_table_data("res_account")
        for dataRow in rowList:
            data = account_data[dataRow]
            if dataRow != 0:
                self.set_res_account(data)    
    
    u'''添加授权资源账号'''
    def add_res_account(self):
        rowList = [1,3]
        self.add_res_account_module(rowList)
    
    u'''添加sso资源账号'''
    def add_sso_res_account(self):
        rowList = [1,2,4,5,6,7]
        #rowList = [1,2,3,4,5,6,7,9,10]
        self.add_res_account_module(rowList)
        
    u'''添加用户组'''
    def add_user_group(self,rowList):
        user_group_data = self.get_table_data("add_user_group")
        for dataRow in rowList:
            data = user_group_data[dataRow]
            if dataRow != 0:
                self.set_add_user_group(data)
    
    u'''删除用户组'''
    def del_user_group(self,rowList):
        user_group_data = self.get_table_data("del_user_group")
        for dataRow in rowList:
            data = user_group_data[dataRow]
            if dataRow != 0:
                self.set_del_user_group(data)
    
    u'''添加资源组'''
    def add_res_group(self,rowList):
        res_group_data = self.get_table_data("add_res_group")
        for dataRow in rowList:
            data = res_group_data[dataRow]
            if dataRow != 0:
                self.set_add_res_group(data)
    
    u'''删除资源组'''
    def del_res_group(self,rowList):
        res_group_data = self.get_table_data("del_res_group")
        for dataRow in rowList:
            data = res_group_data[dataRow]
            if dataRow != 0:
                self.set_del_res_group(data)

    u'''添加授权'''
    def add_authrization(self, rowList):
        auth_data = self.get_table_data("add_authorization")
        for dataRow in rowList:
            data = auth_data[dataRow]
            if dataRow != 0:
                self.set_authorization(data)

    u'''添加授权数据模板'''
    def add_authorization_module(self,rowList):
        autho_data = self.get_table_data("add_account_auth")
        for dataRow in rowList:
            data = autho_data[dataRow]
            if dataRow != 0:
                self.set_authorization_info(data)
                self.authorizationElem.back_button()
                
    u'''添加单点登录授权'''
    def add_sso_authorization(self):
        rowList = [1]
        #rowList = [1,2,3,4,5,6,7]
        self.add_authorization_module(rowList)
    
    u'''单点登录模板'''
    def sso_module(self,rowList):
        sso_data = self.get_table_data("sso")
        for dataRow in rowList:
            data = sso_data[dataRow]
            if dataRow != 0:
                self.frameElem.from_frame_to_otherFrame("rigthFrame")
                self.ssoElem.select_account(data[0],data[1])
                self.ssoElem.select_sso_icon(data[0],data[2])
                if data[3] != "":
                    self.ssoElem.select_protocol(data[3])
                #self.ssoElem.execute_chrome_key()
                self.ssoElem.choice_browser(data[2],data[4],data[5],data[6])               
    
    u'''添加客户端数据模板'''
    def add_client_module(self,rowList):
        client_data = self.get_table_data("add_client")
        self.switch_to_moudle(u"系统配置",u"客户端配置")
        for dataRow in rowList:
            data = client_data[dataRow]
            if dataRow != 0:
                self.set_client_info(data)
    
    u'''删除客户端数据模板'''
    def del_client_module(self,rowList):
        client_data = self.get_table_data("del_client")
        self.switch_to_moudle(u"系统配置",u"客户端配置")
        for dataRow in rowList:
            data = client_data[dataRow]
            if dataRow != 0:
                self.set_delete_client_info(data)
    
    u'''添加数据库资源模板'''
    def add_database_res_module(self,rowList):
        database_data = self.get_table_data("add_database")
        for dataRow in rowList:
            data = database_data[dataRow]
            if dataRow != 0:
                self.set_database_res_info(data)

    u'''删除用户数据模板'''
    def del_user_data_module(self,rowList):
        self.switch_to_moudle(u"运维管理", u"用户")
        time.sleep(2)
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        user_data = self.get_table_data("add_user")
        for dataRow in rowList:
            data = user_data[dataRow]
            if dataRow != 0:
                self.userElem.operate_delete(data[1])
                self.frameElem.switch_to_content()
                self.cmf.click_login_msg_button()
                self.cmf.click_login_msg_button()

    u'''添加密码策略数据模板'''
    def add_strategy_data_module(self,rowList):
        self.switch_to_moudle(u"策略配置", u"密码策略")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        pwd_data = self.get_table_data("add_strategy")
        for dataRow in rowList:
            data = pwd_data[dataRow]
            if dataRow != 0:
                self.PwdStr.add_pwd_button()
                self.PwdStr.set_pwd_name(data[1])
                self.PwdStr.term_of_validity(data[2])
                self.PwdStr.password_length_min(data[3])
                self.PwdStr.password_length_max(data[4])
                self.PwdStr.set_lower_case(data[5])
                self.PwdStr.set_capital(data[6])
                self.PwdStr.set_minimum_digital(data[7])
                self.PwdStr.set_Minimum_symbol(data[8])
                self.PwdStr.save_button()
                self.frameElem.switch_to_content()
                self.cmf.click_msg_button(1)
                self.PwdStr.return_button()

    u'''删除密码策略数据模板'''
    def del_strategy_data_module(self,rowList):
        self.switch_to_moudle(u"策略配置", u"密码策略")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        pwd_data = self.get_table_data("add_strategy")
        for dataRow in rowList:
            data = pwd_data[dataRow]
            if dataRow != 0:
                self.PwdStr.del_sing_strategy(data[1])
                self.frameElem.switch_to_content()
                self.cmf.click_login_msg_button()
                self.cmf.click_login_msg_button()

    u'''删除资源数据模板'''
    def del_resource_modele(self,rowList):
        time.sleep(2)
        self.switch_to_moudle(u"运维管理", u"资源")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        res_data = self.get_table_data("add_res")
        for dataRow in rowList:
            data = res_data[dataRow]
            if dataRow != 0:
                self.resource.click_del_button(data[1])
                self.frameElem.switch_to_content()
                self.cmf.click_login_msg_button()
                self.cmf.click_login_msg_button()

    u'''删除授权数据模板'''
    def del_authorization_module(self,rowList):
        self.switch_to_moudle(u'运维管理', u'授权')
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        autho_data = self.get_table_data("add_account_auth")
        for dataRow in rowList:
            data = autho_data[dataRow]
            if dataRow != 0:
                self.authorizationElem.click_auth_checkbox(data[2])
                self.authorizationElem.del_button()
                self.frameElem.switch_to_content()
                self.cmf.click_login_msg_button()
                self.cmf.click_login_msg_button()

#-------------------------------添加涉密版用户前置条件---------------------------------------
    u'''前置条件通用'''
    def secret_user_prefix_condition(self):
        self.isomper_login()
        self.switch_to_moudle(u'角色管理',u'角色定义')

#------------------------------部门前置条件-----------------------------------
    def depart_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        #切换到组织定义
        self.switch_to_moudle(u"运维管理", u"组织定义")

#------------------------------资源组前置条件-----------------------------------
    def regroup_module_prefix_condition(self):
        #使用安全保密管理员登录
        self.login_secadmin()
        #添加资源
        self.add_resource_modele([9,6])
        self.user_quit()
        #使用系统管理员登录
        self.login_sysadmin()
        #切换到组织定义
        self.switch_to_moudle(u"运维管理", u"组织定义")

    def regroup_module_post_condition(self):
        self.user_quit()
        #使用安全保密管理员登录
        self.login_secadmin()
        #删除资源
        self.del_resource_modele([9,6])
        self.user_quit()

#------------------------------用户组前置条件-----------------------------------
    def usergroup_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        #添加用户
        self.add_user_data_module([5,6])
        #切换到组织定义
        self.switch_to_moudle(u"运维管理", u"组织定义")

    def usergroup_module_post_condition(self):
        self.del_user_data_module([5,6])
        self.user_quit()

#------------------------------NTP服务前置条件---------------------------------
    def ntp_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        #切换到NTP服务
        self.switch_to_moudle(u'系统配置', u'关联服务')
        self.ntp.click_left_moudle(0)

#-------------------------------SYSLOG前置条件---------------------------------
    def syslog_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        #切换到NTP服务
        self.switch_to_moudle(u'系统配置', u'关联服务')
        self.ntp.click_left_moudle(1)

#------------------------------邮件前置条件---------------------------------
    def mail_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        #切换到邮件服务
        self.switch_to_moudle(u'系统配置', u'关联服务')
        self.mail.click_left_moudle_test()

#------------------------------密码信封前置条件---------------------------------
    def passwd_envelope_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        #切换到邮件服务
        self.switch_to_moudle(u'系统配置', u'关联服务')
        self.passwdenvelope.click_left_moudle_envelope()

#-------------------------------应用发布后置条件-------------------------------
    def application_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        self.add_user_data_module([9,10])
        self.switch_to_moudle(u"系统配置", u"关联服务")

    def application_module_post_condition(self):
        self.del_user_data_module([9,10])
        self.user_quit()

#-------------------------------网卡配置前置条件-------------------------------
    def network_card_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        #切换到网卡配置
        self.switch_to_moudle(u'系统配置', u'网络配置')

#-------------------------------路由配置前置条件-------------------------------
    def routing_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        #切换到路由配置
        self.cmf.select_menu(u'系统配置', u'网络配置',u'路由配置')

#------------------------------备份还原前置条件-----------------------------------
    def backup_restore_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()

#-----------------------------客户端配置前置条件------------------------------
    def client_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        self.switch_to_moudle(u"系统配置", u"客户端配置")

#-----------------------------AD域抽取前置条件------------------------------
    def ad_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        self.add_user_data_module([18])
        self.switch_to_moudle(u"系统配置", u"AD定时抽取")

    u'''AD域抽取后置条件'''
    def ad_module_post_condition(self):
        self.del_user_data_module([18])
        self.user_quit()

#------------------------------使用授权前置条件---------------------------------
    def use_auth_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        self.switch_to_moudle(u'系统配置', u'使用授权')

#------------------------------用户模块前置条件--------------------------------
    u'''用户模块前置条件'''
    def user_module_prefix_condition(self):
        #使用系统管理员登录
        self.login_sysadmin()
        self.switch_to_moudle(u'运维管理', u'用户')

#--------------------------认证方式前置条件------------------------------------
    u'''认证方式前置条件'''
    def auth_method_prefix_condition(self):
        #使用安全保密管理员登录
        self.login_secadmin()
        self.add_user_data_module([11])
        self.switch_to_moudle(u"策略配置",u"认证强度")

    u'''认证方式后置条件'''
    def auth_method_post_condition(self):
        self.del_user_data_module([11])
        self.user_quit()

#---------------------------------登录模块前置条件-----------------------------
    u'''登录模块前置条件'''
    def login_module_prefix_condition(self):
        #使用安全保密管理员登录
        self.login_secadmin()
        #配置认证方式
        self.add_meth_method()
        #配置最大登录数
        self.set_login_max_num()
        #添加登录用户数据
        self.add_user_data_module([16,17])
        #系统管理员退出
        self.user_quit()

    u'''登录模块后置条件'''
    def login_module_post_condition(self):
        #使用安全保密管理员登录
        self.login_secadmin()
        #删除认证方式
        self.authElem.del_auth_method()
        self.del_user_data_module([16,17])
        self.user_quit()

#------------------------------告警策略前置条件---------------------------------
    def alarm_strategy_module_prefix_condition(self):
        #使用安全保密管理员登录
        self.login_secadmin()

    def alarm_strategy_module_post_condition(self):
        self.alarm.del_command_config()
        self.alarm.del_default_config()
        self.alarm.del_auth_config()
        self.user_quit()

#------------------------------会话配置前置条件--------------------------------
    def session_module_prefix_condition(self):
        #使用安全保密管理员登录
        self.login_secadmin()
        self.switch_to_moudle(u"策略配置", u"会话配置")

#------------------------------密码策略前置条件--------------------------------
    def pwdstr_module_prefix_condition(self):
        #使用安全保密管理员登录
        self.login_secadmin()
        #添加资源
        self.add_resource_modele([14])
        self.add_user_data_module([19])
        self.switch_to_moudle(u"策略配置", u"密码策略")

    def pwdstr_module_post_condition(self):
        self.del_resource_modele([14])
        self.del_user_data_module([19])
        self.user_quit()

#------------------------------linux资源前置条件-----------------------------------
    def linuxre_module_prefix_condition(self):
        #使用安全保密管理员登录
        self.login_secadmin()
        #切换到资源
        self.switch_to_moudle(u"运维管理", u"资源")

#------------------------------network资源前置条件-----------------------------------
    def networkre_module_prefix_condition(self):
        #使用安全保密管理员登录
        self.login_secadmin()
        #切换到资源
        self.switch_to_moudle(u"运维管理", u"资源")

#------------------------------windows资源前置条件-----------------------------------
    def windowre_module_prefix_condition(self):
        #使用安全保密管理员登录
        self.login_secadmin()
        #切换到资源
        self.switch_to_moudle(u"运维管理", u"资源")

#-----------------------------数据库前置条件----------------------------------
    def database_resource_prefix_condition(self):
        self.login_sysadmin()
        #添加应用发布
        self.add_application([1])
        self.user_quit()
        #使用安全保密管理员登录
        self.login_secadmin()
        self.add_resource_modele([17])
        self.switch_to_moudle(u"运维管理", u"资源")

    def database_resource_post_condition(self):
        self.del_resource_modele([17])
        self.user_quit()
        self.login_sysadmin()
        self.del_application([1])
        self.user_quit()

#------------------------------授权前置条件-----------------------------------
    def authori_module_prefix_condition(self):

        #使用安全保密管理员登录
        self.login_secadmin()
        self.add_resource_modele([15,16])
        self.add_res_account_module([18,19])
        self.user_quit()
        self.login_sysadmin()
        #添加授权用户
        self.add_user_data_module([20,21])
        self.add_res_group([1])
        self.add_user_group([1])
        self.user_quit()
        self.login_secadmin()
        self.switch_to_moudle(u'运维管理', u'授权')

    def authori_module_post_condition(self):

        self.del_resource_modele([15,16])
        self.user_quit()
        self.login_sysadmin()
        self.del_res_group([1])
        self.del_user_group([1])
        self.del_user_data_module([20,21])
        self.user_quit()

#------------------------------命令规则前置条件-----------------------------------
    def commandrule_module_prefix_condition(self):
        self.login_sysadmin()
        #添加用户
        self.add_user_data_module([25])
        self.user_quit()
        self.login_secadmin()
        #添加资源
        self.add_resource_modele([3])
        #添加资源账号
        self.add_res_account_module([4])
        #添加授权
        self.add_authorization_module([2])
        #切换到规则定义
        self.switch_to_moudle(u'运维管理', u'规则定义')
        self.command.click_left_rule(0)

    def commandrule_module_post_condition(self):
        #删除授权
        self.del_authorization_module([2])
        #删除资源
        self.del_resource_modele([3])
        self.user_quit()
        self.login_sysadmin()
        #删除用户
        self.del_user_data_module([25])
        self.user_quit()

#------------------------------时间规则前置条件-----------------------------------
    def timerule_module_prefix_condition(self):
        self.login_secadmin()
        #添加用户
        self.add_user_data_module([26,27])
        #切换到规则定义
        self.switch_to_moudle(u'运维管理', u'规则定义')
        self.command.click_left_rule(1)

    def timerule_module_post_condition(self):
        #删除用户
        self.del_user_data_module([26,27])
        self.user_quit()

#------------------------------地址规则前置条件-----------------------------------
    def addressrule_module_prefix_condition(self):
        self.login_secadmin()
        #添加用户
        self.add_user_data_module([31,32])
        #切换到规则定义
        self.switch_to_moudle(u'运维管理', u'规则定义')
        self.command.click_left_rule(2)

    def addressrule_module_post_condition(self):
        self.del_user_data_module([31,32])
        self.user_quit()

#------------------------------资源时间规则前置条件-----------------------------------
    def retimerule_module_prefix_condition(self):
        self.login_sysadmin()
        #添加用户
        self.add_user_data_module([39])
        self.user_quit()
        self.login_secadmin()
        #添加资源
        self.add_resource_modele([4, 5, 10])
        #添加资源账号
        self.add_res_account_module([5, 6, 14])
        self.add_authorization_module([6])
        #切换到规则定义
        self.switch_to_moudle(u'运维管理', u'规则定义')
        self.command.click_left_rule(3)

    def retimerule_module_post_condition(self):
        self.user_quit()
        self.login_sysadmin()
        #删除用户
        self.del_user_data_module([39])
        self.user_quit()
        self.login_secadmin()
        #删除资源
        self.del_resource_modele([4, 5, 10])
        #删除授权
        self.del_authorization_module([6])
        self.user_quit()

#------------------------------流程前置条件-----------------------------------
    def process_module_prefix_condition(self):
        self.login_sysadmin()
        #添加用户
        self.add_user_data_module([40,41])
        self.user_quit()
        self.login_secadmin()
        #添加资源
        self.add_resource_modele([11,12])
        #添加资源账号
        self.add_res_account_module([15,16])
        self.add_authrization([1])

    def process_module_post_condition(self):
        #删除授权
        self.del_authorization_module([7])
        #删除资源
        self.del_resource_modele([11,12])
        self.user_quit()
        self.login_sysadmin()
        #删除用户
        self.del_user_data_module([40,41])
        self.user_quit()

#------------------------------双人授权前置条件-----------------------------------
    def dualmandate_module_prefix_condition(self):
        self.login_sysadmin()
        #添加用户
        self.add_user_data_module([45, 46])
        self.user_quit()
        self.login_secadmin()
        #添加资源
        self.add_resource_modele([13])
        #添加资源账号
        self.add_res_account_module([17])
        #添加授权
        self.add_authrization([4])

    def dualmandate_module_post_condition(self):
        #删除授权
        self.del_authorization_module([8])
        #删除资源
        self.del_resource_modele([13])
        self.user_quit()
        self.login_sysadmin()
        #删除用户
        self.del_user_data_module([45, 46])
        self.user_quit()

#-----------------------------行为报表前置条件---------------------------------
    def opt_report_module_prefix_condition(self):
        self.login_secadmin()
        self.add_resource_modele([18])
        self.user_quit()
        self.login_sysadmin()
        self.add_user_data_module([47])
        self.add_res_group([2])
        self.add_user_group([2])
        self.user_quit()
        self.login_sysaudit()
        self.switch_to_moudle(u"报表管理", u"审计报表")

    def opt_report_module_post_condition(self):
        self.user_quit()
        self.login_secadmin()
        self.del_resource_modele([18])
        self.user_quit()
        self.login_sysadmin()
        self.del_user_data_module([47])
        self.del_res_group([2])
        self.del_user_group([2])
        self.user_quit()

#-----------------------------配置报表前置条件---------------------------------
    def conf_report_module_prefix_condition(self):
        self.login_sysadmin()
        self.add_user_data_module([48])
        self.add_user_group([3])
        self.user_quit()
        self.login_sysaudit()
        self.switch_to_moudle(u"报表管理", u"审计报表")
        
    def conf_report_module_post_condition(self):
        self.user_quit()
        self.login_sysadmin()
        self.del_user_data_module([48])
        self.del_user_group([3])
        self.user_quit()

#-----------------------------配置审计前置条件------------------------------
    def system_log_prefix_condition(self):
        self.login_sysadmin()
        self.add_user_data_module([49])
        self.switch_to_moudle(u"系统配置", u"关联服务")
        self.ntp.click_left_moudle(1)
        #填写syslog信息
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        self.syslog.set_ip("172.16.10.11")
        self.syslog.set_ident("aa")
        self.syslog.save_button()
        self.cmf.click_login_msg_button()
        self.user_quit()
        self.login_sysaudit()
        self.switch_to_moudle(u"审计管理", u"配置审计")
    
    def system_log_post_condition(self):
        self.user_quit()
        self.login_sysadmin()
        self.del_user_data_module([49])
        self.user_quit()