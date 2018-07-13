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
import time

sys.path.append("/testIsompSecret/common/")
from _icommon import getElement,selectElement,frameElement,commonFun
from _cnEncode import cnEncode
from _log import log

class NtpService:
    #服务器IP
    SERVERIP = "timeSetServerIp"
    #更新按钮
    UPDATA_BUTTON = "update"
    #保存按钮
    SAVE_BUTTON = "timeSet_save"
    #勾选自动与时间服务器同步
    CHECK = "check1"
    #周期方式
    CYCLEDATE = "dateStatus"
    #周期时间
    CYCLETIME = "timeSetDay"
    #同步信息
    MESSAGE = "synchronousMessage"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.getElem = getElement(driver)
        self.select = selectElement(driver)
        self.frameElem = frameElement(driver)
        self.cmf = commonFun(driver)
        self.cnEnde = cnEncode()
        
    u'''点击更新按钮'''
    def updata_button(self):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        time.sleep(1)
        self.getElem.find_element_with_wait_clickable_and_click('id',self.UPDATA_BUTTON)
        time.sleep(9)
        
    u'''点击保存按钮'''
    def save_button(self):
        time.sleep(1)
        self.getElem.find_element_with_wait_clickable_and_click('id',self.SAVE_BUTTON)
        
    u'''点击弹框确定按钮'''
    def click_msg_button(self):
        self.cmf.click_login_msg_button()

    u'''勾选自动与时间服务器同步'''
    def check_time_server(self):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        self.getElem.find_element_with_wait_clickable_and_click('id',self.CHECK)

    u'''左边框点击模块
        Parameters:
            statu:左边框点击，0代表点击NTP服务，1代表点击SYSLOG，2代表点击邮件服务，3代表点击密码信封
    '''
    def click_left_moudle(self,statu):
        self.frameElem.from_frame_to_otherFrame("leftFrame")
        if statu == 0:
            #点击NTP服务
            self.getElem.find_element_wait_and_click_EC("id", "url0")
        elif statu == 1:
            #点击SYSLOG
            self.getElem.find_element_wait_and_click_EC("id", "url1")
        elif statu == 2:
            #点击邮件服务
            self.getElem.find_element_wait_and_click_EC("id", "url2")
        elif statu == 3:
            #点击密码信封
            self.getElem.find_element_wait_and_click_EC("id", "url3")
    
    u'''填写变量内容
        parameters:
            var_text : 变量内容
            value : 定位方式值
    '''
    def set_common_func(self,var_text,value):
        try:
            revar_text = self.cnEnde.is_float(var_text)
            var_elem =self.getElem.find_element_with_wait_EC('id',value)
            var_elem.clear()
            var_elem.send_keys(revar_text)
        except Exception as e:
            print ("set user common text error: ") + str(revar_text) + str(e)
            
    u'''填写服务器IP
        parameters:
            serverIp : 服务器IP
    '''      
    def server_ip(self,serverIp):
        return self.set_common_func(serverIp,self.SERVERIP)    
            
    u'''选择周期方式
            Parameters:
                value:select选项中的value属性值,1代表每天,2代表小时,3代表分钟
        '''
    def set_cycle_date(self, value):
        valu = self.cnEnde.is_float(value)
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        selem = self.getElem.find_element_with_wait_EC('id',self.CYCLEDATE)
        self.select.select_element_by_value(selem, valu)
        
    u'''选择周期时间
            Parameters:
                value:select选项中的value属性值
        '''
    def set_cycle_time(self, value):
        valu = self.cnEnde.is_float(value)
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        selem = self.getElem.find_element_with_wait_EC('id',self.CYCLETIME)
        self.select.select_element_by_value(selem, valu)    
    
    u'''获取同步信息'''
    def get_element_content(self):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        elem_content = self.getElem.find_element_wait_and_get_text('id',self.MESSAGE,3)
        return elem_content
