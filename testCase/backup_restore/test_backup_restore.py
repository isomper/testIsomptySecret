#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2018/1/24
#模块描述：备份还原
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName
sys.path.append("/testIsompSecret/common")
from _icommon import commonFun
from _log import log
sys.path.append("/testIsompSecret/webElement/backup_restore/")
from test_backup_restore_ment import Backuprestore

class testBackupRestore(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.backup = Backuprestore(driver)
		self.data = dataFileName()

	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
		return：表格数据
	'''
	def get_table_data(self, sheetname):
		dataFile = dataFileName()
		backupPath = dataFile.back_restore_test_date_url()
		backupData = dataFile.get_data(backupPath, sheetname)
		return backupData

	u'''备份系统配置'''
	def backup_sys_restore_001(self):

		#日志开始记录
		self.log.log_start("backup_sys_config")
		#获取备份系统配置测试数据
		backupData = self.get_table_data("backup_sys_config")
		#保存成功的弹出框
		backMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(backupData)):
			data = backupData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					time.sleep(3)
					#编写syslog
					self.backup.set_syslog(data[3], data[2])
					#配置系统配置内容
					self.backup.config_backup(data, backMsg, flag)
					filename = self.backup.get_file_name()
					#更改syslog内容
					self.backup.set_syslog(data[8])
					#进行还原操作
					self.backup.execute_restore(filename, data[10])
					#进行校验文本信息是否为原来的端口
					self.backup.check_syslog_content(data[3], data[11])
			except Exception as e:
				print ("backup_sys_config fail:" + str(e))
		self.log.log_end("backup_sys_config")

	u'''备份实体配置'''
	def backup_entity_restore_002(self):

		#日志开始记录
		self.log.log_start("backup_entity_config")
		#获取备份实体配置测试数据
		backupData = self.get_table_data("backup_entity_config")
		#保存成功的弹出框
		backMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(backupData)):
			data = backupData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					#编写用户信息
					self.backup.set_user_info(data[2], data[3], data[13], data[14])
					#配置系统配置内容
					self.backup.config_backup(data, backMsg, flag)
					filename = self.backup.get_file_name()
					#删除用户信息
					self.backup.del_user_info(data[8])
					#进行还原操作
					self.backup.execute_restore(filename, data[10])
					#进行用户信息是否存在
					self.backup.check_content(data[3], "fortUserName", data[11])
					#删除用户信息
					self.backup.del_user_info(data[8])
			except Exception as e:
				print ("backup_entity_config fail:" + str(e))
		self.log.log_end("backup_entity_config")

	u'''备份系统配置和实体配置'''
	def backup_sys_entity_003(self):

		#日志开始记录
		self.log.log_start(" backup_sys_entity")
		#获取备份系统实体配置测试数据
		backupData = self.get_table_data(" backup_sys_entity")
		#保存成功的弹出框
		backMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(backupData)):
			data = backupData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					#编写syslog
					self.backup.set_syslog(data[3], data[2])
					#配置系统配置内容
					self.backup.config_backup(data, backMsg, flag)
					filename = self.backup.get_file_name()
					#进行下载操作
					self.backup.click_operat_file(filename, 1)
					self.log.log_detail(data[13], True)
					#进行删除操作
					self.backup.del_backup_file(filename, data[14])
					#进行上传操作
					self.backup.backup_file_upload(filename, data[15])
					#更改syslog内容
					self.backup.set_syslog(data[8])
					#进行还原操作
					self.backup.execute_restore(filename, data[10], 2)
					#进行校验文本信息是否为原来的端口
					self.backup.check_syslog_content(data[3], data[11])
			except Exception as e:
				print (" backup_sys_entity fail:" + str(e))
		self.log.log_end(" backup_sys_entity")
