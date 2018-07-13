#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2018/1/11
#模块描述：资源时间规则
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
from _icommon import commonFun,frameElement
from _log import log
sys.path.append("/testIsompSecret/webElement/rule")
from test_command_rule_ment import CommandRule
from test_time_rule_ment import TimeRule
from test_resource_time_rule_ment import RetimeRule
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import CommonSuiteData
sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

class testRetime(object):

	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.frameElem = frameElement(driver)
		self.command = CommandRule(driver)
		self.comsuit = CommonSuiteData(driver)
		self.timerule = TimeRule(driver)
		self.retime = RetimeRule(driver)
		self.loginElem = loginPage(driver)

	u'''提示内容框元素路径'''
	def div_msg(self):
		div_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		return div_msg

	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
		return：表格数据
	'''
	def get_table_data(self, sheetname):
		dataFile = dataFileName()
		retrulePath = dataFile.get_retime_test_data_url()
		retruleData = dataFile.get_data(retrulePath, sheetname)
		return retruleData

	u'''添加资源时间规则'''
	def add_retime_rule_001(self):

		#日志开始记录
		self.log.log_start("add_retime_rule")
		#获取添加资源时间规则测试数据
		retruleData = self.get_table_data("add_retime_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(retruleData)):
			data = retruleData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.command.click_add_button()
					if dataRow == 3:
						self.retime.click_running_state()
					self.timerule.start_date(data[2])
					self.timerule.date_of_termination(data[4], data[5])
					self.retime.set_month_start_time(data[6])
					self.retime.set_month_end_time(data[7])
					self.retime.set_week_start_time(data[8])
					self.retime.set_week_end_time(data[9])
					self.retime.set_day_start_time(data[10])
					self.retime.set_day_end_time(data[11])
					self.retime.select_action(data[12])
					self.command.click_add_users_button()
					self.command.check_all_user()
					self.command.click_add_resource_button()
					self.retime.check_resource(data[13])
					self.retime.click_save_retime()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
					self.command.click_back_command()
			except Exception as e:
				print ("add_retime_rule fail:" + str(e))
		self.log.log_end("add_retime_rule")

	u'''编辑资源时间规则'''
	def mod_retime_rule_002(self):

		#日志开始记录
		self.log.log_start("mod_retime_rule")
		#获取编辑资源时间规则测试数据
		retruleData = self.get_table_data("mod_retime_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(retruleData)):
			data = retruleData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.retime.click_option_method(data[2], data[3])
					self.retime.select_action(data[4])
					self.retime.click_save_retime()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
					self.command.click_back_command()
			except Exception as e:
				print ("mod_retime_rule fail:" + str(e))

		self.log.log_end("mod_retime_rule")

	u'''资源时间规则结果'''
	def add_retime_rule_result_003(self):

		#日志开始记录
		self.log.log_start("add_retime_rule_result")
		#获取资源时间审批测试数据
		retruleData = self.get_table_data("add_retime_rule_result")
		for dataRow in range(len(retruleData)):
			data = retruleData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if dataRow == 1:
						self.comsuit.user_quit()
						self.loginElem.login(data)
						self.frameElem.from_frame_to_otherFrame("topFrame")
						self.cmf.select_role_by_text(u"运维操作员")
					self.retime.check_resource_time_rule(data)
			except Exception as e:
				print ("add_retime_rule_result fail:" + str(e))

		self.comsuit.user_quit()
		self.log.log_end("add_retime_rule_result")

	u'''操作资源时间规则'''
	def option_retime_rule_004(self):
		self.comsuit.login_secadmin()
		self.comsuit.switch_to_moudle(u"运维管理", u"规则定义")
		self.command.click_left_rule(3)

		#日志开始记录
		self.log.log_start("option_retime_rule")
		#获取操作资源时间规则测试数据
		retruleData = self.get_table_data("option_retime_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(retruleData)):
			data = retruleData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if dataRow == 1:
						self.retime.click_bulkdel_retime()
					elif dataRow == 2 or dataRow == 3:
						self.retime.click_option_method(data[2], data[3])
					elif dataRow == 4 or dataRow == 5:
						time.sleep(5)
						self.retime.click_option_method(data[2], data[3])
						self.command.set_row_command(data[4])
						self.command.check_sure_button()
						self.frameElem.switch_to_content()
						self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
						time.sleep(3)
						self.command.click_cancel_button()
						continue
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
			except Exception as e:
				print ("option_retime_rule fail:" + str(e))

		self.log.log_end("option_retime_rule")

	u'''校验资源时间规则'''
	def check_retime_rule_005(self):

		#日志开始记录
		self.log.log_start("check_retime_rule")
		#获取校验资源时间规则测试数据
		retruleData = self.get_table_data("check_retime_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()
		self.command.click_add_button()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(retruleData)):
			data = retruleData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if 2 <= dataRow <= 4:
						if dataRow != 4:
							self.timerule.start_date(data[2], data[3])
						else:
							self.timerule.start_date(data[2])
						if dataRow != 2:
							self.timerule.date_of_termination(data[4], data[5])
					elif 5 <= dataRow <= 11:
						if dataRow == 5:
							self.timerule.date_of_termination(data[4], data[5])
						self.retime.set_month_start_time(data[6])
						self.retime.set_month_end_time(data[7])
						if dataRow == 11:
							self.retime.set_day_start_time(data[8])
					elif 12 <= dataRow <= 17:
						self.retime.set_day_start_time(data[8])
						self.retime.set_day_end_time(data[9])
					elif dataRow == 18:
						self.command.click_add_users_button()
						self.command.check_all_user()
					self.retime.click_save_retime()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
			except Exception as e:
				print ("check_retime_rule fail:" + str(e))

		self.command.click_back_command()
		self.log.log_end("check_retime_rule")

	u'''删除资源时间规则'''
	def del_retime_rule_006(self):
		#日志开始记录
		self.log.log_start("del_retime_rule")
		#获取删除资源时间规则测试数据
		retruleData = self.get_table_data("del_retime_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(retruleData)):
			data = retruleData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.retime.click_option_method(data[2], data[3])
					self.retime.click_bulkdel_retime()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
					self.cmf.click_login_msg_button()
			except Exception as e:
				print ("del_retime_rule fail:" + str(e))
		self.log.log_end("del_retime_rule")