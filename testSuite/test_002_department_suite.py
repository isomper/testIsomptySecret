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

#导入驱动
sys.path.append("/testIsompSecret/common/")
from _initDriver import initDriver
sys.path.append("/testIsompSecret/testCase/department/")
from test_department import testDepartment
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
import unittest

class testDepartSuite(unittest.TestCase):

	def setUp(self):

		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.testdptment = testDepartment(self.browser)

		#部门前置条件
		self.comsuit.depart_module_prefix_condition()

	def test_department(self):

		u'''添加和编辑部门'''
		self.testdptment.add_edit_department_001()
		u'''上移和下移部门'''
		self.testdptment.up_down_department_002()
		u'''上移和下移部门校验'''
		self.testdptment.up_down_department_check_003()
		u'''检验添加和编辑部门'''
		self.testdptment.check_add_edit_department_004()
		u'''删除部门'''
		self.testdptment.del_department_005()

	def tearDown(self):
		self.comsuit.user_quit()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()
