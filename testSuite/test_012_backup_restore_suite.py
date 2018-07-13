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
sys.path.append("/testIsompSecret/testCase/backup_restore/")
from test_backup_restore import testBackupRestore
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
import unittest

class testBackupSuite(unittest.TestCase):

	def setUp(self):

		#调用驱动
		self.browser = setDriver().set_driver()
		self.comsuit = CommonSuiteData(self.browser)
		self.backup = testBackupRestore(self.browser)

		#备份还原前置条件
		self.comsuit.backup_restore_module_prefix_condition()

	def test_backupre(self):
		u'''备份系统配置'''
		self.backup.backup_sys_restore_001()
		u'''备份实体配置'''
		self.backup.backup_entity_restore_002()
		u'''备份系统配置和实体配置'''
		self.backup.backup_sys_entity_003()

	def tearDown(self):
		#备份还原后置条件
		self.comsuit.user_quit()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()
