#coding=utf-8
#设定excel数据文件名字，统一调用
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _excelRead import excelRead

#通用数据excel文件
COMMON_SUITE_TEST_DATA_URL = r"/testIsompSecret/testData/common_suite_test_data.xlsx"
#登陆excel数据文件
LOGIN_TEST_DATA_URL = r"/testIsompSecret/testData/login_test_data.xlsx"

#用户excel数据位置
USER_TEST_DATA_URL = r"/testIsompSecret/testData/user_test_data.xlsx"

#组织定义数据文件
DEPARTMENT_TEST_DATA_URL = r"/testIsompSecret/testData/department_test_data.xlsx"

#认证方式数据文件
AUTH_METHOD_TEST_DATA_URL = r"/testIsompSecret/testData/auth_method_test_data.xlsx"

#授权数据文件
AUTHORIZATION_TEST_DATA_URL = r"/testIsompSecret/testData/authorization_test_data.xlsx"

#客户端配置文件
CLIENT_TEST_DATA_URL = r"/testIsompSecret/testData/client_test_data.xlsx"

#应用发布数据文件
APP_TEST_DATA_URL = r"/testIsompSecret/testData/application_test_data.xlsx"

#sso数据文件
SSO_TEST_DATA_URL = r"/testIsompSecret/testData/sso_test_data.xlsx"

#AD域抽取数据文件
AD_EXTRACT_DATA_URL = r"/testIsompSecret/testData/ad_extract_data.xlsx"

#配置报表数据文件
CONF_REPORT_DATA_URL = r"/testIsompSecret/testData/conf_audit_report.xlsx"

#运维报表数据文件
OPT_REPORT_DATA_URL = r"/testIsompSecret/testData/operation_audit_report.xlsx"

#运维审计数据文件
AUDIT_LOG_DATA_URL = r"/testIsompSecret/testData/audit_log.xlsx"

#配置审计数据文件
SYSTEM_LOG_DATA_URL = r"/testIsompSecret/testData/system_log.xlsx"

#会话配置数据文件
SESSION_CONFIGURATION_DATA_URL = r"/testIsompSecret/testData/session_configuration_test_data.xlsx"

#linux资源数据文件
LINUX_RESOURCE_TEST_DATA_URL = r"/testIsompSecret/testData/linux_resource_test_data.xlsx"

#网络设备资源数据位置
NETWORK_RESOURCE_TEST_DATA_URL = r"/testIsompSecret/testData/network_resource_test_data.xlsx"

#Windows资源数据位置
WINDOWS_RESOURCE_TEST_DATA_URL = r"/testIsompSecret/testData/windows_resource_test_data.xlsx"

#数据库资源位置
DATABASE_TEST_DATA_URL = r"/testIsompSecret/testData/database_resource_test_data.xlsx"

#资源组数据文件
REGROUP_TEST_DATA_URL = r"/testIsompSecret/testData/regroup_test_data.xlsx"

#用户组数据文件
USERGROUP_TEST_DATA_URL = r"/testIsompSecret/testData/usergroup_test_data.xlsx"

#访问审批数据文件
ACCAPPROVAL_TEST_DATA_URL = r"/testIsompSecret/testData/accapproval_test_data.xlsx"

#双人授权数据文件
DOUBLE_LICENSE_TEST_DATA_URL = r"/testIsompSecret/testData/double_license_test_data.xlsx"

#命令规则数据文件
COMMAND_RULE_TEST_DATA_URL = r"/testIsompSecret/testData/command_rule_test_data.xlsx"

#时间规则数据文件
TIME_RULE_TEST_DATA_URL = r"/testIsompSecret/testData/time_rule_test_data.xlsx"

#NTP服务数据文件
EDIT_NTP_TEST_DATA_URL = r"/testIsompSecret/testData/edit_ntp_test_data.xlsx"

#地址规则数据文件
ADDRESS_RULE_TEST_DATA_URL = r"/testIsompSecret/testData/address_rule_test_data.xlsx"

#资源时间规则数据文件
RETIME_RULE_TEST_DATA_URL = r"/testIsompSecret/testData/resource_time_rule_test_data.xlsx"

#密码策略数据文件
PASSWORD_STRATRGY_TEST_DATA_URL = r"/testIsompSecret/testData/password_strategy_test_data.xlsx"

#告警策略数据文件
ALARM_STRATEGE_TEST_DATA_URL = r"/testIsompSecret/testData/alarm_strategy_test_data.xlsx"

#syslog服务数据文件
SYSLOG_TEST_DATA_URL = r"/testIsompSecret/testData/syslog_test_data.xlsx"

#网卡配置数据文件
NETWORK_TEST_DATA_URL = r"/testIsompSecret/testData/network_test_data.xlsx"

#路由配置数据文件
ROUTING_TEST_DATA_URL = r"/testIsompSecret/testData/routing_test_data.xlsx"

#邮件配置数据文件
MAIL_TEST_DATE = r"/testIsompSecret/testData/mail_test_data.xlsx"
#备份还原数据文件
BACKUP_RESTORE_TEST_DATE = r"/testIsompSecret/testData/backup_restore_test_data.xlsx"

#使用授权数据文件
USE_AUTH_TEST_DATE = r"/testIsompSecret/testData/use_of_authorization.xlsx"

#密码信封数据文件
PASSWD_ENVELOPE_TEST_DATA_URL = r"/testIsompSecret/testData/passwd_envelope_test_data.xlsx"
class dataFileName(object):
    #获取通用excel中的数据
    def get_common_suite_test_data_url(self):
        return COMMON_SUITE_TEST_DATA_URL
    
    #获取用户登录excel中的数据
    def get_login_test_data_url(self):
        return LOGIN_TEST_DATA_URL
    
    #获取认证方式excel中的数据
    def get_auth_method_test_data_url(self):
       return AUTH_METHOD_TEST_DATA_URL 
    
    #获取用户excel中的数据
    def get_person_test_data_url(self):
        return USER_TEST_DATA_URL
    
    #获取授权excel中的数据
    def get_authorization_test_data_url(self):
        return AUTHORIZATION_TEST_DATA_URL
    
    #获取客户端配置中的数据
    def get_client_test_data_url(self):
        return CLIENT_TEST_DATA_URL
    
    #应用发布数据
    def get_app_test_data_url(self):
        return APP_TEST_DATA_URL
    
    #数据库数据
    def get_database_test_url(self):
        return DATABASE_TEST_DATA_URL
    
    #SSO数据
    def get_sso_test_url(self):
        return SSO_TEST_DATA_URL
    
    #AD域抽取数据
    def get_ad_extract_test_url(self):
        return AD_EXTRACT_DATA_URL
    
    #配置审计报表数据
    def get_conf_report_test_url(self):
        return CONF_REPORT_DATA_URL
    
    #运维审计报表数据
    def get_opt_report_test_url(self):
        return OPT_REPORT_DATA_URL
    
    #配置审计检索数据
    def get_system_log_test_url(self):
        return SYSTEM_LOG_DATA_URL
    
    #运维审计检索数据
    def get_audit_log_test_url(self):
        return AUDIT_LOG_DATA_URL

    u"""获取组织定义部门文件的数据"""
    def get_depart_test_data_url(self):
        return DEPARTMENT_TEST_DATA_URL
    
    u"""获取linux资源文件的数据"""
    def get_linux_resource_test_data_url(self):
        return LINUX_RESOURCE_TEST_DATA_URL
    
    u"""获取资源组文件的数据"""
    def get_regroup_test_data_url(self):
        return REGROUP_TEST_DATA_URL
    
    u"""获取用户组文件的数据"""
    def get_usergroup_test_data_url(self):
        return USERGROUP_TEST_DATA_URL   
    
    u"""获取网络设备资源文件的数据"""
    def get_network_resource_test_data_url(self):
        return NETWORK_RESOURCE_TEST_DATA_URL
    
    u"""获取windows资源文件的数据"""
    def get_windows_resource_test_data_url(self):
        return WINDOWS_RESOURCE_TEST_DATA_URL
     
    u"""获取访问审批文件的数据"""
    def get_accapproval_test_data_url(self):
        return ACCAPPROVAL_TEST_DATA_URL
    
    u"""获取双人授权文件的数据"""
    def get_double_license_test_data_url(self):
        return DOUBLE_LICENSE_TEST_DATA_URL

    u"""获取命令规则数据"""
    def get_command_test_data_url(self):
        return COMMAND_RULE_TEST_DATA_URL

    u"""获取时间规则数据"""
    def get_timerule_test_data_url(self):
        return TIME_RULE_TEST_DATA_URL

    #获取会话配置数据
    def get_session_configuration_data_url(self):
        return SESSION_CONFIGURATION_DATA_URL

    u"""获取地址规则数据"""
    def get_adrerule_test_data_url(self):
        return ADDRESS_RULE_TEST_DATA_URL

    u"""获取资源时间规则数据"""
    def get_retime_test_data_url(self):
        return RETIME_RULE_TEST_DATA_URL
    
    #获取NTP服务数据
    def get_ntp_test_data_url(self):
        return EDIT_NTP_TEST_DATA_URL

    u"""获取syslog服务数据"""
    def get_syslog_test_data_url(self):
        return SYSLOG_TEST_DATA_URL

    u'''获取邮件数据'''
    def mail_test_date_url(self):
        return MAIL_TEST_DATE
    
    u'''获取备份还原数据'''
    def back_restore_test_date_url(self):
        return BACKUP_RESTORE_TEST_DATE

    u'''获取网卡配置数据'''
    def get_network_test_data_url(self):
        return NETWORK_TEST_DATA_URL
    
    u'''获取路由配置数据'''
    def get_routing_test_data_url(self):
        return ROUTING_TEST_DATA_URL
    
    u"""获取密码策略数据"""
    def get_password_stratrgy_test_data_url(self):
        return PASSWORD_STRATRGY_TEST_DATA_URL
    
    u"""获取告警策略数据"""
    def alarm_stratrgy_test_data_url(self):
        return ALARM_STRATEGE_TEST_DATA_URL
    
    u"""获取使用授权数据"""
    def use_auth_test_data_url(self):
        return USE_AUTH_TEST_DATE

    u'''获取密码信封数据'''
    def passwd_envelope_test_data_url(self):
        return PASSWD_ENVELOPE_TEST_DATA_URL
    #从sheet名称获取登陆数据
    def get_data(self,dataPath,sheetName):
        #获取excel数据
        data = excelRead().get_excel_data(dataPath,sheetName)
        
        return data
    
#dataFile = dataFileName()
#login_data = dataFileName().get_data(dataFileName().get_auth_method_test_data_url(),'add_auth_method')
#for dataRow in range(len(login_data)):
#    data = login_data[dataRow]
#    print data
    