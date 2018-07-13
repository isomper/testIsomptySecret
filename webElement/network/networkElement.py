#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：李择优
#生成日期：2018/1/31
#模块描述：网卡配置
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

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

class Network:
    
    #输入网关
    GATEWAY = "gateWay"
    #设置网关
    SET_GATEWAY = "changeGATEWAY"
    #eth0IP
    ETH0_IP = "eth0_ip"
    #eth0子网掩码
    ETH0_MASK = "eth0_mask"
    #eth0设置网卡按钮
    ETH0_SET_BUTTON = "0"
    #eth0清空网卡按钮
    ETH0_DEL_BUTTON = "del_0"    
    #eth1IP
    ETH1_IP = "eth1_ip"
    #eth1子网掩码
    ETH1_MASK = "eth1_mask"
    #eth1设置网卡按钮
    ETH1_SET_BUTTON = "1"
    #eth1清空网卡按钮
    ETH1_DEL_BUTTON = "del_1"
    #eth2IP
    ETH2_IP = "eth2_ip"
    #eth2子网掩码
    ETH2_MASK = "eth2_mask"
    #eth2设置网卡按钮
    ETH2_SET_BUTTON = "2"
    #eth2清空网卡按钮
    ETH2_DEL_BUTTON = "del_2"
    #eth3IP
    ETH3_IP = "eth3_ip"
    #eth3子网掩码
    ETH3_MASK = "eth3_mask"
    #eth3设置网卡按钮
    ETH3_SET_BUTTON = "3"
    #eth3清空网卡按钮
    ETH3_DEL_BUTTON = "del_3"
    #确定按钮
    HIGHLIGHT_BUTTON = "aui_state_highlight"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.getElem = getElement(driver)
        self.dataFile = dataFileName()
        self.select = selectElement(driver)
        self.frameElem = frameElement(driver)
        self.cmf = commonFun(driver)
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
            
    u'''输入网关
        parameters:
            GateWay : 网关
    '''
    def gateway(self,GateWay):
        return self.set_common_func(GateWay,self.GATEWAY)
    
    u'''点击设置网关按钮'''
    def click_set_gateWay_button(self):
        self.getElem.find_element_wait_and_click_EC("id",self.SET_GATEWAY)    
            
    u'''输入eth0的IP
        parameters:
            eth0Ip : IP
    '''
    def set_eth0_ip(self,eth0Ip):
        time.sleep(1)
        return self.set_common_func(eth0Ip,self.ETH0_IP)
    
    u'''输入eth0的子网掩码
        parameters:
            eth0Mask : 子网掩码
    '''
    def set_eth0_mask(self,eth0Mask):
        return self.set_common_func(eth0Mask,self.ETH0_MASK)
    
    u'''点击eth0设置网卡按钮'''
    def click_eth0_set_button(self):
        self.getElem.find_element_wait_and_click_EC("id",self.ETH0_SET_BUTTON)
        
    u'''点击eth0清空网卡按钮'''
    def click_eth0_del_button(self):
        time.sleep(1)
        self.getElem.find_element_wait_and_click_EC("id",self.ETH0_DEL_BUTTON)
    
    u'''点击确定按钮'''    
    def click_highlight_button(self):
        self.frameElem.switch_to_content()
        self.getElem.find_element_wait_and_click_EC("classname",self.HIGHLIGHT_BUTTON)
    
    u'''输入eth1的IP
        parameters:
            eth1Ip : IP
    '''
    def set_eth1_ip(self,eth1Ip):
        time.sleep(1)
        return self.set_common_func(eth1Ip,self.ETH1_IP)
    
    u'''输入eth1的子网掩码
        parameters:
            eth1Mask : 子网掩码
    '''
    def set_eth1_mask(self,eth1Mask):
        return self.set_common_func(eth1Mask,self.ETH1_MASK)
    
    u'''点击eth1设置网卡按钮'''
    def click_eth1_set_button(self):
        self.getElem.find_element_wait_and_click_EC("id",self.ETH1_SET_BUTTON)
        
    u'''点击eth1清空网卡按钮'''
    def click_eth1_del_button(self):
        time.sleep(1)
        self.getElem.find_element_wait_and_click_EC("id",self.ETH1_DEL_BUTTON)    
    
    u'''输入eth2的IP
        parameters:
            eth2Ip : IP
    '''
    def set_eth2_ip(self,eth2Ip):
        time.sleep(1)
        return self.set_common_func(eth2Ip,self.ETH2_IP)
    
    u'''输入eth2的子网掩码
        parameters:
            eth2Mask : 子网掩码
    '''
    def set_eth2_mask(self,eth2Mask):
        return self.set_common_func(eth2Mask,self.ETH2_MASK)
    
    u'''点击eth2设置网卡按钮'''
    def click_eth2_set_button(self):
        self.getElem.find_element_wait_and_click_EC("id",self.ETH2_SET_BUTTON)
        
    u'''点击eth2清空网卡按钮'''
    def click_eth2_del_button(self):
        time.sleep(1)
        self.getElem.find_element_wait_and_click_EC("id",self.ETH2_DEL_BUTTON)    
    
    u'''输入eth3的IP
        parameters:
            eth3Ip : IP
    '''
    def set_eth3_ip(self,eth3Ip):
        time.sleep(1)
        return self.set_common_func(eth3Ip,self.ETH3_IP)
    
    u'''输入eth3的子网掩码
        parameters:
            eth3Mask : 子网掩码
    '''
    def set_eth3_mask(self,eth3Mask):
        return self.set_common_func(eth3Mask,self.ETH3_MASK)
    
    u'''点击eth3设置网卡按钮'''
    def click_eth3_set_button(self):
        self.getElem.find_element_wait_and_click_EC("id",self.ETH3_SET_BUTTON)
        
    u'''点击eth3清空网卡按钮'''
    def click_eth3_del_button(self):
        try:
            time.sleep(1)
            self.getElem.find_element_wait_and_click_EC("id",self.ETH3_DEL_BUTTON)
        except Exception as e:
            print ("del eth3 card fail: ") + str(e)