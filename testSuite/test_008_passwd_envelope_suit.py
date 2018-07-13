# -*- coding:utf-8 -*-
'''
#文件名：
#作者：张利娟
#创建日期：2018/1/31
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
sys.path.append("/testIsompSecret/testCase/passwd_envelope/")
from test_passwd_envelope import testEnvelope
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import setDriver, CommonSuiteData
import unittest

class testPasswdEnvelopeSuit(unittest.TestCase):

    def setUp(self):
        self.browser = setDriver().set_driver()
        self.comsuit = CommonSuiteData(self.browser)
        self.testenvelope = testEnvelope(self.browser)

        #前置条件
        self.comsuit.passwd_envelope_module_prefix_condition()

    def test_passwd_envelope(self):
        #配置密码信封
        self.testenvelope.add_passwd_envelope_001()
        #浏览、上传图片
        self.testenvelope.upload_passwd_envelope_002()
        #同步图片
        self.testenvelope.passwd_envelope_image_sync_003()
        #编辑密码信封
        self.testenvelope.mode_passwd_envelope_004()
        #检验密码信封
        self.testenvelope.check_passwd_envelope_005()

    #后置条件
    def tearDown(self):
        self.comsuit.user_quit()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
