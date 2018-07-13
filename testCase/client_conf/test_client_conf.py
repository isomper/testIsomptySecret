#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/client_conf")
from clientConfElement import ClientPage

class testClient():
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.cnEnde = cnEncode()
		self.clientElem = ClientPage(self.driver)
		self.tableElem = tableElement(self.driver)
		self.selectElem = selectElement(driver)
		self.dataFile = dataFileName()
		self.frameElem = frameElement(self.driver)
	
	u'''提示框元素路径'''
	def auth_msg(self):
		auth_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		return auth_msg

	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
			return：表格数据
	'''
	def get_table_data(self,sheetname):
		dataFile = dataFileName()
		filePath = dataFile.get_client_test_data_url()
		authFileData = dataFile.get_data(filePath,sheetname)
		return authFileData
	
	u'''校验有弹出框类型用例是否通过
			parameters: 
				data : 检查点
				flag : 通过标识(True or False)
	'''
	def check_with_pop_up(self,data,flag):
		
		#点击保存按钮弹出框
		auth_msg = self.auth_msg()	
		self.frameElem.switch_to_content()
		self.cmf.test_win_check_point("xpath",auth_msg,data,flag)
	
	u'''没有弹出框的校验'''
	def check_without_pop_up(self,clientName,data):
		reName = self.cnEnde.is_float(clientName)
		#判断测试项是否通过
		if self.clientElem.get_row_by_account(reName) != None:
			self.log.log_detail(data[0], True)
		else:
			self.log.log_detail(data[0], False)
	
	u'''添加客户端'''
	def add_client_001(self):		
		#日志开始记录
		self.log.log_start("addClient_001")
		#获取添加客户端的数据
		client_data = self.get_table_data("add_client")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(client_data)):
			data = client_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :

					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.clientElem.select_query_res_type(data[2],data[3])
					self.clientElem.click_query_button()
					self.clientElem.add_button()
					self.clientElem.set_client_name(data[4])
					self.clientElem.set_action_stream(data[5])
					self.clientElem.set_database_res_type(data[2],data[3])
					self.clientElem.save_button()
					
					#判断测试项是否通过
					self.log.log_detail(data[0], True)
					#清空标识状态
					flag = False

			except Exception as e:
				print ("Add client fail: ") + str(e)
		self.log.log_end("AddClient")
	
	u'''修改客户端'''
	def edit_client_002(self):	
		#日志开始记录
		self.log.log_start("EditClient_002")
		#获取修改客户端的数据
		client_data = self.get_table_data("edit_client")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(client_data)):
			data = client_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					
					self.clientElem.select_query_res_type(data[2],data[3])
					self.clientElem.click_query_button()
					self.clientElem.edit_operation(data[4])
					#客户端不为空
					if data[5] != "":
						self.clientElem.set_client_name(data[5])
					#动作流不为空
					if data[6] != "":
						self.clientElem.set_action_stream(data[6])
					if dataRow == 1:
						self.clientElem.edit_save_button()
						#判断测试项是否通过
						self.check_without_pop_up(data[5],data)
						
					if dataRow == 2:
						self.clientElem.default_client_save_button()
						#判断测试项是否通过
						self.check_without_pop_up(data[4],data)
						
					#清空标识状态
					flag = False
	
			except Exception as e:
				print ("Edit client fail: ") + str(e)
		self.log.log_end("EditClient")	
	
	u'''校验客户端'''
	def check_client_003(self):	
		#日志开始记录
		self.log.log_start("checkClient_003")
		#获取校验客户端的数据
		client_data = self.get_table_data("check_client")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		self.clientElem.add_button()
		for dataRow in range(len(client_data)):
			data = client_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :

					self.frameElem.from_frame_to_otherFrame("mainFrame")
					
					self.clientElem.set_client_name(data[4])
					self.clientElem.set_action_stream(data[5])
					if data[3] != "":
						self.clientElem.set_database_res_type(data[2],data[3])
					self.clientElem.save_button()
					self.frameElem.switch_to_content()
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False

			except Exception as e:
				print ("Check client fail: ") + str(e)
		self.clientElem.quit_button()
		self.log.log_end("CheckClient")
	
	u'''删除客户端'''
	def del_client_004(self):	
		#日志开始记录
		self.log.log_start("DelClient")
		#获取删除客户端的数据
		client_data = self.get_table_data("del_client")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(client_data)):
			data = client_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :

					self.frameElem.from_frame_to_otherFrame("mainFrame")
					
					self.clientElem.select_query_res_type(data[2],data[3])
					self.clientElem.click_query_button()
					self.clientElem.del_operation(data[4])
					self.cmf.click_login_msg_button()
					
					#判断测试项是否通过
					self.log.log_detail(data[0], True)
					#清空标识状态
					flag = False
	
			except Exception as e:
				print ("Add client fail: ") + str(e)
		self.log.log_end("AddClient")