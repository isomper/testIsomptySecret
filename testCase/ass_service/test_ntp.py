#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：李择优
#生成日期：2018/1/12
#模块描述：NTP服务
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _icommon import frameElement,commonFun
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/ass_service/")
from ntpElement import NtpService

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData

class ServiceNtp():
    def __init__(self,driver):
        self.driver = driver
        self.dataFile = dataFileName()
        self.frameElem = frameElement(driver)
        self.cmf = commonFun(driver)
        self.log = log()
        self.ntp = NtpService(driver)
        self.comm = CommonSuiteData(driver)
        
    u'''获取测试数据
        Parameters:
            sheetname:sheet名称
            return：表格数据
    '''
    def get_table_data(self,sheetname):
        dataFile = dataFileName()
        filePath = dataFile.get_ntp_test_data_url()
        fileData = dataFile.get_data(filePath,sheetname)
        return fileData

    u'''提示框元素路径'''
    def ntp_msg(self):
        ntp_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        return ntp_msg
    
    u'''校验没有弹出框类型用例是否通过
        parameters: 
            data : 检查点
    '''
    def check_without_pop_up(self,data):
        content = self.ntp.get_element_content()
        if content.find(data[1]) == -1:
            self.log.log_detail(data[0],False)
        else:
            self.log.log_detail(data[0],True)

    u'''编辑服务器IP与周期'''
    def edit_ntp_001(self):
        #日志开始记录
        self.log.log_start("editNtp")
        #获取编辑服务器IP与周期的数据
        ntp_data = self.get_table_data("mod_ntp")
        #点击保存按钮弹出框
        ntp_msg = self.ntp_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(ntp_data)):
            data = ntp_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    self.ntp.server_ip(data[2])
                    #自动与时间同步服务器
                    self.ntp.check_time_server()
                    self.ntp.set_cycle_date(data[3])
                    self.ntp.set_cycle_time(data[4])
                    self.ntp.save_button()
                    #返回上级frame
                    self.frameElem.switch_to_content()
                    #判断测试项是否通过
                    self.cmf.test_win_check_point("xpath", ntp_msg, data, flag)
            except Exception as e:
                print ("edit ntp fail: ") + str(e)
        self.log.log_end("editNtp")
        
    u'''校验服务器IP'''
    def check_ntp_002(self):
        #日志开始记录
        self.log.log_start("checkNtp")
        #获取校验服务器IP的数据
        ntp_data = self.get_table_data("check_ntp")
        #点击保存按钮弹出框
        ntp_msg = self.ntp_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(ntp_data)):
            data = ntp_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    self.ntp.server_ip(data[2])
                    self.ntp.save_button()
                    #返回上级frame
                    self.frameElem.switch_to_content()
                    #判断测试项是否通过
                    self.cmf.test_win_check_point("xpath", ntp_msg, data, flag)
                    #清空标识状态
                    flag = False                    
            except Exception as e:
                print ("check ntp fail:") + str(e)
        self.log.log_end("checkNtp")    
        
    u'''更新时间'''
    def update_ntp_003(self):
        #日志开始记录
        self.log.log_start("updateNtp")
        #获取更新时间的数据
        ntp_data = self.get_table_data("update_ntp")
        row_count = len(ntp_data)-1
        for dataRow in range(len(ntp_data)):
            data = ntp_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    self.ntp.server_ip(data[2])
                    if dataRow != row_count:
                        self.ntp.set_cycle_date(data[3])
                        self.ntp.set_cycle_time(data[4])
                    else:
                        #自动与时间同步服务器
                        self.ntp.check_time_server()                       
                    self.ntp.save_button()
                    #点击确定按钮
                    self.ntp.click_msg_button()
                    #更新时间
                    self.ntp.updata_button()
                    #用户退出
                    self.comm.user_quit()
                    #用户登录
                    self.comm.login_sysadmin()
                    self.cmf.select_menu(u"系统配置", u"关联服务")
                    #判断测试项是否通过
                    self.check_without_pop_up(data)
            except Exception as e:
                print ("update ntp fail: ") + str(e)
        self.log.log_end("updateNtp")