#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：顾亚茹
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
sys.path.append("/testIsompSecret/testSuite/")
from common_suite_file import setDriver,CommonSuiteData
sys.path.append("/testIsompSecret/testCase/resource/")
from test_linux_resource import testLinuxResource
from test_resource_accountmgr import testResourceAccount
from test_database_resource import testDatabaseResource
sys.path.append("/testIsompSecret/testData/")
import _testDataPath

class testDatabaseResourceSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.linuxresource = testLinuxResource(self.browser)
		self.database = testDatabaseResource(self.browser)
		self.account = testResourceAccount(self.browser)
		#添加数据库前置条件
		self.comsuit.database_resource_prefix_condition()

	def test_database_resource(self):
		#------------------------------windows资源-----------------------------------
		#添加database资源
		self.database.add_database_resource_001()
		#编辑database资源
		self.database.edit_database_resource_002()
		#校验database资源
		self.database.check_database_resource_003()	
		#添加和编辑mysql资源账号
		self.account.add_edit_resource_account_001(_testDataPath.DATABASE_TEST_DATA_URL, "add_mysql_account")
		#添加和编辑oracle资源账号
		self.account.add_edit_resource_account_001(_testDataPath.DATABASE_TEST_DATA_URL, "add_oracle_account")
		#添加和编辑bs资源账号
		self.account.add_edit_resource_account_001(_testDataPath.DATABASE_TEST_DATA_URL, "add_bs_account")
		#添加和编辑sql资源账号
		self.account.add_edit_resource_account_001(_testDataPath.DATABASE_TEST_DATA_URL, "add_sql_account")		
		#删除mysql资源账号
		self.account.del_resource_account_004(_testDataPath.DATABASE_TEST_DATA_URL, "del_mysql_account")
		#查询database资源
		self.linuxresource.query_resource_004(_testDataPath.DATABASE_TEST_DATA_URL, "query_database_resource")
		#删除mysql资源
		self.linuxresource.del_resource_005(_testDataPath.DATABASE_TEST_DATA_URL, "del_mysql_resource")
		#删除db2资源
		#self.linuxresource.del_resource_005(_testDataPath.DATABASE_TEST_DATA_URL, "del_db2_resorce")
		#全选删除资源
		#self.linuxresource.bulkdel_resource_006()

	def tearDown(self):
		#数据库后置条件
		self.comsuit.database_resource_post_condition()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()