#coding=utf-8
''' 
#文件名：
#作者：顾亚茹
#创建日期：2017/08/14
#模块描述：调用单点登录定义模块
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

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

sys.path.append("/testIsompSecret/webElement/sso")
from ssoElement import SsoPage

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver

class testSso():
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.cnEnde = cnEncode()
		self.ssoElem = SsoPage(self.driver)
		self.tableElem = tableElement(self.driver)
		self.selectElem = selectElement(driver)
		self.dataFile = dataFileName()
		self.frameElem = frameElement(self.driver)
		self.commSuite = CommonSuiteData(self.driver)
	
	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
			return：表格数据
	'''
	def get_table_data(self,sheetname):
		dataFile = dataFileName()
		filePath = dataFile.get_sso_test_url()
		ssoFileData = dataFile.get_data(filePath,sheetname)
		return ssoFileData
	
	u'''命令单点登录通用部分'''
	def sso_common_func(self,data):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.ssoElem.select_account(data[2],data[3])
		self.ssoElem.select_sso_icon(data[2],data[4])
		if data[5] != "":
			self.ssoElem.select_protocol(data[5])
		#self.ssoElem.execute_chrome_key()
		self.ssoElem.choice_browser(data[4],data[6],data[7],data[8])
		#self.ssoElem.refresh_windows()
		#判断测试项是否通过
		self.log.log_detail(data[0], True)
		#清空标识状态
		flag = False
	
	u'''windows资源单点登录通用部分'''
	def windows_common_func(self,data):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.ssoElem.select_account(data[2],data[3])
		self.ssoElem.select_sso_icon(data[2],data[4])
		if data[3] == "$user" or data[3] == "$user(local)":
			self.ssoElem.set_mstsc_account(data[9])
			self.ssoElem.set_mstsc_pwd(data[10])
			self.cmf.click_login_msg_button()
		self.ssoElem.choice_browser(data[4],data[6],data[7],data[8])
		
		#判断测试项是否通过
		self.log.log_detail(data[0], True)
		time.sleep(4)		
	
	u'''cisco资源单点登录'''
	def cisco_sso_login_001(self):
		#日志开始记录
		self.log.log_start("ssoLogin")
		#获取单点登录的数据
		sso_data = self.get_table_data("sso")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(sso_data)):
			data = sso_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				#if dataRow == 2:
				if 0 < dataRow <= 4:
					self.sso_common_func(data)
			except Exception as e:
				print ("Cisco SSO login fail: ") + str(e)
		#self.commSuite.user_quit()
		self.log.log_end("CiscossoLogin")
	
	u'''cisco匿名单点登录'''
	def cisco_niming_sso_login_002(self):
		#日志开始记录
		self.log.log_start("nimingssoLogin")
		#获取单点登录的数据
		sso_data = self.get_table_data("sso")
		#self.commSuite.sso_user_login(8)
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(sso_data)):
			data = sso_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if 4 < dataRow <= 6:
					self.sso_common_func(data)
			except Exception as e:
				print ("niming SSO login fail: ") + str(e)
		#self.commSuite.user_quit()
		self.log.log_end("nimingssoLogin")	
	
	u'''华为资源单点登录'''
	def huawei_sso_login_003(self):
		#日志开始记录
		self.log.log_start("huaweissoLogin")
		#self.commSuite.sso_user_login(9)
		#无检查点的测试项标识，如果为True说明通过
		sso_data = self.get_table_data("sso")
		flag = False
		for dataRow in range(len(sso_data)):
			data = sso_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if  6 < dataRow <= 10 :
					self.sso_common_func(data)
			except Exception as e:
				print ("hauwei SSO login fail: ") + str(e)
		#self.commSuite.user_quit()
		self.log.log_end("huaweissoLogin")
		
	u'''linux资源单点登录'''
	def debian_sso_login_004(self):
		#日志开始记录
		self.log.log_start("debianssoLogin")
		#self.commSuite.sso_user_login(10)
		sso_data = self.get_table_data("sso")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(sso_data)):
			data = sso_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if  11 <= dataRow <= 16 :
					self.sso_common_func(data)
			except Exception as e:
				print ("debian SSO login fail: ") + str(e)
		#self.commSuite.user_quit()
		self.log.log_end("debianssoLogin")
	
	u'''windowsRdp单点登录'''
	def windows_sso_login_005(self):
		#日志开始记录
		self.log.log_start("windowsssoLogin")
		#self.commSuite.sso_user_login(11)
		sso_data = self.get_table_data("windows_sso")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(sso_data)):
			data = sso_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.windows_common_func(data)					
			except Exception as e:
				print ("Windows SSO login fail: ") + str(e)
		self.commSuite.user_quit()
		self.log.log_end("WindowsssoLogin")
	
	u'''domain资源单点登录'''
	def domain_sso_login_006(self):
		#日志开始记录
		self.log.log_start("DomainssoLogin")
		self.commSuite.sso_user_ad_login(42)
		sso_data = self.get_table_data("domain_sso")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(sso_data)):
			data = sso_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.windows_common_func(data)					
			except Exception as e:
				print ("Domain SSO login fail: ") + str(e)
		#self.commSuite.user_quit()
		self.log.log_end("DomainssoLogin")
	
	u'''域内资源单点登录'''
	def yunei_sso_login_007(self):
		#日志开始记录
		self.log.log_start("yuneissoLogin")
		#self.commSuite.sso_user_ad_login(13)
		sso_data = self.get_table_data("yunei_sso")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(sso_data)):
			data = sso_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.windows_common_func(data)					
			except Exception as e:
				print ("yunei SSO login fail: ") + str(e)
		#self.commSuite.user_quit()
		self.log.log_end("yuneissoLogin")
	
	
#if __name__ == "__main__":
#	browser = setDriver().set_local_driver()
#
#	commonSuite = CommonSuiteData(browser)
	#commonSuite.sso_prefix_condition()
	#commonSuite.sso_post_condition()
#	#commonSuite.login_and_switch_to_common()
#	
#	ssoTest = testSso(browser)
#	ssoTest.cisco_sso_login_001()
#	ssoTest.cisco_niming_sso_login_002()
#	ssoTest.huawei_sso_login_003()
#	#ssoTest.debian_sso_login_004()
#	ssoTest.windows_sso_login_005()
	#ssoTest.domain_sso_login_006()