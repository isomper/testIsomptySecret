#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/8/25
#模块描述：命令规则
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
sys.path.append("/testIsompSecret/testCase/sso/")
from test_sso import testSso
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import CommonSuiteData

class testCommand(object):

	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.frameElem = frameElement(driver)
		self.command = CommandRule(driver)
		self.sso = testSso(driver)
		self.comsuit = CommonSuiteData(driver)

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
		comrulPath = dataFile.get_command_test_data_url()
		comrulData = dataFile.get_data(comrulPath, sheetname)
		return comrulData

	u'''添加命令规则'''
	def add_command_rule_001(self):

		#日志开始记录
		self.log.log_start("add_command_rule")
		#获取添加命令规则测试数据
		comrulData = self.get_table_data("add_command_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(comrulData)):
			data = comrulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.command.click_add_button()
					self.command.select_command_type((data[2]))
					self.command.set_command(data[3])
					self.command.click_add_command_button()
					self.command.set_test_command(data[4])
					self.command.click_test_command_button()
					self.cmf.click_login_msg_button()
					if int(data[2]) == 2:
						self.command.click_approver_command()
						self.command.check_all_user()
					self.command.click_add_users_button()
					self.command.check_all_user()
					self.command.click_add_resource_button()
					self.command.check_all_resource()
					self.command.click_save_command()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
					self.command.click_back_command()
			except Exception as e:
				print ("add_command_rule fail:" + str(e))

		self.log.log_end("add_command_rule")

	u'''编辑命令规则'''
	def mod_command_rule_002(self):

		#日志开始记录
		self.log.log_start("mod_command_rule")
		#获取编辑命令规则测试数据
		comrulData = self.get_table_data("mod_command_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(comrulData)):
			data = comrulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.command.click_action_public_command(data[2], data[3])
					self.command.set_command(data[4])
					self.command.click_add_command_button()
					self.command.click_save_command()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
					self.command.click_back_command()
			except Exception as e:
				print ("mod_command_rule fail:" + str(e))

		self.log.log_end("mod_command_rule")

	u'''操作命令规则'''
	def option_command_rule_003(self):

		#日志开始记录
		self.log.log_start("option_command_rule")
		#获取操作命令规则测试数据
		comrulData = self.get_table_data("option_command_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(comrulData)):
			data = comrulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if dataRow == 1:
						self.command.click_del_command()
					elif dataRow == 2:
						self.command.click_deploy_command()
					elif dataRow == 3 or dataRow == 4:
						self.command.click_action_public_command(data[2], data[3])
					elif dataRow == 5 or dataRow == 6:
						time.sleep(5)
						self.command.click_action_public_command(data[2], data[3])
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
				print ("option_command_rule fail:" + str(e))

		self.log.log_end("option_command_rule")

	u'''校验命令规则'''
	def check_command_rule_004(self):

		#日志开始记录
		self.log.log_start("check_command_rule")
		#获取校验命令规则测试数据
		comrulData = self.get_table_data("check_command_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()
		self.command.click_add_button()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(comrulData)):
			data = comrulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if data[2] != "no":
						self.command.select_command_type((data[2]))
					if data[3] != "no":
						self.command.set_command(data[3])
						self.command.click_add_command_button()
					if data[4] != "no":
						self.command.set_test_command(data[4])
						self.command.click_test_command_button()
					if dataRow == 4:
						self.command.click_save_command()
					elif dataRow == 5:
						self.command.click_add_users_button()
						self.command.check_all_user()
						self.command.click_save_command()
					elif dataRow == 6:
						self.command.click_add_resource_button()
						self.command.check_all_resource()
						self.command.click_save_command()
					elif dataRow == 7:
						self.command.click_approver_command()
						self.command.check_all_user()
						self.command.clear_command()
						self.command.click_save_command()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
			except Exception as e:
				print ("check_command_rule fail:" + str(e))

		self.command.click_back_command()
		self.log.log_end("check_command_rule")

	u'''命令审批'''
	def command_approval_005(self):
		self.frameElem.from_frame_to_otherFrame("topFrame")
		self.cmf.select_role_by_text(u"运维操作员")
		#日志开始记录
		self.log.log_start("command_approval")
		#获取命令审批测试数据
		comrulData = self.get_table_data("command_approval")
		for dataRow in range(len(comrulData)):
			data = comrulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.command.sso_command(data)
					handles = self.driver.window_handles
					if dataRow == 2:
						self.command.command_by_message_approval(data[6], data[7], data[8])
						self.cmf.click_login_msg_button()

					self.driver.switch_to.window(handles[1])
					self.driver.close()
					self.driver.switch_to.window(handles[0])

					#关闭浏览器
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("command_approval fail:" + str(e))
		self.log.log_end("command_approval")

	u'''删除命令规则'''
	def del_command_rule_006(self):
		# self.comsuit.sys_switch_to_dep()
		# self.comsuit.switch_to_moudle(u"运维管理", u"规则定义")
		#日志开始记录
		self.log.log_start("del_command_rule")
		#获取删除命令规则测试数据
		comrulData = self.get_table_data("del_command_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(comrulData)):
			data = comrulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.command.click_action_public_command(data[2], data[3])
					self.command.click_del_command()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
					self.cmf.click_login_msg_button()
			except Exception as e:
				print ("del_command_rule fail:" + str(e))
		self.log.log_end("del_command_rule")