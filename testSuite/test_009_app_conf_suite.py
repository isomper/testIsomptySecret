#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/application")
from test_app_conf import testApp

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testAppSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)   
        self.appMethod = testApp(self.browser)
        #应用发布前置条件
        self.commonSuite.application_module_prefix_condition()
    
    def test_app_method(self):
        #添加应用发布
        self.appMethod.add_app_001()
        #编辑应用发布
        self.appMethod.edit_app_002()
        #校验应用发布
        self.appMethod.check_app_003()
        #检索应用发布
        self.appMethod.query_app_004()
        #添加账号
        self.appMethod.add_account_006()
        #修改账号
        self.appMethod.edit_account_007()
        #删除账号
        self.appMethod.del_account_008()
        #删除应用发布
        self.appMethod.del_app_005()

    def tearDown(self):
        #应用发布后置条件
        self.commonSuite.application_module_post_condition()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
