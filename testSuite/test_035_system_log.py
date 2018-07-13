#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/audit_management")
from test_system_log import testSystemLog

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testSystemLogSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)        
        self.systemLog = testSystemLog(self.browser)
        #配置审计前置条件
        self.commonSuite.system_log_prefix_condition()
    
    def test_system_log_query(self):
        #配置审计检索
        self.systemLog.system_log_query_001()

    def tearDown(self):
        #配置审计后置条件
        self.commonSuite.system_log_post_condition()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
