#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：访问审批
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
sys.path.append("/testIsomp/common")
from _icommon import commonFun
from _log import log
sys.path.append("/testIsomp/webElement/process/")
from test_access_approval_ment import Accapproval
from test_process_common import Flowcontrol
sys.path.append("/testIsomp/webElement/authorization")
from authrizationElement import AuthorizationPage
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage


class testAccapproval(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.data = dataFileName()
		self.cmf = commonFun(driver)
		self.acproval = Accapproval(driver)
		self.loginElem = loginPage(self.driver)
		self.authElem = AuthorizationPage(self.driver)
		self.flow = Flowcontrol(self.driver)

	u'''获取测试数据
	   Parameters:
	      - sheetname:sheet名称
	   return：表格数据
	'''
	def get_accapproval_data(self, sheetname):
		dataFile = dataFileName()
		acpPath = dataFile.get_accapproval_test_data_url()
		acpData = dataFile.get_data(acpPath, sheetname)
		return acpData

	u'''添加访问审批'''
	def add_access_approvel_001(self):
		#日志开始记录
		self.log.log_start("add_access_approvel")
		#获取访问审批的数据
		acpData = self.get_accapproval_data("add_access_approvel")
		for dataRow in range(len(acpData)):
			data = acpData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					if dataRow == 1:
						self.acproval.click_access_approval_button(data[2])
						#设置开关状态
						self.authElem.set_switch_on()
					self.authElem.click_add_approval_level()
					self.authElem.click_add_approval(data[3])
					#添加审批人
					self.authElem.set_select_user_search_button()
					self.acproval.check_user(data[4])
					self.authElem.set_ok_button()
					#设置审批级别中的通过审批人个数
					self.acproval.select_approval_num(data[3], data[5])
			except Exception as e:
				print ("add_access_approvell fail: ") + str(e)

		self.log.log_detail(u"添加访问审批成功", True)
		#点击保存
		self.authElem.approval_save_button()
		self.cmf.click_login_msg_button()
		#点击返回
		self.authElem.approval_back_button()
		self.loginElem.quit()
		self.log.log_end("add_access_approvel")

	u'''访问审批通过流程控制拒绝审批'''
	def access_deny_approvel_002(self):
		#日志开始记录
		self.log.log_start("access_deny_approvel")
		#获取访问审批申请的数据
		appData = self.get_accapproval_data("access_approvel_sso")
		#获取访问审批审批的数据
		acpData = self.get_accapproval_data("deny_approvel")

		for dataRow in range(len(appData)):
			data = appData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					list = [data[9],data[10],data[11],data[12],data[13]]
					self.loginElem.login(list)
					self.cmf.select_role_by_text(u"运维操作员")
					self.acproval.send_access_approval_applicant(data)
					number = self.acproval.get_new_process_number()
					self.loginElem.quit()
					self.acproval.approval_by_approver(acpData, number)
			except Exception as e:
				print ("access_deny_approvel fail: ") + str(e)
		self.log.log_end("access_deny_approvel")

	u'''访问审批通过流程控制同意审批'''
	def access_agree_approvel_003(self):
		#日志开始记录
		self.log.log_start("access_agree_approvel")
		#获取访问审批申请的数据
		appData = self.get_accapproval_data("access_approvel_sso")
		#获取访问审批审批的数据
		acpData = self.get_accapproval_data("agree_approvel")

		for dataRow in range(len(appData)):
			data = appData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					list = [data[9],data[10],data[11],data[12],data[13]]
					self.loginElem.login(list)
					self.cmf.select_role_by_text(u"运维操作员")
					self.acproval.send_access_approval_applicant(data)
					number = self.acproval.get_new_process_number()
					self.loginElem.quit()
					self.acproval.approval_by_approver(acpData, number)
			except Exception as e:
				print ("access_agree_approvel fail: ") + str(e)
		self.log.log_end("access_agree_approvel")

	u'''紧急运维通过流程控制拒绝审批'''
	def urgent_deny_approvel_004(self):
		#日志开始记录
		self.log.log_start("urgent_deny_approvel")
		#获取访问审批申请的数据
		appData = self.get_accapproval_data("urgent_approvel")
		#获取访问审批审批的数据
		acpData = self.get_accapproval_data("deny_approvel")

		for dataRow in range(len(appData)):
			data = appData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					list = [data[4],data[5],data[6],data[7],data[8]]
					self.loginElem.login(list)
					self.cmf.select_role_by_text(u"运维操作员")
					self.acproval.send_urgent_operation_applicant(data)
					number = self.acproval.get_new_process_number()
					self.loginElem.quit()
					self.acproval.approval_by_approver(acpData, number)
			except Exception as e:
				print ("urgent_deny_approvel fail: ") + str(e)
		self.log.log_end("urgent_deny_approvel")

	u'''紧急运维通过流程控制同意审批'''
	def urgent_agree_approvel_005(self):

		#日志开始记录
		self.log.log_start("urgent_agree_approvel")
		#获取访问审批申请的数据
		appData = self.get_accapproval_data("urgent_approvel")
		#获取访问审批审批的数据
		acpData = self.get_accapproval_data("agree_urgent")

		for dataRow in range(len(appData)):
			data = appData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					list = [data[4],data[5],data[6],data[7],data[8]]
					self.loginElem.login(list)
					self.cmf.select_role_by_text(u"运维操作员")
					self.acproval.send_urgent_operation_applicant(data)
					number = self.acproval.get_new_process_number()
					self.loginElem.quit()
					self.acproval.approval_by_approver(acpData, number)
			except Exception as e:
				print ("urgent_agree_approvel fail: ") + str(e)
		self.log.log_end("urgent_agree_approvel")

	u'''访问审批流程任务查询'''
	def access_query_process_task_006(self):
		#日志开始记录
		self.log.log_start("access_query_process_task")
		#获取流程任务查询的数据
		taskData = self.get_accapproval_data("process_task")

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
				print ("access_query_process_task fail: ") + str(e)
		self.log.log_end("access_query_process_task")

	u'''访问审批个人历史查询'''
	def access_query_personal_history_007(self):
		#日志开始记录
		self.log.log_start("access_query_personal_history")
		#获取个人历史查询的数据
		perData = self.get_accapproval_data("personal_history")

		for dataRow in range(len(perData)):
			data = perData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					self.flow.query_personal_history(data)
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("access_query_personal_history fail: ") + str(e)
		self.loginElem.quit()
		self.log.log_end("access_query_personal_history")

	u'''访问审批申请历史查询'''
	def access_query_apply_history_008(self):
		#日志开始记录
		self.log.log_start("access_query_apply_history")
		#获取申请历史查询的数据
		applyData = self.get_accapproval_data("apply_history")

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
				print ("access_query_apply_history fail: ") + str(e)
		self.loginElem.quit()
		self.log.log_end("access_query_apply_history")

	u'''访问审批全部历史查询'''
	def access_query_all_history_009(self):
		#日志开始记录
		self.log.log_start("access_query_all_history")
		#获取全部历史查询的数据
		allData = self.get_accapproval_data("all_history")

		for dataRow in range(len(allData)):
			data = allData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					if dataRow ==1:
						self.acproval.user_login(data[1])
					self.flow.query_all_history(data)
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("access_query_all_history fail: ") + str(e)
		self.log.log_end("access_query_all_history")