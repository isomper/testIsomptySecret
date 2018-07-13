#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：网络设备资源
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

class NetworkResource(object):

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.resource = Resource(driver)
		self.cnEn = cnEncode()

	u'''添加和编辑网络设备资源
	   Parameters:
	      - data:excel中的一行数据
	'''
	def add_edit_network_resource(self, data):
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

		self.resource.select_all_agreement()
		#系统版本
		if data[7] != 'no':
			self.resource.set_sys_version(data[7])
		#改密驱动名称
		if data[8] != 'no':
			self.resource.set_changePwd_driver(data[8])

		#管理员帐号
		if data[9] != 'no':
			self.resource.click_account_sync()
			self.resource.set_admin_account(data[9])
		#管理员口令
		if data[10] != 'no':
			self.resource.set_admin_pwd(data[10])
		#口令确认
		if data[11] != 'no':
			self.resource.set_confirm_pwd(data[11])
		#提权
		if data[12] != 'no':
			self.resource.click_up_super()
			#提权账号口令
			self.resource.set_super_pwd(data[12])
			#确认口令
			self.resource.set_super_confirm_pwd(data[13])
		if data[5] != 'no':
			self.resource.resoure_save_button()
		else:
			self.resource.click_save_button()

	u'''校验网络设备资源
	   Parameters:
	      - datarow:excel数据位于第几行
	      - data:excel中的一行数据
	'''
	def check_network_resource(self, datarow, data):
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
			self.resource.clear_port("Ssh2")
		if datarow == 9:
			self.resource.set_port("Ssh2", data[5])
		if datarow == 12:
			self.resource.click_account_sync()
			self.resource.click_up_super()
		if datarow == 13:
			#提权账号口令
			if data[6] != 'no':
				self.resource.set_super_pwd(data[6])
			#确认口令
			if data[7] != 'no':
				self.resource.set_super_confirm_pwd(data[7])
			self.resource.set_super_prompt()
		self.resource.resoure_save_button()

	u'''选择telnet登录模式
	   Parameters:
	      - mode:value属性
	'''
	def telnet_login_type(self, mode):
		model = self.cnEn.is_float(mode)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		selectelem = self.getElem.find_element_with_wait_EC("id", "fortInputModelTelnet")
		self.selectElem.select_element_by_value(selectelem, model)

	u'''勾选匿名认证'''
	def check_anonymous(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "anonymous_auth")
