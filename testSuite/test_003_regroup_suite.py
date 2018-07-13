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
sys.path.append("/testIsompSecret/testCase/group/")
from test_rsgroup import testRegroup
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
import unittest

class testRegroupSuite(unittest.TestCase):

	def setUp(self):

		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.testregroup = testRegroup(self.browser)

		#资源组前置条件
		self.comsuit.regroup_module_prefix_condition()

	def test_regroup(self):

		u'''添加和编辑资源组'''
		self.testregroup.add_edit_regroup_001()
		u'''上移和下移资源组'''
		self.testregroup.up_down_regroup_002()
		u'''上移和下移资源组校验'''
		self.testregroup.up_down_regroup_check_003()
		u'''检验添加和编辑资源组'''
		self.testregroup.check_add_edit_regroup_004()
		u'''资源组中添加资源'''
		self.testregroup.regroup_add_resource_001()
		u'''资源组中查询资源名称和IP'''
		self.testregroup.query_regroup_002()
		u'''资源组删除资源'''
		self.testregroup.regroup_del_resouce_003()
		u'''资源组全选删除资源'''
		self.testregroup.regroup_bulk_resouce_004()
		u'''删除资源组'''
		self.testregroup.del_regroup_005()

	def tearDown(self):
		#资源组后置条件
		self.comsuit.regroup_module_post_condition()

		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()
