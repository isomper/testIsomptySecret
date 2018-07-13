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
sys.path.append("/testIsompSecret/testCase/rule/")
from test_address_rule import testAddress

class testAdreRuleSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.adrerule = testAddress(self.browser)

		#地址规则前置条件
		self.comsuit.addressrule_module_prefix_condition()

	def test_address_rule(self):
		#添加地址规则
		self.adrerule.add_address_rule_001()
		#添加地址规则结果
		self.adrerule.add_address_rule_result_002()
		#编辑地址规则
		self.adrerule.mod_address_rule_003()
		#校验地址规则
		self.adrerule.check_address_rule_004()
		#检索地址规则
		self.adrerule.query_address_rule_005()
		#删除地址规则
		self.adrerule.del_address_rule_006()

	def tearDown(self):
		#时间规则后置条件
		self.comsuit.addressrule_module_post_condition()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()
