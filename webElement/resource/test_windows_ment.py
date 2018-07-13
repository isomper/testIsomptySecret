#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：windows资源
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''


import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsompSecret/common/")
from _icommon import getElement,selectElement,frameElement
from _cnEncode import cnEncode
sys.path.append("/testIsompSecret/webElement/resource/")
from test_resource_common import Resource

class WindowsResource(object):

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.resource = Resource(driver)
		self.cnEn = cnEncode()

	u'''添加和编辑windows资源
	   Parameters:
	      - data:excel中的一行数据
	'''
	def add_edit_windows_resource(self, data):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		#资源名称
		if data[3] != 'no':
			self.resource.set_resource_name(data[3])
		#资源ip
		if data[5] != 'no':
			self.resource.set_resource_ip(data[5])
		#从IP
		if data[6] != 'no':
			self.resource.set_resource_fortIps(data[6])
		#归属部门
		if data[4] != 'no':
			self.resource.set_depart(data[4])
		#密码策略
		if data[7] != 'no':
			self.resource.select_pwd_strategy(data[7])
		#选择所要运维协议
		self.resource.select_all_agreement()
		#windows域名
		if data[8] != 'no':
			self.set_domain_name(data[8])
		#账号分类
		if data[9] != 'no':
			self.resource.click_account_sync()
			self.select_account_type(data[9])
		#归属域控主机
		if data[10] != 'no':
			self.select_attach_domian(data[10])
		#主机名称
		if data[11] != 'no':
			self.set_host_name(data[11])
		#管理员帐号
		if data[12] != 'no':
			if data[9] == 'no':
				self.resource.click_account_sync()
			self.resource.set_admin_account(data[12])
		#管理员帐号
		if data[16] != 'no':
			self.resource.click_account_sync()
			self.select_account_protocol(data[16])
			self.set_port(data[17])
			if data[16] == "Ldap":
				self.set_ldap_account(data[18])
			else:
				self.set_ssh_account(data[18])
		#管理员口令
		if data[13] != 'no':
			self.resource.set_admin_pwd(data[13])
		#口令确认
		if data[14] != 'no':
			self.resource.set_confirm_pwd(data[14])
		#BaseDN
		if data[15] != 'no':
			self.set_base_dn(data[15])

		if data[5] != 'no':
			self.resource.resoure_save_button()
		else:
			self.resource.click_save_button()

	u'''校验windows资源
	   Parameters:
	      - datarow:excel数据位于第几行
	      - data:excel中的一行数据
	'''
	def check_windows_resource(self, datarow, data):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		#资源名称
		self.resource.set_resource_name(data[2])
		#资源ip
		self.resource.set_resource_ip(data[3])
		#协议类型
		if data[4] != 'no':
			self.resource.select_agreement(data[4])
		#协议类型 端口
		if datarow == 7:
			self.resource.set_port(data[4], data[5])
		if datarow == 8:
			self.resource.clear_port("Vnc")
		if datarow == 9:
			self.resource.set_port("Vnc", data[5])
		if datarow == 12:
			self.resource.click_account_sync()
			self.select_account_type(data[6])
		if datarow == 13:
			self.select_attach_domian(data[7])
		self.resource.resoure_save_button()

	u'''填写windows域名
	   parameter:
	       - domainname:windows域名
	'''
	def set_domain_name(self, domainname):
		try:
			doname = self.cnEn.is_float(domainname)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', "fortDomainName")
			self.getElem.find_element_wait_and_sendkeys('id', "fortDomainName", doname)
		except Exception as e:
			print "domainname is error :" + str(e)

	u'''选择账号分类
	   Parameters:
	      - value:value属性
	'''
	def select_account_type(self, value):
		type = self.cnEn.is_float(value)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		selectelem = self.getElem.find_element_with_wait_EC("id", "selectDisplay")
		self.selectElem.select_element_by_value(selectelem, type)

	u'''选择归属域控主机
	   parameter:
	       - text:归属域控主机的名称
	'''
	def select_attach_domian(self, text):
		try:
			domiantext = self.cnEn.is_float(text)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			selectelem = self.getElem.find_element_with_wait_EC('id', "window_select_dc")
			self.selectElem.select_element_by_visible_text(selectelem, domiantext)
		except Exception as e:
			print "Domian select error:" + str(e)

	u'''填写主机名称
	   parameter:
	       - hostname:主机名称
	'''
	def set_host_name(self, hostname):
		try:
			host = self.cnEn.is_float(hostname)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', "window_host_name")
			self.getElem.find_element_wait_and_sendkeys('id', "window_host_name", host)
		except Exception as e:
			print "window_host_name is error :" + str(e)

	u'''填写Base DN
	   parameter:
	       - basedn:Base DN名称
	'''
	def set_base_dn(self, basedn):
		try:
			base = self.cnEn.is_float(basedn)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', "fortBaseDn")
			self.getElem.find_element_wait_and_sendkeys('id', "fortBaseDn", base)
		except Exception as e:
			print "fortBaseDn is error :" + str(e)

	u'''填写连接端口
	   parameter:
	       - portname:连接端口名称
	'''
	def set_port(self, portname):
		try:
			port = self.cnEn.is_float(portname)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', "fortConnectionPort")
			self.getElem.find_element_wait_and_sendkeys('id', "fortConnectionPort", port)
		except Exception as e:
			print "port is error :" + str(e)

	u'''填写ldap账号
	   parameter:
	       - actname:管理员账号
	'''
	def set_ldap_account(self, actname):
		try:
			act = self.cnEn.is_float(actname)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', "fortAdminAccount_ldap")
			self.getElem.find_element_wait_and_sendkeys('id', "fortAdminAccount_ldap", act)
		except Exception as e:
			print "name is error :" + str(e)

	u'''填写ssh账号
	   parameter:
	       - actname:管理员账号
	'''
	def set_ssh_account(self, actname):
		try:
			act = self.cnEn.is_float(actname)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', "fortAdminAccount_ssh")
			self.getElem.find_element_wait_and_sendkeys('id', "fortAdminAccount_ssh", act)
		except Exception as e:
			print "name is error :" + str(e)

	u'''选择账号同步连接协议
	   parameter:
	       - proname:同步
	'''
	def select_account_protocol(self, proname):
		try:
			pro = self.cnEn.is_float(proname)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			selem = self.getElem.find_element_with_wait_EC('id', "fortConnectionProtocol")
			self.selectElem.select_element_by_visible_text(selem, pro)
		except Exception as e:
			print " protocol is error :" + str(e)

	u'''是否勾选获取所有账号'''
	def check_all_account(self):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_click_EC('id', "get_all_accounts")
		except Exception as e:
			print " Check failure :" + str(e)
