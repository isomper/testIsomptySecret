#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/8/25
#模块描述：命令规则
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
import  SendKeys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsompSecret/common/")
from _fileRead import fileRead
from _icommon import getElement,selectElement,frameElement,commonFun
from _cnEncode import cnEncode
sys.path.append("/testIsompSecret/webElement/process/")
from test_access_approval_ment import Accapproval
sys.path.append("/testIsompSecret/webElement/sso")
from ssoElement import SsoPage

class CommandRule(object):
	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)
		self.cnEn = cnEncode()
		self.acproval = Accapproval(driver)
		self.ssoElem = SsoPage(self.driver)

	u'''左边框点击规则
	   Parameters:
	   - statu:左边框点击，0代表点击命令规则，1代表点击时间规则，2代表点击地址规则，3代表点击资源时间规则
	'''
	def click_left_rule(self, statu):
		time.sleep(2)
		self.frameElem.from_frame_to_otherFrame("leftFrame")
		if statu == 0:
			#点击命令规则
			self.getElem.find_element_wait_and_click_EC("id", "url0")
		elif statu == 1:
			#点击时间规则
			self.getElem.find_element_wait_and_click_EC("id", "url1")
		elif statu == 2:
			#点击地址规则
			self.getElem.find_element_wait_and_click_EC("id", "url2")
		elif statu == 3:
			#点击资源时间规则
			self.getElem.find_element_wait_and_click_EC("id", "url3")

	u'''点击添加'''
	def click_add_button(self):
		time.sleep(2)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("classname", "btn_tj")

	u'''点击删除'''
	def click_del_command(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "delete_rule_command")

	u'''点击复选框全选'''
	def check_all(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "checkbox")

	u'''点击部署'''
	def click_deploy_command(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "updateAllState")

	u'''选择命令类型
       Parameters:
            - value:select选项中的value属性值,0代表黑名单,2代表审批命令
    '''
	def select_command_type(self, value):
		valu = self.cnEn.is_float(value)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		selem = self.getElem.find_element_with_wait_EC("id", "fortRuleCommandTypeList")
		self.selectElem.select_element_by_value(selem, valu)

	u'''填写命令
	   Parameters:
            - command:命令内容
	'''
	def set_command(self, command):
		comm = self.cnEn.is_float(command)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear("id", "new_command")
		self.getElem.find_element_wait_and_sendkeys("id", "new_command", comm)

	u'''清空已添加命令'''
	def clear_command(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		inputelems = self.driver.find_elements_by_name("passwordTable")
		for inputelem in inputelems:
			inputelem.click()

	u'''点击添加命令按钮'''
	def click_add_command_button(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "add_command")

	u'''测试命令
	   Parameters:
	   - command:命令内容
	'''
	def set_test_command(self, command):
		comm = self.cnEn.is_float(command)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear("id", "test")
		self.getElem.find_element_wait_and_sendkeys("id", "test", comm)

	u'''点击测试命令按钮'''
	def click_test_command_button(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "test_command")

	u'''点击添加用户按钮'''
	def click_add_users_button(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "btn_tjyh")

	u'''点击添加用户组按钮'''
	def click_add_usergroup_button(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "btn_tjyhz")

	u'''点击添加资源按钮'''
	def click_add_resource_button(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "btn_tjzyzy")

	u'''点击添加资源组按钮'''
	def click_add_regroup_button(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "btn01_tjyhz")

	u'''点击添加资源账号按钮'''
	def click_add_reaccount_button(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "btn_tjzy")

	u'''点击删除资源按钮'''
	def click_del_resource_button(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "del_resource")

	u'''点击删除资源账号按钮'''
	def click_del_reaccount_button(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "del_account")

	u'''点击保存按钮'''
	def click_save_command(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "save_rule_command")

	u'''点击返回按钮'''
	def click_back_command(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "history_skip")

	u'''点击审批人按钮'''
	def click_approver_command(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "btn_tjspr")

	u'''点击用户检索按钮'''
	def click_check_user(self):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_click_EC("id", "quick_user")

	u'''点击资源检索按钮'''
	def click_check_resource(self):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_click_EC("id", "quick_query")

	u'''勾选全部用户'''
	def check_all_user(self):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.click_check_user()
		self.getElem.find_element_wait_and_click_EC("id", "user_check_all")
		self.check_sure_button()

	u'''勾选全部资源'''
	def check_all_resource(self):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.click_check_resource()
		self.getElem.find_element_wait_and_click_EC("id", "resource_check_all")
		self.check_sure_button()

	u'''点击确定按钮'''
	def check_sure_button(self):
		self.frameElem.switch_to_content()
		self.getElem.find_element_wait_and_click_EC("id", "okButton")

	u'''填写插入行数
	   Parameters:
	   - row:行数
	'''
	def set_row_command(self, row):
		rows = self.cnEn.is_float(row)
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_clear("id", "rows")
		self.getElem.find_element_wait_and_sendkeys("id", "rows", rows)

	u'''点击插入行数的返回按钮'''
	def click_cancel_button(self):
		self.frameElem.switch_to_content()
		self.getElem.find_element_wait_and_click_EC("id", "cancelButton")

	u'''勾选用户
	   parameter:
		   - listuser:用户集合
	'''
	def check_user_command(self, listuser):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		# 获取table对象
		tableelem = self.getElem.find_element_with_wait_EC("id", "user_table")
		self.check_common(tableelem, listuser)

	u'''勾选资源
	   parameter:
		   - listresource:资源集合
	'''
	def check_resource_command(self, listresource):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		# 获取table对象
		tableelem = self.getElem.find_element_with_wait_EC("id", "resourceTable")
		self.check_common(tableelem, listresource)

	u'''勾选用户或者资源公共方法
	   parameter:
		   - tableelem:表属性对象
		   - lists:用户集合
	'''
	def check_common(self, tableelem, lists):
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
			for user in lists.split():
				if tdtext == user:
					xpath = "/html/body/div[3]/div[2]/table/tbody/tr[" + str(line) + "]/td[1]/li/input"
					self.getElem.find_element_wait_and_click_EC("xpath", xpath)
					break

	u'''勾选用户组
	   parameter:
		   - listuser:用户集合
	'''
	def check_usergroup_command(self, usergroups):
		self.check_group_common("userGroup_1_switch", "userGroup", usergroups, "userGroup_")

	u'''勾选资源组
	   parameter:
		   - listuser:用户集合
	'''
	def check_regroup_command(self, regroups):
		self.check_group_common("resourceGroup_1_switch", "resourceGroup", regroups, "resourceGroup_")

	u'''勾选组的公共方法
	   parameter:
		   - extendid:闭合按钮的id属性
		   - ulid:ul的id属性
		   - groups:组集合
		   - idfirst:span标签的id属性数字前面的字符
	'''
	def check_group_common(self, extendid, ulid, groups, idfirst):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_click_EC("id", extendid)
		# 获取ul对象
		ulelem = self.getElem.find_element_with_wait_EC("id", ulid)
		# 获取ul对象下的所有a
		aelems = ulelem.find_elements_by_tag_name("a")

		for elem in aelems:
			#获取tr的title属性
			atext = elem.get_attribute("title")
			for usergrop in groups.split():
				if atext == usergrop:
					#获取tr的id属性
					aid = elem.get_attribute("id")
					spanid = idfirst + filter(str.isdigit, aid) + "_check"
					self.getElem.find_element_wait_and_click_EC("id", spanid)
					break

	u'''点击操作的公共方法
	   parameter:
		   - value:序号
		   - statu:代表点击的操作，1代表勾选复选框；2代表状态开关；3代表上移；4代表下移；5代表插入；6代表编辑
	'''
	def click_action_public_command(self, value, status):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		valu = self.cnEn.is_float(value)
		statu = self.cnEn.is_float(status)
		# 获取table对象
		tableelem = self.getElem.find_element_with_wait_EC("id", "content_table")
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

			if tdtext == valu:
				#勾选复选框
				if statu == '1':
					xpath = "/html/body/div/div[6]/div[2]/div/table/tbody/tr[" + str(line) + "]/td[1]/input[1]"
				#状态开关
				elif statu == '2':
					xpath = "/html/body/div/div[6]/div[2]/div/table/tbody/tr[" + str(line) + "]/td[8]/input[1]"
				#上移
				elif statu == '3':
					xpath = "/html/body/div/div[6]/div[2]/div/table/tbody/tr[" + str(line) + "]/td[9]/a[1]"
				#下移
				elif statu == '4':
					xpath = "/html/body/div/div[6]/div[2]/div/table/tbody/tr[" + str(line) + "]/td[9]/a[2]"
				#插入
				elif statu == '5':
					xpath = "/html/body/div/div[6]/div[2]/div/table/tbody/tr[" + str(line) + "]/td[9]/a[3]"
				#编辑
				elif statu == '6':
					xpath = "/html/body/div/div[6]/div[2]/div/table/tbody/tr[" + str(line) + "]/td[9]/a[4]"
				self.getElem.find_element_wait_and_click_EC("xpath", xpath)
				break

	u'''点击消息提示'''
	def click_message_prompt(self):
		self.frameElem.from_frame_to_otherFrame('topFrame')
		self.getElem.find_element_wait_and_click_EC("id", "link_tc")

	u'''点击消息详情'''
	def click_message_detail(self):
		self.frameElem.from_frame_to_otherFrame('topFrame')
		time.sleep(3)
		self.click_message_prompt()
		time.sleep(2)
		ulselem = self.getElem.find_element_with_wait_EC("id", "digest")
		# 找到ul下所有a对象
		aselems = ulselem.find_elements_by_tag_name("a")
		aselems[0].click()

	u'''选择审批用户
	   parameter:
		   - username:审批用户名称
	'''
	def select_approval_user(self, username):
		self.frameElem.from_frame_to_otherFrame('artIframe')
		name = self.cnEn.is_float(username)
		elem = self.getElem.find_element_with_wait_EC("id", "fortApproverId")
		self.selectElem.select_element_by_visible_text(elem, name)

	u'''填写口令
	   Parameters:
		- pwd:口令
	'''
	def set_passwd(self, pwd):
		passwd = self.cnEn.is_float(pwd)
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_clear("id", "password")
		self.getElem.find_element_wait_and_sendkeys("id", "password", passwd)

	u'''填写备注信息
	   Parameters:
		- descrip:备注信息
	'''
	def set_descrip(self, descrip):
		description = self.cnEn.is_float(descrip)
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_clear("id", "fortDescription")
		self.getElem.find_element_wait_and_sendkeys("id", "fortDescription", description)

	u'''通过消息进行命令审批
	   Parameters:
		- user:用
		- pwd:密码
		- descrip:备注信息
	'''
	def command_by_message_approval(self, user, pwd, descrip):
		self.frameElem.switch_to_content()
		time.sleep(5)
		self.click_message_detail()
		time.sleep(2)
		self.select_approval_user(user)
		time.sleep(1)
		self.set_passwd(pwd)
		self.set_descrip(descrip)
		self.check_sure_button()
		time.sleep(2)

	u'''通过流程控制进行命令审批
	   Parameters:
		- user:用户名称
		- pwd:密码
		- descrip:备注信息
	'''
	def command_by_flow_approval(self, user, pwd, descrip):
		#获取流程号
		number = self.acproval.get_new_process_number()
		self.cmf.select_menu(u"流程控制", u"流程任务")
		self.acproval.click_approval_by_number(number)
		self.select_approval_user(user)
		self.set_passwd(pwd)
		self.set_descrip(descrip)
		self.check_sure_button()

	u'''根据浏览器类型进行单点登录'''
	def choice_browser_open(self,iconType,username,pwd,cmdList):
		fileList = fileRead().get_ip_address()
		browserType = fileList[1].strip('\n')
		if browserType == '1':
			time.sleep(5)
			self.ssoElem.execute_chrome_key()
		elif browserType != '0' or browserType != '1':
			self.ssoElem.opt_cmd("\\testIsomp\\webElement\\sso\\sso_firefox.exe","", "","","")
		time.sleep(3)
		self.ssoElem.opt_cmd("\\testIsomp\\webElement\\rule\\sso_command_open.exe",iconType, username,pwd,cmdList)

	u'''根据浏览器类型关闭单点登录'''
	def choice_browser_close(self,iconType):
		self.ssoElem.opt_cmd("\\testIsomp\\webElement\\rule\\sso_command_close.exe",iconType,"","","")

	u'''命令审批单点登录'''
	def sso_command(self, data):
		time.sleep(2)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.ssoElem.select_account(data[2],data[3])
		self.click_sso_icon(data[2])
		if data[4] != "":
			self.ssoElem.select_protocol(data[4])
		time.sleep(5)
		SendKeys.SendKeys(str(data[5]))
		SendKeys.SendKeys('\n', with_newlines=True)
		time.sleep(2)

	u'''点击单点登录图标
		parameters :
			rename : 资源名称
	'''
	def click_sso_icon(self, rename):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		rname = self.cnEn.is_float(rename)
		row = self.acproval.select_resoure_sso(rname)
		xpath = "/html/body/div[1]/div[7]/div[2]/div/table/tbody/tr[" + str(
			row * 2) + "]/td/div/table/tbody/tr/td[2]/a/img"
		time.sleep(2)
		self.getElem.find_element_wait_and_click_EC("xpath", xpath)
		time.sleep(2)