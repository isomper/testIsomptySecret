#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/report")
from test_conf_report import testConfReport

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testConfReportSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)        
        self.reportMethod = testConfReport(self.browser)
        #配置报表前置条件
        self.commonSuite.conf_report_module_prefix_condition()
    
    def test_client_method(self):
        #添加配置报表
        self.reportMethod.add_conf_report_001()
        #添加配置报表校验
        self.reportMethod.conf_report_check_002()
        #删除和删除校验配置报表
        self.reportMethod.conf_report_del_004()

    def tearDown(self):
        #配置报表后置条件
        self.commonSuite.conf_report_module_post_condition()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()


