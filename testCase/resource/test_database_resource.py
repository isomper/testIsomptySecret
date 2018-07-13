#coding=utf-8
''' 
#文件名：
#作者：
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
import time

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName
sys.path.append("/testIsompSecret/common")
from _icommon import commonFun,frameElement,getElement
from _log import log
sys.path.append("/testIsompSecret/webElement/resource/")
from test_resource_common import Resource
from databaseElement import DatabaseResource
sys.path.append("/testIsompSecret/testSuite")


class testDatabaseResource(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.frameElem = frameElement(driver)
		self.resource = Resource(driver)
		self.database = DatabaseResource(driver)

	u'''提示内容框元素路径'''
	def div_msg(self):
		div_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		return div_msg

	u'''获取测试数据
	   Parameters:
	      - sheetname:sheet名称
	   return：表格数据
	'''
	def get_database_table_data(self, sheetname):
		dataFile = dataFileName()
		databasePath = dataFile.get_database_test_url()
		databaseData = dataFile.get_data(databasePath, sheetname)
		return databaseData

	u'''添加database资源'''
	def add_database_resource_001(self):

		#日志开始记录
		self.log.log_start("add_database_resource")
		#获取添加windows资源测试数据
		databaseData = self.get_database_table_data("add_database_resource")
		#保存成功的弹出框
		windowsMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(databaseData)):
			data = databaseData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.resource.click_add_edit_button()
					self.resource.select_resource_type(data[2])
					self.database.add_edit_database_resource(data)
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", windowsMsg, data, flag)
					time.sleep(2)
					self.cmf.back()
			except Exception as e:
				print ("add_database_resource fail:" + str(e))

		self.log.log_end("add_database_resource")

	u'''编辑database资源'''
	def edit_database_resource_002(self):

		#日志开始记录
		self.log.log_start("edit_database_resource")
		#获取编辑windows资源测试数据
		databaseData = self.get_database_table_data("edit_database_resource")
		#保存成功的弹出框
		windowsMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(databaseData)):
			data = databaseData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.resource.click_add_edit_button(data[2])
					self.database.add_edit_database_resource(data)
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", windowsMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("edit_database_resource fail:" + str(e))

		self.log.log_end("edit_database_resource")
	
	'''数据库校验'''
	def check_database_resource_003(self):
		#日志开始记录
		self.log.log_start("check_database_resource")
		#获取编辑windows资源测试数据
		databaseData = self.get_database_table_data("check_database_resource")
		#保存成功的弹出框
		windowsMsg = self.div_msg()
		
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		#点击添加按钮
		self.resource.click_add_edit_button()
		#选择windows类型
		self.resource.select_resource_type("Oracle10g")	
		
		for dataRow in range(len(databaseData)):
			data = databaseData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					#资源名称
					self.database.set_resource_name(data[2])				
					self.database.set_resource_ip(data[3])
					self.database.set_database_name(data[4])
					self.database.set_service_name(data[5])
					if data[6] != "":
						self.database.select_protocol(data[6])
					if data[7] !="":
						self.database.select_application(data[7])
					
					self.resource.resoure_save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", windowsMsg, data, flag)
					
			except Exception as e:
				print ("check_database_resource fail:" + str(e))
		self.cmf.back()
		self.database.is_pop_up()			
		self.log.log_end("check_database_resource")