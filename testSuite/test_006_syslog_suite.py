#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.9涉密
#修改人：陈圆圆
#生成日期：2018/5/8
#模块描述：SYSLOG
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
from test_syslog import SyslogService

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class SyslogSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)
        self.sys = SyslogService(self.browser)
        self.initDriver = initDriver()
        
        #前置条件
        self.commonSuite.syslog_module_prefix_condition()
        
    def test_syslog(self):
        #编辑syslog信息
        self.sys.mod_syslog_001()
        #测试发送syslog
        self.sys.test_syslog_002()
        #校验syslog信息
        self.sys.checkout_syslog_003()
        
    def tearDown(self):
        #退出用户
        self.commonSuite.user_quit()
        #关闭浏览器
        self.initDriver.close_driver(self.browser)
        
if __name__ == "__main__":
    unittest.main()
