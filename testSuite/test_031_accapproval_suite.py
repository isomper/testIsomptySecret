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
sys.path.append("/testIsompSecret/testCase/process/")
from test_access_approval import testAccapproval

class testAccapprovalSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.accapproval = testAccapproval(self.browser)

		#流程前置条件

		self.comsuit.process_module_prefix_condition()

	def test_access_approval(self):
		# 添加访问审批
		self.accapproval.add_access_approvel_001()
		u'''访问审批通过流程控制拒绝审批'''
		self.accapproval.access_deny_approvel_002()
		u'''访问审批通过流程控制同意审批'''
		self.accapproval.access_agree_approvel_003()
		u'''紧急运维通过流程控制拒绝审批'''
		self.accapproval.urgent_deny_approvel_004()
		u'''紧急运维通过流程控制同意审批'''
		self.accapproval.urgent_agree_approvel_005()
		u'''访问审批流程任务查询'''
		self.accapproval.access_query_process_task_006()
		u'''访问审批个人历史查询'''
		self.accapproval.access_query_personal_history_007()
		u'''访问审批申请历史查询'''
		self.accapproval.access_query_apply_history_008()
		u'''访问审批全部历史查询'''
		self.accapproval.access_query_all_history_009()

	def tearDown(self):
		#流程后置条件
		self.comsuit.process_module_post_condition()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()