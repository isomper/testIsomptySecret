#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入驱动
sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/session_configuration/")
from test_session_configuration import conversationStrategy

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testSessionConfigSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        
        self.commonSuite = CommonSuiteData(self.browser)
        self.sessionCase = conversationStrategy(self.browser)
        self.initDriver = initDriver()
        #前置条件
        self.commonSuite.session_module_prefix_condition()
    
    def test_session(self):
        #添加访问失败次数和失败锁定时间
        self.sessionCase.add_session_config_001()
        #校验访问失败次数和失败锁定时间
        self.sessionCase.check_session_config_002()
        #单用户登录方式和web超时时间添加
        self.sessionCase.sing_user_login_and_session_003()
        #单用户登录方式校验
        self.sessionCase.check_sing_user_login_004()
        
    def tearDown(self):
        #后置条件
        self.commonSuite.user_quit()
        #关闭浏览器
        self.initDriver.close_driver(self.browser)
        
if __name__ == "__main__":
    unittest.main()
