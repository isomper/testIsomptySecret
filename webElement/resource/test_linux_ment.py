#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：liunx资源
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsompSecret/common/")
from _icommon import frameElement
sys.path.append("/testIsompSecret/webElement/resource/")
from test_resource_common import Resource
from test_resource_accountmgr_ment import Accountmgr

class LinuxResource(object):

	def __init__(self, driver):
		self.driver = driver
		self.frameElem = frameElement(driver)
		self.resource = Resource(driver)
		self.account = Accountmgr(driver)

	u'''添加和编辑Linux资源
	   Parameters:
	      - data:excel中的一行数据
	'''
	def add_edit_linux_resource(self, data):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		#资源名称
		self.resource.set_resource_name(data[3])
		#资源ip
		self.resource.set_resource_ip(data[4])
		#归属部门
		if data[5] != 'no':
			self.resource.set_depart(data[5])
		self.resource.select_all_agreement()
		#从IP
		if data[6] != 'no':
			self.resource.set_resource_fortIps(data[6])
		#系统版本
		if data[7] != 'no':
			self.resource.set_sys_version(data[7])
		#密码策略
		if data[8] != 'no':
			self.resource.select_pwd_strategy(data[8])
		#改密驱动名称
		if data[9] != 'no':
			self.resource.set_changePwd_driver(data[9])

		#管理员帐号
		if data[10] != 'no':
			self.resource.click_account_sync()
			self.resource.set_admin_account(data[10])
		#管理员口令
		if data[11] != 'no':
			self.resource.set_admin_pwd(data[11])
		#口令确认
		if data[12] != 'no':
			self.resource.set_confirm_pwd(data[12])
			self.resource.click_up_super()
			#提权账号口令
			self.resource.set_super_pwd(data[13])
			#确认口令
			self.resource.set_super_confirm_pwd(data[14])
		self.resource.resoure_save_button()

	u'''校验Linux资源
	   Parameters:
	      - datarow:excel数据位于第几行
	      - data:excel中的一行数据
	'''
	def check_linux_resource(self, datarow, data):
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
			self.resource.clear_port("Ssh1")
		if datarow == 9:
			self.resource.set_port("Ssh1", data[5])
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

	u'''添加资源账号
	   Parameters:
	      - editacttname:编辑的资源账号名称
	      - value:选择编辑方式的value值
	      - addactname:填写的资源账号名称
	      - pwd:账号口令
	      - cmfpwd:确认口令
	'''
	def add_edit_resource_account(self, editacttname='no', value='no', addactname='no', pwd='no', cmfpwd='no'):
		self.account.click_account_add_edit_button(editacttname)
		if value != 'no':
			self.account.select_edit_way(value)
		if addactname != 'no':
			self.account.set_account_name(addactname)
		if pwd != 'no':
			self.account.set_account_pwd(pwd)
		if cmfpwd != 'no':
			self.account.set_account_confirm_pwd(cmfpwd)
		self.account.set_authorize()
		self.account.click_save_account()

	u'''校验资源账号
	   Parameters:
	      - value:选择编辑方式的value值
	      - addactname:填写的资源账号名称
	      - pwd:账号口令
	      - cmfpwd:确认口令
	'''
	def check_resource_account(self, value='no', addactname='no', pwd='no', cmfpwd='no'):
		if addactname == 'no':
			self.account.clear_account_name()
		if pwd == 'no':
			self.account.clear_account_pwd()
		if cmfpwd == 'no':
			self.account.clear_account_confirm_pwd()
		if value != 'no':
			self.account.select_edit_way(value)
		if addactname != 'no':
			self.account.set_account_name(addactname)
		if pwd != 'no':
			self.account.set_account_pwd(pwd)
		if cmfpwd != 'no':
			self.account.set_account_confirm_pwd(cmfpwd)
		self.account.set_authorize()
		self.account.click_save_account()
