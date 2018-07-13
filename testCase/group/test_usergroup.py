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
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName
sys.path.append("/testIsompSecret/common")
from _icommon import commonFun,frameElement
from _log import log
sys.path.append("/testIsompSecret/webElement/department/")
from test_dptm_ment import Department
sys.path.append("/testIsompSecret/webElement/group/")
from test_regroup_ment import Regroup
from test_usergroup_ment import Usergroup

class testUsergroup(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.frameElem = frameElement(driver)
		self.regroup = Regroup(driver)
		self.dptment = Department(driver)
		self.usergroup = Usergroup(driver)

	u'''获取测试数据
	   Parameters:
	      - sheetname:sheet名称
	   return：表格数据
	'''
	def get_usergroup_data(self, sheetname):
		dataFile = dataFileName()
		usergrPath = dataFile.get_usergroup_test_data_url()
		usergrData = dataFile.get_data(usergrPath, sheetname)
		return usergrData

	u'''添加和编辑用户组'''
	def add_edit_usergroup_001(self):

		#日志开始记录
		self.log.log_start("add_edit_usergroup")
		#获取添加用户组测试数据
		usergrData = self.get_usergroup_data("add_edit_usergroup")
		#保存成功的弹出框
		usergrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		self.usergroup.click_left_usergroup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		#页面弹出框的文本信息
		pagetext = u"消息"

		#点击展开按钮
		self.usergroup.click_usergroup_switch()

		for dataRow in range(len(usergrData)):
			data = usergrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.usergroup.usergroup_click_basic_operation(int(data[4]), data[2], data[3])
					self.dptment.popup_sendkey(data[5])
					self.dptment.click_ok_button()
					time.sleep(3)
					self.frameElem.switch_to_content()
					self.dptment.multil_div_check_point("xpath", usergrMsg, data, flag, pagetext)
			except Exception as e:
				print ("add_edit_usergroup fail:" + str(e))

		self.log.log_end("add_edit_usergroup")

	u'''上移和下移用户组'''
	def up_down_usergroup_002(self):

		#日志开始记录
		self.log.log_start("up_down_usergroup")
		#获取上移用户组测试数据
		usergrData = self.get_usergroup_data("up_down_usergroup")

		self.usergroup.click_left_usergroup()

		#点击展开按钮
		self.usergroup.click_usergroup_switch()

		for dataRow in range(len(usergrData)):
			data = usergrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.usergroup.usergroup_click_basic_operation(int(data[4]), data[2], data[3])
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("up_down_usergroup fail:" + str(e))

		self.log.log_end("up_down_usergroup")

	u'''上移和下移用户组校验'''
	def up_down_usergroup_check_003(self):

		#日志开始记录
		self.log.log_start("up_down_usergroup_check")

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		#获取上移用户组测试数据
		usergrData = self.get_usergroup_data("up_down_usergroup")

		#保存成功的弹出框
		usergrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		self.usergroup.click_left_usergroup()

		#点击展开按钮
		self.usergroup.click_usergroup_switch()

		for dataRow in range(len(usergrData)):
			data = usergrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.usergroup.usergroup_click_up_down_check(int(data[4]), data[2], data[3])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", usergrMsg, data, flag)
			except Exception as e:
				print ("up_down_usergroup_check fail:" + str(e))

		self.log.log_end("up_down_usergroup_check")

	u'''检验添加和编辑用户组'''
	def check_add_edit_usergroup_004(self):

		#日志开始记录
		self.log.log_start("check_add_edit_usergroup")
		#获取检验添加用户组测试数据
		usergrData = self.get_usergroup_data("check_add_edit_usergroup")
		#保存成功的弹出框
		usergrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		#页面弹出框的文本信息
		pagetext = u"警告"

		self.usergroup.click_left_usergroup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		#点击展开按钮
		self.usergroup.click_usergroup_switch()

		for dataRow in range(len(usergrData)):
			data = usergrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.usergroup.usergroup_click_basic_operation(int(data[4]), data[2], data[3])
					if dataRow != 1 and dataRow != 2:
						self.dptment.popup_sendkey(data[5])

					if dataRow == 2:
						self.dptment.clear_depart_text()

					self.dptment.click_ok_button()
					self.frameElem.switch_to_content()
					self.dptment.multil_div_check_point("xpath", usergrMsg, data, flag, pagetext)
					self.driver.implicitly_wait(20)
					self.frameElem.switch_to_content()
					self.dptment.click_cancel_button()
			except Exception as e:
				print ("check_add_edit_usergroup fail:" + str(e))

		self.log.log_end("check_add_edit_usergroup")

	u'''删除用户组'''
	def del_usergroup_005(self):

		#日志开始记录
		self.log.log_start("del_usergroup")
		#删除的弹出框
		usergrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#获取删除用户组测试数据
		usergrData = self.get_usergroup_data("del_usergroup")

		self.usergroup.click_left_usergroup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		#点击展开按钮
		self.usergroup.click_usergroup_switch()

		for dataRow in range(len(usergrData)):
			data = usergrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.usergroup.usergroup_click_basic_operation(int(data[4]), data[2], data[3])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", usergrMsg, data, flag)
					self.frameElem.switch_to_content()
					self.cmf.click_msg_button(1)
			except Exception as e:
				print ("del_usergroup fail:" + str(e))

		self.log.log_end("del_usergroup")

	u'''用户组中添加用户'''
	def usergroup_add_user_001(self):

		#日志开始记录
		self.log.log_start("usergroup_add_user")
		#获取添加用户组测试数据
		usergrData = self.get_usergroup_data("usergroup_add_user")
		#保存成功的弹出框
		usergrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		self.usergroup.click_left_usergroup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		#点击展开按钮
		self.usergroup.click_usergroup_switch()

		for dataRow in range(len(usergrData)):
			data = usergrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					time.sleep(3)
					self.usergroup.click_usergroup_add_user(data[3], data[2])
					self.regroup.check_depart(data[4])
					self.usergroup.click_usergroup_add_user_query()
					self.regroup.check_all_resource()
					self.regroup.click_resource_okbutton()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", usergrMsg, data, flag)
			except Exception as e:
				print ("usergroup_add_user fail:" + str(e))

		self.log.log_end("usergroup_add_user")

	u'''用户组中查询用户账号/名称'''
	def query_usergroup_002(self):

		#日志开始记录
		self.log.log_start("query_usergroup")
		self.usergroup.click_left_usergroup()

		#点击展开按钮
		self.usergroup.click_usergroup_switch()

		#获取查询用户组测试数据
		usergrData = self.get_usergroup_data("query_usergroup")

		for dataRow in range(len(usergrData)):
			data = usergrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if dataRow == 1:
						#选中用户组
						self.dptment.click_basic_operation_public_method(data[2], "user_group_", "_span")
						self.regroup.click_regroup_reset()
					else:
						self.usergroup.set_username(data[3])

					self.usergroup.click_usergroup_query()
					self.regroup.click_regroup_reset()
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("query_usergroup fail:" + str(e))

		self.log.log_end("query_usergroup")

	u'''用户组删除用户'''
	def usergroup_del_user_003(self):

		#日志开始记录
		self.log.log_start("usergroup_del_user")
		#删除的弹出框
		usergrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#获取删除用户组测试数据
		usergrData = self.get_usergroup_data("usergroup_del_user")

		self.usergroup.click_left_usergroup()

		#点击展开按钮
		self.usergroup.click_usergroup_switch()
		flag = False

		for dataRow in range(len(usergrData)):
			data = usergrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.usergroup.click_usergroup_del_user(data[3], data[4])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", usergrMsg, data, flag)
					self.frameElem.switch_to_content()
					self.cmf.click_msg_button(1)
			except Exception as e:
				print ("usergroup_del_user fail:" + str(e))

		self.log.log_end("usergroup_del_user")

	u'''用户组全选删除用户'''
	def usergroup_bulk_user_004(self):

		#日志开始记录
		self.log.log_start("usergroup_bulk_user")
		#删除的弹出框
		usergrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#获取删除用户组测试数据
		usergrData = self.get_usergroup_data("usergroup_bulk_user")
		self.usergroup.click_left_usergroup()

		#点击展开按钮
		self.usergroup.click_usergroup_switch()

		flag = False

		for dataRow in range(len(usergrData)):
			data = usergrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.usergroup.click_usergroup_bulk_user(data[3])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", usergrMsg, data, flag)
					self.frameElem.switch_to_content()
					self.cmf.click_msg_button(1)
			except Exception as e:
				print ("usergroup_bulk_user fail:" + str(e))

		self.log.log_end("usergroup_bulk_user")

