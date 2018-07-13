#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/7/18
#模块描述：资源
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
sys.path.append("/testIsompSecret/testData/")
import _testDataPath


class testLinuxResourceSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.linuxresource = testLinuxResource(self.browser)
		self.account = testResourceAccount(self.browser)

		#资源前置条件
		self.comsuit.linuxre_module_prefix_condition()

	def test_linux_resource(self):
		#------------------------------linux资源-----------------------------------
		#添加linux资源
		self.linuxresource.add_linux_resource_001()
		#编辑linux资源
		self.linuxresource.edit_linux_resource_002()
		#校验linux资源
		self.linuxresource.check_linux_resource_003()
		#添加和编辑linux资源账号
		self.account.add_edit_resource_account_001(_testDataPath.LINUX_RESOURCE_TEST_DATA_URL, "add_linux_account")
		#查询linux资源账号
		self.account.query_resource_account_002(_testDataPath.LINUX_RESOURCE_TEST_DATA_URL, "query_linux_account")
		#校验linux资源账号
		self.account.check_resource_account_003(_testDataPath.LINUX_RESOURCE_TEST_DATA_URL, "check_linux_account")
		#删除linux资源账号
		self.account.del_resource_account_004(_testDataPath.LINUX_RESOURCE_TEST_DATA_URL, "del_linux_account")
		#全选删除linux资源账号
		self.account.bulkdel_resource_account_005(_testDataPath.LINUX_RESOURCE_TEST_DATA_URL, "bulkdel_linux_account")
		#查询linux资源
		self.linuxresource.query_resource_004(_testDataPath.LINUX_RESOURCE_TEST_DATA_URL, "query_linux_resource")
		#删除linux资源
		self.linuxresource.del_resource_005(_testDataPath.LINUX_RESOURCE_TEST_DATA_URL, "del_linux_resource")

	def tearDown(self):

		self.comsuit.user_quit()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()