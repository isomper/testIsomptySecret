#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/report")
from confReportElement import ConfReportPage

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData
sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

class testConfReport():
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.cnEnde = cnEncode()
		self.confReport = ConfReportPage(self.driver)
		self.tableElem = tableElement(self.driver)
		self.selectElem = selectElement(driver)
		self.dataFile = dataFileName()
		self.frameElem = frameElement(self.driver)
		self.loginFun = loginPage(self.driver)
		self.commonSuite = CommonSuiteData(self.driver)
	
	u'''提示内容框元素路径'''
	def login_msg(self):
		login_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/ \
		tbody/tr[2]/td[2]/div"
		return login_msg

	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
			return：表格数据
	'''
	def get_table_data(self,sheetname):
		dataFile = dataFileName()
		filePath = dataFile.get_conf_report_test_url()
		reportData = dataFile.get_data(filePath,sheetname)
		return reportData

	u'''添加配置审计报表'''
	def add_conf_report_001(self):
		#日志开始记录
		self.log.log_start("AddConfReport_001")
		#获取配置报表添加的数据
		ad_data = self.get_table_data("add_conf_report")
		#self.confReport.swotch_to_conf_report()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.confReport.switch_to_conf_report()
					self.confReport.set_module_name(data[2])
					self.confReport.set_user_account(data[3])
					self.confReport.set_user_name(data[4])
					self.confReport.select_group(data[5])
					self.confReport.select_module(data[6])
					self.confReport.click_field()
					self.confReport.click_add_module()
					#判断测试项是否通过
					self.driver.switch_to_default_content()
					self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Add conf report fail: ") + str(e)
		self.log.log_end("AddConfReport_001")

	u'''添加配置审计报表校验'''
	def conf_report_check_002(self):
		#日志开始记录
		self.log.log_start("ConfReportCheck_002")
		#获取校验配置报表的数据
		ad_data = self.get_table_data("conf_report_check")
		#self.confReport.swotch_to_conf_report()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.confReport.set_module_name(data[2])
					self.confReport.click_field()
					if dataRow == 2:
						self.confReport.quit_click_field()
					self.confReport.click_add_module()
					#判断测试项是否通过
					self.driver.switch_to_default_content()
					self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Conf Report Check fail: ") + str(e)
		self.log.log_end("ConfReportCheck_002")
		
	u'''删除配置审计报表'''
	def conf_report_del_004(self):
		#日志开始记录
		self.log.log_start("ConfReportDel_004")
		#获取导出配置报表的数据
		ad_data = self.get_table_data("del_conf_report")
		
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.confReport.switch_to_conf_report()
					self.confReport.select_report(data[2])
					self.confReport.click_del_module()
					#判断测试项是否通过
					self.driver.switch_to_default_content()
					self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Conf Report del fail: ") + str(e)
		self.log.log_end("ConfReportDel_004")
