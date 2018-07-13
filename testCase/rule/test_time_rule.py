#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/9/1
#模块描述：时间规则
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName
sys.path.append("/testIsompSecret/common")
from _icommon import commonFun,frameElement,getElement
from _log import log
sys.path.append("/testIsompSecret/webElement/rule")
from test_command_rule_ment import CommandRule
from test_time_rule_ment import TimeRule
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import CommonSuiteData
sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

class testTime(object):

	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.frameElem = frameElement(driver)
		self.command = CommandRule(driver)
		self.comsuit = CommonSuiteData(driver)
		self.timerule = TimeRule(driver)
		self.getElem = getElement(driver)
		self.loginElem = loginPage(self.driver)

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
		timerulPath = dataFile.get_timerule_test_data_url()
		timerulData = dataFile.get_data(timerulPath, sheetname)
		return timerulData

	u'''添加时间规则'''
	def add_time_rule_001(self):

		#日志开始记录
		self.log.log_start("add_time_rule")
		#获取添加时间规则测试数据
		timerulData = self.get_table_data("add_time_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(timerulData)):
			data = timerulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.command.click_add_button()
					self.timerule.set_rulename((data[2]))
					self.timerule.select_depart(data[3])
					self.timerule.start_date(data[4])
					self.timerule.date_of_termination(data[6], data[7])
					self.timerule.set_status_type(data[8])
					self.timerule.set_time(data[9], data[10], data[11])
					self.timerule.set_descrip(data[12])
					self.timerule.click_save_time()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
					self.command.click_back_command()
			except Exception as e:
				print ("add_time_rule fail:" + str(e))
		self.comsuit.user_quit()
		self.log.log_end("add_time_rule")

	u'''添加时间规则结果'''
	def add_time_rule_result_002(self):

		#日志开始记录
		self.log.log_start("add_time_rule_result")
		#获取添加时间规则测试数据
		timerulData = self.get_table_data("add_time_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(timerulData)):
			data = timerulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.comsuit.login_secadmin()
					self.comsuit.switch_to_moudle(u'运维管理', u'用户')
					self.timerule.edit_user_time_rule(data[13], data[14])

					list = [data[15], data[16], data[17], data[18], data[19]]
					self.comsuit.user_quit()
					self.loginElem.login(list)
					self.frameElem.from_frame_to_otherFrame("topFrame")
					if self.getElem.is_element_exsit('id', "logout"):
						self.comsuit.user_quit()
					else:
						self.cmf.click_login_msg_button()
					flag = True
					self.cmf.test_win_check_point("xpath", comrulMsg, list, flag)
			except Exception as e:
				print ("add_time_rule_result fail:" + str(e))
		self.comsuit.login_secadmin()
		self.comsuit.switch_to_moudle(u'运维管理', u'规则定义')
		self.command.click_left_rule(1)
		self.log.log_end("add_time_rule_result")

	u'''编辑时间规则'''
	def mod_time_rule_003(self):
		#日志开始记录
		self.log.log_start("mod_time_rule")
		#获取编辑时间规则测试数据
		timerulData = self.get_table_data("mod_time_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(timerulData)):
			data = timerulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.timerule.click_edit_time(data[2])
					self.timerule.set_rulename((data[3]))
					self.timerule.start_date(data[4])
					self.timerule.date_of_termination(data[5], data[6])
					self.timerule.set_status_type(data[7])
					self.timerule.deselect_time(data[8], data[9], data[10])
					self.timerule.set_time(data[11], data[12], data[13])
					self.timerule.set_descrip(data[14])
					self.timerule.click_save_time()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
					self.command.click_back_command()
			except Exception as e:
				print ("mod_time_rule fail:" + str(e))
		self.log.log_end("mod_time_rule")

	u'''校验时间规则'''
	def check_time_rule_004(self):
		#日志开始记录
		self.log.log_start("check_time_rule")
		#获取校验时间规则测试数据
		timerulData = self.get_table_data("check_time_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		self.command.click_add_button()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(timerulData)):
			data = timerulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 2 or dataRow == 3:
					self.timerule.set_rulename((data[2]))
				elif dataRow == 4:
					self.timerule.select_depart(data[3])
				elif dataRow == 5:
					self.timerule.start_date(data[4], data[5])
				elif dataRow == 6:
					self.timerule.date_of_termination(data[6], data[7])
				elif dataRow == 7:
					self.timerule.start_date(data[4])
				elif dataRow == 8 or dataRow == 9:
					self.timerule.set_time(data[8], data[9], data[10])
				if dataRow != 0:
					self.timerule.click_save_time()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
			except Exception as e:
				print ("check_time_rule fail:" + str(e))
		self.command.click_back_command()
		self.log.log_end("check_time_rule")

	u'''检索时间规则'''
	def query_time_rule_005(self):
		#日志开始记录
		self.log.log_start("query_time_rule")
		#获取检索时间规则测试数据
		timerulData = self.get_table_data("query_time_rule")

		for dataRow in range(len(timerulData)):
			data = timerulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.timerule.click_reset_time()
					if dataRow != 4:
						self.timerule.set_search_timename((data[1]))
					self.timerule.click_search_time()
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("query_time_rule fail:" + str(e))
		self.log.log_end("query_time_rule")

	u'''删除时间规则'''
	def del_time_rule_006(self):
		#日志开始记录
		self.log.log_start("del_time_rule")
		#获取删除时间规则测试数据
		timerulData = self.get_table_data("del_time_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(timerulData)):
			data = timerulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if dataRow == 1:
						self.timerule.click_bulkdel_time()
						self.cmf.click_login_msg_button()
						self.log.log_detail(data[0],True)
					else:
						self.timerule.click_del_time(data[2])
						self.frameElem.switch_to_content()
						self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
						self.cmf.click_login_msg_button()
			except Exception as e:
				print ("del_time_rule fail:" + str(e))
		self.log.log_end("del_time_rule")