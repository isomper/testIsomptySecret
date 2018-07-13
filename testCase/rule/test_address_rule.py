#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：地址规则
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
from test_address_rule_ment import AddressRule
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import CommonSuiteData
sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

class testAddress(object):

	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.frameElem = frameElement(driver)
		self.command = CommandRule(driver)
		self.comsuit = CommonSuiteData(driver)
		self.timerule = TimeRule(driver)
		self.getElem = getElement(driver)
		self.loginElem = loginPage(driver)
		self.adrerule = AddressRule(driver)

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
		adrerulePath = dataFile.get_adrerule_test_data_url()
		adreruleData = dataFile.get_data(adrerulePath, sheetname)
		return adreruleData

	u'''添加地址规则'''
	def add_address_rule_001(self):

		#日志开始记录
		self.log.log_start("add_address_rule")
		#获取添加地址规则测试数据
		adreruleData = self.get_table_data("add_address_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(adreruleData)):
			data = adreruleData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.command.click_add_button()
					self.adrerule.set_rulename((data[2]))
					self.timerule.select_depart(data[3])
					self.timerule.set_status_type(data[4])
					self.adrerule.checkbox_ip_rule(data[5])
					self.adrerule.set_ip(data[6])
					self.adrerule.set_ip_mask(data[7])
					if dataRow != 1 and dataRow != 5:
						if dataRow == 3 or dataRow == 7:
							self.adrerule.click_add_ip_segment()
						self.adrerule.set_ip_start(data[9])
						self.adrerule.set_ip_end(data[10])
					else:
						self.adrerule.set_ip_test(data[8])
						self.adrerule.click_test()
						self.cmf.click_msg_button(1)
					self.adrerule.set_description(data[11])
					self.adrerule.click_save()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
					self.command.click_back_command()
			except Exception as e:
				print ("add_address_rule fail:" + str(e))
		self.comsuit.user_quit()
		self.log.log_end("add_address_rule")

	u'''添加地址规则结果'''
	def add_address_rule_result_002(self):

		#日志开始记录
		self.log.log_start("add_address_rule_result")
		#获取添加地址规则测试数据
		adreruleData = self.get_table_data("add_address_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		for dataRow in range(len(adreruleData)):
			data = adreruleData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.comsuit.login_secadmin()
					self.comsuit.switch_to_moudle(u'运维管理', u'用户')
					self.adrerule.edit_user_address_rule(data[12], data[13])
					self.comsuit.user_quit()
					list = [data[14], data[15], data[16], data[17], data[18]]
					self.loginElem.login(list)
					self.frameElem.from_frame_to_otherFrame("topFrame")
					if self.getElem.is_element_exsit('id', "logout"):
						self.comsuit.user_quit()
					flag = True
					self.cmf.test_win_check_point("xpath", comrulMsg, list, flag)
			except Exception as e:
				print ("add_address_rule_result fail:" + str(e))
		self.comsuit.login_secadmin()
		self.comsuit.switch_to_moudle(u'运维管理', u'规则定义')
		self.command.click_left_rule(2)
		self.log.log_end("add_address_rule_result")

	u'''编辑地址规则'''
	def mod_address_rule_003(self):
		#日志开始记录
		self.log.log_start("mod_address_rule")
		#获取编辑地址规则测试数据
		adreruleData = self.get_table_data("mod_address_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(adreruleData)):
			data = adreruleData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.adrerule.click_edit_address(data[2])
					self.adrerule.set_rulename((data[3]))
					self.timerule.set_status_type(data[4])
					self.adrerule.checkbox_ip_rule(data[5])
					self.adrerule.set_ip(data[6])
					self.adrerule.set_ip_mask(data[7])
					self.adrerule.set_ip_start(data[8])
					self.adrerule.set_ip_end(data[9])
					self.adrerule.set_description(data[10])
					self.adrerule.click_save()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
					self.command.click_back_command()
			except Exception as e:
				print ("mod_address_rule fail:" + str(e))
		self.log.log_end("mod_address_rule")

	u'''校验地址规则'''
	def check_address_rule_004(self):
		#日志开始记录
		self.log.log_start("check_address_rule")
		#获取校验地址规则测试数据
		adreruleData = self.get_table_data("check_address_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()
		self.command.click_add_button()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(adreruleData)):
			data = adreruleData[dataRow]
			try:
				if dataRow != 0:
					#如果不是第一行标题，则读取数据
					if dataRow == 2:
						self.adrerule.checkbox_ip_rule(data[3])
					elif dataRow == 3 or dataRow == 4:
						self.adrerule.set_ip(data[4])
					elif dataRow == 5:
						self.adrerule.set_ip_mask(data[5])
					elif dataRow != 1:
						self.adrerule.set_rulename(data[2])
					self.adrerule.click_save()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)
			except Exception as e:
				print ("check_address_rule fail:" + str(e))
		self.command.click_back_command()
		self.log.log_end("check_address_rule")

	u'''检索地址规则'''
	def query_address_rule_005(self):
		#日志开始记录
		self.log.log_start("query_address_rule")
		#获取检索地址规则测试数据
		adreruleData = self.get_table_data("query_address_rule")

		for dataRow in range(len(adreruleData)):
			data = adreruleData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.timerule.click_reset_time()
					if dataRow != 4:
						self.adrerule.set_search_addressname((data[1]))
					self.adrerule.click_search_address()
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("query_address_rule fail:" + str(e))
		self.log.log_end("query_address_rule")

	u'''删除地址规则'''
	def del_address_rule_006(self):
		#日志开始记录
		self.log.log_start("del_address_rule")
		#获取删除地址规则测试数据
		adrerulData = self.get_table_data("del_address_rule")
		#保存成功的弹出框
		comrulMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(adrerulData)):
			data = adrerulData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if dataRow == 1:
						self.adrerule.click_bulkdel_address()
					else:
						self.adrerule.click_del_address(data[2])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", comrulMsg, data, flag)

					if dataRow != 1:
						self.cmf.click_login_msg_button()

			except Exception as e:
				print ("del_address_rule fail:" + str(e))
		self.log.log_end("del_address_rule")