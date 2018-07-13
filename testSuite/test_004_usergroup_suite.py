#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/7/28
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
sys.path.append("/testIsompSecret/testCase/group/")
from test_usergroup import testUsergroup
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
import unittest

class testUsergroupSuite(unittest.TestCase):

	def setUp(self):

		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.testusergroup = testUsergroup(self.browser)

		#用户组前置条件
		self.comsuit.usergroup_module_prefix_condition()

	def test_usergroup(self):

		u'''添加和编辑用户组'''
		self.testusergroup.add_edit_usergroup_001()
		u'''上移和下移用户组'''
		self.testusergroup.up_down_usergroup_002()
		u'''上移和下移用户组校验'''
		self.testusergroup.up_down_usergroup_check_003()
		u'''检验添加和编辑用户组'''
		self.testusergroup.check_add_edit_usergroup_004()
		u'''用户组中添加用户'''
		self.testusergroup.usergroup_add_user_001()
		u'''用户组中查询用户账号/名称'''
		self.testusergroup.query_usergroup_002()
		u'''用户组删除用户'''
		self.testusergroup.usergroup_del_user_003()
		u'''用户组全选删除用户'''
		self.testusergroup.usergroup_bulk_user_004()
		u'''删除用户组'''
		self.testusergroup.del_usergroup_005()

	def tearDown(self):

		#用户组后置条件
		self.comsuit.usergroup_module_post_condition()

		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()

