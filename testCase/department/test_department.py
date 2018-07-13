#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/07/07
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

class testDepartment(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.frameElem = frameElement(driver)
		self.dptment = Department(driver)

	u'''获取测试数据
	   Parameters:
	      - sheetname:sheet名称
	   return：表格数据
	'''
	def get_dptmtable_data(self, sheetname):
		dataFile = dataFileName()
		dptmPath = dataFile.get_depart_test_data_url()
		dptmData = dataFile.get_data(dptmPath, sheetname)
		return dptmData

	u'''添加和编辑部门'''
	def add_edit_department_001(self):

		#日志开始记录
		self.log.log_start("add_edit_department")
		#获取添加部门测试数据
		dptmData = self.get_dptmtable_data("add_edit_department")
		#保存成功的弹出框
		dptmMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		self.dptment.click_left_department()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		#页面弹出框的文本信息
		pagetext = u"消息"

		#点击展开按钮
		self.dptment.click_dept_switch()

		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_basic_operation(data[2], int(data[3]))
					self.dptment.popup_sendkey(data[4])
					self.dptment.click_ok_button()
					time.sleep(3)
					self.frameElem.switch_to_content()
					self.dptment.multil_div_check_point("xpath", dptmMsg, data, flag, pagetext)
			except Exception as e:
				print ("add_edit_department fail:" + str(e))

		self.log.log_end("add_edit_department")

	u'''上移和下移部门'''
	def up_down_department_002(self):

		#日志开始记录
		self.log.log_start("up_down_department")
		#获取上移部门测试数据
		dptmData = self.get_dptmtable_data("up_down_department")

		self.dptment.click_left_department()

		#点击展开按钮
		self.dptment.click_dept_switch()

		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_basic_operation(data[2], int(data[3]))
					self.log.log_detail(data[0],True)
			except Exception as e:
				print ("up_down_department fail:" + str(e))

		self.log.log_end("up_down_department")

	u'''上移和下移部门校验'''
	def up_down_department_check_003(self):

		#日志开始记录
		self.log.log_start("up_down_department_check")
		dptmMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		#获取上移部门测试数据
		dptmData = self.get_dptmtable_data("up_down_department")

		self.dptment.click_left_department()
		self.dptment.click_dept_switch()

		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_up_button(data[2], int(data[3]))
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", dptmMsg, data, flag)
			except Exception as e:
				print ("up_down_department_check fail:" + str(e))

		self.log.log_end("up_down_department_check")

	u'''删除部门'''
	def del_department_005(self):

		#日志开始记录
		self.log.log_start("del_department")
		#删除的弹出框
		dptmMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#获取删除部门测试数据
		dptmData = self.get_dptmtable_data("del_department")

		self.dptment.click_left_department()
		flag = False

		#点击展开按钮
		self.dptment.click_dept_switch()

		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_basic_operation(data[2], int(data[3]))
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", dptmMsg, data, flag)
					self.frameElem.switch_to_content()
					self.cmf.click_msg_button(1)
			except Exception as e:
				print ("del_department fail:" + str(e))

		self.log.log_end("del_department")

	u'''检验添加和编辑部门'''
	def check_add_edit_department_004(self):

		#日志开始记录
		self.log.log_start("check_add_edit_department")
		#获取检验添加部门测试数据
		dptmData = self.get_dptmtable_data("check_add_edit_department")
		#保存成功的弹出框
		dptmMsg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		self.dptment.click_left_department()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		#页面弹出框的文本信息
		pagetext = u"警告"

		#点击展开按钮
		self.dptment.click_dept_switch()

		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_basic_operation(data[2], int(data[3]))
					if dataRow != 1 and dataRow != 6:
						self.dptment.popup_sendkey(data[4])

					if dataRow == 6:
						self.dptment.clear_depart_text()

					self.dptment.click_ok_button()
					self.frameElem.switch_to_content()
					self.dptment.multil_div_check_point("xpath", dptmMsg, data, flag, pagetext)
					self.driver.implicitly_wait(1)
					self.frameElem.switch_to_content()
					self.dptment.click_cancel_button()
			except Exception as e:
				print ("check_add_edit_department fail:" + str(e))

		self.log.log_end("check_add_edit_department")