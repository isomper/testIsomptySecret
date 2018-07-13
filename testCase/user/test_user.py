#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：顾亚茹
#生成日期：2017-07-08
#模块描述：用户测试用例
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

#导入通用方法类
sys.path.append("/testIsompSecret/common/")
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

#导入文件操作类
sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

#导入用户元素类
sys.path.append("/testIsompSecret/webElement/user/")
from userElement import UserPage

class User():
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.user = UserPage(driver)
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.cnEnde = cnEncode()
		self.selectElem = selectElement(driver)
		self.dataFile = dataFileName()
		self.frameElem = frameElement(self.driver)
		self.tableEle = tableElement(self.driver)

	u'''提示框元素路径'''
	def user_msg(self):
		user_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		return user_msg

	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
			return：表格数据
	'''
	def get_table_data(self,sheetname):
		dataFile = dataFileName()
		filePath = dataFile.get_person_test_data_url()
		authFileData = dataFile.get_data(filePath,sheetname)
		return authFileData

	u'''校验有弹出框类型用例是否通过
			parameters: 
				data : 检查点
				flag : 通过标识(True or False)
	'''
	def check_with_pop_up(self,data,flag):
		
		#点击保存按钮弹出框
		user_msg = self.user_msg()	
		self.frameElem.switch_to_content()
		self.cmf.test_win_check_point("xpath",user_msg,data,flag)
		
	u'''校验没有弹出框类型用例是否通过
			parameters: 
				data : 检查点
				flag : 通过标识(True lse)
				status : 0,代表判断条件为相等
	'''
	def check_without_pop_up(self,var1,var2,data):
		if var1 == var2:
			self.cmf.test_win_check_point("","",data,True)
		else:
			self.cmf.test_win_check_point("","",data,False)		

	u'''重置'''	
	def reset(self):
		self.user.click_reset_button()
		self.user.click_search_button()
	
	u'''切换至用户模块'''
	def switch_to_user_module(self):
		time.sleep(2)
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_top()
		time.sleep(1)
		self.cmf.select_menu(u"运维管理")
		self.cmf.select_menu(u"运维管理",u"用户")	

	u'''添加用户'''
	def add_user_001(self):
		#日志开始记录
		self.log.log_start("addUser")
		#获取添加用户的数据
		user_data = self.get_table_data("add_user")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.add_button()
					self.user.set_user_account(data[2])
					self.user.set_user_name(data[3])
					if data[6] != "":
						self.user.set_dep(data[6])
					self.user.set_user_pwd(data[7])
					self.user.set_user_enquire_pwd(data[8])
					self.user.save_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
					self.user.click_back_button()
			except Exception as e:
				print ("user add fail: ") + str(e)
		self.log.log_end("addUser")

	u'''编辑用户'''
	def edit_user_002(self):

		#日志开始记录
		self.log.log_start("editUser")
		#获取编辑用户的数据
		user_data = self.get_table_data("mod_user")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")

					self.user.operate_edit(data[2])
					self.user.set_user_account(data[3])
					self.user.set_user_name(data[4])
					self.user.set_user_status(data[8])
					self.user.set_user_pwd(data[9])
					self.user.set_user_enquire_pwd(data[10])               
					self.user.save_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)

					#清空标识状态
					flag = False
					self.switch_to_user_module()
			except Exception as e:
				print ("edit user fail: ") + str(e)
		self.log.log_end("editUser")	

	u'''生成证书'''
	def create_user_cert_003(self):
		
		#日志开始记录
		self.log.log_start("CreateUserCert")
		#获取生成证书用户的数据
		user_data = self.get_table_data("create_cert")

		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.operate_cert(data[3])
					self.user.create_cert()
					cert_name = self.user.get_cert()
					
					#判断生成的证书名字和指定的名字是否相等
					self.check_without_pop_up(cert_name,data[2],data)

					self.switch_to_user_module()
			except Exception as e:
				print ("Create user cert fail: ") + str(e)
		self.log.log_end("CreateUserCert")

	u'''重新生成证书'''
	def create_user_cert_again_003(self):
		#点击保存按钮弹出框
		user_msg = self.user_msg()
		
		#日志开始记录
		self.log.log_start("ReCreateUserCert")
		#获取重新生成证书的数据
		user_data = self.get_table_data("reCreate_cert")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.operate_cert(data[2])
					cert_num_old = self.user.get_cert_serial_num()

					self.user.create_cert()
					self.cmf.click_login_msg_button()
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					cert_num_new = self.user.get_cert_serial_num()

					if cert_num_old != cert_num_new:
						self.cmf.test_win_check_point("","",data,True)
					else:
						self.cmf.test_win_check_point("","",data,False)

					self.switch_to_user_module()
			except Exception as e:
				print ("ReCreate user cert fail: ") + str(e)
		self.log.log_end("ReCreateUserCert")

	u'''删除证书'''
	def delete_user_cert_004(self):

		#日志开始记录
		self.log.log_start("DeleteUserCert")
		#获取删除证书的数据
		user_data = self.get_table_data("delete_cert")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.operate_cert(data[3])
					self.user.delete_cert()

					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					#清空标识状态
					flag = False
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.cmf.back()
			except Exception as e:
				print ("Delete user cert fail: ") + str(e)
		self.log.log_end("DeleteUserCert")

	u'''校验用户'''
	def checkout_user_005(self):
		#日志开始记录
		self.log.log_start("checkoutUser")
		#获取用户校验的数据
		user_data = self.get_table_data("user_check")#user_check
		#无检查点的测试项标识，如果为True说明通过
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.user.add_button()		
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.set_user_account(data[2])
					self.user.set_user_name(data[3])
					if dataRow == range(len(user_data))[-1]:
						self.user.clear_dep()				
					self.user.set_user_pwd(data[7])
					self.user.set_user_enquire_pwd(data[8])
					self.user.set_user_mobile(data[9])
					self.user.set_user_phone(data[10])
					self.user.set_user_email(data[11])            
					self.user.save_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)

					#清空标识状态
					flag = False
			except Exception as e:
				print ("checkoutUser fail: ") + str(e)
		self.switch_to_user_module()
		self.log.log_end("checkoutUser")

	u'''检索条件:用户状态'''
	def search_user_by_status_006(self):

		#日志开始记录
		self.log.log_start("Search user by status")
		#获取按照用户状态检索的数据
		user_data = self.get_table_data("search_by_status")#user_check

		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					row = self.user.search_by_status(data[3])
					self.user.search_by_user_status(data[2])
					self.user.click_search_button()
					search_row = self.user.get_rows()
					
					#判断测试项是否通过
					self.check_without_pop_up(row,search_row,data)
					self.reset()
			except Exception as e:
				print ("search user by status fail: ") + str(e)
		
		self.log.log_end("Search user by status")

	u'''检索条件:账号或者名称'''
	def search_user_by_username_006(self):

		#日志开始记录
		self.log.log_start("Search user by username")
		#获取按照账号或名称检索的数据
		user_data = self.get_table_data("search_by_name")#user_check

		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					row = self.user.search_direct_by_account_or_name(data[3])
					self.user.search_accountorname(data[3])
					self.user.click_search_button()
					search_row = self.user.get_rows()
					
					#判断测试项是否通过
					self.check_without_pop_up(row,search_row,data)
					self.reset()
			except Exception as e:
				print ("search user by username fail: ") + str(e)
		
		self.log.log_end("Search user by username")

	u'''检索条件:部门'''
	def search_user_by_dep_006(self):

		#日志开始记录
		self.log.log_start("Search user by department")
		#获取按部门检索的数据
		user_data = self.get_table_data("search_by_dep")#user_check
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					if dataRow == 1:
						row = self.user.search_direct_by_dep(data[3])
						self.user.set_dep(data[3])
					elif dataRow == 2:
						row = self.user.get_rows()
						self.user.click_child_node()
						self.user.set_dep(data[3])
					
					self.user.click_search_button()
					search_row = self.user.get_rows()
					
					#判断测试项是否通过
					self.check_without_pop_up(row,search_row,data)
					self.reset()
			except Exception as e:
				print ("search user by department fail: ") + str(e)
		
		self.log.log_end("Search user by department")

	u'''删除单个用户'''
	def del_user_007(self):

		#日志开始记录
		self.log.log_start("DelOneUser")
		#获取删除用户（单个）的数据
		user_data = self.get_table_data("del_user")#user_check
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.operate_delete(data[2])
					self.cmf.click_login_msg_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False

			except Exception as e:
				print ("DelOneUser fail: ") + str(e)
		self.log.log_end("DelOneUser")

	u'''删除全部用户'''
	def del_all_user_008(self):

		#日志开始记录
		self.log.log_start("DelAllUser")
		#获取用户删除的数据
		user_data = self.get_table_data("del_all_user")#user_check
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.del_specified_user(data[2])
					self.user.del_button()
					self.cmf.click_login_msg_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
				
			except Exception as e:
				print ("del all fail: ") + str(e)
		self.log.log_end("DelAllUser")