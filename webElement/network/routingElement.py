#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：李择优
#生成日期：2018/2/1
#模块描述：路由配置
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
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

class Routing:
    #标志
    MARK = "select"
    #网段
    NET = "destinationNet"
    #网关
    GATEWAY = "gateWay"
    #子网掩码
    NETMASK = "netMask"
    #主机
    HOST = "destinationHost"
    #添加
    ADD_BUTTON = "add_route"
    #删除
    DEL_BUTTON = "del_route"
    #全选框
    ALL = "checkAll"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.getElem = getElement(driver)
        self.dataFile = dataFileName()
        self.select = selectElement(driver)
        self.frameElem = frameElement(driver)
        self.cmf = commonFun(driver)
        self.cnEnde = cnEncode()
        self.tableElem = tableElement(driver)   
    
    u'''选择标志
            Parameters:
                value:select选项中的value属性值,net代表net,host代表host
        '''
    def choose_mark(self, value):
        valu = self.cnEnde.is_float(value)
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        selem = self.getElem.find_element_with_wait_EC('id',self.MARK)
        self.select.select_element_by_value(selem, valu)
    
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
            print ("set common func text error: ") + str(revar_text) + str(e)
    
    u'''输入网段
            parameters:
                netIp: 网段
    '''      
    def set_net(self,netIp):
        return self.set_common_func(netIp,self.NET)
    
    u'''输入网关
            parameters:
                gateway: 网关
    '''      
    def set_gateway(self,gateway):
        return self.set_common_func(gateway,self.GATEWAY)
    
    u'''输入子网掩码
            parameters:
                netmask: 子网掩码
    '''      
    def set_netmask(self,netmask):
        return self.set_common_func(netmask,self.NETMASK)
    
    u'''输入主机
            parameters:
                host: 主机
    '''      
    def set_host(self,host):
        return self.set_common_func(host,self.HOST)
    
    u'''点击添加'''      
    def click_add_button(self):
        time.sleep(1)
        self.getElem.find_element_wait_and_click_EC('id',self.ADD_BUTTON)
            
    u'''点击删除'''      
    def click_del_button(self):
        time.sleep(1)
        self.getElem.find_element_wait_and_click_EC('id',self.DEL_BUTTON)
    
    u'''点击全选框'''      
    def click_all(self):
        time.sleep(1)
        self.getElem.find_element_wait_and_click_EC('id',self.ALL)
        
    u'''获取路由行数'''
    def get_routing_num(self):
        self.frameElem.from_frame_to_otherFrame("rigthFrame")
        table_xpath = "//table[@id='route_list']"
        rows = self.tableElem.get_table_rows_count(table_xpath)
        return rows
    
    u'''通过名称获取所在行数
        parameters : 
            rountName : 名称
    '''
    def get_row_by_account(self,rountName):
        table_xpath = "//table[@id='route_list']"
        reName = self.cnEnde.is_float(rountName)
        table_num = self.get_routing_num()
        for row in range(table_num):
            if row != 0:
                cell_text = self.tableElem.get_table_cell_text(table_xpath,row,2)[0]
                if cell_text == reName:
                    row = row+1
                    return row
                
    u'''点击单选框
        parameters : 
            box : 单选框
    '''
    def click_box(self,box):
        time.sleep(1)
        row = self.get_row_by_account(box)
        box_xpath = "//table[@id='route_list']/tr[" + str(row) + "]/td/input[@name='checkbox']"
        try:
            time.sleep(1)
            self.getElem.find_element_wait_and_click_EC('xpath',box_xpath)
        except Exception as e:
            print ("click box error: ") + str(e)