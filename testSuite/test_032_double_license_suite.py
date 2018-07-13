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
from _icommon import commonFun
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
sys.path.append("/testIsompSecret/testCase/process/")
from test_double_license import testDobapproval

class testDoubleSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.cmf = commonFun(self.browser)
		self.double = testDobapproval(self.browser)

		#双人授权前置条件
		self.comsuit.dualmandate_module_prefix_condition()

	def test_double_approval(self):
		# 添加双人授权
		self.double.add_double_license_001()
		u'''双人审批同终端审批'''
		self.double.same_termina_approvel_002()
		u'''双人审批申请人已下线审批过期'''
		self.double.termina_expired_approvel_003()
		u'''双人审批审批人拒绝申请'''
		self.double.termina_deny_approvel_004()
		u'''双人审批审批人同意申请'''
		self.double.termina_agree_approvel_005()
		u'''双人审批流程任务查询'''
		self.double.double_query_process_task_006()
		u'''双人审批个人历史查询'''
		self.double.double_query_personal_history_007()
		u'''双人审批申请历史查询'''
		self.double.double_query_apply_history_008()
		u'''双人审批全部历史查询'''
		self.double.double_query_all_history_009()

	def tearDown(self):
		#双人授权后置条件
		self.comsuit.dualmandate_module_post_condition()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()
