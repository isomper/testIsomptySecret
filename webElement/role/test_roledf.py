#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2018/5/7
#模块描述：角色定义
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

class Role(object):

	#角色名称
	FORTROLE_NAME = "fortRoleName"
	#名称简写
	FORTROLE_SHORTNAME = "fortRoleShortName"
	#添加按钮
	ADD_ROLE = "add_role"
	#保存按钮
	SAVE_ROLE = "save_role"

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)

	u'''点击角色添加按钮'''
	def role_add_button(self):
		try:
			self.frameElem.from_frame_to_otherFrame("mainFrame")
			self.getElem.find_element_wait_and_click("id", self.ADD_ROLE)
		except Exception:
			print("Click the Add button to fail")

	u'''编辑角色名称
	   Parameters:
	      - rolename:角色名称
	'''
	def edit_rolename(self, rolename):
		try:
			self.getElem.find_element_wait_and_clear("id", self.FORTROLE_NAME)
			self.getElem.find_element_wait_and_sendkeys("id", self.FORTROLE_NAME, rolename)
		except Exception:
			print("Role name fill in error")

	u'''编辑名称简写
	    Parameters：
	       -shortname 名称简写
	'''
	def edit_shortname(self, shortname):
		try:
			self.getElem.find_element_wait_and_clear("id", self.FORTROLE_SHORTNAME)
			self.getElem.find_element_wait_and_sendkeys("id", self.FORTROLE_SHORTNAME, shortname)
		except Exception:
			print("Name abbreviation fill in error")

	u'''展开角色树(三角形)；
		parameter:
		- treeDemo_switch:角色演示树'''
	def set_tree_demo_switch(self,treeDemo_switch):
		self.getElem.find_element_wait_and_click_EC('id',treeDemo_switch)

	u'''勾选一层角色;
		parameter:
		- treeDemo_check:角色树勾选框'''
	def set_tree_demo_check(self,treeDemo_check):
		self.getElem.find_element_wait_and_click_EC('id',treeDemo_check)

	u'''勾选底层角色框;
		parameter:
		- inputName:底层角色勾选框'''
	def set_input_click(self,inputName):
		self.getElem.find_element_wait_and_click_EC('name',inputName)

	u'''选择其他角色；
		parameter:
		- roleName：角色名称 '''
	def set_other_role(self,roleName):
		sele = self.getElem.find_element_with_wait_EC('id','allOtherPrivileges')
		time.sleep(1)
		self.selectElem.select_element_by_visible_text(sele,roleName)
		self.getElem.find_element_wait_and_click_EC('id','add_privileges')

	u'''保存角色'''
	def save_role_button(self):
		self.getElem.find_element_wait_and_click_EC('id','save_role')
		self.cmf.click_login_msg_button()
		time.sleep(1)
		self.frameElem.switch_to_main()
		self.getElem.find_element_wait_and_click_EC('id','history_skip')

	u'''添加用户'''
	def add_sercret_user(self,account,name,pwd,roleText):
		time.sleep(1)
		#点击添加按钮
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC('classname','btn_tj')
		#输入账号，名称，密码
		self.getElem.find_element_wait_and_clear_EC('id','fortUserAccount')
		self.getElem.find_element_sendkyes_EC('id','fortUserAccount',account)
		self.getElem.find_element_wait_and_clear_EC('id','fortUserName')
		self.getElem.find_element_sendkyes_EC('id','fortUserName',name)
		self.getElem.find_element_wait_and_clear_EC('id','fortUserPassword')
		self.getElem.find_element_sendkyes_EC('id','fortUserPassword',pwd)
		self.getElem.find_element_wait_and_clear_EC('id','fortUserPasswordAgain')
		self.getElem.find_element_sendkyes_EC('id','fortUserPasswordAgain',pwd)
		#切换到角色页面
		self.getElem.find_element_wait_and_click_EC('id','userMessage')
		#为用户赋予角色
		selem = self.getElem.find_element_with_wait_EC('id','Roles')
		self.selectElem.select_element_by_visible_text(selem,roleText)
		self.getElem.find_element_wait_and_click_EC('id','add_roles')
		#保存用户
		self.getElem.find_element_wait_and_click_EC('id','save_user')
		self.cmf.click_login_msg_button()
		#点击返回
		self.frameElem.switch_to_main()
		self.getElem.find_element_wait_and_click_EC('id','history_skip')