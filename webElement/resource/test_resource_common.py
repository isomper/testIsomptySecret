#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：217/7/18
#模块描述：资源
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsompSecret/common/")
from _icommon import getElement,selectElement,frameElement,commonFun
from _cnEncode import cnEncode

class Resource(object):

	# 添加按钮
	RESOURCE_ADD_BUTTON = "add_resource"
	#资源名称
	RESOURCE_NAME = "fortResourceName"
	#资源IP
	RESOURCE_IP = "fortResourceIp"
	#从IP
	RESOURCE_RESERVE_IP = "fortIps"
	#系统版本
	SYSTEM_VERSION = "fortVersion"
	#改密驱动名称
	CHANGE_PWD_DRIVER = "fortDriverName"
	#密码策略
	RESOURCE_STRATEGY_PWD = "fortStrategyPasswordId"
	#账号同步
	ACCOUNT_SYNCHRONIZE = "btn_high"
	#管理员账号
	ADMIN_ACCOUNT = "fortAdminAccount"
	#管理员口令
	ADMIN_PASSWORD = "fortAdminPassword"
	#确认口令
	ADMIN_REPASSWORD = "reFortAdminPassword"
	#保存按钮
	SAVE_BUTTON = "save_resource"
	#需要提权
	UP_SUPER = "up_super"
	#归属部门
	ATTRIBUTION_DEPARTMENT = "fortDepartmentName"
	#运维协议
	OPERATIONS_AGREEMENT = "fortOperationsProtocolId"
	#提权口令
	UP_SUPER_PWD = "fortUpSuperPassword"
	#确认口令
	UP_SUPER_CONFIRMPWD = "reFortUpSuperPassword"

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)
		self.cnEn = cnEncode()

	u'''点击删除资源按钮
	   Parameters:
	      - resourcename:传入的要编辑的资源名称
	'''
	def click_del_button(self, resourcename):
		rename = self.cnEn.is_float(resourcename)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		row = self.cmf.find_row_by_name(rename, "fortResourceName")
		del_xpath = "/html/body/form/div/div[8]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[7]/input[3]"
		self.getElem.find_element_wait_and_click("xpath", del_xpath)

	u'''点击添加或编辑资源按钮
	   Parameters:
	      - resourcename:传入的要编辑的资源名称，可不填
	'''
	def click_add_edit_button(self, resourcename='no'):
		rename = self.cnEn.is_float(resourcename)
		time.sleep(3)
		try:
			#如果资源名称等于no就点击添加按钮，否则点击编辑按钮
			if rename == 'no':
				self.frameElem.from_frame_to_otherFrame("mainFrame")
				return self.getElem.find_element_wait_and_click_EC("id", self.RESOURCE_ADD_BUTTON)
			else:
				self.frameElem.from_frame_to_otherFrame("mainFrame")
				row = self.cmf.find_row_by_name(rename, "fortResourceName")
				update_xpath = "/html/body/form/div/div[8]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[7]/input[2]"
				self.getElem.find_element_wait_and_click_EC("xpath", update_xpath)
		except Exception:
			print("Click the add or edit resource button to fail")

	u'''选择资源类型
	   parameter:
	       - reName:选取的资源类型名称
	'''
	def select_resource_type(self, reName):

		try:
			self.frameElem.from_frame_to_otherFrame("artIframe")
			self.select_resource_type_common(reName)
			self.click_ok_button()
		except Exception:
			print ("Failed to select the resource type")

	u'''点击确定按钮'''
	def click_ok_button(self):
		self.frameElem.switch_to_content()
		self.getElem.find_element_wait_and_click_EC("id", "okButton")

	u'''填写资源名称
	   parameter:
	       - resourcename:资源名称
	'''
	def set_resource_name(self, resourcename):
		try:
			rename = self.cnEn.is_float(resourcename)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', self.RESOURCE_NAME)
			self.getElem.find_element_wait_and_sendkeys('id', self.RESOURCE_NAME, rename)
		except Exception as e:
			print "resourcename is error :" + str(e)

	u'''填写资源IP
	   parameter:
	       - ip:ip地址
	'''
	def set_resource_ip(self, ip):
		try:
			ipdress = self.cnEn.is_float(ip)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', self.RESOURCE_IP)
			self.getElem.find_element_wait_and_sendkeys('id', self.RESOURCE_IP, ipdress)
			time.sleep(5)
		except Exception as e:
			print "resourceip is error :" + str(e)

	u'''填写归属部门
	   parameter:
	       - deptname:部门名称
	'''
	def set_depart(self, deptname):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		depart = self.cnEn.is_float(deptname)
		time.sleep(3)
		self.select_depart_common(self.ATTRIBUTION_DEPARTMENT, "tree_1_switch", depart)

	u'''选择所有运维协议'''
	def select_all_agreement(self):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			agreements = self.driver.find_elements_by_name(self.OPERATIONS_AGREEMENT)
			#第几次勾选
			check_times = 0

			for agreement in agreements:
				self.driver.implicitly_wait(10)
				check_times = check_times + 1
				if check_times != 1:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					if agreement.get_attribute("checked") != "checked":
						agreement.click()
		except Exception as e:
			print "Agreement select error:" + str(e)

	u'''选择运维协议
	   parameter:
	       - agreement:协议的id属性中协议名称
	'''
	def select_agreement(self, agreement):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		agreementid = "fortOperationsProtocolId" + str(agreement)
		self.getElem.find_element_with_wait_clickable_and_click("id", agreementid)

	u'''填写端口
	   parameter:
	       - agreement:协议名称
	       - port:端口
	'''
	def set_port(self, agreement, port):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		porttext = self.cnEn.is_float(port)
		portid = "fortResourceOperationsProtocolPort" + str(agreement)
		self.getElem.find_element_wait_and_clear("id", portid)
		self.getElem.find_element_wait_and_sendkeys("id", portid, porttext)

	u'''清空端口
	   parameter:
	       - agreement:协议名称
	'''
	def clear_port(self, agreement):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		portid = "fortResourceOperationsProtocolPort" + str(agreement)
		self.getElem.find_element_wait_and_clear("id", portid)

	u'''填写从IP
	   parameter:
	       - fortIps:从ip地址
	'''
	def set_resource_fortIps(self, fortIps):
		try:
			fortIp = self.cnEn.is_float(fortIps)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', self.RESOURCE_RESERVE_IP)
			self.getElem.find_element_wait_and_sendkeys('id', self.RESOURCE_RESERVE_IP, fortIp)
		except Exception as e:
			print "fortIps is error:" + str(e)

	u'''填写系统版本
	   parameter:
	       - sysVersion:系统版本
	'''
	def set_sys_version(self, sysVersion):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			version = self.cnEn.is_float(sysVersion)
			self.getElem.find_element_wait_and_clear('id', self.SYSTEM_VERSION)
			self.getElem.find_element_wait_and_sendkeys('id', self.SYSTEM_VERSION, version)
		except Exception as e:
			print "system_version is error:" + str(e)

	u'''填写改密驱动名称
	   parameter:
	       - driverName:改密驱动名称
	'''
	def set_changePwd_driver(self, driverName):
		try:
			drivername = self.cnEn.is_float(driverName)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', self.CHANGE_PWD_DRIVER)
			self.getElem.find_element_wait_and_sendkeys('id', self.CHANGE_PWD_DRIVER, drivername)
		except Exception as e:
			print "change_pwd_driver is error:" + str(e)

	u'''选择密码策略
	   parameter:
	       - text:密码策略的名称
	'''
	def select_pwd_strategy(self, text):
		try:
			pwdtext = self.cnEn.is_float(text)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			pwd_strategy = self.getElem.find_element_with_wait_EC('id', self.RESOURCE_STRATEGY_PWD)
			self.selectElem.select_element_by_visible_text(pwd_strategy, pwdtext)
		except Exception as e:
			print "Pwd strategy select error:" + str(e)

	u'''点击账号同步'''
	def click_account_sync(self):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_click_EC('id', self.ACCOUNT_SYNCHRONIZE)
		except Exception as e:
			print "account sync element is not available:" + str(e)

	u'''设置管理员账号
	   parameter:
	       - adminAccount:管理员账号
	'''
	def set_admin_account(self, adminAccount):
		try:
			account = self.cnEn.is_float(adminAccount)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', self.ADMIN_ACCOUNT)
			self.getElem.find_element_wait_and_sendkeys('id', self.ADMIN_ACCOUNT, account)
		except Exception as e:
			print "Admin account error:" + str(e)

	u'''设置管理员口令
	   parameter:
	       - adminPwd:管理员口令
	'''
	def set_admin_pwd(self, adminPwd):
		try:
			pwd = self.cnEn.is_float(adminPwd)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', self.ADMIN_PASSWORD)
			self.getElem.find_element_wait_and_sendkeys('id', self.ADMIN_PASSWORD, pwd)
		except Exception as e:
			print "Admin password error :" + str(e)

	u'''口令确认
	   parameter:
	       - confirmPwd:口令确认
	'''
	def set_confirm_pwd(self, confirmPwd):
		try:
			confirm = self.cnEn.is_float(confirmPwd)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', self.ADMIN_REPASSWORD)
			self.getElem.find_element_wait_and_sendkeys('id', self.ADMIN_REPASSWORD, confirm)
		except Exception as e:
			print "confirm Password is error :" + str(e)

	u'''勾选提权框'''
	def click_up_super(self):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_click_EC('id', self.UP_SUPER)
		except Exception as e:
			print "Fail to check the option :" + str(e)

	u'''设置提权口令
	   parameter:
	       - superPwd:提权口令
	'''
	def set_super_pwd(self, superPwd):
		try:
			superpwd = self.cnEn.is_float(superPwd)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', self.UP_SUPER_PWD)
			self.getElem.find_element_wait_and_sendkeys('id', self.UP_SUPER_PWD, superpwd)
		except Exception as e:
			print "Admin password error :" + str(e)

	u'''提权口令确认
	   parameter:
	       - upcfPwd:提权口令确认
	'''
	def set_super_confirm_pwd(self, upcfPwd):
		try:
			upcfpwd = self.cnEn.is_float(upcfPwd)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', self.UP_SUPER_CONFIRMPWD)
			self.getElem.find_element_wait_and_sendkeys('id', self.UP_SUPER_CONFIRMPWD, upcfpwd)
		except Exception as e:
			print "confirm Password is error :" + str(e)

	u'''填写提权口令提示符
	   parameter:
	       - upcfPwd:提权口令确认
	'''
	def set_super_prompt(self):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', "fortUpSuperPasswordPrompt")
			self.getElem.find_element_wait_and_sendkeys('id', "fortUpSuperPasswordPrompt", "assword:")
		except Exception as e:
			print "confirm Password is error :" + str(e)

	u'''填写描述信息
	   parameter:
	       - description:信息内容
	'''
	def set_description(self, description):
		try:
			descri = self.cnEn.is_float(description)
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_clear('id', "fortDescription")
			self.getElem.find_element_wait_and_sendkeys('id', "fortDescription", descri)
		except Exception as e:
			print "confirm Password is error :" + str(e)

	u'''点击保存按钮'''
	def click_save_button(self):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			time.sleep(3)
			self.getElem.find_element_wait_and_click_EC("id", self.SAVE_BUTTON)
		except Exception as e:
			print "resource save button error:" + str(e)

	u'''点击保存按钮'''
	def resoure_save_button(self):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			time.sleep(6)
			self.getElem.find_element_wait_and_click_EC("id", "spanid")
			self.getElem.find_element_with_wait_EC("classname", "ip_succ")
			self.getElem.find_element_wait_and_click_EC("id", self.SAVE_BUTTON)
		except Exception as e:
			print "resource save button error:" + str(e)

	u'''点击查询按钮'''
	def click_resource_query(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "fort_resource")

	u'''点击重置按钮'''
	def click_reset(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "resetting")

	u'''部门查询
	   parameter:
	       - deptname:部门名称
	'''
	def query_depart(self, deptname):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		depart = self.cnEn.is_float(deptname)
		self.select_depart_common("resource_department_name", "cc_1_switch", depart)

	u'''勾选部门子节点查询'''
	def click_child_node(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		time.sleep(1)
		self.getElem.find_element_wait_and_click_EC('id', "resource_department_name")
		time.sleep(1)
		self.getElem.find_element_wait_and_click_EC("id", "query_child_node")

	u'''查询部门清空'''
	def query_depart_clear(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "clean_tree_data")

	u'''资源类型查询
	   parameter:
	       - firstname:一级资源资源类型名称
		   - secondname:二级资源资源类型名称
		   - treename:三级资源资源类型名称
	'''
	def query_type(self, firstname, secondname='no', treename='no'):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_click_EC('id', "resource_type_name")
			#点击一级树
			if secondname == 'no' and treename == 'no':
				self.getElem.find_element_with_wait_clickable_and_click("link", firstname)

			#点击二级树
			if secondname != 'no' and treename == 'no':
				#获取span标签的class和id
				spanclass, spanid = self.get_span_class(firstname)
				#判断span标签的class属性是否为闭合状态
				if spanclass == "button level0 switch roots_close" or spanclass == "button level0 switch center_close" or spanclass == "button level0 switch bottom_close":
					#开启闭合状态
					self.getElem.find_element_wait_and_click_EC("id", spanid)

				self.getElem.find_element_with_wait_clickable_and_click("link", secondname)

			#点击三级树
			if secondname != 'no' and treename != 'no':
				#获取一级树span标签的class和Id
				spanclass1, spanid1 = self.get_span_class(firstname)
				#判断span标签的class属性是否为闭合状态
				if spanclass1 == "button level0 switch roots_close" or spanclass1 == "button level0 switch center_close" or spanclass1 == "button level0 switch bottom_close":
					#开启闭合状态
					self.getElem.find_element_wait_and_click_EC("id", spanid1)
				#获取二级树span标签的class和Id
				spanclass2, spanid2 = self.get_span_class(secondname)
				#判断span标签的class属性是否为闭合状态
				if spanclass2 == "button level1 switch center_close" or spanclass2 == "button level1 switch bottom_close":
					#开启闭合状态
					self.getElem.find_element_wait_and_click_EC("id", spanid2)

				self.getElem.find_element_with_wait_clickable_and_click("link", treename)
		except Exception:
			print ("Failed to select the resource type")

	u'''获取span标签的class和id属性
	   parameter:
	       - text:选取的资源类型名称
	   Return:返回span标签的class和id属性
	'''
	def get_span_class(self, text):

		selem = self.getElem.find_element_with_wait_EC("link", text)
		idelm = selem.get_attribute("id")
		#获取span标签的id
		spanid = str(idelm[:-1]) + "switch"
		#获取span标签的对象
		spanelem = self.getElem.find_element_with_wait_EC("id", spanid)
		#获取span标签的class
		spanclass = spanelem.get_attribute("class")
		return spanclass, spanid

	u'''获取资源类型闭合按钮的class属性
	   parameter:
	       - idname:闭合按钮id
	'''
	def get_class_attribute(self, idname):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		switch = self.getElem.find_element_with_wait_EC("id", idname)
		switchclass = switch.get_attribute("class")
		return switchclass

	u'''查询资源类型清空'''
	def query_resource_type_clear(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "clean_tree_data_two")

	u'''查询资源IP或名称
	   parameter:
	       - value:资源IP或名称
	'''
	def query_ip_rename(self, value):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_sendkeys("id", "fortResourceIpOrName", value)

	u'''选择资源类型公共方法
	   parameter:
	       - typename:资源类型名称
	'''
	def select_resource_type_common(self, reName):

		#获取页面展开的一级和二级菜单的所有a标签对象
			elems = self.driver.find_elements_by_tag_name("a")

			#循环所有对象
			for elem in elems:

				#获取a标签class属性
				elemclass = elem.get_attribute("class")
				#获取a标签id属性
				elemid = elem.get_attribute("id")

				#判断a标签class属性是否为level
				if elemclass == "level1":

					#获取span标签的id
					spanid = str(elemid[:-1]) + "switch"
					#获取span标签的对象
					spanelem = self.getElem.find_element_with_wait_EC("id", spanid)
					#获取span标签的class
					spanclass = spanelem.get_attribute("class")

					#判断span标签的class属性是否为闭合状态
					if spanclass == "button level1 switch bottom_close" or spanclass == "button level1 switch center_close":
						#开启闭合状态
						self.getElem.find_element_wait_and_click_EC("id", spanid)
						time.sleep(2)
						#循环开启闭合状态下的a标签进行选择资源类型
						click_resource_type = self.two_level_tree_cycle(reName)
						#判断返回的类型是否为True
						if click_resource_type == True:
							break

	u'''选择部门公共方法
	   parameter:
	       - idname:填写框id
	       - swithid:部门展开按钮id
	       - deptname:部门名称
	'''
	def select_depart_common(self, idname, swithid, deptname):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			time.sleep(1)
			self.getElem.find_element_wait_and_click_EC('id', idname)
			time.sleep(2)
			self.getElem.find_element_wait_and_click_EC('id', swithid)
			time.sleep(2)

			#获取所有a标签的对象
			elems = self.driver.find_elements_by_tag_name("a")

			for elem in elems:
				elemtext = elem.get_attribute("title")
				elemid = elem.get_attribute("id")

				if deptname == elemtext:
					self.getElem.find_element_wait_and_click("id", elemid)
					break

		except Exception as e:
			print "Department select error:" + str(e)

	u'''循环选择二级菜单下资源类型
	   parameter:
	       - reName:选取的资源类型名称
	   Return:返回True代表点击了资源类型
	'''
	def two_level_tree_cycle(self, reName):

		try:
			#获取a标签的所有对象
			elemas = self.driver.find_elements_by_tag_name("a")

			#循环所有对象
			for elema in elemas:

				#获取a标签title属性
				atext = elema.get_attribute("title")
				#获取a标签id属性
				aid = elema.get_attribute("id")

				#判断所选择的的资源类型和a标签的title是否相等
				if atext == reName:
					time.sleep(2)
					self.getElem.find_element_wait_and_click_EC("id", aid)
					#一个标志已经点击资源类型
					return True

		except Exception:
			print("Select the resource type under the two menu")

	u'''点击账号列表'''
	def click_account_list(self):

		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "account_list")