#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2018/1/11
#模块描述：资源时间规则
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
from test_resource_time_rule import testRetime

class testRetimeRuleSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.retime = testRetime(self.browser)

		#资源时间规则前置条件
		self.comsuit.retimerule_module_prefix_condition()

	def test_retime_rule(self):
		#添加资源时间规则
		self.retime.add_retime_rule_001()
		#编辑资源时间规则
		self.retime.mod_retime_rule_002()
		#资源时间规则结果验证
		self.retime.add_retime_rule_result_003()
		#操作资源时间规则
		self.retime.option_retime_rule_004()
		#校验资源时间规则
		self.retime.check_retime_rule_005()
		#删除资源时间规则
		self.retime.del_retime_rule_006()

	def tearDown(self):
		#资源时间规则后置条件
		self.comsuit.retimerule_module_post_condition()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()