#coding=utf-8
u'''
#文件名：
#被测软件版本号：V2.8.1
#作成人：张利娟
#生成日期：2018/1/24
#模块描述：邮件配置
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
#导入通用模块
sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,commonFun,frameElement
from _cnEncode import cnEncode

class MailPage(object):
    #开关按钮
    ONOFF = "btn_qh"
    #发送服务器地址
    MAILSERADDRESS = "mailServerAddress"
    #发送方用户名
    MAILSENDACCOUNT = "mailSenderAccount"
    #发送方口令
    MAILSENDPASSWD = "mailSenderPassword"
    #确认口令
    MAILSENDPASSWD2 = "mailSenderPassword2"
    #测试按钮
    TESTMAIL = "test_mail"
    #保存按钮
    SAVEMAIL = "save_mailService"

    def __init__(self, driver):
        self.driver = driver
        self.getElem = getElement(driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(driver)
        self.cmf = commonFun(driver)
        self.cnEn = cnEncode()

    u'''点击运行状态按钮'''
    def condition(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_click_EC("id", self.ONOFF)
        except Exception:
            print("Click the condition button")

    u'''点击测试按钮'''
    def test_mail(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_click_EC("id", self.TESTMAIL)
        except Exception:
            print("Click the test button")

    u'''点击保存按钮'''
    def save_mail(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_click_EC("id", self.SAVEMAIL)
        except Exception:
            print("Click the save button")

    u'''发送服务器地址
	    Parameters：
	       -mailsendaddr 服务器地址
    '''
    def mail_address(self, mailsendaddr):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_clear_EC("id", self.MAILSERADDRESS)
            self.getElem.find_element_wait_and_sendkeys("id", self.MAILSERADDRESS, mailsendaddr)
        except Exception:
            print("mail address is error")

    u'''发送方用户名
	    Parameters：
	       -sendaccount 用户名
    '''
    def mail_account(self, sendaccount):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_clear_EC("id", self.MAILSENDACCOUNT)
            self.getElem.find_element_wait_and_sendkeys("id", self.MAILSENDACCOUNT, sendaccount)
        except Exception:
            print("mail accuont is error")

    u'''发送方口令
	    Parameters：
	       -sendpasswd 口令
    '''
    def mail_passwd(self, sendpasswd):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_clear_EC("id", self.MAILSENDPASSWD)
            self.getElem.find_element_wait_and_sendkeys("id", self.MAILSENDPASSWD, sendpasswd)
        except Exception:
            print("mail passwd is error")

    u'''确认口令
	    Parameters：
	       -conpasswd 确认口令
    '''
    def confirm_passwd(self, conpasswd):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_clear_EC("id", self.MAILSENDPASSWD2)
            self.getElem.find_element_wait_and_sendkeys("id", self.MAILSENDPASSWD2, conpasswd)
        except Exception:
            print("mail confirm passwd is error")

    u'''左边框点击邮件'''
    def click_left_moudle_test(self):
        self.frameElem.from_frame_to_otherFrame("leftFrame")
        time.sleep(2)
        self.getElem.find_element_wait_and_click_EC("id", "url2")
        time.sleep(2)