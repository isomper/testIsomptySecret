#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import unittest
sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
sys.path.append("/testIsompSecret/testCase/resource/")
from test_linux_resource import testLinuxResource
from test_resource_accountmgr import testResourceAccount
from test_windows_resource import testWindowsResource
sys.path.append("/testIsompSecret/testData/")
import _testDataPath

class testWindowsResourceSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.linuxresource = testLinuxResource(self.browser)
		self.windows = testWindowsResource(self.browser)
		self.account = testResourceAccount(self.browser)

		#资源前置条件
		self.comsuit.windowre_module_prefix_condition()

	def test_windows_resource(self):
		#------------------------------windows资源-----------------------------------
		#添加windows资源
		self.windows.add_windows_resource_001()
		#校验windows资源
		self.windows.check_windows_resource_003()
		#编辑windows资源
		self.windows.edit_windows_resource_002()
		#添加和编辑windows资源账号
		self.account.add_edit_resource_account_001(_testDataPath.WINDOWS_RESOURCE_TEST_DATA_URL, "add_windows_account")
		#查询windows资源账号
		self.account.query_resource_account_002(_testDataPath.WINDOWS_RESOURCE_TEST_DATA_URL, "query_windows_account")
		#校验windows资源账号
		self.account.check_resource_account_003(_testDataPath.WINDOWS_RESOURCE_TEST_DATA_URL, "check_windows_account")
		#删除windows资源账号
		self.account.del_resource_account_004(_testDataPath.WINDOWS_RESOURCE_TEST_DATA_URL, "del_windows_account")
		#全选删除windows资源账号
		self.account.bulkdel_resource_account_005(_testDataPath.WINDOWS_RESOURCE_TEST_DATA_URL, "bulkdel_windows_account")
		#查询windows资源
		self.linuxresource.query_resource_004(_testDataPath.WINDOWS_RESOURCE_TEST_DATA_URL, "query_windows_resource")
		#删除windows资源
		self.linuxresource.del_resource_005(_testDataPath.WINDOWS_RESOURCE_TEST_DATA_URL, "del_windows_resource")

	def tearDown(self):
		self.comsuit.user_quit()

		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()