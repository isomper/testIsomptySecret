#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：李择优
#生成日期：2018/1/24
#模块描述：SYSLOG
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _icommon import frameElement,commonFun
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/ass_service/")
from syslogElement import Syslog

class SyslogService():
    def __init__(self,driver):
        self.driver = driver
        self.dataFile = dataFileName()
        self.frameElem = frameElement(driver)
        self.cmf = commonFun(driver)
        self.log = log()
        self.syslog = Syslog(driver)
        
    u'''获取测试数据
        Parameters:
            sheetname:sheet名称
            return：表格数据
    '''
    def get_table_data(self,sheetname):
        dataFile = dataFileName()
        filePath = dataFile.get_syslog_test_data_url()
        fileData = dataFile.get_data(filePath,sheetname)
        return fileData

    u'''提示框元素路径'''
    def syslog_msg(self):
        syslog_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        return syslog_msg

    u'''编辑syslog信息'''
    def mod_syslog_001(self):
        #日志开始记录
        self.log.log_start("modSyslog")
        #获取编辑syslog的数据
        syslog_data = self.get_table_data("mod_syslog")
        #点击保存按钮弹出框
        syslog_msg = self.syslog_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(syslog_data)):
            data = syslog_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    self.syslog.set_ip(data[2])
                    self.syslog.set_port(data[3])
                    self.syslog.set_protocol(data[4])
                    self.syslog.set_ident(data[5])
                    self.syslog.set_facility(data[6])
                    self.syslog.save_button()
                    #返回上级frame
                    self.frameElem.switch_to_content()
                    #判断测试项是否通过
                    self.cmf.test_win_check_point("xpath", syslog_msg, data, flag)
            except Exception as e:
                print ("mod syslog fail: ") + str(e)
        self.log.log_end("modSyslog")

    u'''测试发送syslog'''
    def test_syslog_002(self):
        #日志开始记录
        self.log.log_start("testSyslog")
        #获取测试syslog的数据
        syslog_data = self.get_table_data("test_syslog")
        row_count = len(syslog_data)-1
        #点击保存按钮弹出框
        syslog_msg = self.syslog_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(syslog_data)):
            data = syslog_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:

                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    if dataRow == 1:               
                        self.syslog.change_switch_status()
                    self.syslog.set_ip(data[2])
                    self.syslog.set_port(data[3])
                    self.syslog.set_protocol(data[4])
                    self.syslog.set_ident(data[5])
                    self.syslog.set_facility(data[6])
                    if dataRow == row_count:
                        #打开运行开关
                        self.syslog.change_switch_status()
                    self.syslog.test_button()
                    #返回上级frame
                    self.frameElem.switch_to_content()
                    #判断测试项是否通过
                    self.cmf.test_win_check_point("xpath", syslog_msg, data, flag)
            except Exception as e:
                print ("test syslog fail: ") + str(e)
        self.log.log_end("testSyslog")
        
    u'''校验syslog信息'''
    def checkout_syslog_003(self):
        #日志开始记录
        self.log.log_start("checkoutSyslog")
        #获取校验syslog的数据
        syslog_data = self.get_table_data("checkout_syslog")
        #点击保存按钮弹出框
        syslog_msg = self.syslog_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(syslog_data)):
            data = syslog_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    self.syslog.set_ip(data[2])
                    self.syslog.set_port(data[3])
                    self.syslog.set_protocol(data[4])
                    self.syslog.set_ident(data[5])
                    self.syslog.set_facility(data[6])
                    self.syslog.save_button()
                    #返回上级frame
                    self.frameElem.switch_to_content()
                    #判断测试项是否通过
                    self.cmf.test_win_check_point("xpath", syslog_msg, data, flag)
            except Exception as e:
                print ("checkout syslog fail: ") + str(e)
        self.log.log_end("checkoutSyslog")