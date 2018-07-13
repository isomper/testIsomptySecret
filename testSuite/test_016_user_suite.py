#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入驱动
sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/user/")
from test_user import User

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testUserSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()

        self.commonSuite = CommonSuiteData(self.browser)
        self.userCase = User(self.browser)
        
        #前置条件
        self.commonSuite.user_module_prefix_condition()

    def test_login(self):
        #添加用户
        self.userCase.add_user_001()
        #修改用户
        self.userCase.edit_user_002()
        #生成证书
        self.userCase.create_user_cert_003()
        #重新生成证书
        self.userCase.create_user_cert_again_003()
        #删除证书
        self.userCase.delete_user_cert_004()
        #用户校验
        self.userCase.checkout_user_005()
        #用户检索
        self.userCase.search_user_by_username_006()
        self.userCase.search_user_by_status_006()
        self.userCase.search_user_by_dep_006()
        #删除单一用户
        self.userCase.del_user_007()
        #删除全部用户
        self.userCase.del_all_user_008()
    
    def tearDown(self):
        self.commonSuite.user_quit()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()

