# -*- coding:utf-8 -*-
'''
#文件名：
#作者：张利娟
#创建日期：2018/1/17
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 导入驱动
sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver
sys.path.append("/testIsompSecret/testCase/mail/")
from test_mail import testMail
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import setDriver, CommonSuiteData
import unittest

class testMailSuit(unittest.TestCase):
    def setUp(self):
        self.browser = setDriver().set_driver()
        self.comsuit = CommonSuiteData(self.browser)
        self.testmail = testMail(self.browser)

        #前置条件
        self.comsuit.mail_module_prefix_condition()

    def test_mail(self):
        #配置邮件
        self.testmail.add_mail_001()
        #编辑邮件
        self.testmail.mod_mail_002()
        #测试邮件
        self.testmail.test_mail_003()
        #校验邮件
        self.testmail.check_mail_004()
        #测试开关
        self.testmail.onoff_mail_005()

    #后置条件
    def tearDown(self):
        self.comsuit.user_quit()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
