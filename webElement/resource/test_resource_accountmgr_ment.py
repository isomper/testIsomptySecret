#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/7/18
#模块描述：资源账号管理
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

class Accountmgr(object):

	# 添加资源账号按钮
	ADD_ACCOUNT = "add_account"

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)
		self.cnEn = cnEncode()

	u'''点击账号管理按钮
	   Parameters:
	      - resourcename:传入的要编辑的资源名称
	'''
	def click_account_manage_button(self, resourcename):
		rename = self.cnEn.is_float(resourcename)

		self.frameElem.from_frame_to_otherFrame("mainFrame")
		row = self.cmf.find_row_by_name(rename, "fortResourceName")
		account_manage_xpath = "/html/body/form/div/div[8]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[7]/input[1]"
		self.getElem.find_element_wait_and_click("xpath", account_manage_xpath)

	u'''点击添加或编辑资源账号按钮
	   Parameters:
	      - resourcename:传入的要编辑的资源账号名称
	'''
	def click_account_add_edit_button(self, accountname='no'):
		time.sleep(3)
		try:
			actname = self.cnEn.is_float(accountname)
			isexist = self.cmf.is_namevalue_exsit(actname, "fortAccountName")
			#time.sleep(1)
			#如果资源名称等于no就点击添加按钮，否则点击编辑按钮
			if actname == 'no' or isexist == False :
				self.frameElem.from_frame_to_otherFrame("mainFrame")
				self.getElem.find_element_wait_and_click_EC("id", self.ADD_ACCOUNT)
			else:
				self.frameElem.from_frame_to_otherFrame("mainFrame")
				row = self.cmf.find_row_by_name(actname, "fortAccountName")
				edit_xpath = "/html/body/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[1]"
				self.getElem.find_element_wait_and_click_EC("xpath", edit_xpath)
		except Exception:
			print("Click the add or edit resource button to fail")

	u'''点击账号添加按钮'''
	def click_account_add(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", self.ADD_ACCOUNT)

	u'''点击账号编辑按钮
	   Parameters:
	      - accountname:传入的要编辑的资源账号名称
	'''
	def click_account_edit(self, accountname):
		actname = self.cnEn.is_float(accountname)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		row = self.cmf.find_row_by_name(actname, "fortAccountName")
		edit_xpath = "/html/body/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[1]"
		self.getElem.find_element_wait_and_click_EC("xpath", edit_xpath)

	u'''点击账号删除按钮
	   Parameters:
	      - accountname:传入的要编辑的资源账号名称
	'''
	def click_account_del(self, accountname):
		actname = self.cnEn.is_float(accountname)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		row = self.cmf.find_row_by_name(actname, "fortAccountName")
		del_xpath = "/html/body/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[2]"
		self.getElem.find_element_wait_and_click_EC("xpath", del_xpath)

	u'''点击账号查询按钮'''
	def click_account_query(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "fort_account")

	u'''点击是否可授权按钮
	   Parameters:
	      - accountname:传入的要编辑的资源账号名称
	'''
	def click_authorize(self, accountname):
		actname = self.cnEn.is_float(accountname)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		row = self.cmf.find_row_by_name(actname, "fortAccountName")
		authorize_xpath = "/html/body/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[5]/input"
		self.getElem.find_element_wait_and_click_EC("xpath", authorize_xpath)

	u'''查询名称
	   Parameters:
	      - accountname:传入的要编辑的资源账号名称
	'''
	def query_name(self, accountname):
		actname = self.cnEn.is_float(accountname)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_clear("id", "fortAccountName")
		self.getElem.find_element_wait_and_sendkeys("id", "fortAccountName", actname)

	u'''点击重置按钮'''
	def click_reset(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "resetting")

	u'''查询是否授权
	   Parameters:
	      - value:select选项中的value属性值
	'''
	def is_authorize(self, value):
		vle = self.cnEn.is_float(value)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		selectelem = self.getElem.find_element_with_wait_EC("id", "fortIsAllowAuthorized")
		self.selectElem.select_element_by_value(selectelem, vle)

	u'''选择编辑方式
	   Parameters:
	      - value:select选项中的value属性值
	'''
	def select_edit_way(self, value):
		vle = self.cnEn.is_float(value)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		selectelem = self.getElem.find_element_with_wait_EC("id", "accountStyle")
		self.selectElem.select_element_by_value(selectelem, vle)

	u'''点击账号保存按钮'''
	def click_save_account(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "save_account")

	u'''填写资源账号名称
	   Parameters:
	      - accountname:资源账号名称
	'''
	def set_account_name(self, accountname):
		actname = self.cnEn.is_float(accountname)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_clear("id", "fortAccountName")
		self.getElem.find_element_wait_and_sendkeys("id", "fortAccountName", actname)

	u'''清空资源账号名称'''
	def clear_account_name(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_clear("id", "fortAccountName")

	u'''填写资源账号口令
	   Parameters:
	      - pwd:资源账号口令
	'''
	def set_account_pwd(self, pwd):
		rspwd = self.cnEn.is_float(pwd)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_clear("id", "fortAccountPassword")
		self.getElem.find_element_wait_and_sendkeys("id", "fortAccountPassword", rspwd)

	u'''清空资源账号口令'''
	def clear_account_pwd(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_clear("id", "fortAccountPassword")

	u'''填写资源账号确认口令
	   Parameters:
	      - confpwd:资源账号确认口令
	'''
	def set_account_confirm_pwd(self, confpwd):
		rscfpwd = self.cnEn.is_float(confpwd)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_clear("id", "fortAccountPasswordAgain")
		self.getElem.find_element_wait_and_sendkeys("id", "fortAccountPasswordAgain", rscfpwd)

	u'''清空资源账号确认口令
	   Parameters:
	      - confpwd:资源账号确认口令
	'''
	def clear_account_confirm_pwd(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_clear("id", "fortAccountPasswordAgain")

	u'''勾选是否可授权按钮
	   Parameters:
	      - accountname:传入的要编辑的资源账号名称
	'''
	def set_authorize(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		elem = self.getElem.find_element_with_wait_EC("id", "fortIsAllowAuthorized")
		if elem.is_selected() == False:
			elem.click()
		#self.getElem.find_element_wait_and_click_EC("id", "fortIsAllowAuthorized")

