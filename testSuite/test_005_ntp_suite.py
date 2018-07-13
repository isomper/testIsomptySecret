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
import time
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/ass_service/")
from test_ntp import ServiceNtp

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class TestNtpSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)
        self.service = ServiceNtp(self.browser)
        self.initDriver = initDriver()
        
        #前置条件
        self.commonSuite.ntp_module_prefix_condition()
        
    def test_ntp(self):
        #编辑服务器IP与周期
        self.service.edit_ntp_001()
        #校验服务器IP
        self.service.check_ntp_002()        
        #更新系统时间
        self.service.update_ntp_003()        
        
    def tearDown(self):
        #后置条件
        self.commonSuite.user_quit()
        #关闭浏览器
        self.initDriver.close_driver(self.browser)
        
        
if __name__ == "__main__":
    unittest.main()
