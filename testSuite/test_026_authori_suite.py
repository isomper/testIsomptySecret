#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入驱动
sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/authorization/")
from test_authorization import testAuthorization

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testAuthSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()

        self.commonSuite = CommonSuiteData(self.browser)
        self.authCase = testAuthorization(self.browser)

        self.commonSuite.authori_module_prefix_condition()

    def test_authori(self):
        #添加用户和资源类型的授权
        self.authCase.add_user_and_res_auth_001()
        #添加用户和资源组类型的授权
        self.authCase.add_user_and_res_group_auth_002()
        #添加用户和资源账号类型的授权
        self.authCase.add_user_and_res_account_auth_003()
        #添加用户组和资源类型的授权
        self.authCase.add_user_group_and_res_auth_004()
        #添加用户组和资源组类型的授权
        self.authCase.add_user_group_and_res_group_auth_005()
        #添加用户组和资源账号类型的授权
        self.authCase.add_user_group_and_res_account_auth_006()
        #修改授权名称
        self.authCase.edit_auth_name_007()
        #授权校验
        self.authCase.auth_checkout_008()
        #授权检索
        self.authCase.auth_query_009()
        #添加访问审批
        # self.authCase.Opt_access_approvel_011()
        #双人授权
        # self.authCase.add_double_approvel_012()
        #删除授权
        self.authCase.auth_del_010()
    
    def tearDown(self):
        self.commonSuite.authori_module_post_condition()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()

