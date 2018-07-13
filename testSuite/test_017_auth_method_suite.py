#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

#导入认证
sys.path.append("/testIsompSecret/testCase/auth_method")
from test_auth_method import testAuthMethod

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testAuthMethodSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)        
        self.authMethod = testAuthMethod(self.browser)
        #认证方式前置条件
        self.commonSuite.auth_method_prefix_condition()
    
    def test_auth_method(self):
        #添加AD域认证方式
        self.authMethod.add_ad_method_001()
        #添加radius认证方式
        self.authMethod.add_radius_method_002()
        #添加AD域+口令认证方式
        self.authMethod.add_ad_and_pwd_method_003()
        #添加RADIUS+口令认证方式
        self.authMethod.add_radius_and_pwd_method_004()
        #添加数字证书认证方式
        self.authMethod.add_cert_method_005()
        #校验认证方式是否添加成功
        self.authMethod.auth_method_add_is_success_006()
        #修改AD域认证方式
        self.authMethod.mod_ad_method_007()
        #AD域认证方式校验
        self.authMethod.ad_method_checkout_008()
        #radius认证方式校验
        self.authMethod.radius_checkout_009()
        #删除多种认证方式
        self.authMethod.del_auth_method_010()

    def tearDown(self):
        #认证方式后置条件
        self.commonSuite.auth_method_post_condition()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
