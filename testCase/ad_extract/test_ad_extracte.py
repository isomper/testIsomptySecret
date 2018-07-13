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

sys.path.append("/testIsompSecret/webElement/ad_extract")
from adExtractElement import AdExtractPage

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData,setDriver
sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

class testAdEx():
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.cnEnde = cnEncode()
		self.adExElem = AdExtractPage(self.driver)
		self.tableElem = tableElement(self.driver)
		self.selectElem = selectElement(driver)
		self.dataFile = dataFileName()
		self.frameElem = frameElement(self.driver)
		self.loginFun = loginPage(self.driver)
		self.commonSuite = CommonSuiteData(self.driver)
	
	u'''提示内容框元素路径'''
	def login_msg(self):
		login_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/ \
		tbody/tr[2]/td[2]/div"
		return login_msg
	
	u'''修改密码弹出框'''
	def modey_pwd_msg(self):
		self.frameElem.switch_to_content()
		modey_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/ \
		tbody/tr[1]/td/div/div"
		return modey_msg
	
	u'''关闭修改密码弹出框'''
	def close_aui(self):
		self.frameElem.switch_to_content()
		close_aui = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/ \
		tbody/tr[1]/td/div/a"
		return close_aui
	
	def test_win_check_point(self,value,data):
		elemText = self.getElem.find_element_wait_and_compare_text("xpath",value,data)
		if elemText:
		# 页面的内容与检查点内容一致，测试点通过
			self.log.log_detail(data[0], True)
		else:
			#页面抓取到的内容与检查点不一致，测试点不通过
			self.log.log_detail(data[0],False)

	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
			return：表格数据
	'''
	def get_table_data(self,sheetname):
		dataFile = dataFileName()
		filePath = dataFile.get_ad_extract_test_url()
		adFileData = dataFile.get_data(filePath,sheetname)
		return adFileData
	
	u'''没有弹出框的校验'''
	def check_without_pop_up(self,type,data):
		retype = self.cnEnde.is_float(type)
		num = self.adExElem.get_account_count(retype)
		recount = int(self.cnEnde.is_float(data[5]))
		#判断测试项是否通过
		if self.adExElem.get_account_count(retype) == recount:
			self.log.log_detail(data[0], True)
		else:
			self.log.log_detail(data[0], False)

	def base_on_dataRow(self,dataRow,data,flag):
		#AD发现账号列表移动到已选账号列表
		if dataRow == 1 or dataRow == 2:
			if dataRow == 1:
				self.frameElem.from_frame_to_otherFrame("mainFrame")
				self.adExElem.set_new_account(data[3])
				self.adExElem.click_new_query_button()
				self.adExElem.click_new_reset_button()
				self.adExElem.click_new_query_button()
				self.adExElem.select_type(data[2],data[3])
				self.adExElem.new_to_selected()
				self.adExElem.set_pwd(data[6])
				self.cmf.click_login_msg_button()
			
		#从已选账号列表移动到AD发现账号列表
			if dataRow == 2:
				self.commonSuite.login_sysadmin()
				self.commonSuite.switch_to_moudle(u"系统配置", u"AD定时抽取")
				self.adExElem.discover_tab()
				self.adExElem.set_selected_account(data[3])
				self.adExElem.click_selected_button()
				self.adExElem.click_selected_reset_button()
				self.adExElem.select_type(data[2],data[3])
				self.adExElem.select_to_new()
			self.loginFun.quit()
			self.frameElem.switch_to_content()
			self.loginFun.set_login_username(data[3])
			self.loginFun.set_login_pwd(data[6])
			self.loginFun.click_login_button()
			if dataRow ==1:
				self.test_win_check_point(self.modey_pwd_msg(),data)
				self.getElem.find_element_with_wait_clickable_and_click("xpath",self.close_aui())
			if dataRow ==2:
				self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
			
		#AD发现账号列表移动到过滤账号列表
		if dataRow == 3:
			self.commonSuite.login_sysadmin()
			self.commonSuite.switch_to_moudle(u"系统配置", u"AD定时抽取")
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.adExElem.discover_tab()
			self.adExElem.set_new_account(data[3])
			self.adExElem.click_new_query_button()
			self.adExElem.click_new_reset_button()
			self.adExElem.click_new_query_button()
			self.adExElem.select_type(data[2],data[3])
			self.adExElem.new_to_filter()
			self.check_without_pop_up(data[4],data)
		#从过滤账号列表移动到AD发现账号列表
		if dataRow == 4:

			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.adExElem.set_filter_account(data[3])
			self.adExElem.click_filter_query_button()
			self.adExElem.select_type(data[2],data[3])
			self.adExElem.filter_to_new()
			self.check_without_pop_up(data[4],data)

	u'''AD抽取'''
	def ad_extract_001(self):
		#日志开始记录
		self.log.log_start("ADExtract_001")
		#获取AD域抽取的数据
		ad_data = self.get_table_data("ad_extract")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.adExElem.connect_tab()
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.adExElem.set_address_ip(data[2])
					self.adExElem.set_base_dn(data[3])
					self.adExElem.set_admin(data[4])
					self.adExElem.set_admin_pwd(data[5])
					self.adExElem.set_home_node1(data[6])
					if dataRow == 5:
						self.adExElem.add_muli_node()
						self.adExElem.set_home_node2(data[7])
					if dataRow == 3:
						self.adExElem.subtree_query()
					self.adExElem.set_query_condition(data[8])
					if dataRow == 1:
						self.adExElem.user_attri_map()
						self.adExElem.set_account_map(data[10])
						self.adExElem.set_name_map(data[11])
					self.adExElem.click_find_immdiate()
					#判断测试项是否通过
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.adExElem.del_node()
					self.adExElem.quit_subtree_query()
					#清空标识状态
					flag = False
			except Exception as e:
				print ("AD Extract fail: ") + str(e)
		self.log.log_end("AdExtract")

	u'''发现'''
	def ad_discover_002(self):
		#日志开始记录
		self.log.log_start("AdDiscover_002")
		#获取AD域账号移动的数据
		ad_data = self.get_table_data("ad_discover")
		#无检查点的测试项标识，如果为True说明通过
		self.commonSuite.switch_to_moudle(u"系统配置", u"AD定时抽取")
		flag = False
		self.adExElem.discover_tab()
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				self.base_on_dataRow(dataRow,data,flag)

					#清空标识状态
				flag = False
	
			except Exception as e:
				print ("AD discover fail: ") + str(e)
		self.log.log_end("AdDiscover_002")
	
	u'''移动ad域账号校验'''
	def move_user_check_003(self):
		#日志开始记录
		self.log.log_start("MoveUserCheck_003")
		#获取AD域账号移动校验的数据
		ad_data = self.get_table_data("move_new_to_select_check")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		self.commonSuite.switch_to_moudle(u"系统配置", u"AD定时抽取")
		self.adExElem.discover_tab()
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.adExElem.select_type(data[2],data[3])
					self.adExElem.new_to_selected()
					if dataRow == 3:
						self.cmf.click_login_msg_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
					if dataRow == 2:
						self.frameElem.from_frame_to_otherFrame("mainFrame")
						self.adExElem.select_type(data[2],data[3])
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Move user check fail: ") + str(e)
		self.log.log_end("MoveUserCheck_003")	

	u'''账号密码校验'''
	def ad_pwd_checkout_004(self):
		#日志开始记录
		self.log.log_start("AdPwdCheckout_004")
		#获取AD域密码校验的数据
		ad_data = self.get_table_data("pwd_check")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		self.commonSuite.switch_to_moudle(u"系统配置", u"AD定时抽取")
		self.adExElem.discover_tab()
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.adExElem.select_type(data[2],data[3])
					self.adExElem.new_to_selected()
					self.adExElem.set_pwd(data[4])
					self.cmf.click_login_msg_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
					#清空标识状态
					flag = False
			except Exception as e:
				print ("AD pwd checkout fail: ") + str(e)
		self.log.log_end("AdPwdCheckout_004")
	
	u'''定时'''
	def cycle_005(self):
		#日志开始记录
		self.log.log_start("cycle_005")
		#获取AD域清空历史记录的数据
		ad_data = self.get_table_data("cycle")
		self.adExElem.quartz_tab()
		row_count = len(ad_data)-1
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					#设置四种方式的定时
					if dataRow != row_count:
						self.adExElem.set_execute_type(data[4])
						self.adExElem.set_hour(data[2])
						self.adExElem.set_minute(data[3])
						self.adExElem.set_execute_date(data[4],data[5],data[6])
						self.adExElem.find_by_quartz()
					#如果是最后一行数据，关闭定时
					if dataRow == row_count:
						self.adExElem.quartz_off()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Set cycle fail: ") + str(e)
		self.log.log_end("cycle_005")	

	u'''清空历史记录'''
	def clear_history_006(self):
		#日志开始记录
		self.log.log_start("ClearHistory_006")
		#获取AD域清空历史记录的数据
		ad_data = self.get_table_data("clear_history")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.adExElem.history_tab()
					self.adExElem.clear_history_button()
					self.cmf.click_login_msg_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",self.login_msg(),data,flag)
					#清空标识状态
					flag = False
			except Exception as e:
				print ("Clear History fail: ") + str(e)
		self.log.log_end("ClearHistory_006")

