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

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName
from _icommon import commonFun,frameElement
from _log import log
sys.path.append("/testIsomp/webElement/process/")
from test_double_license_ment import Dobapproval
sys.path.append("/testIsomp/webElement/authorization")
from authrizationElement import AuthorizationPage
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage
sys.path.append("/testIsomp/testSuite/common_suite_file/")
from common_suite_file import CommonSuiteData
sys.path.append("/testIsomp/webElement/process/")
from test_access_approval_ment import Accapproval
from test_process_common import Flowcontrol

class testDobapproval(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.data = dataFileName()
		self.cmf = commonFun(driver)
		self.double = Dobapproval(driver)
		self.comsuit = CommonSuiteData(self.driver)
		self.loginElem = loginPage(self.driver)
		self.authElem = AuthorizationPage(self.driver)
		self.acproval = Accapproval(driver)
		self.flow = Flowcontrol(self.driver)
		self.frameElem = frameElement(self.driver)

	u'''获取测试数据
	   Parameters:
	      - sheetname:sheet名称
	   return：表格数据
	'''
	def get_double_data(self, sheetname):
		dataFile = dataFileName()
		dobPath = dataFile.get_double_license_test_data_url()
		dobData = dataFile.get_data(dobPath, sheetname)
		return dobData

	u'''添加双人授权'''
	def add_double_license_001(self):
		#日志开始记录
		self.log.log_start("add_double_license")
		#获取双人授权的数据
		dobData = self.get_double_data("add_double_license")
		for dataRow in range(len(dobData)):
			data = dobData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					self.double.click_double_license_button(data[1])
					self.authElem.click_all_approver()
					self.authElem.click_all_candidate()
					self.authElem.click_start_association()
					self.authElem.click_create_relate()
					self.cmf.click_login_msg_button()
					#点击返回
					self.authElem.click_child_page_back_button()
					self.log.log_detail(u"添加双人授权成功", True)
			except Exception as e:
				print ("add_double_license fail: ") + str(e)
		self.loginElem.quit()
		self.log.log_end("add_double_license")

	u'''双人审批同终端审批'''
	def same_termina_approvel_002(self):

		#日志开始记录
		self.log.log_start("same_termina_approvel")
		#获取双人审批申请的数据
		dobData = self.get_double_data("double_license_sso")

		for dataRow in range(len(dobData)):
			data = dobData[dataRow]
			try:
				#如果是第1行,读取数据
				if dataRow == 1:
					self.acproval.user_login(data[6])
					self.cmf.select_role_by_text(u"运维操作员")
					self.double.send_double_license_applicant(data)
					self.double.check_ico_len(data[1],data[2])
					self.loginElem.quit()
			except Exception as e:
				print ("same_termina_approvel fail: ") + str(e)
		self.log.log_end("same_termina_approvel")

	u'''双人审批申请人已下线审批过期'''
	def termina_expired_approvel_003(self):

		#日志开始记录
		self.log.log_start("Expired_approvel")
		#获取双人审批申请的数据
		dobData = self.get_double_data("double_license_sso")
		expData = self.get_double_data("termina_approvel")

		for dataRow in range(len(dobData)):
			data = dobData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow == 2:
					self.acproval.user_login(data[6])
					self.double.send_double_license_applicant(data)
					number = self.acproval.get_new_process_number()
					self.loginElem.quit()
					self.double.approver_by_process_approval(expData, number)
			except Exception as e:
				print ("Expired_approvel fail: ") + str(e)
		self.log.log_end("Expired_approvel")

	u'''双人审批审批人拒绝申请'''
	def termina_deny_approvel_004(self):

		#日志开始记录
		self.log.log_start("deny_double_approvel")
		#获取双人审批申请的数据
		dobData = self.get_double_data("double_license_sso")
		expData = self.get_double_data("deny_approvel")

		for dataRow in range(len(dobData)):
			data = dobData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow == 2:
					self.acproval.user_login(data[6])
					self.double.send_double_license_applicant(data)
					number = self.acproval.get_new_process_number()
					self.double.approver_remote_approval(expData, number)
					self.cmf.select_menu(u"运维操作", u"SSO")
					self.double.check_ico_len(data[1],data[2])
					self.loginElem.quit()
			except Exception as e:
				print ("deny_double_approvel fail: ") + str(e)
		self.log.log_end("deny_double_approvel")

	u'''双人审批审批人同意申请'''
	def termina_agree_approvel_005(self):

		#日志开始记录
		self.log.log_start("agree_double_approvel")
		#获取双人审批申请的数据
		dobData = self.get_double_data("double_license_sso")
		expData = self.get_double_data("agree_approvel")

		for dataRow in range(len(dobData)):
			data = dobData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow == 2:
					self.acproval.user_login(data[6])
					self.double.send_double_license_applicant(data)
					number = self.acproval.get_new_process_number()
					self.double.approver_remote_approval(expData, number)
					self.cmf.select_menu(u"运维操作", u"SSO")
					self.double.check_ico_len(data[1],data[2])
					self.loginElem.quit()
			except Exception as e:
				print ("agree_double_approvel fail: ") + str(e)
		self.log.log_end("agree_double_approvel")

	u'''访问审批流程任务查询'''
	def double_query_process_task_006(self):
		#日志开始记录
		self.log.log_start("double_query_process_task")
		#获取流程任务查询的数据
		taskData = self.get_double_data("process_task")

		for dataRow in range(len(taskData)):
			data = taskData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					if dataRow == 1:
						self.acproval.user_login(data[1])
					self.flow.query_process_task(data)
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("double_query_process_task fail: ") + str(e)
		self.log.log_end("double_query_process_task")

	u'''访问审批个人历史查询'''
	def double_query_personal_history_007(self):
		#日志开始记录
		self.log.log_start("double_query_personal_history")
		#获取个人历史查询的数据
		perData = self.get_double_data("personal_history")

		for dataRow in range(len(perData)):
			data = perData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					self.flow.query_personal_history(data)
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("double_query_personal_history fail: ") + str(e)
		self.loginElem.quit()
		self.log.log_end("double_query_personal_history")

	u'''访问审批申请历史查询'''
	def double_query_apply_history_008(self):
		#日志开始记录
		self.log.log_start("double_query_apply_history")
		#获取申请历史查询的数据
		applyData = self.get_double_data("apply_history")

		for dataRow in range(len(applyData)):
			data = applyData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					if dataRow == 1:
						self.acproval.user_login(data[9])
					self.flow.query_apply_history(data)
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("double_query_apply_history fail: ") + str(e)
		self.loginElem.quit()
		self.log.log_end("double_query_apply_history")

	u'''访问审批全部历史查询'''
	def double_query_all_history_009(self):
		#日志开始记录
		self.log.log_start("double_query_all_history")
		#获取全部历史查询的数据
		allData = self.get_double_data("all_history")

		for dataRow in range(len(allData)):
			data = allData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					if dataRow == 1:
						self.acproval.user_login(data[12])
					self.flow.query_all_history(data)
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("double_query_all_history fail: ") + str(e)
		self.log.log_end("double_query_all_history")