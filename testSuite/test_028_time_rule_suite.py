#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：时间规则
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
from test_time_rule import testTime

class testTimeRuleSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.timerule = testTime(self.browser)

		#时间规则前置条件
		self.comsuit.timerule_module_prefix_condition()

	def test_time_rule(self):
		#添加时间规则
		self.timerule.add_time_rule_001()
		#添加时间规则结果
		self.timerule.add_time_rule_result_002()
		#编辑时间规则
		self.timerule.mod_time_rule_003()
		#校验时间规则
		self.timerule.check_time_rule_004()
		#检索时间规则
		self.timerule.query_time_rule_005()
		#删除时间规则
		self.timerule.del_time_rule_006()

	def tearDown(self):
		#时间规则后置条件
		self.comsuit.timerule_module_post_condition()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()
