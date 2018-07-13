#-*- coding:utf-8 -*-
'''
#文件名：
#作者：张利娟
#创建日期：2018/1/24
#模块描述：调用test_mail_ment模块
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
sys.path.append("/testIsompSecret/webElement/mail/")
from test_mail_ment import MailPage


class testMail(object):
    def __init__(self, driver):
        self.driver = driver
        self.log = log()
        self.mailpage = MailPage(driver)
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
        mailPath = dateFile.mail_test_date_url()
        mailDate = dateFile.get_data(mailPath, sheetname)
        return mailDate

    u'''弹出框'''
    def pupop(self):
        mailMsg = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        return mailMsg

    u'''配置邮件'''
    def add_mail_001(self):

        #日志开始记录
        self.log.log_start("add mail")
        #获取配置邮件测试数据
        mailDate = self.get_table_date("add_mail")
        #保存成功的弹出框
        mailMsg = self.pupop()
        #无检查点的测试项标识，如果为True说明通过
        flag = False

        for dataRow in range(len(mailDate)):
            data = mailDate[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.mailpage.mail_address(data[2])
                    self.mailpage.mail_account(data[3])
                    self.mailpage.mail_passwd(data[4])
                    self.mailpage.confirm_passwd(data[5])
                    self.mailpage.save_mail()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", mailMsg, data, flag)
            except Exception as e:
                print("add mail fail" + str(e))
        self.log.log_end("add mail")

    u'''编辑邮件'''
    def mod_mail_002(self):
        #日志开始记录
        self.log.log_start("mod mail")
        #获取配置邮件测试数据
        mailDate = self.get_table_date("mod_mail")
        #保存成功的弹出框
        mailMsg = self.pupop()
        #无检查点的测试项标识，如果为True说明通过
        flag = False

        for dataRow in range(len(mailDate)):
            data = mailDate[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.mailpage.mail_address(data[2])
                    self.mailpage.mail_account(data[3])
                    self.mailpage.save_mail()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", mailMsg, data, flag)
            except Exception as e:
                print("mod mail fail" + str(e))
        self.log.log_end("mod mail")

    u'''测试邮件'''
    def test_mail_003(self):

        #日志开始记录
        self.log.log_start("test mail")
        #获取配置邮件测试数据
        mailDate = self.get_table_date("test_mail")
        #保存成功的弹出框
        mailMsg = self.pupop()
        #无检查点的测试项标识，如果为True说明通过
        flag = False

        for dataRow in range(len(mailDate)):
            data = mailDate[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.mailpage.mail_address(data[2])
                    self.mailpage.mail_account(data[3])
                    self.mailpage.mail_passwd(data[4])
                    self.mailpage.confirm_passwd(data[5])
                    self.mailpage.test_mail()
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", mailMsg, data, flag)
            except Exception as e:
                print("test mail fail" + str(e))
        self.log.log_end("test mail")

    u'''校验邮件'''
    def check_mail_004(self):

        #日志开始记录
        self.log.log_start("check mail")
        #获取配置邮件测试数据
        mailDate = self.get_table_date("check_mail")
        #保存成功的弹出框
        mailMsg = self.pupop()
        #无检查点的测试项标识，如果为True说明通过
        flag = False

        for dataRow in range(len(mailDate)):
            data = mailDate[dataRow]
            try:
                if dataRow == 1:
                    self.mailpage.mail_address(data[2])
                    self.mailpage.test_mail()
                elif dataRow == 2:
                    self.mailpage.mail_address(data[2])
                    self.mailpage.mail_account(data[3])
                    self.mailpage.test_mail()
                elif dataRow == 3:
                    self.mailpage.mail_account(data[3])
                    self.mailpage.mail_passwd(data[4])
                    self.mailpage.test_mail()
                elif dataRow == 4:
                    self.mailpage.mail_address(data[2])
                elif dataRow == 5:
                    self.mailpage.mail_address(data[2])
                    self.mailpage.mail_account(data[3])
                elif dataRow == 6:
                    self.mailpage.mail_account(data[3])
                    self.mailpage.mail_passwd(data[4])
                elif dataRow == 7:
                    self.mailpage.mail_address(data[2])
                    self.mailpage.mail_account(data[3])
                    self.mailpage.mail_passwd(data[4])
                    self.mailpage.confirm_passwd(
                        data[5]
                    )
                if 3 < dataRow:
                    self.mailpage.save_mail()
                if dataRow != 0:
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", mailMsg, data, flag)
                    time.sleep(2)
            except Exception as e:
                print("check mail fail" + str(e))
        self.log.log_end("check mail")

    u'''测试开关'''
    def onoff_mail_005(self):
        #日志开始记录
        self.log.log_start("condition mail")
        #获取配置邮件测试数据
        mailDate = self.get_table_date("on_off_mail")
        #保存成功的弹出框
        mailMsg = self.pupop()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        #点击关
        for dataRow in range(len(mailDate)):
            data = mailDate[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow == 1:
                    self.mailpage.condition()
                    self.mailpage.save_mail()
                    time.sleep(2)
                if dataRow == 2:
                    self.mailpage.condition()
                    self.mailpage.save_mail()
                if dataRow != 0:
                    self.frameElem.switch_to_content()
                    self.cmf.test_win_check_point("xpath", mailMsg, data, flag)
                    self.mailpage.click_left_moudle_test()
            except Exception as e:
                print("condition fail" + str(e))
        self.log.log_end("condition mail")
