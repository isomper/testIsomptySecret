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

sys.path.append("/testIsompSecret/webElement/authorization")
from authrizationElement import AuthorizationPage

class testAuthorization():
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.cnEnde = cnEncode()
		self.authElem = AuthorizationPage(self.driver)
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
		filePath = dataFile.get_authorization_test_data_url()
		authFileData = dataFile.get_data(filePath,sheetname)
		return authFileData
	
	u'''添加数据通用部分'''	
	def common_part(self,data):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.authElem.add_button()
		self.authElem.set_auth_name(data[2])
		self.authElem.set_dep(data[3],data[9])
	
	u'''添加用户'''
	def add_user(self,data):
		self.authElem.click_add_user()
		self.authElem.set_select_user_name(data[4])
		self.authElem.set_select_user_search_button()
		self.authElem.set_user_check_all_button()
		self.authElem.set_ok_button()

	u'''添加用户组'''
	def add_user_group(self,data):
		self.authElem.click_add_user_group()
		self.authElem.select_user_group(data[5])
		self.authElem.set_ok_button()		
	
	u'''添加资源'''
	def add_res(self,data):
		self.authElem.click_add_res()
		self.authElem.set_select_res_ip(data[6])
		self.authElem.set_select_res_search_button()
		self.authElem.set_res_check_all_button()
		self.authElem.set_ok_button()

	u'''添加资源组'''
	def add_res_group(self,data):
		self.authElem.click_add_res_group()
		self.authElem.select_res_group(data[7])
		self.authElem.set_ok_button()
	
	u'''添加资源账号'''
	def add_res_account(self,data):
		self.authElem.click_add_res_account()
		self.authElem.set_select_res_account(data[8])
		self.authElem.set_select_res_search_button()
		self.authElem.set_res_check_all_button()
		self.authElem.set_ok_button()

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

	u'''判断没有弹出框比较条件不等的用例是否通过
			parameters: 
				var1 : 比较条件1
				var2 : 比较条件2
				data : 测试项
	'''
	def check_without_pop_up(self,var1,var2,data):
		#点击保存按钮弹出框
		auth_msg = self.auth_msg()
		if var1 != var2:
			self.cmf.test_win_check_point("","",data,True)
		else:
			self.cmf.test_win_check_point("","",data,False)
	
	u'''判断没有弹出框，比较条件相等的用例是否通过'''
	def check_with_condition_equal(self,var1,var2,data):

		if var1 == var2:
			self.cmf.test_win_check_point("","",data,True)
		else:
			self.cmf.test_win_check_point("","",data,False)

	u'''重置'''	
	def reset(self):
		self.authElem.click_reset_button()
		self.authElem.click_search_button()
	
	u'''添加用户和资源类型的授权'''
	def add_user_and_res_auth_001(self):		
		#日志开始记录
		self.log.log_start("addAuthorization_001")
		#获取添加授权的数据
		user_data = self.get_table_data("add_authorization")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 1 or dataRow == 2:
					self.common_part(data)
					
					self.add_user(data)
					#添加资源
					self.add_res(data)
					
					self.authElem.save_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
					self.authElem.back_button()
			except Exception as e:
				print ("Authorization 001 add fail: ") + str(e)
		self.log.log_end("addAuthorization_001")
	
	u'''添加用户和资源组类型的授权'''
	def add_user_and_res_group_auth_002(self):		
		#日志开始记录
		self.log.log_start("addAuthorization_002")
		#获取添加授权的数据
		user_data = self.get_table_data("add_authorization")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 3:
					self.common_part(data)
					
					self.add_user(data)
					#添加资源组
					self.add_res_group(data)
					
					self.authElem.save_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
					self.authElem.back_button()
			except Exception as e:
				print ("Authorization 002 add fail: ") + str(e)
		self.log.log_end("addAuthorization_002")
	
	u'''添加用户和资源账号类型的授权'''
	def add_user_and_res_account_auth_003(self):	
		#日志开始记录
		self.log.log_start("addAuthorization_003")
		#获取添加授权的数据
		user_data = self.get_table_data("add_authorization")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 4:
					self.common_part(data)
					
					self.add_user(data)
					#添加资源账号
					self.add_res_account(data)
					
					self.authElem.save_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
					self.authElem.back_button()
			except Exception as e:
				print ("Authorization 003 add fail: ") + str(e)
		self.log.log_end("addAuthorization_003")
	
	u'''添加用户组和资源类型的授权'''
	def add_user_group_and_res_auth_004(self):		
		#日志开始记录
		self.log.log_start("addAuthorization_004")
		#获取添加授权的数据
		user_data = self.get_table_data("add_authorization")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 5:
					self.common_part(data)
					
					self.add_user_group(data)
					#添加资源
					self.add_res(data)
					
					self.authElem.save_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
					self.authElem.back_button()
			except Exception as e:
				print ("Authorization 004 add fail: ") + str(e)
		self.log.log_end("addAuthorization_004")
	
	u'''添加用户组和资源组类型的授权'''
	def add_user_group_and_res_group_auth_005(self):		
		#日志开始记录
		self.log.log_start("addAuthorization_005")
		#获取添加授权的数据
		user_data = self.get_table_data("add_authorization")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果是第5行标题，则读取数据
				if dataRow == 6:
					self.common_part(data)
					
					self.add_user_group(data)
					#添加资源组
					self.add_res_group(data)
					
					self.authElem.save_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
					self.authElem.back_button()
			except Exception as e:
				print ("Authorization 005 add fail: ") + str(e)
		self.log.log_end("addAuthorization_005")

	u'''添加用户组和资源账号类型的授权'''
	def add_user_group_and_res_account_auth_006(self):		
		#日志开始记录
		self.log.log_start("addAuthorization_006")
		#获取添加授权的数据
		user_data = self.get_table_data("add_authorization")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 7:
					self.common_part(data)
					
					self.add_user_group(data)
					#添加资源账号
					self.add_res_account(data)
					
					self.authElem.save_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False

					self.authElem.back_button()
			except Exception as e:
				print ("Authorization 006 add fail: ") + str(e)
		self.log.log_end("addAuthorization_006")
	
	u'''修改授权名称'''
	def edit_auth_name_007(self):		
		#日志开始记录
		self.log.log_start("EditAuthorization_007")
		#获取修改授权数据
		user_data = self.get_table_data("mod_authorization")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					
					self.authElem.operate_edit(data[2])
					self.authElem.set_auth_name(data[3])
					self.authElem.save_button()
					self.cmf.click_login_msg_button()
					
					auth_name_new = self.authElem.get_auth_name_text()
					
					#判断测试项是否通过
					self.check_without_pop_up(auth_name_new,data[2],data)
					
					#清空标识状态
					flag = False
					self.authElem.back_button()
				
			except Exception as e:
				print ("Edit uuthorization fail: ") + str(e)
		self.log.log_end("EditAuthorization_007")
	
	u'''授权校验'''
	def auth_checkout_008(self):	
		#日志开始记录
		self.log.log_start("Authorizationcheckout_008")
		#获取授权校验的数据
		user_data = self.get_table_data("authorization_check")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.authElem.add_button()
		
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if  dataRow != 0:

					self.authElem.set_auth_name(data[2])
					#选择部门
					if dataRow >= 5:
						self.authElem.set_dep(data[3])
					
					#第6行,添加运维用户
					if dataRow == 6:
						self.add_user(data)
					if dataRow == 7:
						self.add_user(data)
						self.add_res(data)
					self.authElem.save_button()
					
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Authorization checkout fail: ") + str(e)
		self.authElem.back_button()
		self.log.log_end("Authorizationcheckout_008")
	
	u'''授权查询'''
	def auth_query_009(self):		
		#日志开始记录
		self.log.log_start("Authorizationquery_009")
		#获取授权查询的数据
		user_data = self.get_table_data("authorazation_search")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if  dataRow != 0:
					self.authElem.set_query_conditon(data[2],data[3])

					self.authElem.click_search_button()
					self.log.log_detail(data[0], True)
					
					#清空标识状态
					flag = False
					self.reset()
			except Exception as e:
				print ("Authorization checkout fail: ") + str(e)
		self.log.log_end("Authorizationcheckout_009")
	
	u'''授权删除'''
	def auth_del_010(self):	
		#日志开始记录
		self.log.log_start("Deloneauthorization_010")
		#获取删除授权的数据
		auth_data = self.get_table_data("del_authorization")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		
		for dataRow in range(len(auth_data)):
			data = auth_data[dataRow]
			try:
				#如果不是第1行,读取数据
				if  dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					#如果是第一行，删除单条授权
					self.authElem.click_auth_checkbox(data[2])
					#如果是第二行删除全部授权
					self.authElem.del_button()
					self.cmf.click_login_msg_button()
					#判断测试项是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Del one authorization fail: ") + str(e)
		self.log.log_end("Deloneauthorization_010")

	u'''添加访问审批'''
	def Opt_access_approvel_011(self):		
		#日志开始记录
		self.log.log_start("OperationAccessApprovel_011")
		
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		
		#获取访问审批的数据
		auth_data = self.get_table_data("access_approvel")
		for dataRow in range(len(auth_data)):
			data = auth_data[dataRow]
			try:
				#如果不是第1行,读取数据
				if  dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					#点击访问审批
					self.authElem.operate_access_approval(data[2])
					#添加访问审批
					if dataRow == 1 or dataRow == 2:
						#设置开关状态
						self.authElem.set_switch_on()
						self.authElem.click_add_approval_level()
						self.authElem.click_add_approval(data[3])
						#添加审批人
						self.authElem.set_select_user_name(data[4])
						self.authElem.set_select_user_search_button()
						self.authElem.set_user_check_all_button()
						self.authElem.set_ok_button()
						#设置审批级别中的通过审批人个数
						self.authElem.set_approver_num(data[3],data[5])
					#删除一级审批
					if dataRow == 3:
						self.authElem.click_del_approvel(data[3])
					#重置审批
					if dataRow == 4:
						self.authElem.click_approvel_reset_button()
					#点击保存
					self.authElem.approval_save_button()
					self.cmf.click_login_msg_button()
					#点击返回
					self.authElem.approval_back_button()
					#判断测试项是否通过
					text = self.authElem.get_access_approvel_value(data[2])
					self.check_with_condition_equal(text,data[6],data)

					#清空标识状态
					flag = False
		
			except Exception as e:
				print ("Operation access approvel fail: ") + str(e)
		
		self.log.log_end("OperationAccessApprovel_011")

	u'''添加双人审批'''
	def add_double_approvel_012(self):	
		#日志开始记录
		self.log.log_start("AddDoubleApprovel_012")
		
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		
		#获取访问审批的数据
		auth_data = self.get_table_data("double_approvel")
		
		for dataRow in range(len(auth_data)):
			data = auth_data[dataRow]
			try:
				
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authElem.operate_double_approval(data[2])
					#添加双人审批
					if dataRow == 1 or dataRow == 2:
						self.authElem.click_start_association()
						self.authElem.select_status(data[3])
						self.authElem.double_approvel_account_or_name(data[4])
						self.authElem.double_approvel_query()
						#勾选审批人和被审批人
						self.authElem.click_all_approver()
						self.authElem.click_all_candidate()
						self.authElem.click_create_relate()

					#取消关联
					if dataRow == 3:
						self.authElem.click_quit_relate()
					self.cmf.click_login_msg_button()
					self.authElem.click_child_page_back_button()
					text = self.authElem.get_double_approvel_value(data[2])
					#判断测试项是否通过
					self.check_with_condition_equal(text,data[6],data)
					
					#清空标识状态
					flag = False
		
			except Exception as e:
				print ("Add double approvel fail: ") + str(e)
		
		self.log.log_end("AddDoubleApprovel_012")