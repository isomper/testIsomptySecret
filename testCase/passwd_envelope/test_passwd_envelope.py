#-*- coding:utf-8 -*-
'''
#文件名：
#作者：张利娟
#创建日期：2018/1/31
#模块描述：调用test_passwd_envelope模块
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName
sys.path.append("/testIsompSecret/common")
from _icommon import commonFun,frameElement
from _log import log
sys.path.append("/testIsompSecret/webElement/passwd_envelope/")
from test_passwd_envelope_ment import EnvelopePage

class testEnvelope(object):
    def __init__(self, driver):
        self.driver = driver
        self.log = log()
        self.envelopePage = EnvelopePage(driver)
        self.cmf = commonFun(driver)
        self.frameElem = frameElement(driver)

    u'''
    获取测试数据
        Parameters:
            - sheetname:sheet名称
        return：表格数据
    '''
    def get_table_date(self, sheetname):
        dateFile = dataFileName()
        envolopePath = dateFile.passwd_envelope_test_data_url()
        envelopeDate = dateFile.get_data(envolopePath, sheetname)
        return envelopeDate

    u'''弹出框'''
    def pupop(self):
        envelopeMsg = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        return envelopeMsg

    u'''配置密码信封'''
    def add_passwd_envelope_001(self):

        #日志开始记录
        self.log.log_start("add passwd envelope")
        #获取配置邮件测试数据
        EnvelopeDate = self.get_table_date("add_passwd_envelope")
        #保存成功的弹出框
        EnvelopeMsg = self.pupop()
        #无检查点的测试项标识，如果为True说明通过
        flag = False

        for dataRow in range(len(EnvelopeDate)):
            data = EnvelopeDate[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.envelopePage.envelope_company(data[2])
                    self.envelopePage.envelope_server_ip(data[3])
                    self.envelopePage.envelope_server_port(data[4])
                    self.envelopePage.envelope_file_port(data[5])
                    self.envelopePage.envelope_save()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", EnvelopeMsg, data, flag)
            except Exception as e:
                print("add passwd envelope fail" + str(e))
        self.log.log_end("add passwd envelope")

    u'''浏览、上传图片'''
    def upload_passwd_envelope_002(self):

        #日志开始记录
        self.log.log_start("upload passwd envelope")
        #获取配置邮件测试数据
        EnvelopeDate = self.get_table_date("upload_passwd_envelope")
        #保存成功的弹出框
        EnvelopeMsg = self.pupop()
        #无检查点的测试项标识，如果为True说明通过
        flag = False

        for dataRow in range(len(EnvelopeDate)):
            data = EnvelopeDate[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.envelopePage.envelope_upload(data[2])
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", EnvelopeMsg, data, flag)
            except Exception as e:
                print("upload passwd envelope fail" + str(e))
        self.log.log_end("upload passwd envelope")

    u'''同步图片'''
    def passwd_envelope_image_sync_003(self):
        #日志开始记录
        self.log.log_start("sync passwd envelope")
        #获取配置邮件测试数据
        EnvelopeDate = self.get_table_date("passwd_envelope_image_sync")
        #保存成功的弹出框
        EnvelopeMsg = self.pupop()
        #无检查点的测试项标识，如果为True说明通过
        flag = False

        for dataRow in range(len(EnvelopeDate)):
            data = EnvelopeDate[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.envelopePage.envelope_sync()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", EnvelopeMsg, data, flag)
            except Exception as e:
                print("sync passwd envelope fail" + str(e))
        self.log.log_end("sync passwd envelope")

    u'''编辑密码信封'''
    def mode_passwd_envelope_004(self):
        #日志开始记录
        self.log.log_start("mode passwd envelope")
        #获取配置邮件测试数据
        EnvelopeDate = self.get_table_date("mode_passwd_envelope")
        #保存成功的弹出框
        EnvelopeMsg = self.pupop()
        #无检查点的测试项标识，如果为True说明通过
        flag = False

        for dataRow in range(len(EnvelopeDate)):
            data = EnvelopeDate[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.envelopePage.envelope_company(data[2])
                    self.envelopePage.envelope_server_ip(data[3])
                    self.envelopePage.envelope_save()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", EnvelopeMsg, data, flag)
            except Exception as e:
                print("mode passwd envelope fail" + str(e))
        self.log.log_end("mode passwd envelope")

    u'''校验密码信封'''
    def check_passwd_envelope_005(self):

        #日志开始记录
        self.log.log_start("check passwd envelope")
        #获取配置邮件测试数据
        EnvelopeDate = self.get_table_date("check_passwd_envelope")
        #保存成功的弹出框
        EnvelopeMsg = self.pupop()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        #清空数据
        self.envelopePage.envelope_empty()

        for dataRow in range(len(EnvelopeDate)):
            data = EnvelopeDate[dataRow]
            try:
                if dataRow == 2:
                    self.envelopePage.envelope_company(data[2])
                elif dataRow == 3:
                    self.envelopePage.envelope_server_ip(data[3])
                elif dataRow == 4:
                    self.envelopePage.envelope_server_port(data[4])
                elif dataRow == 5:
                    self.envelopePage.envelope_server_ip(data[3])
                    self.envelopePage.envelope_file_port(data[5])
                elif dataRow == 6:
                    self.envelopePage.envelope_server_ip(data[3])
                    self.envelopePage.envelope_server_port(data[4])
                elif dataRow == 7:
                    self.envelopePage.envelope_server_port(data[4])
                    self.envelopePage.envelope_file_port(data[5])
                if dataRow != 0:
                    self.envelopePage.envelope_save()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", EnvelopeMsg, data, flag)
                    time.sleep(2)
            except Exception as e:
                print("check passwd envelope fail" + str(e))
        self.log.log_end("check passwd envelope")