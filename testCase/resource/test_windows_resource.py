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
sys.path.append("/testIsompSecret/webElement/resource/")
from test_resource_common import Resource
from test_windows_ment import WindowsResource

class testWindowsResource(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.frameElem = frameElement(driver)
		self.resource = Resource(driver)
		self.window = WindowsResource(driver)

	u'''提示内容框元素路径'''
	def div_msg(self):
		div_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		return div_msg

	u'''获取测试数据
	   Parameters:
	      - sheetname:sheet名称
	   return：表格数据
	'''
	def get_windows_table_data(self, sheetname):
		dataFile = dataFileName()
		windowsPath = dataFile.get_windows_resource_test_data_url()
		windowsData = dataFile.get_data(windowsPath, sheetname)
		return windowsData

	u'''添加windows资源'''
	def add_windows_resource_001(self):

		#日志开始记录
		self.log.log_start("add_windows_resource")
		#获取添加windows资源测试数据
		windowsData = self.get_windows_table_data("add_windows_resource")
		#保存成功的弹出框
		windowsMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(windowsData)):
			data = windowsData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.resource.click_add_edit_button()
					self.resource.select_resource_type(data[2])
					self.window.add_edit_windows_resource(data)
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", windowsMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("add_windows_resource fail:" + str(e))

		self.log.log_end("add_windows_resource")

	u'''编辑windows资源'''
	def edit_windows_resource_002(self):

		#日志开始记录
		self.log.log_start("edit_windows_resource")
		#获取编辑windows资源测试数据
		windowsData = self.get_windows_table_data("edit_windows_resource")
		#保存成功的弹出框
		windowsMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(windowsData)):
			data = windowsData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.resource.click_add_edit_button(data[2])
					self.window.add_edit_windows_resource(data)
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", windowsMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("edit_windows_resource fail:" + str(e))

		self.log.log_end("edit_windows_resource")

	u'''检验windows资源'''
	def check_windows_resource_003(self):

		#日志开始记录
		self.log.log_start("check_windows_resource")
		#获取校验windows资源测试数据
		windowsData = self.get_windows_table_data("check_windows_resource")
		#保存成功的弹出框
		windowsMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		#点击添加按钮
		self.resource.click_add_edit_button()
		#选择windows类型
		self.resource.select_resource_type("Windows Server 2008")

		for dataRow in range(len(windowsData)):
			data = windowsData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.window.check_windows_resource(dataRow, data)
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", windowsMsg, data, flag)
			except Exception as e:
				print ("check_windows_resource fail:" + str(e))
		time.sleep(5)
		self.cmf.back()

		self.log.log_end("check_windows_resource")