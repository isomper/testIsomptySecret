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
reload(sys)
sys.setdefaultencoding('utf-8')
import time

sys.path.append("/testIsompSecret/common/")
from _icommon import getElement,selectElement,frameElement,commonFun
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsompSecret/webElement/ass_service/")
from ntpElement import NtpService


class Syslog:
    #运行状态开关
    SWITCH = "btn_qh"    
    #IP
    HOST = "host"
    #端口
    PORT = "port"
    #协议
    PROTOCOL = "protocol"
    #标识
    IDENT = "ident"
    #机制
    FACILITY = "facility"
    #测试按钮
    TEST_BUTTON = "test_syslog"
    #保存按钮
    SAVE_BUTTON = "save_syslog"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.getElem = getElement(driver)
        self.select = selectElement(driver)
        self.frameElem = frameElement(driver)
        self.cmf = commonFun(driver)
        self.ntp = NtpService(driver)
        self.cnEnde = cnEncode()
            
    u'''填写变量内容
        parameters:
            var_text : 变量内容
            value : 定位方式值
    '''
    def set_common_func(self,var_text,value):
        try:
            revar_text = self.cnEnde.is_float(var_text)
            var_elem =self.getElem.find_element_with_wait_EC("id",value)
            var_elem.clear()
            var_elem.send_keys(revar_text)
        except Exception as e:
            print ("set user common text error: ") + str(revar_text) + str(e)
            
    u'''输入IP
        parameters:
            setIp : IP
    '''
    def set_ip(self,setIp):
        return self.set_common_func(setIp,self.HOST)
    
    u'''输入端口
        parameters:
            setPort : 端口
    '''
    def set_port(self,setPort):
        return self.set_common_func(setPort,self.PORT)
    
    u'''选择协议
            Parameters:
                value:select选项中的value属性值,udp代表UDP,tcp代表TCP,nix_syslog代表nix_syslog
        '''
    def set_protocol(self, value):
        valu = self.cnEnde.is_float(value)
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        selem = self.getElem.find_element_with_wait_EC("id",self.PROTOCOL)
        self.select.select_element_by_value(selem, valu)
        
    u'''输入标识
        parameters:
            setIdent : 标识
    '''
    def set_ident(self,setIdent):
        return self.set_common_func(setIdent,self.IDENT)
    
    u'''选择机制
            Parameters:
                value:select选项中的value属性值,32代表facility
        '''
    def set_facility(self, value):
        valu = self.cnEnde.is_float(value)
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        selem = self.getElem.find_element_with_wait_EC("id",self.FACILITY)
        self.select.select_element_by_value(selem, valu)
        
    u'''点击测试按钮'''
    def test_button(self):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        self.getElem.find_element_wait_and_click_EC("id",self.TEST_BUTTON)
        
    u'''点击保存按钮'''
    def save_button(self):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        self.getElem.find_element_wait_and_click_EC("id",self.SAVE_BUTTON)
        
    u'''改变开关状态'''     
    def change_switch_status(self):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        try:
            button_elem = self.getElem.find_element_with_wait_EC("id",self.SWITCH)
            class_attr = button_elem.get_attribute("class")
            off_status = "switch_off"
            on_status = "switch_on"            
            if class_attr == on_status:
                self.ntp.click_left_moudle(1)
                self.frameElem.from_frame_to_otherFrame("rigthFrame")
                button_elem = self.getElem.find_element_with_wait_EC("id",self.SWITCH)
                time.sleep(1)
                button_elem.click()
                button_elem.click()
            else:
                button_elem.click()            
        except Exception as e:
            print ("Change  button status  error: ") + str(e)


        
        
    
    
    
    
        