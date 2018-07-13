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

sys.path.append("/testIsompSecret/common/")
from _icommon import getElement,selectElement,frameElement,commonFun
from _log import log
from _cnEncode import cnEncode

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/network/")
from routingElement import Routing

class RoutingConfiguration():
    def __init__(self,driver):
        self.driver = driver
        self.getElem = getElement(driver)
        self.dataFile = dataFileName()
        self.select = selectElement(driver)
        self.frameElem = frameElement(driver)
        self.cmf = commonFun(driver)
        self.log = log()
        self.cnEnde = cnEncode()
        self.routing = Routing(driver)
        
    u'''获取测试数据
        Parameters:
            sheetname:sheet名称
            return：表格数据
    '''
    def get_table_data(self,sheetname):
        dataFile = dataFileName()
        filePath = dataFile.get_routing_test_data_url()
        fileData = dataFile.get_data(filePath,sheetname)
        return fileData
    
    u'''提示框元素路径'''
    def routing_msg(self):
        routing_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        return routing_msg
    
    u'''添加路由配置'''
    def add_routing_001(self):
        #日志开始记录
        self.log.log_start("addRouting")
        #获取添加路由配置的数据
        routing_data = self.get_table_data("add_routing")
        #点击添加按钮弹出框
        routing_msg = self.routing_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(routing_data)):
            data = routing_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    self.routing.choose_mark(data[2])
                    if dataRow == 1:
                        self.routing.set_net(data[3])
                        self.routing.set_netmask(data[6])
                    elif dataRow == 2:
                        self.routing.set_host(data[4])
                    self.routing.set_gateway(data[5])
                    self.routing.click_add_button()
                    #返回上级frame
                    self.frameElem.switch_to_content()
                    #判断测试项是否通过
                    self.cmf.test_win_check_point("xpath", routing_msg, data, flag)
            except Exception as e:
                print ("add routing fail: ") + str(e)
        self.log.log_end("addRouting")
        
    u'''校验路由配置'''
    def check_routing_002(self):
        #日志开始记录
        self.log.log_start("checkRouting")
        #获取校验路由配置的数据
        routing_data = self.get_table_data("check_routing")
        row_count = len(routing_data)-1
        #点击添加按钮弹出框
        routing_msg = self.routing_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(routing_data)):
            data = routing_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    if dataRow != row_count:
                        self.routing.choose_mark(data[2])
                        if data[2] == "net":
                            self.routing.set_net(data[3])
                            self.routing.set_netmask(data[6])
                        elif data[2] == "host":
                            self.routing.set_host(data[4])
                        self.routing.set_gateway(data[5])
                        self.routing.click_add_button()
                    else:
                        self.routing.click_del_button()
                    #返回上级frame
                    self.frameElem.switch_to_content()
                    #判断测试项是否通过
                    self.cmf.test_win_check_point("xpath", routing_msg, data, flag)                  
            except Exception as e:
                print ("check routing fail: ") + str(e)
        self.log.log_end("checkRouting")
        
    u'''删除路由配置'''
    def del_routing_003(self):
        #日志开始记录
        self.log.log_start("delRouting")
        #获取删除路由配置的数据
        routing_data = self.get_table_data("del_routing")
        #点击添加按钮弹出框
        routing_msg = self.routing_msg()
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(routing_data)):
            data = routing_data[dataRow]
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    self.frameElem.from_frame_to_otherFrame("rigthFrame")
                    if data[4] != "":
                        self.routing.click_box(data[4])
                    else:
                        self.routing.click_box(data[3])
                    self.routing.click_del_button()
                    #返回上级frame
                    self.frameElem.switch_to_content()
                    #判断测试项是否通过
                    self.cmf.test_win_check_point("xpath", routing_msg, data, flag)
            except Exception as e:
                print ("check routing fail: ") + str(e)
        self.log.log_end("checkRouting")