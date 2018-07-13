#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：张泽方
#生成日期：
#模块描述：使用授权
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,frameElement,commonFun
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/use_of_authorization/")
from useAuthElement import UseAuth

class UseAuthorization():
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.useauth = UseAuth(driver)
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.dataFile = dataFileName()
        self.frameElem = frameElement(self.driver)

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
        filePath = dataFile.use_auth_test_data_url()
        authFileData = dataFile.get_data(filePath,sheetname)
        return authFileData
    
    #添加产品基本信息
    def add_product_information_001(self):
        #日志开始记录
        self.log.log_start("addProductInformation")
        #获取数据
        use_data = self.get_table_data("add_OPI")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(use_data)):
            data = use_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.useauth.add_customer_name(data[2])
                    self.useauth.add_system_name(data[3])
                    self.useauth.save_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("product adding error: ") + str(e)
        self.log.log_end("addProductInformation")
    
    #上传logo
    def upload_logo_upgrade_002(self):
        #日志开始记录
        self.log.log_start("uploadLogo")
        #获取数据
        use_data = self.get_table_data("upload_operation")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(use_data)):
            data = use_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据upload
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.useauth.click_or_check_logo(1)
                    self.useauth.up_logo_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("upload error: ") + str(e)
        self.log.log_end("uploadLogo")
    
    #产品基本信息校验
    def check_product_information_003(self):
        #日志开始记录
        self.log.log_start("checkProductInformation")
        #获取数据
        use_data = self.get_table_data("check_OPI")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(use_data)):
            data = use_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.useauth.add_customer_name(data[2])
                    self.useauth.add_system_name(data[3])
                    self.useauth.save_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("product check error: ") + str(e)
        self.log.log_end("checkProductInformation")

    #logo校验
    def check_logo_upgrade_004(self):
        #日志开始记录
        self.log.log_start("checkUpgradeUplogo")
        #获取数据
        use_data = self.get_table_data("check_upgrade_uplogo")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(use_data)):
            data = use_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据upload
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    if dataRow == 1:
                        #文件为空校验
                        self.useauth.up_logo_button()
                    elif dataRow == 2:
                        #以图片格式校验
                        self.useauth.click_or_check_logo(2)
                        self.useauth.up_logo_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("check upgrad uplogo error: ") + str(e)
        self.log.log_end("checkUpgradeUplogo")
    
    #更新授权码
    def add_product_information_005(self):
        #日志开始记录
        self.log.log_start("updateAuthorization")
        #获取数据
        use_data = self.get_table_data("update_authorization")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(use_data)):
            data = use_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.useauth.add_authcode_name(data[2])
                    self.useauth.click_updateAuth_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("update authorization error: ") + str(e)
        self.log.log_end("updateAuthorization")
    
    #更新授权码校验
    def check_updata_auth_006(self):
        #日志开始记录
        self.log.log_start("checkUpdatAuth")
        #获取数据
        use_data = self.get_table_data("check_updata_auth")
        #保存弹框
        saveMsg = self.save_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(use_data)):
            data = use_data[dataRow]
            try:
            #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("mainFrame")
                    self.useauth.add_authcode_name(data[2])
                    self.useauth.click_updateAuth_button()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", saveMsg, data, flag)
            except Exception as e:
                print ("check updat auth error: ") + str(e)
        self.log.log_end("checkUpdatAuth")