#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：李择优
#生成日期：2018/5/11
#模块描述：网卡配置
#历史修改记录
#修改人：陈圆圆
#修改日期：
#修改内容：
'''
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/network/")
from test_network import NetworkCard

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class NetworkCardSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)
        self.net = NetworkCard(self.browser)
        self.initDriver = initDriver()
        
        #前置条件
        self.commonSuite.network_card_module_prefix_condition()
        
    def test_network_card(self):
        #设置网卡
        self.net.set_network_card_001()
        #清空网卡
        self.net.del_network_card_002()
        #校验网卡
        self.net.check_network_card_003()
       
    def tearDown(self):
        #后置条件
        self.commonSuite.user_quit()
        #关闭浏览器
        self.initDriver.close_driver(self.browser)
        
if __name__ == "__main__":
    unittest.main()

