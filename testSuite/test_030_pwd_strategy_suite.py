#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：张泽方
#生成日期：2018/1/25
#模块描述：密码策略
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/password_strategy/")
from test_passsword_strstegy import PasswordStr

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class TestPwdSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)
        self.pwdstr = PasswordStr(self.browser)
        self.initDriver = initDriver()
        #前置条件
        self.commonSuite.pwdstr_module_prefix_condition()
        
    def test_pwdstr(self):
        #添加密码策略
        self.pwdstr.add_strategy_001()
        #编辑密码策略
        self.pwdstr.edit_strategy_002()
        #密码策略校验
        self.pwdstr.check_strategy_003()
        #密码策略检索
        self.pwdstr.search_strategy_004()
        #删除单条密码策略
        self.pwdstr.del_sing_policy_005()
        #配置全局密码策略
        self.pwdstr.session_association_007()
        #与密码策略关联的用户
        self.pwdstr.user_association_008()
        #与密码策略关联的资源
        self.pwdstr.resource_association_009()
        #与密码策略关联的资源账号
        self.pwdstr.resource_account_association_010()
        #删除所有密码策略
        self.pwdstr.del_all_policy_006()

    def tearDown(self):
        #后置条件
        self.commonSuite.pwdstr_module_post_condition()
        #关闭浏览器
        self.initDriver.close_driver(self.browser)
        
if __name__ == "__main__":
    unittest.main()
