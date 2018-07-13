#coding=utf-8
u''' 
#文件名：authMethodElement.py
#被测软件版本号：V2.8.1
#作成人：顾亚茹
#生成日期：2017-07-01
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import time


#导入通用模块
sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun
from _cnEncode import cnEncode
from _log import log

#导入文件操作模块
sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

#导入登录元素模块
sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

class AuthMethodPage():

	#全部认证方式
	ALL_METH_METHOD = "all_globalAuthMethod"
	#已选认证方式
	SELECTED_AUTH_METHOD = "select_globalAuthMethod"
	#认证方式添加按钮
	ADD_BUTTON = "add"
	#删除按钮
	DELETE_BUTTON = "delete"
	#保存按钮
	SAVE_BUTTON = "save_auth_method"
	#AD域1认证IP
	AD_AUTH_IP = "ldapHost0"
	#AD域1认证port
	AD_AUTH_PORT = "ldapPort0"
	#AD域1认证域名
	AD_AUTH_DOMIAN_NAME = "ldapName0"
	#域1对应的添加按钮
	DOMIAN1_ADD_BUTTON = "btn_01"
	#域2对应的删除按钮
	DOMIAN2_DEL_BUTTON = "delete_01"
	#域2配置IP
	DOMIAN2_IP = "ldapHost1"
	#主RADIUS认证IP
	RADIUS_AUTH_IP = "radiusIp0"
	#主RADIUS认证PORT
	RADIUS_AUTH_PORT = "radiusPort0"
	#主RADIUS认证通讯秘钥
	RADIUS_AUTH_KEY = "radiusShareSecret0"
	#备RADIUS认证IP
	BACKUP_RADIUS_IP = "radiusIp1"
	#备RADIUS认证通讯秘钥
	BACKUP_RADIUS_KEY = "radiusShareSecret1"
	
	def __init__(self,driver):
		#selenuim驱动
		self.driver = driver
		self.getElem = getElement(self.driver)
		self.selectElem = selectElement(self.driver)
		self.frameElem = frameElement(self.driver)
		self.commElem = commonFun(self.driver)
		self.cmf = commonFun(self.driver)
		self.dataFile = dataFileName()
		self.login = loginPage(self.driver)
		self.cnEnde = cnEncode()
		self.log = log()
	
	u'''选择认证方式
			parameters:
				value : 认证方式中选择的value值
	'''
	def select_meth_method(self,authValue,value):
		try:
			reauthValue = self.cnEnde.is_float(authValue)
			select_elem = self.getElem.find_element_with_wait_EC('id',value)
			self.selectElem.select_element_by_value(select_elem,reauthValue)
		except Exception as e:
			print ("select auth method error: ") + value + str(e)

	u'''选择添加的认证方式
			parameters:
				value : 认证方式中选择的value值
	'''	
	def select_add_meth_method(self,value):
		return self.select_meth_method(value,self.ALL_METH_METHOD)

	u'''选择删除的认证方式
			parameters:
				value : 认证方式中选择的value值
	'''		
	def selected_del_meth_method(self,value):
		return self.select_auth_method(value,self.SELECTED_AUTH_METHOD)

	u'''检查全部认证方式中是否存在添加过的认证方式  
			parameters:
				type : 定位方式
				elem : 定位方式对应值
				list_text : 添加的认证方式名字
	'''		
	def check_option_is_not_exist(self,type,value,list_text):
		isExsit = True
		try:
			selectd_elem = self.getElem.find_element_with_wait_EC(type,value)
			allText = self.selectElem.get_all_option_text(selectd_elem)
			for text in allText:
				if text == list_text:
					isExsit = False
					break
		except Exception:
			print ("Selectd Auth method is not exist ") + list_text
		return isExsit
	
	u'''检查认证方式是否添加到已选认证方式
			parameters:
				type : 定位方式
				elem : 定位方式对应值
				list_text : 添加的认证方式名字
	'''	
	def check_option_is_selectd(self,type,value,list_text):
		isExsit = False
		try:
			selectd_elem = self.getElem.find_element_with_wait_EC(type,value)
			allText = self.selectElem.get_all_option_text(selectd_elem)
			for text in allText:
				if text == list_text:
					isExsit = True
					break
		except Exception:
			print ("Auth method is not selected: ") + list_text
		return isExsit

	u'''填写变量内容
	    parameters:
	        var_text : 变量内容
	        locator : 定位方式对应的属性值
	'''    	
	def set_common_var_text(self,var_text,value):
		try:

			self.frameElem.from_frame_to_otherFrame("mainFrame")
			revar_text = self.cnEnde.is_float(var_text)
			var_elem = self.getElem.find_element_with_wait_EC('id',value)
			var_elem.clear()
			var_elem.send_keys(revar_text)
		except Exception as e:
			print ("set meth method var text error: ") + revar_text + str(e)
			
	u'''填写AD域1认证IP
		parameters:
			ip_ : AD域1认证IP
	'''  		
	def set_ad_auth_ip(self,ip_):
		return self.set_common_var_text(ip_,self.AD_AUTH_IP)

	u'''填写AD域2认证IP
		parameters:
			ip_ : AD域2认证IP
	'''  		
	def set_domian2_ip(self,ip_):
		return self.set_common_var_text(ip_,self.DOMIAN2_IP)

	u'''填写AD域1认证PORT
		parameters:
			port_ : AD域1认证PORT
	'''  		
	def set_ad_auth_port(self,port_):
		return self.set_common_var_text(port_,self.AD_AUTH_PORT)
				
	u'''填写AD域1认证域名
		parameters:
			domianName_ : AD域1认证域名
	'''	
	def set_ad_auth_domian_name(self,domianName_):
		return self.set_common_var_text(domianName_,self.AD_AUTH_DOMIAN_NAME)

	u'''填写主RADIUS认证IP
		parameters:
			radiusIp_ : 主RADIUS认证IP
	'''		
	def set_radius_auth_ip(self,radiusIp_):
		return self.set_common_var_text(radiusIp_,self.RADIUS_AUTH_IP)

	u'''填写备机RADIUS认证IP
		parameters:
			radiusIp_ : 备机RADIUS认证IP
	'''		
	def set_backup_radius_ip(self,radiusIp_):
		return self.set_common_var_text(radiusIp_,self.BACKUP_RADIUS_IP)

	u'''填写主RADIUS认证PORT
		parameters:
			radiusPort_ : 主RADIUS认证PORT
	'''		
	def set_radius_auth_port(self,radiusPort_):
		return self.set_common_var_text(radiusPort_,self.RADIUS_AUTH_PORT)

	u'''填写主RADIUS认证秘钥
		parameters:
			radiusKey : 主RADIUS认证秘钥
	'''	
	def set_radius_auth_key(self,radiusKey):
		return self.set_common_var_text(radiusKey,self.RADIUS_AUTH_KEY)

	u'''填写备RADIUS认证秘钥
		parameters:
			backupKey : 备RADIUS认证秘钥
	'''		
	def set_backup_radius_key(self,backupKey):
		return self.set_common_var_text(backupKey,self.BACKUP_RADIUS_KEY)

	u'''点击域1对应的添加按钮'''
	def domian1_add_button(self):
		try:
			self.getElem.find_element_with_wait_clickable_and_click('id',self.DOMIAN1_ADD_BUTTON)
		except Exception as e:
			print ("domian1 add button error: ") + str(e)

	u'''点击AD域2对应的删除按钮'''
	def domian2_del_button(self):
		try:
			time.sleep(1)
			self.getElem.find_element_with_wait_clickable_and_click('id',self.DOMIAN2_DEL_BUTTON)
		except Exception as e:
			print ("domian2 del button error: ") + str(e)

	u'''点击认证方式添加按钮'''
	def auth_add_button(self):
		try:
			self.getElem.find_element_with_wait_clickable_and_click('id',self.ADD_BUTTON)
		except Exception as e:
			print ("Auth_method add button error: ") + str(e)
	
	u'''点击认证方式删除按钮''' 
	def auth_del_button(self):
		try:
			self.getElem.find_element_with_wait_clickable_and_click('id',self.DELETE_BUTTON)
		except Exception as e:
			print ("Auth method delete button error: ") + str(e)

	u'''点击保存按钮'''
	def save_button(self):
		try:
			self.getElem.find_element_with_wait_clickable_and_click('id',self.SAVE_BUTTON)
		except Exception as e:
			print ("Auth method save button error : ") + str(e)
			
	u'''取消所有选中的证书'''
	def quit_selectd_all_method(self):
		try:
			
			#获取已选认证方式的所有option
			selem = self.getElem.find_element_with_wait_EC("id",self.SELECTED_AUTH_METHOD)
			options = selem.find_elements_by_tag_name("option")
			for option in options:
				value = option.get_attribute('value')
				self.selectElem.deselect_element_by_value(selem,value)

		except Exception as e:
			print ("Quit all method error：") + str(e)

	u'''选中select框中除默认方式以外的其他认证方式
			parameters:
				selem : select元素
				value_ : option选项的value值
				status : 是否点击认证方式删除按钮(默认点击)
	'''
	def selectd_all_method(self,selem,value_,status='0'):
		try:
			options = selem.find_elements_by_tag_name("option")
			select_options_text = self.selectElem.get_all_option_text(selem)
			default_auth_text = "用户名+口令(默认方式)"
			text =  self.cnEnde.cnCode(','.join(select_options_text))			
			num = len(options)
			
			#认证方式不是默认方式
			if num != 1 or(num == 1 and default_auth_text not in select_options_text):
				for option in options:
					value = option.get_attribute('value')
					if value != value_:
						self.selectElem.select_element_by_value(selem,value)
				if status == '0':
					self.auth_del_button()
					self.save_button()
					self.cmf.click_login_msg_button()
		except Exception as e:
			print ("Seleted all method error: ") + str(e)

	u'''判断两个list是否相等
			parameters : 
				list1 : 比较的第一个list
				list2 : 比较的第二个list
				data : 测试点内容
	'''
	def compare_list_is_equal(self,list1,list2,data):
		try:
			selem1_option_text = sorted(list1)
			selem2_option_text = sorted(list2)
			selem1_option_num = len(selem1_option_text)
			selem2_option_num = len(selem2_option_text)
			if selem1_option_num != selem2_option_num:
				return False
			elif (selem1_option_text) == selem2_option_text and (selem2_option_num == 6):
				self.log.log_detail(data[0],True)
				return True
			else:
				return False
		except Exception as e:
			print ("Two select element is not equal: ") + str(e)
			
	u'''获取select元素的所有文本值
			parameters:
				type : 定位方式
				value : 定位方式对应的属性值
	'''
	def get_select_options_text(self,type,value):
		try:
			selem = self.getElem.find_element_with_wait_EC(type,value)
			select_options_text = self.selectElem.get_all_option_text(selem)
			return select_options_text
		except Exception as e:
			print ("select element text get error: ") + str(e)

	u'''点击用户的高级选项
			parameters:
				data : 查找的用户账号
	'''
	def get_user_select_auth_text(self,data):
		time.sleep(3)
		self.frameElem.from_frame_to_otherFrame("topFrame")
		
		self.cmf.select_menu(u"运维管理")
		self.cmf.select_menu(u"运维管理",u"用户")
		
		#获取用户isomper对应的行号
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		user_row = self.cmf.find_row_by_name(data[3],"fortUserAccount")

		#点击编辑按钮
		edit_xpath = "//table[@id='content_table']/tbody/tr[" + str(user_row) + "]/td[9]/input[1]"
		
		self.getElem.find_element_with_wait_clickable_and_click('xpath',edit_xpath)
		self.frameElem.from_frame_to_otherFrame("mainFrame")

		#点击高级选项
		self.getElem.find_element_with_wait_clickable_and_click('id','btn_high')

	'''登录并切换至认证方式页面'''
	def login_and_switch_auth_method(self):
		#登录
		file_path = self.dataFile.get_auth_method_test_data_url()
		login_data = self.dataFile.get_data(file_path,'login')
		logindata = login_data[1]
		self.login.login(logindata)

		self.frameElem.from_frame_to_otherFrame("topFrame")

		self.cmf.select_menu(u"策略配置")
		self.cmf.select_menu(u"策略配置",u"认证强度")
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		
	u'''添加所有认证方式'''
	def select_all_auth(self,methdata):
		#获取全部认证方式文本
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		selem = self.getElem.find_element_with_wait_EC('id',self.ALL_METH_METHOD)
		select_list_text = self.selectElem.get_all_option_text(selem)
		
		options = selem.find_elements_by_tag_name("option")
		for option in options:
			if option.is_selected() == False:
				option.click()

		#判断文本是否为空
		if select_list_text != []:
			self.auth_add_button()
			self.set_ad_auth_ip(methdata[0])
			self.set_ad_auth_domian_name(methdata[1])
			self.set_radius_auth_ip(methdata[2])
			self.set_radius_auth_key(methdata[3])
			self.save_button()
			self.cmf.click_login_msg_button()
			time.sleep(3)

	u'''删除其他认证方式'''
	def del_auth_method(self):
		self.frameElem.from_frame_to_otherFrame('topFrame')
		self.cmf.select_menu(u"策略配置")
		self.cmf.select_menu(u"策略配置",u"认证强度")
		self.frameElem.from_frame_to_otherFrame('mainFrame')
		selem = self.getElem.find_element_with_wait("id", "select_globalAuthMethod")
		self.selectd_all_method(selem, '2', '1')
		self.auth_del_button()
		self.save_button()
		self.cmf.click_login_msg_button()