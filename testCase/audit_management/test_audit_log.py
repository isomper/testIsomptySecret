#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import time

sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/audit_management")
from auditLogElement import AuditLogPage
sys.path.append("/testIsompSecret/webElement/audit_management")
from systemLogElement import SystemLogPage

sys.path.append("/testIsompSecret/webElement/user")
from userElement import UserPage
sys.path.append("/testIsompSecret/webElement/resource/")
from test_resource_common import Resource

sys.path.append("/testIsomp/testSuite")
from common_suite_file import CommonSuiteData,setDriver

class testAuditLog():
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.cnEnde = cnEncode()
		self.userElem = UserPage(driver)
		self.systemLog = SystemLogPage(self.driver)
		self.auditLog = AuditLogPage(self.driver)
		self.systemLog = SystemLogPage(self.driver)
		self.tableElem = tableElement(self.driver)
		self.selectElem = selectElement(driver)
		self.dataFile = dataFileName()
		self.frameElem = frameElement(self.driver)
		self.resource = Resource(driver)
		self.commonSuite = CommonSuiteData(self.driver)
	
	u'''校验没有弹出框类型用例是否通过
			parameters: 
				data : 检查点
				count :正确的行数
	'''
	def check_without_pop_up(self,count,data):
		#获取行数
		table_count = str(self.systemLog.get_table_count())
		if count == table_count:
			self.cmf.test_win_check_point("","",data,True)
		else:
			self.cmf.test_win_check_point("","",data,False)

	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
			return：表格数据
	'''
	def get_table_data(self,sheetname):
		dataFile = dataFileName()
		filePath = dataFile.get_audit_log_test_url()
		queryData = dataFile.get_data(filePath,sheetname)
		return queryData

	u'''运维审计检索功能'''
	def Audit_log_query_001(self):#query_type
		#日志开始记录
		self.log.log_start("AuditLogQuery_001")
		#获取配置审计检索的数据
		ad_data = self.get_table_data("audit_log_query")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.auditLog.select_date(data[2])
					if data[3] != "":
						self.auditLog.select_depmt(data[3])
					if data[4] != "":
						self.auditLog.click_select_audit()
						self.auditLog.select_audit(data[4])
					if data[2] == "":
						self.auditLog.click_high_level(data[17])
						self.auditLog.select_audit_type(data[5])
						if data[6] != "":
							self.resource.query_type(data[6],data[7],data[8])
						self.auditLog.set_res_account(data[9])
						self.auditLog.set_user_name(data[10])
						self.auditLog.set_client_ip(data[11])
						self.userElem.set_start_time(data[12])
						self.userElem.set_end_time(data[13])
						self.auditLog.set_key_word(data[14])
						self.auditLog.set_source_ip(data[15])
						self.auditLog.set_user_account(data[16])
					self.auditLog.click_search()
					#判断测试项是否通过
					self.check_without_pop_up(data[18],data)
					#清空标识状态
					flag = False
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.userElem.click_reset_button()
			except Exception as e:
				print ("Audit Log query fail: ") + str(e)
		self.log.log_end("AuditLogQuery_001")

#if __name__ == "__main__":
#	browser = setDriver().set_local_driver()
#	commonSuite = CommonSuiteData(browser)
#	adTest = testAuditLog(browser)
#	#commonSuite.audit_log_prefix_condition()
#	commonSuite.login_and_switch_to_sys()
#	commonSuite.switch_to_moudle(u"审计管理", u"运维审计")
#
#	adTest.Audit_log_query_001()
#	adTest.conf_report_check_002()
#	adTest.conf_report_del_004()
