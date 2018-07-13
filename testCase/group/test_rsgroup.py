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

class testRegroup(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.frameElem = frameElement(driver)
		self.regroup = Regroup(driver)
		self.dptment = Department(driver)

	u'''获取测试数据
	   Parameters:
	      - sheetname:sheet名称
	   return：表格数据
	'''
	def get_regroup_data(self, sheetname):
		dataFile = dataFileName()
		regrPath = dataFile.get_regroup_test_data_url()
		regrData = dataFile.get_data(regrPath, sheetname)
		return regrData

	u'''添加和编辑资源组'''
	def add_edit_regroup_001(self):

		#日志开始记录
		self.log.log_start("add_edit_regroup")
		#获取添加资源组测试数据
		regrData = self.get_regroup_data("add_edit_regroup")
		#保存成功的弹出框
		regrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		self.regroup.click_left_regroup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		#页面弹出框的文本信息
		pagetext = u"消息"

		#点击展开按钮
		self.regroup.click_regroup_switch()

		for dataRow in range(len(regrData)):
			data = regrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.regroup.regroup_click_basic_operation(int(data[4]), data[2], data[3])
					self.dptment.popup_sendkey(data[5])
					self.dptment.click_ok_button()
					time.sleep(2)
					self.frameElem.switch_to_content()
					self.dptment.multil_div_check_point("xpath", regrMsg, data, flag, pagetext)
			except Exception as e:
				print ("add_edit_regroup fail:" + str(e))

		self.log.log_end("add_edit_regroup")

	u'''上移和下移资源组'''
	def up_down_regroup_002(self):

		#日志开始记录
		self.log.log_start("up_down_regroup")
		#获取上移资源组测试数据
		regrData = self.get_regroup_data("up_down_regroup")

		self.regroup.click_left_regroup()

		#点击展开按钮
		self.regroup.click_regroup_switch()

		for dataRow in range(len(regrData)):
			data = regrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					time.sleep(2)
					self.regroup.regroup_click_basic_operation(int(data[4]), data[2], data[3])
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("up_down_regroup fail:" + str(e))

		self.log.log_end("up_down_regroup")

	u'''上移和下移资源组校验'''
	def up_down_regroup_check_003(self):

		#日志开始记录
		self.log.log_start("up_down_regroup_check")

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		#获取上移资源组测试数据
		regrData = self.get_regroup_data("up_down_regroup")

		#保存成功的弹出框
		regrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		self.regroup.click_left_regroup()
		#点击展开按钮
		self.regroup.click_regroup_switch()

		for dataRow in range(len(regrData)):
			data = regrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					time.sleep(2)
					self.regroup.regroup_click_up_down_check(int(data[4]), data[2], data[3])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", regrMsg, data, flag)
			except Exception as e:
				print ("up_down_regroup_check fail:" + str(e))

		self.log.log_end("up_down_regroup_check")

	u'''检验添加和编辑资源组'''
	def check_add_edit_regroup_004(self):

		#日志开始记录
		self.log.log_start("check_add_edit_regroup")
		#获取检验添加资源组测试数据
		regrData = self.get_regroup_data("check_add_edit_regroup")
		#保存成功的弹出框
		regrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		#页面弹出框的文本信息
		pagetext = u"警告"

		self.regroup.click_left_regroup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False

		#点击展开按钮
		self.regroup.click_regroup_switch()

		for dataRow in range(len(regrData)):
			data = regrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					time.sleep(2)
					self.regroup.regroup_click_basic_operation(int(data[4]), data[2], data[3])
					if dataRow != 1 and dataRow != 2:
						self.dptment.popup_sendkey(data[5])

					if dataRow == 2:
						self.dptment.clear_depart_text()

					self.dptment.click_ok_button()
					self.frameElem.switch_to_content()
					self.dptment.multil_div_check_point("xpath", regrMsg, data, flag, pagetext)
					time.sleep(2)
					self.frameElem.switch_to_content()
					self.dptment.click_cancel_button()
			except Exception as e:
				print ("check_add_edit_regroup fail:" + str(e))

		self.log.log_end("check_add_edit_regroup")

	u'''删除资源组'''
	def del_regroup_005(self):

		#日志开始记录
		self.log.log_start("del_regroup")
		#删除的弹出框
		regrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#获取删除资源组测试数据
		regrData = self.get_regroup_data("del_regroup")

		self.regroup.click_left_regroup()
		flag = False

		#点击展开按钮
		self.regroup.click_regroup_switch()

		for dataRow in range(len(regrData)):
			data = regrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.regroup.regroup_click_basic_operation(int(data[4]), data[2], data[3])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", regrMsg, data, flag)
					self.frameElem.switch_to_content()
					self.cmf.click_msg_button(1)
			except Exception as e:
				print ("del_regroup fail:" + str(e))

		self.log.log_end("del_regroup")

	u'''资源组中添加资源'''
	def regroup_add_resource_001(self):

		#日志开始记录
		self.log.log_start("regroup_add_resource")
		#获取添加资源组测试数据
		regrData = self.get_regroup_data("regroup_add_resource")
		#保存成功的弹出框
		regrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		self.regroup.click_left_regroup()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		#点击展开按钮
		self.regroup.click_regroup_switch()

		for dataRow in range(len(regrData)):
			data = regrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.regroup.click_regroup_add_resouce(data[3], data[2])
					self.regroup.check_depart(data[4])
					self.regroup.click_regroup_add_resouce_query()
					self.regroup.check_all_resource()
					self.regroup.click_resource_okbutton()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", regrMsg, data, flag)
			except Exception as e:
				print ("regroup_add_resource fail:" + str(e))

		self.log.log_end("regroup_add_resource")

	u'''资源组中查询资源名称和IP'''
	def query_regroup_002(self):

		#日志开始记录
		self.log.log_start("query_regroup")
		self.regroup.click_left_regroup()

		#点击展开按钮
		self.regroup.click_regroup_switch()

		#获取查询资源组测试数据
		regrData = self.get_regroup_data("query_regroup")

		for dataRow in range(len(regrData)):
			data = regrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if dataRow == 1:
						#选中资源组
						self.dptment.click_basic_operation_public_method(data[2], "resource_group_", "_span")
						self.regroup.click_regroup_reset()
					else:
						self.regroup.set_rename_ip(data[3])

					self.regroup.click_regroup_query()
					self.regroup.click_regroup_reset()
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("query_regroup fail:" + str(e))

		self.log.log_end("query_regroup")

	u'''资源组删除资源'''
	def regroup_del_resouce_003(self):

		#日志开始记录
		self.log.log_start("regroup_del_resouce")
		#删除的弹出框
		regrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#获取删除资源组测试数据
		regrData = self.get_regroup_data("regroup_del_resouce")

		self.regroup.click_left_regroup()
		flag = False

		#点击展开按钮
		self.regroup.click_regroup_switch()

		for dataRow in range(len(regrData)):
			data = regrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.regroup.click_regroup_del_resouce(data[3], data[4])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", regrMsg, data, flag)
					self.frameElem.switch_to_content()
					self.cmf.click_msg_button(1)
			except Exception as e:
				print ("regroup_del_resouce fail:" + str(e))

		self.log.log_end("regroup_del_resouce")

	u'''资源组全选删除资源'''
	def regroup_bulk_resouce_004(self):

		#日志开始记录
		self.log.log_start("regroup_bulk_resouce")
		#删除的弹出框
		regrMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#获取删除资源组测试数据
		regrData = self.get_regroup_data("regroup_bulk_resouce")

		self.regroup.click_left_regroup()
		flag = False

		#点击展开按钮
		self.regroup.click_regroup_switch()

		for dataRow in range(len(regrData)):
			data = regrData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.regroup.click_regroup_bulk_resouce(data[3])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", regrMsg, data, flag)
					self.frameElem.switch_to_content()
					self.cmf.click_msg_button(1)
			except Exception as e:
				print ("regroup_bulk_resouce fail:" + str(e))

		self.log.log_end("regroup_bulk_resouce")
