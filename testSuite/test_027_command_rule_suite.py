#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：命令规则
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
sys.path.append("/testIsompSecret/testCase/rule/")
from test_command_rule import testCommand

class testComRuleSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.comm = testCommand(self.browser)

		#命令规则前置条件
		self.comsuit.commandrule_module_prefix_condition()

	def test_command_rule(self):
		#添加命令规则
		self.comm.add_command_rule_001()
		#编辑命令规则
		self.comm.mod_command_rule_002()
		#操作命令规则
		self.comm.option_command_rule_003()
		#校验命令规则
		self.comm.check_command_rule_004()
		#命令审批
		# self.comm.command_approval_005()
		#删除命令规则
		self.comm.del_command_rule_006()

	def tearDown(self):
		#命令规则后置条件
		self.comsuit.commandrule_module_post_condition()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()