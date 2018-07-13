#coding=utf-8
''' 
#文件名：
#作者：顾亚茹
#创建日期：2017/7/04
#模块描述：调用认证方式定义模块
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
from _icommon import commonFun,getElement,selectElement,frameElement
from _cnEncode import cnEncode
from _log import log
from _initDriver import *
sys.path.append("/testIsompSecret/webElement/auth_method/")
from authMethodElement import AuthMethodPage
#导入登录
sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData


class testAuthMethod(object):

	#提示框文件元素路径
	def auth_method_msg(self):
		auth_method_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		return auth_method_msg

	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.authMethod = AuthMethodPage(driver)
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.login = loginPage(self.driver)
		self.cnEnde = cnEncode()
		self.commonSuite = CommonSuiteData(self.driver)
		
	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
			return：表格数据
	'''
	def get_table_data(self,sheetname):
		dataFile = dataFileName()
		filePath = dataFile.get_auth_method_test_data_url()
		authFileData = dataFile.get_data(filePath,sheetname)
		return authFileData	

	u'''校验有弹出框类型用例是否通过
			parameters: 
				data : 检查点
				flag : 通过标识(True or False)
	'''
	def check_with_pop_up(self,data,flag):
		
		#点击保存按钮弹出框
		auth_method_msg = self.auth_method_msg()	
		self.frameElem.switch_to_content()
		self.cmf.test_win_check_point("xpath",auth_method_msg,data,flag)

	u'''添加AD域认证方式'''
	def add_ad_method_001(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		selem = self.getElem.find_element_with_wait("id",selectd_auth_method)
		self.authMethod.selectd_all_method(selem,'2')
		#日志开始记录
		self.log.log_start("addADMethod")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("add_auth_method")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 1:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.select_add_meth_method(data[2])
					self.authMethod.auth_add_button()
					self.authMethod.check_option_is_not_exist('id',all_auth_method,data[3])
					#校验是否添加到已选认证方式
					self.authMethod.check_option_is_selectd('id',selectd_auth_method,data[3])
					self.authMethod.set_ad_auth_ip(data[4])
					self.authMethod.set_ad_auth_port(data[5])
					self.authMethod.set_ad_auth_domian_name(data[6])
					self.authMethod.save_button()
					
					#判断测试点是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False					
			except Exception as e:
				print ("AD auth method add fail: ") + str(e)
		self.log.log_end("addADMethod")
		
	u'''添加radius认证方式'''
	def add_radius_method_002(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"

		#日志开始记录
		self.log.log_start("addRadiusMethod")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("add_auth_method")

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 2:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.select_add_meth_method(data[2])
					self.authMethod.auth_add_button()
					self.authMethod.check_option_is_not_exist('id',all_auth_method,data[3])
					#校验是否添加到已选认证方式
					self.authMethod.check_option_is_selectd('id',selectd_auth_method,data[3])
					self.authMethod.set_radius_auth_ip(data[4])
					self.authMethod.set_radius_auth_port(data[5])
					self.authMethod.set_radius_auth_key(data[7])
					self.authMethod.save_button()
					
					#判断测试点是否通过
					self.check_with_pop_up(data,flag)

					#清空标识状态
					flag = False					
			except Exception as e:
				print ("Radius auth method add fail: ") + str(e)
		self.log.log_end("addRadiusMethod")
		
	u'''添加AD域+口令认证方式'''
	def add_ad_and_pwd_method_003(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"

		#日志开始记录
		self.log.log_start("addADAndPwdMethod")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("add_auth_method")
	
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 3:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.select_add_meth_method(data[2])
					self.authMethod.auth_add_button()
					self.authMethod.check_option_is_not_exist('id',all_auth_method,data[3])
					#校验是否添加到已选认证方式
					self.authMethod.check_option_is_selectd('id',selectd_auth_method,data[3])
					self.authMethod.save_button()
					
					#判断测试点是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
			except Exception as e:
				print ("AdAndPwd auth method add fail: ") + str(e)
		self.log.log_end("addADAndPwdMethod")

	u'''添加radius+口令认证方式'''
	def add_radius_and_pwd_method_004(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"

		#日志开始记录
		self.log.log_start("addRadiusMethod")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("add_auth_method")

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 4:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.select_add_meth_method(data[2])
					self.authMethod.auth_add_button()
					self.authMethod.check_option_is_not_exist('id',all_auth_method,data[3])
					#校验是否添加到已选认证方式
					self.authMethod.check_option_is_selectd('id',selectd_auth_method,data[3])
					self.authMethod.save_button()
					
					#判断测试点是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
			except Exception as e:
				print ("RadiusAndPwd auth method add fail: ") + str(e)
		self.log.log_end("addRadiusAndPwdMethod")

	u'''添加证书认证方式'''
	def add_cert_method_005(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"

		#日志开始记录
		self.log.log_start("addCertMethod")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("add_auth_method")

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 5:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.select_add_meth_method(data[2])
					self.authMethod.auth_add_button()
					self.authMethod.check_option_is_not_exist('id',all_auth_method,data[3])
					#校验是否添加到已选认证方式
					self.authMethod.check_option_is_selectd('id',selectd_auth_method,data[3])
					self.authMethod.save_button()
					
					#判断测试点是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Cert auth method add fail: ") + str(e)
		self.log.log_end("addCertMethod")

	u'''添加所有的认证方式并校验是否添加成功'''
	def auth_method_add_is_success_006(self):
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"

		auth_method_data = self.get_table_data("login")

		#日志开始记录
		self.log.log_start("checkout auth method whether add success")
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 1:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					auth_select_text = self.authMethod.get_select_options_text("id",selectd_auth_method)
					self.authMethod.get_user_select_auth_text(data)
					user_select_text = self.authMethod.get_select_options_text("id","fortAuthenticationCode")
					self.authMethod.compare_list_is_equal(auth_select_text,user_select_text,data)
					self.frameElem.from_frame_to_otherFrame("topFrame")
					self.commonSuite.user_quit()
					login_select_text = self.authMethod.get_select_options_text("id","loginMethod")
					self.authMethod.compare_list_is_equal(auth_select_text,login_select_text,data)
			except Exception as e:
				print "is not equal" + str(e)
		self.log.log_end("Add all auth method and checkout whether add success")
	
	#修改AD域认证配置
	def mod_ad_method_007(self):

		#日志开始记录
		self.log.log_start("ModeyADMethodConfig")
		self.commonSuite.login_secadmin()
		self.commonSuite.switch_to_moudle(u"策略配置", u"认证强度")
		time.sleep(3)
		#获取修改AD域配置测试数据
		auth_method_data = self.get_table_data("mod_ad_method")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.set_ad_auth_ip(data[2])
					self.authMethod.set_ad_auth_port(data[3])
					self.authMethod.set_ad_auth_domian_name(data[4])
					self.authMethod.save_button()
					
					#判断测试点是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False					
			except Exception as e:
				print ("Modey AD method config fail: ") + str(e)
		self.log.log_end("ModeyADMethodConfig")
	
	#AD域认证配置校验
	def ad_method_checkout_008(self):

		#日志开始记录
		self.log.log_start("ADMethodCheckout")
		#获取修改AD域配置测试数据
		auth_method_data = self.get_table_data("ad_method_checkout")
	
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.set_ad_auth_ip(data[2])
					self.authMethod.set_ad_auth_port(data[3])
					self.authMethod.set_ad_auth_domian_name(data[4])
					if dataRow == range(len(auth_method_data))[-1]:
						self.authMethod.domian1_add_button()
						self.authMethod.set_domian2_ip(data[5])
					self.authMethod.save_button()
					
					#判断测试点是否通过
					self.check_with_pop_up(data,flag)
					
					#清空标识状态
					flag = False					
			except Exception as e:
				print ("ADMethodCheckout fail: ") + str(dataRow) + str(e)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.authMethod.domian2_del_button()
		self.log.log_end("ADMethodCheckout")
	
	u'''radius认证校验'''
	def radius_checkout_009(self):

		#日志开始记录
		self.log.log_start("RadiusCheckout")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("radius_method_checkout")#radius_method_checkout,Sheet1
		#radius通讯秘钥
		radius_auth_key = "radiusShareSecret0"

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.set_radius_auth_ip(data[2])
					self.authMethod.set_radius_auth_port(data[3])
					if data[2] == "" or data[2] == "123.abc":
						self.getElem.find_element_with_wait('id',radius_auth_key).click()
						self.cmf.click_login_msg_button()
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.set_radius_auth_key(data[4])
					self.authMethod.set_radius_auth_key(data[4])
					self.authMethod.set_backup_radius_ip(data[5])
					self.authMethod.set_backup_radius_key(data[6])
					self.authMethod.save_button()

					#判断测试点是否通过
					self.check_with_pop_up(data,flag)
										
					#清空标识状态
					flag = False					

			except Exception as e:
				print ("RadiusCheckout fail: ") + str(e)
		self.log.log_end("RadiusCheckout")

	u'''删除其他认证方式'''
	def del_auth_method_010(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("del_raius_method")		

		#日志开始记录
		self.log.log_start("delotherMethod")
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果是第2行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.quit_selectd_all_method()
					selem = self.getElem.find_element_with_wait("id",selectd_auth_method)
					self.authMethod.selectd_all_method(selem,'2','1')
					self.authMethod.auth_del_button()
					#校验已选认证方式只有默认方式
					self.authMethod.check_option_is_selectd('id',all_auth_method,data[3])
					self.authMethod.save_button()
					
					#判断测试点是否通过
					self.check_with_pop_up(data,flag)
					
				#清空标识状态
				flag = False
							
			except Exception as e:
				print ("delAuthMethod fail: ") + str(e)
		self.log.log_end("delAuthMethod")