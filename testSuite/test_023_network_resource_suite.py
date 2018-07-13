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
from test_network_resource import testNetworkResource
sys.path.append("/testIsompSecret/testData/")
import _testDataPath

class testNetworkResourceSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.linuxresource = testLinuxResource(self.browser)
		self.network = testNetworkResource(self.browser)
		self.account = testResourceAccount(self.browser)

		#资源前置条件
		self.comsuit.networkre_module_prefix_condition()

	def test_network_resource(self):
		#------------------------------网络设备资源-----------------------------------
		#添加网络设备资源
		self.network.add_network_resource_001()
		#编辑网络设备资源
		self.network.edit_network_resource_002()
		#校验网络设备资源
		self.network.check_network_resource_003()
		#添加和编辑网络设备资源账号
		self.account.add_edit_resource_account_001(_testDataPath.NETWORK_RESOURCE_TEST_DATA_URL, "add_network_account")
		#查询网络设备资源账号
		self.account.query_resource_account_002(_testDataPath.NETWORK_RESOURCE_TEST_DATA_URL, "query_network_account")
		#校验网络设备资源账号
		self.account.check_resource_account_003(_testDataPath.NETWORK_RESOURCE_TEST_DATA_URL, "check_network_account")
		#删除网络设备资源账号
		self.account.del_resource_account_004(_testDataPath.NETWORK_RESOURCE_TEST_DATA_URL, "del_network_account")
		#全选删除网络设备资源账号
		self.account.bulkdel_resource_account_005(_testDataPath.NETWORK_RESOURCE_TEST_DATA_URL, "bulkdel_network_account")
		#查询网络设备资源
		self.linuxresource.query_resource_004(_testDataPath.NETWORK_RESOURCE_TEST_DATA_URL, "query_network_resource")
		#删除网络设备资源
		self.linuxresource.del_resource_005(_testDataPath.NETWORK_RESOURCE_TEST_DATA_URL, "del_network_resource")

	def tearDown(self):
		self.comsuit.user_quit()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()