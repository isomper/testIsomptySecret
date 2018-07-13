#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/client_conf")
from test_client_conf import testClient

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testClientSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)        
        self.clientMethod = testClient(self.browser)
        #客户端前置条件
        self.commonSuite.client_module_prefix_condition()
    
    def test_client_method(self):
        #添加客户端
        self.clientMethod.add_client_001()
        #修改客户端
        self.clientMethod.edit_client_002()
        #校验客户端
        self.clientMethod.check_client_003()
        #删除客户端
        self.clientMethod.del_client_004()

    def tearDown(self):
        #客户端后置条件
        self.commonSuite.user_quit()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
