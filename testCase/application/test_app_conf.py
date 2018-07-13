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

sys.path.append("/testIsompSecret/webElement/application")
from appConfElement import AppPage

class testApp():
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.cnEnde = cnEncode()
		self.appElem = AppPage(self.driver)
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
		filePath = dataFile.get_app_test_data_url()
		appFileData = dataFile.get_data(filePath,sheetname)
		return appFileData
	
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
	
	u'''添加应用发布'''
	def add_app_001(self):
		#日志开始记录
		self.log.log_start("addApp_001")
		#获取添加应用发布的数据
		app_data = self.get_table_data("add_app")
		msg = self.auth_msg()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		self.appElem.app_module_button()
		for dataRow in range(len(app_data)):
			data = app_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.frameElem.from_frame_to_otherFrame("rigthFrame")
					self.appElem.click_add_button()
					self.appElem.set_name(data[2])
					self.appElem.set_ip(data[3])
					self.appElem.set_app_account(data[5])
					self.appElem.set_pwd(data[6])
					self.appElem.set_repwd(data[7])
					self.appElem.set_desp(data[8])
					self.appElem.ip_is_succ()
					self.appElem.click_save_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					#清空标识状态
					flag = False
					self.appElem.click_back_button()

			except Exception as e:
				print ("Add app fail: ") + str(e)
		self.log.log_end("Addapp")
	
	u'''编辑应用发布'''
	def edit_app_002(self):
		#日志开始记录
		self.log.log_start("EditClient_002")
		#获取编辑应用发布的数据
		client_data = self.get_table_data("edit_app")
		self.appElem.app_module_button()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(client_data)):
			data = client_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.frameElem.from_frame_to_otherFrame("rigthFrame")
					
					self.appElem.operate_edit(data[2])
					self.appElem.set_name(data[3])
					self.appElem.click_save_button()
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					self.appElem.click_back_button()
					#清空标识状态
					flag = False

			except Exception as e:
				print ("Edit client fail: ") + str(e)
		self.log.log_end("EditClient")
	
	u'''校验应用发布'''
	def check_app_003(self):	
		#日志开始记录
		self.log.log_start("CheckClient_003")
		account = "fortApplicationReleaseServerAccount"
		#校验应用发布
		client_data = self.get_table_data("check_app")
		self.appElem.app_module_button()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(client_data)):
			data = client_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.frameElem.from_frame_to_otherFrame("rigthFrame")
					self.appElem.click_add_button()
					self.appElem.set_name(data[2])
					self.appElem.set_ip(data[3])
					self.appElem.set_port(data[4])
					self.appElem.set_app_account(data[5])
					self.appElem.set_pwd(data[6])
					self.appElem.set_repwd(data[7])
					if dataRow != 3:
						self.appElem.ip_is_succ()
					if data[3] == "":
						self.cmf.click_login_msg_button()
					self.appElem.click_save_button()
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					self.appElem.click_back_button()
					
					#清空标识状态
					flag = False
	
			except Exception as e:
				print ("Check client fail: ") + str(e)

		self.appElem.is_pop_up()
		self.log.log_end("CheckClient")
	
	u'''检索应用发布'''
	def query_app_004(self):
		#日志开始记录
		self.log.log_start("QueryClient_004")
		#获取检索应用发布的数据
		client_data = self.get_table_data("query_app")
		self.appElem.app_module_button()

		for dataRow in range(len(client_data)):
			data = client_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.frameElem.from_frame_to_otherFrame("rigthFrame")
					self.appElem.set_app_query_name(data[2])
					self.appElem.click_query_button()
					
					#判断测试项是否通过
					self.log.log_detail(data[0], True)
					self.appElem.click_reset_button()
	
			except Exception as e:
				print ("Query client fail: ") + str(e)
		self.log.log_end("QueryClient")

	u'''删除应用发布'''
	def del_app_005(self):	
		#日志开始记录
		self.log.log_start("DelClient_005")
		#获取删除应用发布的数据
		client_data = self.get_table_data("del_app")
		self.appElem.app_module_button()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(client_data)):
			data = client_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.frameElem.from_frame_to_otherFrame("rigthFrame")
					self.appElem.operate_del(data[2])
					self.cmf.click_login_msg_button()
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
	
			except Exception as e:
				print ("Del client fail: ") + str(e)
		self.log.log_end("DelClient")
	
	u'''添加账号'''
	def add_account_006(self):
		#日志开始记录
		self.log.log_start("Addaccount_006")
		#获取账号的数据
		client_data = self.get_table_data("add_account")
		self.appElem.app_module_button()
			
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(client_data)):
			data = client_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					if dataRow == 1:
						self.appElem.operate_account_manage(data[2])
					self.appElem.click_add_button()
					self.appElem.set_account(data[3])
					self.appElem.set_account_pwd(data[4])
					self.appElem.set_account_repwd(data[5])
					#是否存在绑定用户
					if data[6] != "":
						self.appElem.click_bound_user()
						self.appElem.set_account_or_name(data[6])
						self.appElem.user_query_button()
						self.appElem.select_user_checkbox(data[6])
					self.appElem.click_save_button()
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					self.appElem.click_back_button()
					#清空标识状态
					flag = False
	
			except Exception as e:
				print ("Add account fail: ") + str(e)
		self.log.log_end("Addaccount")

	u'''编辑账号'''
	def edit_account_007(self):	
		#日志开始记录
		self.log.log_start("Editaccount")
		#获取编辑账号的数据
		client_data = self.get_table_data("edit_account")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(client_data)):
			data = client_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.frameElem.from_frame_to_otherFrame("rigthFrame")
					self.appElem.operate_account_edit(data[3])
					self.appElem.set_account(data[4])
					if data[5] != "":
						self.appElem.set_account_pwd(data[5])
					if data[6] != "":
						self.appElem.set_account_repwd(data[6])
					self.appElem.click_save_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					self.appElem.click_back_button()
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Edit account fail: ") + str(e)
		self.log.log_end("Editaccount")
	
	u'''删除账号'''
	def del_account_008(self):	
		#日志开始记录
		self.log.log_start("Delaccount")
		#获取删除账号的数据
		client_data = self.get_table_data("del_account")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(client_data)):
			data = client_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :

					self.frameElem.from_frame_to_otherFrame("rigthFrame")
					self.appElem.operate_account_del(data[3])
					self.cmf.click_login_msg_button()
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
	
			except Exception as e:
				print ("Del account fail: ") + str(e)
		self.log.log_end("Delaccount")