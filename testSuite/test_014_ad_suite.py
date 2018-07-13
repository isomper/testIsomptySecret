#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/ad_extract")
from test_ad_extracte import testAdEx

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testAdSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)        
        self.adMethod = testAdEx(self.browser)
        #AD域前置条件
        self.commonSuite.ad_module_prefix_condition()
    
    def test_client_method(self):
        #发现AD域账号
        self.adMethod.ad_extract_001()
        #移动AD域账号
        self.adMethod.ad_discover_002()
        #移动AD域账号校验
        self.adMethod.move_user_check_003()
        #移动AD域账号密码校验
        self.adMethod.ad_pwd_checkout_004()
        #设置定时
        self.adMethod.cycle_005()
        #清空历史记录
        self.adMethod.clear_history_006()

    def tearDown(self):
        #AD域后置条件
        self.commonSuite.ad_module_post_condition()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()

