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

sys.path.append("/testIsompSecret/common/")
from _log import log
from _icommon import getElement,selectElement,frameElement
from _cnEncode import cnEncode
sys.path.append("/testIsompSecret/webElement/resource/")
from test_resource_common import Resource
from test_resource_accountmgr_ment import Accountmgr

class DatabaseResource(object):
	#数据库名称
	DATABASE_NAME = "fortDatabaseName"
	#服务名
	SERVICE_NAME = "fortDatabaseServerName"
	#全选应用发布
	SELECT_ALL_APP = "add_app_release"
	#应用发布添加到右侧
	ADD_APP = "add"
	#服务名
	SERVICE_NAME = "fortDatabaseServerName"
	#BS账号属性
	ACCOUNT_ATTRIBUTE = "fortBsAccountAttribute"
	#BS表单名称
	FORM_NAME = "fortBsFormName"
	#口令属性
	PWD_ATTRIBUTE = "fortBsPasswordAttribute"
	#表单提交方式
	SUBMIT_METHOD = "submitType"
	#登录URL
	LOGIN_URL = "fortBsLoginUrl"
	#连接端口
	CONNECT_PORT = "fortDatabasePort"
	#选择归属操作系统
	SELECT_SYSTEM = "system_data_select_system"
	#归属资源IP
	SYSTEM_IP = "fortResourceIp"
	#归属资源检索
	SYSTEM_QUERY = "quick_query"
	#全选按钮
	SYSTEM_CHECK_ALL= "resource_check_all"
	#确认按钮
	SYSTEM_OK_BUTTON = "okButton"
	#取消按钮
	SYSTEM_QUIT_BUTTON = "cancelButton"

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.log = log()
		self.resource = Resource(driver)
		self.account = Accountmgr(driver)
		self.cnEn = cnEncode()

	u'''添加和编辑database资源
		Parameters:
			- data:excel中的一行数据
	'''
	def add_edit_database_resource(self, data):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		#资源名称
		self.resource.set_resource_name(data[3])
		#归属部门
		if data[4] != "":
			self.resource.set_depart(data[4])
		#资源ip
		if data[5] != "":
			self.resource.set_resource_ip(data[5])			
		#库名
		if data[6] != "":
			self.set_database_name(data[6])
		#服务名
		if data[7] != "":
			self.set_service_name(data[7])
		#密码策略
		if data[8] != "":
			self.resource.select_pwd_strategy(data[8])
		#账号属性
		if data[9] != "":
			self.set_account_attribute(data[9])
			self.set_submit_method(data[12])
			self.set_form_name(data[10])
			self.set_pwd_attribute(data[11])
			time.sleep(1)
			self.set_login_url(data[13])
		#选择客户端
		if data[14] != "":
			self.select_protocol(data[14])
		#选择应用发布
		if data[15] != "":
			self.select_application(data[15])
		#依附操作系统IP
		if data[16] != "":
			self.click_select_button()
			self.set_system_ip(data[16])
			self.click_query_button()
			self.click_check_all_button()
			self.click_confirm_button()
		#管理员帐号
		if data[17] != "":
			self.resource.click_account_sync()
			self.resource.set_admin_account(data[17])
			#管理员口令
			self.resource.set_admin_pwd(data[18])
			#口令确认
			self.resource.set_confirm_pwd(data[19])
		time.sleep(1)
		if data[5] != "":
			self.resource.resoure_save_button()
		else:
			self.resource.click_save_button()

	u'''填写资源名称'''
	def set_resource_name(self,resourceName):
		reName = self.cnEn.is_float(resourceName)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		name = self.getElem.find_element_with_wait_EC('id','fortResourceName')
		name.clear()
		name.send_keys(reName)
	
	u'''填写资源IP'''
	def set_resource_ip(self,resourceIp):
		reIp = self.cnEn.is_float(resourceIp)
		ip = self.getElem.find_element_with_wait_EC('id','fortResourceIp')
		ip.clear()
		ip.send_keys(reIp)
		self.getElem.find_element_wait_and_click_EC("id", "spanid")
		self.getElem.find_element_with_wait_EC("classname", "ip_succ")
		time.sleep(3)
		#self.driver.implicitly_wait(5)
		
	u'''填写database库名
		parameter:
			- databaseName:数据库库名
	'''
	def set_database_name(self, databaseName):
		try:
			reName = self.cnEn.is_float(databaseName)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			name = self.getElem.find_element_with_wait_EC('id', self.DATABASE_NAME)
			name.clear()
			name.send_keys(reName)
		except Exception as e:
			print "DatabaseName is error :" + str(e)
	
	u'''填写database服务名
		parameter:
			- serviceName:数据库库名
	'''
	def set_service_name(self, serviceName):
		reName = self.cnEn.is_float(serviceName)
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			serviceName = self.getElem.find_element_with_wait_EC('id', self.SERVICE_NAME)
			serviceName.clear()
			serviceName.send_keys(reName)
		except Exception as e:
			print "ServiceName is error :" + str(e)
	
	u'''点击添加到应用发布到右侧'''
	def add_application(self):
		self.getElem.find_element_wait_and_click_EC('id',self.ADD_APP)
	
	u'''选择客户端'''
	def select_protocol(self,proName):
		reName = self.cnEn.is_float(proName)
		parent_xpath = "//table[@id='trees']/tbody/tr[7]/td[2]"
		parent_elem = self.getElem.find_element_with_wait_EC('xpath',parent_xpath)
		elems = parent_elem.find_elements_by_tag_name("span")
		for index in range(len(elems)):
			if elems[index].text == reName:
				protocol_xpath = parent_xpath + "/" + "span[" + str(index+1) + "]/input[1]"
				protocol_elem = self.getElem.find_element_with_wait_EC('xpath',protocol_xpath)
				if not protocol_elem.is_selected():
					protocol_elem.click()

	u'''选择应用发布
		parameter:
			- appStr:应用发布
	'''
	def select_application(self, appStr):
		reappStr = self.cnEn.is_float(appStr)
		appList = reappStr.split(',')
		appSelect = self.getElem.find_element_with_wait_EC('id',self.SELECT_ALL_APP)
		try:
			if appStr != "":
				for appName in appList:
					self.selectElem.select_element_by_visible_text(appSelect, appName)
					self.add_application()

		except Exception as e:
			print "Domian select error:" + str(e)

#---------------------------------BS属性--------------------------------------
	
	u'''填写BS账号属性
		parameter:
			- accountAtt:账号属性
	'''
	def set_account_attribute(self, accountAtt):
		reName = self.cnEn.is_float(accountAtt)
		try:
			accountArrbt = self.getElem.find_element_with_wait_EC('id', self.ACCOUNT_ATTRIBUTE)
			accountArrbt.clear()
			accountArrbt.send_keys(reName)
		except Exception as e:
			print "Set BS Account Attribute is error :" + str(e)
	
	u'''填写BS表单名称
		parameter:
			- formName:表单名称
	'''
	def set_form_name(self, formName):
		reName = self.cnEn.is_float(formName)
		try:
			accountArrbt = self.getElem.find_element_with_wait_EC('id', self.FORM_NAME)
			accountArrbt.clear()
			accountArrbt.send_keys(reName)
		except Exception as e:
			print "Set BS form name is error :" + str(e)
	
	u'''填写BS口令属性
		parameter:
			- pwdAtt:口令属性
	'''
	def set_pwd_attribute(self, pwdAtt):
		reATtt = self.cnEn.is_float(pwdAtt)
		try:
			pwdArrbt = self.getElem.find_element_with_wait_EC('id', self.PWD_ATTRIBUTE)
			pwdArrbt.clear()
			pwdArrbt.send_keys(reATtt)
		except Exception as e:
			print "Set BS Pwd Attribute is error :" + str(e)
	
	u'''填写BS表单提交方式
		parameter:
			- submitMethod:提交方式
	'''
	def set_submit_method(self, submitMethod):
		reMethod = self.cnEn.is_float(submitMethod)
		try:
			smtMethod = self.getElem.find_element_with_wait_EC('id', self.SUBMIT_METHOD)
			time.sleep(2)
			self.selectElem.select_element_by_value(smtMethod, reMethod)
		except Exception as e:
			print "Set BS submit method error :" + str(e)
	
	u'''填写BS登录URL
		parameter:
			- loginUrl:登录url
	'''
	def set_login_url(self, loginUrl):
		reUrl = self.cnEn.is_float(loginUrl)
		try:
			url = self.getElem.find_element_with_wait_EC('id', self.LOGIN_URL)
			url.clear()
			url.send_keys(reUrl)
		except Exception as e:
			print "Set BS login url error :" + str(e)

#--------------------------------依附操作系统----------------------------------
	
	u'''点击选择'''
	def click_select_button(self):
		
		self.getElem.find_element_wait_and_click_EC('id',self.SELECT_SYSTEM)
	
	u'''检索的依附操作系统IP'''
	def set_system_ip(self,systemIp):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		reIp = self.cnEn.is_float(systemIp)
		try:
			system_ip = self.getElem.find_element_with_wait_EC('id', self.SYSTEM_IP)
			system_ip.clear()
			system_ip.send_keys(reIp)
		except Exception as e:
			print "Set system ip error :" + str(e)
	
	u'''点击检索按钮'''
	def click_query_button(self):
		self.getElem.find_element_wait_and_click_EC('id',self.SYSTEM_QUERY)
	
	u'''点击全选按钮'''
	def click_check_all_button(self):
		self.getElem.find_element_wait_and_click_EC('id',self.SYSTEM_CHECK_ALL)
	
	u'''点击确认按钮'''
	def click_confirm_button(self):
		self.frameElem.switch_to_content()
		self.getElem.find_element_wait_and_click_EC('id',self.SYSTEM_OK_BUTTON)
	
	u'''点击取消按钮'''
	def click_quit_button(self):
		self.frameElem.switch_to_content()
		self.getElem.find_element_wait_and_click_EC('id',self.SYSTEM_QUIT_BUTTON)
	
	u'''判断是否是有ip可用性校验'''
	def is_pop_up(self):
		xpath = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		flag = self.getElem.find_element_wait_and_compare_text("xpath", xpath, [0, "ip可用性校验失败！"])
		if flag:
			self.cmf.click_login_msg_button()

#--------------------------windows资源-----------------------------------------
	u'''填写windows域名
	   parameter:
	       - domainname:windows域名
	'''
	def set_domain_name(self, domainname):
		try:
			doname = self.cnEn.is_float(domainname)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear_EC('id', "fortDomainName")
			self.getElem.find_element_wait_and_sendkeys('id', "fortDomainName", doname)
		except Exception as e:
			print "domainname is error :" + str(e)
	
	u'''填写主机名称
	   parameter:
	       - hostname:主机名称
	'''
	def set_host_name(self, hostname):
		try:
			host = self.cnEn.is_float(hostname)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear_EC('id', "window_host_name")
			self.getElem.find_element_wait_and_sendkeys('id', "window_host_name", host)
		except Exception as e:
			print "window_host_name is error :" + str(e)