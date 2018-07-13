#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：用户组
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsompSecret/common/")
from _cnEncode import cnEncode
from _icommon import getElement,frameElement
sys.path.append("/testIsompSecret/webElement/department/")
from test_dptm_ment import Department
sys.path.append("/testIsompSecret/webElement/group/")
from test_regroup_ment import Regroup

class Usergroup(object):

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.frameElem = frameElement(driver)
		self.cnEn = cnEncode()
		self.dptment = Department(driver)
		self.regroup = Regroup(driver)

	u'''左边框点击用户组'''
	def click_left_usergroup(self):
		self.frameElem.from_frame_to_otherFrame("leftFrame")
		self.getElem.find_element_wait_and_click_EC("id", "url2")

	u'''点击用户组展开按钮'''
	def click_usergroup_switch(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "user_group_1_switch")

	u'''点击基本操作
	   parameter:
	       - operation：代表基本操作0代表添加、1代表编辑、2代表上移、3代表下移、4代表删除
	       - deptname:传入要被操作的部门名称
	       - usergroup:传入要被操作的用户组名称
	'''
	def usergroup_click_basic_operation(self, operation, deptname='no', usergroup='no'):
		if deptname != 'no':
			self.dptment.click_basic_operation_public_method(deptname, "user_group_", "_switch")
		if operation == 0:
				self.dptment.click_basic_operation_public_method(deptname, "addBtn_user_group_")
		elif usergroup != 'no':
			if operation == 1:
				self.dptment.click_basic_operation_public_method(usergroup, "user_group_", "_edit")
			elif operation == 2:
				self.dptment.click_basic_operation_public_method(usergroup, "toUpBtn_user_group_")
			elif operation == 3:
				self.dptment.click_basic_operation_public_method(usergroup, "toDownBtn_user_group_")
			elif operation == 4:
				self.dptment.click_basic_operation_public_method(usergroup, "user_group_", "_remove")

	u'''点击上移、下移按钮校验
	   parameter:
	       - operation：代表基本操作2代表上移、3代表下移
	       - deptname:传入要被操作的部门名称
	       - usergroup:传入要被操作的用户组名称
	'''
	def usergroup_click_up_down_check(self, operation, deptname='no', usergroup='no'):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		if deptname != 'no':
			#点击要操作部门的展开按钮
			self.dptment.click_basic_operation_public_method(deptname, "user_group_", "_switch")

		#获取所有a标签对象
		elems = self.driver.find_elements_by_tag_name("a")

		for elem in elems:
			elemtext = elem.get_attribute("title")
			elemid = elem.get_attribute("id")

			#判断传入要被操作的资源组和获取的文本是否相等
			if usergroup == elemtext:
				self.getElem.find_element_wait_and_click("id", elemid)
				#点击上移按钮
				if operation == 2:
					#移动次数
					locates = range(self.usergroup_return_locate_line(usergroup))
					self.dptment.move_down_check(elemid, locates, "toUpBtn_user_group_")
				#点击下移按钮
				elif operation == 3:
					locates = range(self.return_usergroup_all_line() - self.usergroup_return_locate_line(usergroup))
					self.dptment.move_down_check(elemid, locates, "toDownBtn_user_group_")
				break

	u'''返回在用户组树中位于第几行
	   parameter:
	       - usergroup:传入要被操作的用户组
	'''
	def usergroup_return_locate_line(self, usergroup):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		elems = self.driver.find_elements_by_tag_name("a")
		#位于第几行
		locate = 0
		for elem in elems:
			elemid = elem.get_attribute("id")
			elemtext = elem.get_attribute("title")
			selemid = self.cnEn.cnCode(elemid)

			sapnid = "user_group_" + filter(str.isdigit, selemid) + "_ico"
			spanelem = self.getElem.find_element_with_wait_EC("id", sapnid)
			spanclass = spanelem.get_attribute("class")

			if spanclass == "button icoyh_ico_docu":
				locate += 1
				if usergroup == elemtext:
					return locate

	u'''返回在用户组总共几行'''
	def return_usergroup_all_line(self):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		elems = self.driver.find_elements_by_tag_name("a")
		#总共几行
		locate = 0
		for elem in elems:
			elemid = elem.get_attribute("id")
			selemid = self.cnEn.cnCode(elemid)

			sapnid = "user_group_" + filter(str.isdigit, selemid) + "_ico"
			spanelem = self.getElem.find_element_with_wait_EC("id", sapnid)
			spanclass = spanelem.get_attribute("class")

			if spanclass == "button icoyh_ico_docu":

				locate += 1

		return locate + 1

	u'''点击用户组添加用户按钮
	   parameter:
	       - usergroup:传入要被操作的用户组名称
	       - deptname:传入要被操作的部门名称
	'''
	def click_usergroup_add_user(self, usergroup, deptname='no'):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		if deptname != 'no':
			#点击要操作部门的展开按钮
			self.dptment.click_basic_operation_public_method(deptname, "user_group_", "_switch")
		#选中用户组
		self.dptment.click_basic_operation_public_method(usergroup, "user_group_", "_span")

		self.getElem.find_element_wait_and_click_EC("id", "add_user")

	u'''点击用户组添加用户的检索按钮'''
	def click_usergroup_add_user_query(self):

		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_click_EC("id", "quick_user")

	u'''用户组页面填写用户名称或账号
	   parameter:
	       - username:用户名称或账号
	'''
	def set_username(self, username):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear('id', "txtUserNameOrAccount")
		self.getElem.find_element_wait_and_sendkeys('id', "txtUserNameOrAccount", username)

	u'''点击用户组检索按钮'''
	def click_usergroup_query(self):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "query_user")

	u'''点击用户组删除用户按钮
	   parameter:
	       - usergroup:传入要被操作的用户组名称
	       - username:用户名称
	       - deptname:传入要被操作的部门名称
	'''
	def click_usergroup_del_user(self, usergroup, username, deptname='no'):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		if deptname != 'no':
			#点击要操作部门的展开按钮
			self.dptment.click_basic_operation_public_method(deptname, "user_group_", "_switch")
		#选中用户组
		self.dptment.click_basic_operation_public_method(usergroup, "user_group_", "_span")

		#获取table对象
		tableelem = self.getElem.find_element_with_wait_EC("id", "ta")
		#获取table对象下的所有tr
		trelems = tableelem.find_elements_by_tag_name("tr")
		#位于第几行
		line = 0

		#循环所有tr
		for trelem in trelems:
			line += 1
			#找到tr下所有td对象
			tds = trelem.find_elements_by_tag_name("td")
			#获取td[2]的文本
			tdtext = tds[2].text
			if tdtext == username:
				xpath = "/html/body/div/div[2]/div[7]/div/table/tbody/tr[" + str(line) + "]/td[6]/input"
				self.getElem.find_element_wait_and_click_EC("xpath", xpath)
				break

	u'''点击用户组批量删除用户按钮
	   parameter:
	       - usergroup:传入要被操作的用户组名称
	       - deptname:传入要被操作的部门名称
	'''
	def click_usergroup_bulk_user(self, usergroup, deptname='no'):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		if deptname != 'no':
			#点击要操作部门的展开按钮
			self.dptment.click_basic_operation_public_method(deptname, "user_group_", "_switch")
		#选中用户组
		self.dptment.click_basic_operation_public_method(usergroup, "user_group_", "_span")
		self.regroup.check_delect_all()

		self.getElem.find_element_wait_and_click_EC("id", "delete_all_user")
