#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/report")
from test_opt_report import testOptReport

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testOptReportSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)        
        self.reportMethod = testOptReport(self.browser)
        #行为报表前置条件
        self.commonSuite.opt_report_module_prefix_condition()
    
    def test_client_method(self):
        #添加行为报表
        self.reportMethod.add_opt_report_001()
        #添加行为报表校验
        self.reportMethod.opt_report_check_002()
        #添加和修改计划报表
        self.reportMethod.add_plan_report_003()
        #删除和删除校验行为报表
        self.reportMethod.opt_report_del_004()

    def tearDown(self):
        #行为报表后置条件
        self.commonSuite.opt_report_module_post_condition()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()