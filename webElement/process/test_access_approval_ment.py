# -*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：访问审批
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys, time

reload(sys)
sys.setdefaultencoding('utf-8')
from datetime import datetime
from xlrd import xldate_as_tuple

sys.path.append("/testIsompSecret/common/")
from _log import log
from _icommon import getElement, selectElement, frameElement, commonFun
from _cnEncode import cnEncode

sys.path.append("/testIsompSecret/webElement/authorization")
from authrizationElement import AuthorizationPage

sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

class Accapproval(object):

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)
		self.log = log()
		self.cnEn = cnEncode()
		self.loginElem = loginPage(self.driver)
		self.authElem = AuthorizationPage(self.driver)

	u'''点击授权操作列访问审批按钮
		parameters:
			name : 授权名称
	'''
	def click_access_approval_button(self, name):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.authElem.operate_access_approval(name)

	u'''勾选用户
	   parameter:
		   - listuser:用户集合
	'''
	def check_user(self, listuser):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		# 获取table对象
		tableelem = self.getElem.find_element_with_wait_EC("id", "user_table")
		# 获取table对象下的所有tr
		trelems = tableelem.find_elements_by_tag_name("tr")
		# 位于第几行
		line = 0

		# 循环所有tr
		for trelem in trelems:
			line += 1
			# 找到tr下所有td对象
			tds = trelem.find_elements_by_tag_name("td")
			# 获取td[2]的文本
			tdtext = tds[1].text
			for user in listuser.split():
				if tdtext == user:
					xpath = "/html/body/div[3]/div[2]/table/tbody/tr[" + str(line) + "]/td[1]/li/input"
					self.getElem.find_element_wait_and_click_EC("xpath", xpath)
					break

	u'''设置级别中的审批人个数
		parameters :
		    level : 级别
		    value : option的value值
	'''
	def select_approval_num(self, level, value):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		relevel = self.cnEn.is_float(level)
		revalue = self.cnEn.is_float(value)
		level_xpath = "/html/body/div/div[3]/div[" + relevel + "]/div[3]/select"
		selem = self.getElem.find_element_with_wait_EC('xpath', level_xpath)
		self.selectElem.select_element_by_value(selem, revalue)

	u'''选择进行单点登录的资源并且返回该资源位于第几行
		parameters :
		    rename : 资源名称
		return: row代表资源名称位于第几行
	'''
	def select_resoure_sso(self, rename):
		rname = self.cnEn.is_float(rename)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		row = self.find_name_by_row(rname, "fortResourceName")
		rename_xpath = "/html/body/div[1]/div[7]/div[2]/div/table/tbody/tr[" + str(row * 2 - 1) + "]/td[3]"
		self.getElem.find_element_wait_and_click_EC("xpath", rename_xpath)
		return row

	u'''点击访问审批或紧急运维图标
		parameters :
		    rename : 资源名称
		    statu : 1代表访问审批，2代表紧急运维
	'''
	def click_access_approval_icon(self, rename, statu):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		rname = self.cnEn.is_float(rename)
		status = self.cnEn.is_float(statu)
		row = self.select_resoure_sso(rname)
		xpath = "/html/body/div[1]/div[7]/div[2]/div/table/tbody/tr[" + str(
			row * 2) + "]/td/div/table/tbody/tr/td[2]/a[" + str(status) + "]/img"
		time.sleep(2)
		self.getElem.find_element_wait_and_click_EC("xpath", xpath)

	u'''选择进行资源账号
		parameters :
		    rename : 资源名称
		    reactname : 资源账号名称
	'''
	def select_resoure_account(self, rename, reactname):
		rname = self.cnEn.is_float(rename)
		actname = self.cnEn.is_float(reactname)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		row = self.find_name_by_row(rname, "fortResourceName")
		rename_xpath = "/html/body/div[1]/div[7]/div[2]/div/table/tbody/tr[" + str(row * 2 - 1) + "]/td[6]/select"
		selem = self.getElem.find_element_with_wait_EC("xpath", rename_xpath)
		self.selectElem.select_element_by_visible_text(selem, actname)

	u'''判断名称是否存在
		Parameters:
			- namevalue:传入的要被查询名称
			- name:表格列的name属性
		return：true代表存在，false代表不存在
	'''
	def namevalue_is_exsit(self, namevalue, name):
		nameval = self.cnEn.is_float(namevalue)
		namesex = self.cnEn.is_float(name)
		isExsit = False
		text_list = self.driver.find_elements_by_name(namesex)
		for fortNameValue in text_list:
			fortNameValue_text = fortNameValue.text
			if fortNameValue_text == nameval:
				isExsit = True
				break
		return isExsit

	u'''查询已存在名称位于第几行
		Parameters:
			- namevalue:传入的要被查询名称
			- name:表格列的name属性
		return：定位该名称位于第几行
	'''
	def find_name_by_row(self, namevalue, name):
		nameval = self.cnEn.is_float(namevalue)
		namesex = self.cnEn.is_float(name)
		row = 0
		if self.namevalue_is_exsit(nameval, namesex):
			text_list = self.driver.find_elements_by_name(namesex)
			for fortNameValue in text_list:
				row = row + 1
				fortNameValue_text = fortNameValue.text
				if fortNameValue_text == nameval:
					break
		return row

	u'''填写审批的描述
		Parameters:
			- description:描述内容
	'''
	def set_operation_description(self, description):
		descri = self.cnEn.is_float(description)
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_clear("id", "fortDescription")
		self.getElem.find_element_wait_and_sendkeys("id", "fortDescription", descri)

	u'''点击确定按钮'''
	def click_sure_button(self):
		self.frameElem.switch_to_content()
		self.getElem.find_element_wait_and_click_EC("id", "okButton")

	u'''点击提交按钮'''
	def click_submit(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "save_process_approval")

	u'''用户登录
		Parameters:
			- listuser:用户登录集
	'''
	def user_login(self, listuser):
		users = listuser.split()
		self.frameElem.switch_to_content()
		time.sleep(2)
		self.loginElem.set_login_method(users[0])
		self.loginElem.set_login_username(users[1])
		self.loginElem.set_login_pwd(users[2])
		time.sleep(1)
		self.loginElem.click_login_button()

	u'''点击消息提示'''
	def click_message_prompt(self):
		self.frameElem.from_frame_to_otherFrame('topFrame')
		self.getElem.find_element_wait_and_click_EC("id", "link_tc")

	u'''点击全部信息'''
	def click_all_message(self):
		self.frameElem.from_frame_to_otherFrame('topFrame')
		self.getElem.find_element_wait_and_click_EC("xpath", "/html/body/div[3]/div/div/div[1]/a")

	u'''通过申请时间点击要审批的信息
		Parameters:
			- applytime:申请时间
	'''
	def click_approval_by_message(self, applytime):
		self.frameElem.from_frame_to_otherFrame('mainFrame')
		row = self.find_name_by_row(applytime, "fortTime")
		xpath = "/html/body/div/div[2]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[5]/lable"
		self.getElem.find_element_wait_and_click_EC("xpath", xpath)

	u'''通过流程号点击要审批的信息
		Parameters:
			- number:流程号
	'''
	def click_approval_by_number(self, number):
		self.frameElem.from_frame_to_otherFrame('mainFrame')
		row = self.find_name_by_row(number, "fortProcessInstanceId")
		xpath = "/html/body/form/div/div[7]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[8]/input[1]"
		self.getElem.find_element_wait_and_click_EC("xpath", xpath)

	u'''消息弹框是否同意审批
		Parameters:
			- status:1代表同意审批，2代表拒绝审批
	'''
	def message_is_agree_approval(self, status):
		self.frameElem.from_frame_to_otherFrame('artIframe')
		self.is_agree_common(status)

	u'''流程控制是否同意审批
		Parameters:
			- status:1代表同意审批，2代表拒绝审批
	'''
	def process_is_agree_approval(self, status):
		self.frameElem.from_frame_to_otherFrame('mainFrame')
		self.is_agree_common(status)

	u'''是否同意审批公共方法
		Parameters:
			- status:1代表同意审批，2代表拒绝审批
	'''
	def is_agree_common(self, status):
		statu = self.cnEn.is_float(status)
		if statu == '1':
			self.getElem.find_element_wait_and_click_EC("id", "yes")
		elif statu == '2':
			self.getElem.find_element_wait_and_click_EC("id", "no")

	u'''填写消息中审批申请单的描述
		Parameters:
			- description:描述内容
	'''
	def set_message_apply_description(self, description):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.set_apply_description_common(description)

	u'''填写流程控制中审批申请单的描述
		Parameters:
			- description:描述内容
	'''
	def set_process_apply_description(self, description):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.set_apply_description_common(description)

	u'''填写消息中审批申请单的描述公共方法
		Parameters:
			- description:描述内容
	'''
	def set_apply_description_common(self, description):
		descri = self.cnEn.is_float(description)
		self.getElem.find_element_wait_and_clear("id", "fortApprovalOpinions")
		self.getElem.find_element_wait_and_sendkeys("id", "fortApprovalOpinions", descri)

	u'''点击关闭按钮'''
	def click_close_button(self):
		self.frameElem.switch_to_content()
		self.getElem.find_element_wait_and_click_EC("classname", "aui_close")

	u'''获取申请历史中最新的申请时间'''
	def get_new_apply_time(self):
		self.frameElem.from_frame_to_otherFrame("topFrame")
		self.cmf.select_menu(u"流程控制", u"申请历史")
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		selem = self.getElem.find_element_with_wait_EC("xpath","/html/body/form/div/div[6]/div[2]/div/table/tbody/tr[1]/td[3]")
		applytime = selem.get_attribute('textContent')
		return applytime

	u'''获取申请历史中最新的流程号'''
	def get_new_process_number(self):
		self.frameElem.from_frame_to_otherFrame("topFrame")
		time.sleep(2)
		self.cmf.select_menu(u"流程控制", u"申请历史")
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		selem = self.getElem.find_element_with_wait_EC("xpath","/html/body/form/div/div[6]/div[2]/div/table/tbody/tr[1]/td[2]")
		number = selem.get_attribute('textContent')
		time.sleep(3)
		return number

	u'''返回退出公共方法'''
	def back_quit_common(self):
		self.cmf.back()
		self.driver.implicitly_wait(5)
		self.loginElem.quit()

	u'''点击确定按钮'''
	def click_message_button(self):
		self.driver.switch_to_default_content()
		time.sleep(2)
		self.frame_public_method(u"提示", u"提示×保存成功！确定")

	u'''弹窗的公用方法
		Parameters:
			- pagetext：页面弹框的title文本
			- tabletext：表格文本
	'''
	def frame_public_method(self, pagetext, tabletext):

		self.frameElem.switch_to_content()
		#获取title集合
		divselems = self.driver.find_elements_by_class_name("aui_title")
		#获取table集合
		tableselems = self.driver.find_elements_by_class_name("aui_dialog")
		#是否点击确定按钮标识，如果为True说明已经点击确定按钮
		step = False

		#循环table集合
		for table in tableselems:
			#获取table文本
			test = table.get_attribute('textContent')
			#循环title集合
			for divselem in divselems:
				#获取title文本
				messagetext = divselem.get_attribute('textContent')
				if messagetext == pagetext and test == tabletext:
					table.find_element_by_class_name("aui_state_highlight").click()
					step = True
					break
			if step is True:
				break

	u'''勾选审批人
		Parameters:
			- approvers：审批者集合
	'''
	def check_the_approver(self, approvers):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		#获取span集合
		spanselems = self.driver.find_elements_by_tag_name("span")
		apvers = approvers.split()
		#循环审批者集合进行勾选操作
		for approver in apvers:
			for span in spanselems:
				#获取span的内容
				test = span.get_attribute('textContent')
				if test == approver:
					span.find_element_by_tag_name("input").click()
					break

	u'''紧急运维中全选审批人'''
	def check_all_approver(self):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		#获取input集合
		inputselems = self.driver.find_elements_by_class_name("choseAll")
		for input in inputselems:
			input.click()

	u'''点击刷新图标
		parameters :
			rename : 资源名称
	'''
	def click_refresh_icon(self, rename):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		rname = self.cnEn.is_float(rename)
		row = self.find_name_by_row(rname, "fortResourceName")
		xpath = "/html/body/div[1]/div[7]/div[2]/div/table/tbody/tr[" + str(
			row * 2) + "]/td/div/table/tbody/tr/td[3]/a/img"
		isExsit = self.getElem.is_element_exsit("xpath", xpath)

		if isExsit == True:
			self.getElem.find_element_wait_and_click_EC("xpath", xpath)

	u'''校验图标
		parameters :
			- rename:资源名称
	'''
	def check_access_ico_len(self, rename):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		time.sleep(5)
		row = self.select_resoure_sso(rename)
		self.click_refresh_icon(rename)
		ico_xpath = "/html/body/div[1]/div[7]/div[2]/div[1]/table/tbody/tr[" + str(
			row * 2) + "]/td/div/table/tbody/tr/td[2]"
		selem = self.getElem.find_element_with_wait_EC("xpath", ico_xpath)
		selems = selem.find_elements_by_tag_name("a")
		lengh = len(selems)
		if lengh > 2:
			self.log.log_detail(u"访问审批已同意申请，可进行单点登录操作", True)
		else:
			self.log.log_detail(u"访问审批已拒绝申请，不可进行单点登录操作", True)

	u'''申请人发送访问审批申请
		Parameters:
			- data:excel中的一行数据
	'''
	def send_access_approval_applicant(self, data):
		# 时间控件的fram的xpath
		fxpath = "//iframe[@hidefocus='true']"
		# 日期控件table的xpath路径
		txpath = "/html/body/div/div[3]/table"
		self.select_resoure_account(data[1], data[2])
		time.sleep(2)
		self.click_access_approval_icon(data[1], data[3])
		self.frameElem.from_frame_to_otherFrame("artIframe")
		time.sleep(2)
		self.cmf.select_time("fortStartTime", fxpath, data[4], data[5], txpath)
		self.frameElem.from_frame_to_otherFrame("artIframe")
		# 转成datetime对象
		date = datetime(*xldate_as_tuple(data[9], 0))
		endtime = date.strftime('%Y-%m-%d %H:%M:%S')
		status = self.cnEn.is_float(data[7])
		self.cmf.select_time("fortEndTime", fxpath, status, data[8], txpath, endtime)
		self.set_operation_description(data[10])
		self.log.log_detail(data[0], True)
		self.click_sure_button()
		self.click_message_button()

	u'''审批人通过消息进行审批
		Parameters:
			- acpData:审批人进行审批的数据
			- applytime:申请时间
	'''
	def approval_by_message_approver(self, acpData, applytime):
		for dataRow in range(len(acpData)):
			data = acpData[dataRow]
			# 如果不是第1行,读取数据
			if dataRow != 0:
				self.user_login(data[0])
				self.click_message_prompt()
				self.click_all_message()
				self.click_approval_by_message(applytime)
				if data[1] != 'no':
					self.message_is_agree_approval(data[1])
				if data[2] != 'no':
					self.set_message_apply_description(data[2])
				if data[1] == 'no' and data[2] == 'no':
					self.click_close_button()
					self.loginElem.quit()
					continue
				self.click_sure_button()
				self.loginElem.quit()

	u'''审批人通过流程控制进行审批
		Parameters:
			- acpData:审批人进行审批的数据
			- number:流程号
	'''
	def approval_by_approver(self, acpData, number):
		for dataRow in range(len(acpData)):
			data = acpData[dataRow]
			# 如果不是第1行,读取数据
			if dataRow != 0:
				self.user_login(data[1])
				time.sleep(2)
				self.frameElem.from_frame_to_otherFrame("topFrame")
				self.cmf.select_menu(u"流程控制", u"流程任务")
				time.sleep(2)
				if dataRow == 2 or dataRow == 3:
					# 获取第一行数据的第1个字符
					firststr = str(acpData[1][2])
					if firststr == '2.0':
						self.loginElem.quit()
						self.log.log_detail(data[0], True)
						continue
				self.click_approval_by_number(number)
				if data[2] != 'no':
					self.process_is_agree_approval(data[2])
				if data[3] != 'no':
					self.set_process_apply_description(data[3])
				if data[2] == 'no' and data[3] == 'no':
					self.back_quit_common()
					self.log.log_detail(data[0], True)
					continue
				self.log.log_detail(data[0], True)
				self.click_submit()
				self.cmf.click_login_msg_button()
				self.back_quit_common()

	u'''申请人发送紧急运维申请
		Parameters:
			- data:excel中的一行数据
	'''
	def send_urgent_operation_applicant(self, data):

		self.select_resoure_account(data[1], data[2])
		self.click_access_approval_icon(data[1], data[3])
		#全选审批人
		self.check_all_approver()
		#可单独选择一级二级审批人
		# self.check_the_approver(data[4])
		self.set_operation_description(data[5])
		self.log.log_detail(data[0], True)
		self.click_sure_button()
		self.click_message_button()
