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

sys.path.append("/testIsompSecret/webElement/report")
from confReportElement import ConfReportPage
sys.path.append("/testIsompSecret/webElement/report")
from optReportElement import OptReportPage
sys.path.append("/testIsompSecret/webElement/authorization")
from authrizationElement import AuthorizationPage

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver
sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

class testOptReport():
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.cnEnde = cnEncode()
		self.confReport = ConfReportPage(self.driver)
		self.optReport = OptReportPage(self.driver)
		self.tableElem = tableElement(self.driver)
		self.selectElem = selectElement(driver)
		self.dataFile = dataFileName()
		self.frameElem = frameElement(self.driver)
		self.loginFun = loginPage(self.driver)
		self.commonSuite = CommonSuiteData(self.driver)
		self.authElem = AuthorizationPage(self.driver)
	
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
		filePath = dataFile.get_opt_report_test_url()
		reportData = dataFile.get_data(filePath,sheetname)
		return reportData

	u'''添加行为审计报表'''
	def add_opt_report_001(self):
		#日志开始记录
		self.log.log_start("AddOptReport_001")
		#获取行为报表添加的数据
		ad_data = self.get_table_data("add_opt_report")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			self.optReport.switch_to_opt_report()
			status = self.optReport.check_report_is_exist(data[2])
			if status == False:
				break
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					if status == True:
						self.confReport.set_module_name(data[2])
						self.confReport.set_user_account(data[3])
						self.optReport.set_res_account(data[4])
						self.confReport.select_group(data[5])
						self.optReport.select_res_group(data[6])
						self.optReport.sel_sigle_type(data[7])
						self.optReport.sel_sigle_type(data[8])
						self.optReport.sel_all_field()
						self.confReport.click_add_module()
					#判断测试项是否通过
					self.driver.switch_to_default_content()
					self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Add opt report fail: ") + str(e)
		self.log.log_end("AddOptReport_001")

	u'''添加行为审计报表校验'''
	def opt_report_check_002(self):
		#日志开始记录
		self.log.log_start("OptReportCheck_002")
		#获取校验行为报表的数据
		ad_data = self.get_table_data("opt_report_check")
		self.optReport.switch_to_opt_report()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.confReport.set_module_name(data[2])
					self.optReport.sel_all_field()
					if dataRow == 2:
						self.optReport.unsel_all_field()
					self.confReport.click_add_module()
					#判断测试项是否通过
					self.driver.switch_to_default_content()
					self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Opt Report Check fail: ") + str(e)
		self.log.log_end("OptReportCheck_002")

	u'''添加和修改行为审计计划模板'''
	def add_plan_report_003(self):
		#日志开始记录
		self.log.log_start("AddPlanReport_003")
		#获取添加计划模板的数据
		ad_data = self.get_table_data("add_plan_export")
		self.optReport.switch_to_opt_report()
		self.optReport.plan_report_btn()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.confReport.select_report(data[2])
					self.optReport.sel_cycle_type(data[3])
					if data[3] != "天":
						self.optReport.sel_cycle_date(data[4])
					self.optReport.set_time(data[5])
					if dataRow == 1:
						self.optReport.set_switch_to_on()
						self.optReport.sel_email_user_btn()
						self.authElem.set_select_user_search_button()
						self.authElem.set_user_check_all_button()
						self.authElem.set_ok_button()
					if dataRow == 2:
						self.optReport.set_switch_to_off()
					self.optReport.click_save()
					#判断测试项是否通过
					self.driver.switch_to_default_content()
					self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Add plan report fail: ") + str(e)
		self.optReport.click_back()
		self.log.log_end("AddPlanReport_003")

	u'''删除行为审计报表'''
	def opt_report_del_004(self):
		#日志开始记录
		self.log.log_start("OptReportDel_004")
		#获取删除行为报表的数据
		ad_data = self.get_table_data("del_opt_report")
		self.optReport.switch_to_opt_report()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					#self.optReport.switch_to_opt_report()
					self.confReport.select_report(data[2])
					self.confReport.click_del_module()
					#判断测试项是否通过
					self.driver.switch_to_default_content()
					self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Opt Report del fail: ") + str(e)
		self.log.log_end("OptReportDel_004")

