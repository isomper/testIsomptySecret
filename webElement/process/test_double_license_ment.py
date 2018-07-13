#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsompSecret/common/")
from _log import log
from _icommon import getElement, selectElement, frameElement, commonFun
from _cnEncode import cnEncode

sys.path.append("/testIsompSecret/webElement/authorization")
from authrizationElement import AuthorizationPage

sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

sys.path.append("/testIsompSecret/webElement/department/")
from test_dptm_ment import Department

sys.path.append("/testIsompSecret/webElement/process/")
from test_access_approval_ment import Accapproval


class Dobapproval(object):

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)
		self.log = log()
		self.cnEn = cnEncode()
		self.depart = Department(driver)
		self.loginElem = loginPage(self.driver)
		self.authElem = AuthorizationPage(self.driver)
		self.acproval = Accapproval(driver)

	u'''点击授权操作列双人授权按钮
        parameters:
            name : 授权名称
    '''
	def click_double_license_button(self, name):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.authElem.operate_double_approval(name)

	u'''点击双人审批图标
            parameters :
                rename : 资源名称
    '''
	def click_double_license_icon(self, rename):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		rname = self.cnEn.is_float(rename)
		row = self.acproval.select_resoure_sso(rname)
		xpath = "/html/body/div[1]/div[7]/div[2]/div/table/tbody/tr[" + str(
			row * 2) + "]/td/div/table/tbody/tr/td[2]/a/img"
		time.sleep(2)
		self.getElem.find_element_wait_and_click_EC("xpath", xpath)
		time.sleep(2)

	u'''校验图标
	   parameters :
            - rename:资源名称
            - react :资源账号
	'''
	def check_ico_len(self, rename, react):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		time.sleep(3)
		self.acproval.select_resoure_account(rename, react)
		row = self.acproval.select_resoure_sso(rename)
		self.acproval.click_refresh_icon(rename)
		ico_xpath = "/html/body/div[1]/div[7]/div[2]/div[1]/table/tbody/tr[" + str(
			row * 2) + "]/td/div/table/tbody/tr/td[2]/a/img"
		time.sleep(2)
		selem = self.getElem.find_element_with_wait_EC("xpath", ico_xpath)
		selems = selem.get_attribute("alt")
		if selems != u'双人授权':
			self.log.log_detail(u"双人授权已同意申请，可以进行单点登录", True)
		else:
			self.log.log_detail(u"双人授权已拒绝申请，不可以进行单点登录", True)

	u'''选择授权人
       parameters :
            - authorizer:授权人名称
    '''
	def select_authorizer(self, authorizer):
		self.frameElem.switch_to_artIframe()
		author = self.cnEn.is_float(authorizer)
		selem = self.getElem.find_element_with_wait_EC("id", "fortApproverId")
		self.selectElem.select_element_by_visible_text(selem, author)

	u'''勾选同终端直接输入口令访问'''
	def check_same_termina(self):
		self.frameElem.switch_to_artIframe()
		self.getElem.find_element_wait_and_click_EC("id", "fortIsRemoteApply")

	u'''填写授权人密码
	   Parameters:
	      - passwd:授权人密码
	'''
	def set_authorizer_pwd(self, passwd):
		self.frameElem.switch_to_artIframe()
		pwd = self.cnEn.is_float(passwd)
		self.getElem.find_element_wait_and_clear("id", "password")
		self.getElem.find_element_wait_and_sendkeys("id", "password", pwd)

	u'''调用新浏览器'''
	def call_other_browsers(self):
		newbrowser = webdriver.Edge()
		# newbrowser = webdriver.Chrome()
		#IE窗口最大化
		newbrowser.maximize_window()
		newbrowser.get("https://172.16.10.65")
		newbrowser.get("javascript:document.getElementById('overridelink').click();")
		return newbrowser

	u'''远程用户登录
	   Parameters:
          - listusers:用户集
	'''
	def user_remote_approval(self, newbrowser, listusers):
		users = listusers.split()
		newbrowser.switch_to_default_content()
		selem = newbrowser.find_element_by_id("loginMethod")
		Select(selem).select_by_value(users[0])
		newbrowser.find_element_by_id("username").click()
		newbrowser.find_element_by_id("username").send_keys(users[1])
		newbrowser.find_element_by_id("pwd").click()
		newbrowser.find_element_by_id("pwd").send_keys(users[2])
		time.sleep(1)
		newbrowser.find_element_by_id("do_login").click()

	u'''菜单选择
        Parameters:
            - newbrowser：新浏览器驱动
            - levelText1：1级菜单文本
            - levelText2：2级菜单文本
            - levelText3：3级菜单文本
    '''
	def click_menu(self,newbrowser, levelText1, levelText2='no',levelText3='no'):
		time.sleep(2)
		self.remote_break_frame(newbrowser, "topFrame")
		time.sleep(2)
		#点击一级菜单
		newbrowser.find_element_by_link_text(levelText1).click()
		time.sleep(1)
		#如果有2级菜单，再点击2级菜单
		if levelText2 != 'no':
			newbrowser.find_element_by_link_text(levelText2).click()
		#如果有3级菜单，根据名称点击3级菜单
		if levelText3 != 'no':
			self.remote_break_frame(newbrowser, "leftFrame")
			newbrowser.find_element_by_link_text(levelText3).click()

	u'''判断名称是否存在
       Parameters:
          - namevalue:传入的要被查询名称
          - name:表格列的name属性
       return：true代表存在，false代表不存在
    '''
	def namevalue_remote_is_exsit(self, newbrowser,namevalue, name):
		nameval = self.cnEn.is_float(namevalue)
		namesex = self.cnEn.is_float(name)
		isExsit = False
		text_list = newbrowser.find_elements_by_name(namesex)
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
	def find_name_remote_by_row(self, newbrowser, namevalue, name):
		self.remote_break_frame(newbrowser, "mainFrame")
		nameval = self.cnEn.is_float(namevalue)
		namesex = self.cnEn.is_float(name)
		row = 0
		if self.namevalue_remote_is_exsit(newbrowser,nameval, namesex):
			text_list = newbrowser.find_elements_by_name(namesex)
			for fortNameValue in text_list:
				row = row + 1
				fortNameValue_text = fortNameValue.text
				if fortNameValue_text == nameval:
					break
		return row

	u'''通过流程号点击要审批的信息
	   Parameters:
          - number:流程号
	'''
	def click_remote_approval_by_number(self, newbrowser, number):
		time.sleep(2)
		row = self.find_name_remote_by_row(newbrowser, number, "fortProcessInstanceId")
		xpath = "/html/body/form/div/div[7]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[8]/input[1]"
		newbrowser.find_element_by_xpath(xpath).click()

	u'''流程控制是否同意审批
	   Parameters:
          - status:1代表同意审批，2代表拒绝审批
	'''
	def process_remote_is_agree_approval(self, newbrowser, status):
		statu = self.cnEn.is_float(status)
		self.remote_break_frame(newbrowser, "mainFrame")
		time.sleep(2)
		if statu == '1':
			newbrowser.find_element_by_id("yes").click()
		elif statu == '2':
			newbrowser.find_element_by_id("no").click()

	u'''填写流程控制中审批申请单的描述
	   Parameters:
          - description:描述内容
	'''
	def set_process_remote_description(self, newbrowser, description):
		descri = self.cnEn.is_float(description)
		self.remote_break_frame(newbrowser, "mainFrame")
		newbrowser.find_element_by_id("fortApprovalOpinions").clear()
		newbrowser.find_element_by_id("fortApprovalOpinions").send_keys(descri)

	u'''点击提交按钮'''
	def click_remote_submit(self, newbrowser):
		self.remote_break_frame(newbrowser, "mainFrame")
		newbrowser.find_element_by_id("save_process_approval").click()

	u'''点击确定按钮'''
	def click_remote_msg_button(self, newbrowser):
		newbrowser.switch_to_default_content()
		OKBTN = "//div[@id='aui_buttons']/button[1]"
		newbrowser.find_element_by_xpath(OKBTN).click()

	u'''点击返回按钮'''
	def remote_back(self, newbrowser):
		self.remote_break_frame(newbrowser, "mainFrame")
		newbrowser.find_element_by_id("history_skip").click()

	u'''跳转frame
	   Parameters:
            - frameName:要跳转到的frame的名字
	'''
	def remote_break_frame(self, newbrowser, frameName):
		time.sleep(2)
		newbrowser.switch_to_default_content()
		newbrowser.switch_to_frame("content1")
		time.sleep(2)
		newbrowser.switch_to_frame(frameName)
		time.sleep(2)

	u'''点击退出'''
	def remote_quit(self,newbrowser):
		time.sleep(2)
		self.remote_break_frame(newbrowser, "topFrame")
		time.sleep(1)
		newbrowser.find_element_by_id("logout").click()

	u'''申请人发送双人审批申请
	   Parameters:
          - data:excel中的一行数据
	'''
	def send_double_license_applicant(self, data):
		self.acproval.select_resoure_account(data[1], data[2])
		self.click_double_license_icon(data[1])
		self.select_authorizer(data[3])
		if data[4] != 'no':
			self.check_same_termina()
			self.set_authorizer_pwd(data[4])
		self.acproval.set_operation_description(data[5])
		self.acproval.click_sure_button()
		self.driver.implicitly_wait(10)
		self.log.log_detail(data[0], True)

	u'''审批人通过当前浏览器流程控制进行审批
	   Parameters:
          - number:流程号
	'''
	def approver_by_process_approval(self, expData, number):

		xpathMsg = ".//*[@id='body1']/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(expData)):
			data = expData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					self.acproval.user_login(data[2])
					self.frameElem.from_frame_to_otherFrame("topFrame")
					self.cmf.select_menu(u"流程控制", u"流程任务")
					self.acproval.click_approval_by_number(number)
					if data[1] != 'no':
						self.frameElem.switch_to_content()
						self.cmf.test_win_check_point("xpath", xpathMsg, data, flag)
					else:
						self.acproval.process_is_agree_approval(data[3])
						self.acproval.set_process_apply_description(data[4])
						self.acproval.click_submit()
						self.cmf.click_login_msg_button()
					self.acproval.back_quit_common()
			except Exception as e:
				print ("expired_approvel fail:" + str(e))

	u'''审批人通过新开启的浏览器流程控制进行审批
	   Parameters:
          - number:流程号
	'''
	def approver_remote_approval(self, expData, number):
		for dataRow in range(len(expData)):
			data = expData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					newbrowser = self.call_other_browsers()
					self.user_remote_approval(newbrowser, data[1])
					self.click_menu(newbrowser, u"流程控制", u"流程任务")
					self.click_remote_approval_by_number(newbrowser, number)
					self.process_remote_is_agree_approval(newbrowser, data[2])
					self.set_process_remote_description(newbrowser, data[3])
					self.click_remote_submit(newbrowser)
					self.click_remote_msg_button(newbrowser)
					self.remote_back(newbrowser)
					time.sleep(3)
					self.remote_quit(newbrowser)
					time.sleep(2)
					newbrowser.quit()
			except Exception as e:
				print ("expired_approvel fail:" + str(e))