#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：张泽方
#生成日期：2018/2/1
#模块描述：使用授权
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/use_auth/")
from test_use_auth import UseAuthorization

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class UseAuthSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)
        self.useAuthCase = UseAuthorization(self.browser)
        self.initDriver = initDriver()
        
        #前置条件
        self.commonSuite.use_auth_module_prefix_condition()
        
    def test_use_auth(self):
        #填写产品信息
        self.useAuthCase.add_product_information_001()
        #上传logo
        self.useAuthCase.upload_logo_upgrade_002()
        #产品信息校验
        self.useAuthCase.check_product_information_003()
        #logo包校验
        self.useAuthCase.check_logo_upgrade_004()
        #上传授权码
        # self.useAuthCase.add_product_information_005()
        #上传授权码校验
        # self.useAuthCase.check_updata_auth_006()
        
    def tearDown(self):
        self.commonSuite.user_quit()
        self.initDriver.close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
