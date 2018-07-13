#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：
#生成日期：2018-01-23
#模块描述：密码策略测试用例
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入通用方法类
sys.path.append("/testIsompSecret/common/")
from _icommon import frameElement,commonFun
from _log import log

#导入文件操作类
sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/testSuite/")
from common_suite_file import CommonSuiteData

sys.path.append("/testIsompSecret/webElement/password_strategy/")
from pwdStrategyElement import PwdStrategy

#导入与密码策略相关的用户模块
sys.path.append("/testIsompSecret/webElement/user/")
from userElement import UserPage

sys.path.append("/testIsompSecret/testCase/user/")
from test_user import User

#导入与密码策略相关的会话模块
sys.path.append("/testIsompSecret/webElement/session_configuration/")
from sessionElement import sessionConfig

#带入与密码策略相关的资源模块
sys.path.append("/testIsompSecret/webElement/resource/")
from test_resource_common import Resource

sys.path.append("/testIsompSecret/webElement/resource/")
from test_resource_accountmgr_ment import Accountmgr

class PasswordStr():
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.PwdStr = PwdStrategy(self.driver)
        self.cmf = commonFun(driver)
        self.dataFile = dataFileName()
        self.frameElem = frameElement(self.driver)
        self.commonsuite = CommonSuiteData(driver)
        self.user = UserPage(self.driver)
        self.session = sessionConfig(self.driver)
        self.conuser = User(driver)
        self.resource = Resource(driver)
        self.account = Accountmgr(driver)
        
    u'''提示框元素路径'''
    def save_msg(self):
        save_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        return save_msg

    u'''获取测试数据
        Parameters:
            sheetname:sheet名称
            return：表格数据
    '''
    def get_table_data(self,sheetname):
        dataFile = dataFileName()
        filePath = dataFile.get_password_stratrgy_test_data_url()
        authFileData = dataFile.get_data(filePath,sheetname)
        return authFileData

    #添加策略
    def add_strategy_001(self):
        #日志开始记录
        self.log.log_start("pwdStrategy")
        #获取数据
        strategy_data = self.get_table_data("add_strategy")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(strategy_data)):
            data = strategy_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.PwdStr.add_pwd_button()
                    self.PwdStr.set_pwd_name(data[2])
                    self.PwdStr.term_of_validity(data[3])
                    self.PwdStr.password_length_min(data[4])
                    self.PwdStr.password_length_max(data[5])
                    self.PwdStr.set_lower_case(data[6])
                    self.PwdStr.set_capital(data[7])
                    self.PwdStr.set_minimum_digital(data[8])
                    self.PwdStr.set_Minimum_symbol(data[9])
                    self.PwdStr.set_prohibition_of_using_keywords(data[10])
                    self.PwdStr.add_using_keywords_button()
                    self.PwdStr.save_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
                    self.PwdStr.return_button()
            except Exception as e:
                print ("Policy adding error: ") + str(e)
        self.log.log_end("pwdStrategy")
    
    #编辑策略test
    def edit_strategy_002(self):
        #日志开始记录
        self.log.log_start("editPwdStrategy")
        #获取数据
        strategy_data = self.get_table_data("edit_strategy")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(strategy_data)):
            data = strategy_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.PwdStr.edit(data[2])
                    self.PwdStr.set_pwd_name(data[3])
                    self.PwdStr.term_of_validity(data[4])
                    self.PwdStr.password_length_min(data[5])
                    self.PwdStr.password_length_max(data[6])
                    self.PwdStr.set_lower_case(data[7])
                    self.PwdStr.set_capital(data[8])
                    self.PwdStr.set_minimum_digital(data[9])
                    self.PwdStr.set_Minimum_symbol(data[10])
                    self.PwdStr.set_prohibition_of_using_keywords(data[11])
                    self.PwdStr.add_using_keywords_button()
                    self.PwdStr.save_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
                    self.PwdStr.return_button()
            except Exception as e:
                print ("Policy edit error: ") + str(e)
        self.log.log_end("editPwdStrategy")
    
    #策略校验
    def check_strategy_003(self):
        #日志开始记录
        self.log.log_start("checkPwdStrategy")
        #获取数据
        strategy_data = self.get_table_data("check_strategy")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False

        for dataRow in range(len(strategy_data)):
            data = strategy_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.PwdStr.add_pwd_button()
                    self.PwdStr.set_pwd_name(data[2])
                    self.PwdStr.term_of_validity(data[3])
                    self.PwdStr.password_length_min(data[4])
                    self.PwdStr.password_length_max(data[5])
                    self.PwdStr.set_lower_case(data[6])
                    self.PwdStr.set_capital(data[7])
                    self.PwdStr.set_minimum_digital(data[8])
                    self.PwdStr.set_Minimum_symbol(data[9])
                    self.PwdStr.set_prohibition_of_using_keywords(data[10])
                    self.PwdStr.add_using_keywords_button()
                    self.PwdStr.save_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
                    self.PwdStr.return_button()
            except Exception as e:
                print ("Policy checkout error: ") + str(e)
        self.log.log_end("checkeditPwdStrategy")
    
    #检索名称test
    def search_strategy_004(self):
        #日志开始记录
        self.log.log_start("searchPwdStrategy")
        #获取数据
        strategy_data = self.get_table_data("search_strategy")
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(strategy_data)):
            data = strategy_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.PwdStr.search_name(data[2])
                    self.PwdStr.click_search_button()
                    self.PwdStr.click_reset_button()
                    self.PwdStr.click_search_button()
                    #清空标识状态
                    flag = False
                    self.log.log_detail(data[0], True)
            except Exception as e:
                print ("Policy search error: ") + str(e)
        self.log.log_end("searchPwdStrategy")
        
    #删除单个策略
    def del_sing_policy_005(self):
        #日志开始记录
        self.log.log_start("delPwdStrategy")
        #获取数据
        strategy_data = self.get_table_data("del_strategy")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(strategy_data)):
            data = strategy_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.PwdStr.del_sing_strategy(data[2])
                    self.frameElem.switch_to_content()
                    self.cmf.click_msg_button(1)
                    self.cmf.test_win_check_point("xpath",saveMsg,data,flag)
                    #校验删除后的名称是否存在
                    if self.cmf.is_namevalue_exsit(data[2], "fortStrategyPasswordName"):
                        print("Delete success")
            except Exception as e:
                print ("Policy del error: ") + str(e)
        self.log.log_end("delPwdStrategy")
        
    #与密码策略关联的会话配置
    def session_association_007(self):
        #日志开始记录
        self.log.log_start("sessionAssociation")
        #获取数据
        strate_data = self.get_table_data("configure_strateg")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(strate_data)):
            data = strate_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.commonsuite.switch_to_moudle(u"策略配置", u"会话配置")
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.PwdStr.set_pwd_strategy(data[4])
                    self.session.add_session(data[2])
                    self.session.add_locking_time(data[3])
                    self.session.save_global_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("session association error: ") + str(e)
        self.log.log_end("sessionAssociation")
                    
    #与密码策略关联的用户
    def user_association_008(self):
        #日志开始记录
        self.log.log_start("userAssociation")
        #获取数据
        strate_data = self.get_table_data("user_association")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(strate_data)):
            data = strate_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.conuser.switch_to_user_module()
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.PwdStr.user_edit(data[2])
                    self.PwdStr.set_pwd(data[9])
                    self.PwdStr.set_pwd_agin(data[10])
                    self.user.save_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
                    self.user.click_back_button()
            except Exception as e:
                print ("user association error: ") + str(e)
        self.log.log_end("userAssociation")
    
    #为Windows资源添加密码策略
    def resource_association_009(self):
        #日志开始记录
        self.log.log_start("resourAcessociation")
        #获取数据
        strate_data = self.get_table_data("resource_association")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(strate_data)):
            data = strate_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.commonsuite.switch_to_moudle(u"运维管理", u"资源")
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.PwdStr.resource_edit(data[2])
                    self.PwdStr.set_resource_strategy(data[8])
                    self.resource.click_save_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
                    self.PwdStr.return_button()
            except Exception as e:
                print ("resour acessociation error: ") + str(e)
        self.log.log_end("resourAcessociation")
    
    #为Windows资源账号添加密码策略
    def resource_account_association_010(self):
        #日志开始记录
        self.log.log_start("resourAceccountAssociation")
        #获取数据
        strate_data = self.get_table_data("resource_account_association")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(strate_data)):
            data = strate_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.PwdStr.account_manage(data[2])
                    self.account.click_account_add()
                    self.PwdStr.set_resource_account_name(data[3])
                    self.PwdStr.set_resource_account_pwd(data[4])
                    self.PwdStr.set_resource_account_pwdagin(data[5])
                    self.PwdStr.save_account()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
                    #点击资源账号编辑页面返回
                    self.PwdStr.return_button()
                    #点击资源账号页面返回
                    self.PwdStr.return_button()
            except Exception as e:
                print ("resour aceccount association error: ") + str(e)
        self.log.log_end("resourAceccountAssociation")

    #删除全部策略
    def del_all_policy_006(self):
        #日志开始记录
        self.log.log_start("delAllPwdStrategy")
        #获取数据
        strategy_data = self.get_table_data("del_all_strategy")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(strategy_data)):
            data = strategy_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.commonsuite.switch_to_moudle(u"策略配置",u"密码策略")
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.PwdStr.select_all_button()
                    self.PwdStr.del_button()
                    self.frameElem.switch_to_content()
                    self.cmf.click_msg_button(1)
                    self.cmf.test_win_check_point("xpath",saveMsg,data,flag)
                    #校验删除后的名称是否存在
                    if self.cmf.is_namevalue_exsit(data[2], "fortStrategyPasswordName"):
                        print("Delete all success")
            except Exception as e:
                print ("Policy delAll error: ") + str(e)
        self.log.log_end("delAllPwdStrategy")