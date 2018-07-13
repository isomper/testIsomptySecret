#coding=utf-8
import sys
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

sys.path.append("/testIsompSecret/webElement/session_configuration/")
from sessionElement import sessionConfig

sys.path.append("/testIsompSecret/webElement/password_strategy/")
from pwdStrategyElement import PwdStrategy


class conversationStrategy():
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.session = sessionConfig(driver)
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.selectElem = selectElement(driver)
        self.dataFile = dataFileName()
        self.frameElem = frameElement(self.driver)
        self.tableEle = tableElement(self.driver)
        self.pwdstr = PwdStrategy(self.driver)
    
    u'''获取测试数据
    Parameters:
    sheetname:sheet名称
    return：表格数据
    '''
    def get_table_data(self,sheetname):
        dataFile = dataFileName()
        filePath = dataFile.get_session_configuration_data_url()
        authFileData = dataFile.get_data(filePath,sheetname)
        return authFileData

    u'''提示框元素路径'''
    def save_msg(self):
        save_msg = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        return save_msg

    #添加会话策略
    def add_session_config_001(self):
        #日志开始
        self.log.log_start("session")
        #获取会话策略数据
        session_data = self.get_table_data("add_Visit")
        #保存成功弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(session_data)):
            data = session_data[dataRow]
            try:
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.pwdstr.set_pwd_strategy(data[2])
                    self.session.add_session(data[3])
                    self.session.add_locking_time(data[4])
                    self.session.save_global_button()
                    #返回到上一级frme
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("Session add fail: ") + str(e)
        self.log.log_end("addSession")
        
    #校验会话策略
    def check_session_config_002(self):
        #日志开始
        self.log.log_start("sessionConfig")
        #获取会话策略数据
        session_data = self.get_table_data("check_Visit")
        #弹出框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(session_data)):
            data = session_data[dataRow]
            try:
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.session.add_session(data[2])
                    self.session.add_locking_time(data[3])
                    self.session.save_global_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("checkout session policy error: " + str(e))
        self.log.log_end("addSessionConfig")
        
    #单用户登录方式和web会话超时添加
    def sing_user_login_and_session_003(self):
        #日志开始
        self.log.log_start("userLoginAndSession")
        #获取会话策略数据
        session_data = self.get_table_data("add_SingleUserLoginAndSession")
        #弹出框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(session_data)):
            data = session_data[dataRow]
            try:
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.session.set_sing_user_login(data[2])
                    self.session.set_out_time(data[4])
                    self.session.save_session_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("Single user login failure: " + str(e))
        self.log.log_end("userLoginAndSessionEnd")
        
    #单用户登录校验
    def check_sing_user_login_004(self):
        #日志开始
        self.log.log_start("checkUserLogin")
        #获取会话策略数据
        session_data = self.get_table_data("check_SingleUserLogin")
        #弹出框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(session_data)):
            data = session_data[dataRow]
            try:
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.session.set_sing_user_login(data[2])
                    self.session.max_number_online(data[3])
                    self.session.save_session_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("Single user login failure: " + str(e))
        self.log.log_end("checkUserLoginEnd")


