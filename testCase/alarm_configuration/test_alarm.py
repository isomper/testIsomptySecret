#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：张泽方
#生成日期：2018-01-31
#模块描述：告警归纳测试用例
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

#导入通用方法类
sys.path.append("/testIsompSecret/common/")
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

#导入文件操作类
sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/alarm_configuration/")
from alarmElement import AlarmPage

class AlarmConfig():
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.alarm = AlarmPage(driver)
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.selectElem = selectElement(driver)
        self.dataFile = dataFileName()
        self.frameElem = frameElement(self.driver)
        self.tableEle = tableElement(self.driver)
        
    u'''提示框元素路径'''
    def save_msg(self):
        save_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        return save_msg
    
    u'''获取测试数据
        Parameters:
            - sheetname:sheet名称
            return：表格数据
    '''
    def get_table_data(self,sheetname):
        dataFile = dataFileName()
        filePath = dataFile.alarm_stratrgy_test_data_url()
        authFileData = dataFile.get_data(filePath,sheetname)
        return authFileData
    
    #添加邮件接收人
    def add_receive_user(self):
        self.frameElem.from_frame_to_otherFrame("artIframe")
        self.alarm.click_receive_user()
        self.alarm.check_all_button()
        self.alarm.ok_button()
    
    u'''切换至告警策略模块'''
    def switch_to_alarm_module(self):
        time.sleep(1)
        self.frameElem.switch_to_content()
        self.frameElem.switch_to_top()
        self.cmf.select_menu(u"策略配置")
        self.cmf.select_menu(u"策略配置",u"告警策略")
    
    #为用户添加邮箱
    def mod_user_mail_008(self):
        #日志开始记录
        self.log.log_start("modUsrMail")
        #获取数据
        com_data = self.get_table_data("userMessagee")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(com_data)):
            data = com_data[dataRow]
            try:
                if dataRow != 0:
                    self.alarm.click_user_message_menu()
                    self.alarm.set_user_mail(data[2])
                    self.alarm.click_save_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                    print ("mod user mail error: ") + str(e)
        self.log.log_end("modUsrMail")
    
    #配置高危运维
    def command_alarm_level_config_001(self):
        #日志开始记录
        self.log.log_start("commandAlarmLevelConfig")
        #获取数据
        command_data = self.get_table_data("HighRiskOperation")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(command_data)):
            data = command_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.alarm.click_left_config_test()
                    self.alarm.click_command_alarm_menu()
                    self.alarm.command_alarm_level(data[2])
                    self.alarm.syslog_check()
                    self.alarm.mail_check()
                    #点击邮件接收人添加按钮
                    self.alarm.click_illegal_command_receive_user()
                    #选择邮件接收人
                    self.add_receive_user()
                    self.alarm.save_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("High risk operation and maintenance failure: ") + str(e)
        self.log.log_end("commandAlarmLevelConfig")
    
    #运行状态告警模块
    def default_alarm_level_config_002(self):
        #日志开始记录
        self.log.log_start("defaultAlarmLevelConfig")
        #获取数据
        default_data = self.get_table_data("runningState")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(default_data)):
            data = default_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    #点击告警配置菜单
                    self.alarm.click_left_config_test()
                    self.alarm.click_default_alarm_menu()
                    self.alarm.memory_alarm_select(data[2])
                    self.alarm.disk_alarm_select(data[3])
                    self.alarm.cpu_alarm_select(data[4])
                    self.alarm.test_cycle_select(data[5])
                    self.alarm.default_alarm_level_select(data[6])
                    self.alarm.run_syslog_check()
                    self.alarm.run_mail_check()
                    #点击检索按钮
                    self.alarm.system_state_receive_user()
                    self.add_receive_user()
                    #设置事件升级开关
                    self.alarm.change_switch_status()
                    self.alarm.repeat_times_select(data[7])
                    self.alarm.defaultA_alarm_update_elect(data[8])
                    self.alarm.save_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
                    
            except Exception as e:
                print ("Running state alarm error: ") + str(e)
        self.log.log_end("defaultAlarmLevelConfig")

    #运行状态告警校验
    def default_alarm_level_checkout_003(self):
        #日志开始记录
        self.log.log_start("defaultAlarmLevelCheck")
        #获取数据
        default_data = self.get_table_data("runStateCheck")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(default_data)):
            data = default_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.switch_to_alarm_module()
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.alarm.click_left_config_test()
                    self.alarm.click_default_alarm_menu()
                    self.alarm.memory_alarm_select(data[2])
                    self.alarm.disk_alarm_select(data[3])
                    self.alarm.cpu_alarm_select(data[4])
                    self.alarm.test_cycle_select(data[5])
                    self.alarm.default_alarm_level_select(data[6])
                    self.alarm.run_mail_check()
                    self.alarm.change_switch_status()
                    self.alarm.repeat_times_select(data[7])
                    self.alarm.defaultA_alarm_update_elect(data[8])
                    self.alarm.save_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("Running state alarm check error: ") + str(e)
        self.log.log_end("defaultAlarmLevelCheck")

    #认证异常模块
    def auth_alarm_level_config_004(self):
        #日志开始记录
        self.log.log_start("authAlarmLevelConfig")
        #获取数据
        auth_data = self.get_table_data("AutException")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(auth_data)):
            data = auth_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.alarm.click_left_config_test()
                    self.alarm.auth_default_alarm_menu()
                    self.alarm.auth_alarm_level(data[2])
                    self.alarm.auth_syslog_check()
                    self.alarm.auth_mail_check()
                    self.alarm.auth_exception_receive_user()
                    self.add_receive_user()
                    self.alarm.save_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("Authentication exception error: ") + str(e)
        self.log.log_end("authAlarmLevelConfig")
    
    #告警归纳类型检索
    def search_by_type_005(self):
        #日志开始记录
        self.log.log_start("searchByType")
        #获取数据
        search_data = self.get_table_data("searchByType")
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(search_data)):
            data = search_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.alarm.click_left_Induce_test()
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    self.alarm.search_type(data[2])
                    self.alarm.search_button()
                    self.alarm.rest_button()
                    #清空标识状态
                    flag = False
                    self.log.log_detail(data[0], True)
            except Exception as e:
                print ("Retrieval type error: ") + str(e)
        self.log.log_end("searchByType")
    
    #告警归纳级别检索
    def search_by_level_006(self):
        #日志开始记录
        self.log.log_start("searchByLevel")
        #获取数据
        search_data = self.get_table_data("searchByLevel")
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(search_data)):
            data = search_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.alarm.click_left_Induce_test()
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    self.alarm.search_level(data[2])
                    self.alarm.search_button()
                    self.alarm.rest_button()
                    #清空标识状态
                    flag = False
                    self.log.log_detail(data[0], True)
            except Exception as e:
                print ("Retrieval level error: ") + str(e)
        self.log.log_end("searchByLevel")
    
    def del_config(self):
        #日志开始记录
        self.log.log_start("delConfig")
        flag = False
        self.frameElem.from_frame_to_otherFrame("mainFrame")
