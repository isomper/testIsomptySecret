#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：添加涉密版用户
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入驱动
sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver

sys.path.append("/testIsompSecret/testCase/secret_user_role/")
from test_secret_user_role import testSecretUserRole

sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
import unittest

class testAddUserSuite(unittest.TestCase):

	def setUp(self):

		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.testseuser = testSecretUserRole(self.browser)

		#部门前置条件
		self.comsuit.secret_user_prefix_condition()

	def test_add_secret_user(self):

		u'''编辑运维角色'''
		self.testseuser.edit_operation_role()
		u'''添加系统管理员角色'''
		self.testseuser.set_sysAdmin_role()
		u'''添加安全保密管理员角色'''
		self.testseuser.set_secAdmin_role()
		u'''添加安全审计员角色'''
		self.testseuser.set_sysAudit_role()
		u'''添加涉密用户'''
		self.testseuser.add_secret_user()

	def tearDown(self):
		self.comsuit.user_quit()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()
