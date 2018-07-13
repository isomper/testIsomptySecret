#coding=utf-8
u'''
#文件名：
#被测软件版本号：V2.8.1
#作成人：张利娟
#生成日期：2018/1/31
#模块描述：密码信封
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

class EnvelopePage(object):
    #浏览按钮
    LOGOIMAGE = "logoImage"
    #上传按钮
    SAVE_IMAGES_BUTTON = "save_images_button"
    #同步按钮
    IMAGESELECT = "imagesSelect"
    #信封抬头
    COMPANY = "company"
    #打印服务器IP
    SERVERIP = "serverIp"
    #打印服务器监听端口
    SERLISPORT = "serverListenerPort"
    #打印服务器文件监听端口
    FILELISPORT = "fileListenerPort"
    #保存按钮
    SAVE_METHOD = "save_method"
    #同步图片ID
    IMAGEONESPAN = "imageOneSpan"

    def __init__(self, driver):
        self.driver = driver
        self.getElem = getElement(driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(driver)
        self.cmf = commonFun(driver)
        self.cnEn = cnEncode()

    u'''点击保存按钮'''
    def envelope_save(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_click_EC("id", self.SAVE_METHOD)
        except Exception:
            print("Click the save button is error")

    u'''上传操作
		parameters:
			- fileurl :上传图片路径
	'''
    def envelope_upload(self,fileurl):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_sendkeys("id", self.LOGOIMAGE, fileurl)
            time.sleep(2)
            self.getElem.find_element_wait_and_click_EC("id", self.SAVE_IMAGES_BUTTON)
            time.sleep(2)

        except Exception:
            print("upload passwd envelope image is error")


    u'''同步操作'''
    def envelope_sync(self):
        try:
            time.sleep(2)
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_click_EC("id", self.IMAGESELECT)
            time.sleep(3)
            self.getElem.find_element_wait_and_click_EC("id", self.IMAGEONESPAN)
        except Exception:
            print("passwd envelope images sync is error")

    u'''发送公司（信封抬头）
    	Parameters：
	       -sendcompany 公司（信封抬头）
    '''
    def envelope_company(self, sendcompany):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_clear_EC("id", self.COMPANY)
            self.getElem.find_element_wait_and_sendkeys("id", self.COMPANY, sendcompany)
        except Exception:
            print("passwd envelope company is error")

    u'''发送打印服务器IP
	    Parameters：
	       -sendserverip 打印服务器IP
    '''
    def envelope_server_ip(self, sendserverip):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_clear_EC("id", self.SERVERIP)
            self.getElem.find_element_wait_and_sendkeys("id", self.SERVERIP, sendserverip)
        except Exception:
            print("server ip is error")

    u'''发送打印服务器监听端口
	    Parameters：
	       -sendserverport 打印服务器端口
    '''
    def envelope_server_port(self, sendserverport):
        sendserverport = self.cnEn.is_float(sendserverport)
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_clear_EC("id", self.SERLISPORT)
            self.getElem.find_element_wait_and_sendkeys("id", self.SERLISPORT, sendserverport)
        except Exception:
            print("server port is error")

    u'''发送打印服务器文件监听端口
	    Parameters：
	       -sendfileport 打印服务器文件监听端口
    '''
    def envelope_file_port(self, sendfileport):
        sendfileport = self.cnEn.is_float(sendfileport)
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_clear_EC("id", self.FILELISPORT)
            self.getElem.find_element_wait_and_sendkeys("id", self.FILELISPORT, sendfileport)
        except Exception:
            print("file port is error")

    u'''清空数据-->进行校验测试'''
    def envelope_empty(self):
        try:
            self.frameElem.from_frame_to_otherFrame("rigthFrame")
            self.getElem.find_element_wait_and_clear_EC("id",self.COMPANY)
            self.getElem.find_element_wait_and_clear_EC("id",self.SERVERIP)
            self.getElem.find_element_wait_and_clear_EC("id",self.SERLISPORT)
            self.getElem.find_element_wait_and_clear_EC("id",self.FILELISPORT)
        except Exception:
            print("envelope empty is error")

    u'''左边框点击密码信封'''
    def click_left_moudle_envelope(self):
        self.frameElem.from_frame_to_otherFrame("leftFrame")
        time.sleep(2)
        self.getElem.find_element_wait_and_click_EC("id", "url3")
        time.sleep(2)