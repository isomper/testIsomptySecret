#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：资源组
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsompSecret/common/")
from _cnEncode import cnEncode
from _icommon import getElement,frameElement
sys.path.append("/testIsompSecret/webElement/department/")
from test_dptm_ment import Department

class Regroup(object):

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.frameElem = frameElement(driver)
		self.cnEn = cnEncode()
		self.dptment = Department(driver)

	u'''左边框点击资源组'''
	def click_left_regroup(self):
		time.sleep(2)
		self.frameElem.from_frame_to_otherFrame("leftFrame")
		self.getElem.find_element_wait_and_click_EC("id", "url1")

	u'''点击资源组展开按钮'''
	def click_regroup_switch(self):
		time.sleep(2)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "resource_group_1_switch")

	u'''点击基本操作
	   parameter:
	       - operation：代表基本操作0代表添加、1代表编辑、2代表上移、3代表下移、4代表删除
	       - deptname:传入要被操作的部门名称
	       - regroup:传入要被操作的资源组名称
	'''
	def regroup_click_basic_operation(self, operation, deptname='no', regroup='no'):
		time.sleep(2)

		if deptname != 'no':
			self.dptment.click_basic_operation_public_method(deptname, "resource_group_", "_switch")
		if operation == 0:
				self.dptment.click_basic_operation_public_method(deptname, "addBtn_resource_group_")
		elif regroup != 'no':
			if operation == 1:
				self.dptment.click_basic_operation_public_method(regroup, "resource_group_", "_edit")
			elif operation == 2:
				self.dptment.click_basic_operation_public_method(regroup, "toUpBtn_resource_group_")
			elif operation == 3:
				self.dptment.click_basic_operation_public_method(regroup, "toDownBtn_resource_group_")
			elif operation == 4:
				self.dptment.click_basic_operation_public_method(regroup, "resource_group_", "_remove")

	u'''点击上移、下移按钮校验
	   parameter:
	       - operation：代表基本操作2代表上移、3代表下移
	       - deptname:传入要被操作的部门名称
	       - regroup:传入要被操作的资源组名称
	'''
	def regroup_click_up_down_check(self, operation, deptname='no', regroup='no'):
		if deptname != 'no':
			#点击要操作部门的展开按钮
			self.dptment.click_basic_operation_public_method(deptname, "resource_group_", "_switch")

		self.frameElem.from_frame_to_otherFrame("rigthFrame")

		#获取所有a标签对象
		elems = self.driver.find_elements_by_tag_name("a")

		for elem in elems:
			elemtext = elem.get_attribute("title")
			elemid = elem.get_attribute("id")

			#判断传入要被操作的资源组和获取的文本是否相等
			if regroup == elemtext:
				self.getElem.find_element_wait_and_click("id", elemid)
				#点击上移按钮
				if operation == 2:
					#移动次数
					locates = range(self.regroup_return_locate_line(regroup))
					self.dptment.move_down_check(elemid, locates, "toUpBtn_resource_group_")
				#点击下移按钮
				elif operation == 3:
					locates = range(self.return_regroup_all_line() - self.regroup_return_locate_line(regroup))
					self.dptment.move_down_check(elemid, locates, "toDownBtn_resource_group_")
				break

	u'''返回在资源组树中位于第几行
	   parameter:
	       - regroup:传入要被操作的资源组
	'''
	def regroup_return_locate_line(self, regroup):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		elems = self.driver.find_elements_by_tag_name("a")
		#位于第几行
		locate = 0
		for elem in elems:
			elemid = elem.get_attribute("id")
			elemtext = elem.get_attribute("title")
			selemid = self.cnEn.cnCode(elemid)

			sapnid = "resource_group_" + filter(str.isdigit, selemid) + "_ico"
			spanelem = self.getElem.find_element_with_wait_EC("id", sapnid)
			spanclass = spanelem.get_attribute("class")

			if spanclass == "button icozy_ico_docu":
				locate += 1
				if regroup == elemtext:
					return locate

	u'''返回在资源组总共几行'''
	def return_regroup_all_line(self):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		elems = self.driver.find_elements_by_tag_name("a")
		#总共几行
		locate = 0
		for elem in elems:
			elemid = elem.get_attribute("id")
			selemid = self.cnEn.cnCode(elemid)

			sapnid = "resource_group_" + filter(str.isdigit, selemid) + "_ico"
			spanelem = self.getElem.find_element_with_wait_EC("id", sapnid)
			spanclass = spanelem.get_attribute("class")

			if spanclass == "button icozy_ico_docu":

				locate += 1

		return locate + 1

	u'''点击资源组添加资源按钮
	   parameter:
	       - regroup:传入要被操作的资源组名称
	       - deptname:传入要被操作的部门名称
	'''
	def click_regroup_add_resouce(self, regroup, deptname='no'):
		time.sleep(2)

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		if deptname != 'no':
			#点击要操作部门的展开按钮
			self.dptment.click_basic_operation_public_method(deptname, "resource_group_", "_switch")
		#选中资源组
		self.dptment.click_basic_operation_public_method(regroup, "resource_group_", "_span")

		self.getElem.find_element_wait_and_click_EC("id", "add_Resource")

	u'''点击资源组批量删除资源按钮
	   parameter:
	       - regroup:传入要被操作的资源组名称
	       - deptname:传入要被操作的部门名称
	'''
	def click_regroup_bulk_resouce(self, regroup, deptname='no'):
		time.sleep(2)

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		if deptname != 'no':
			#点击要操作部门的展开按钮
			self.dptment.click_basic_operation_public_method(deptname, "resource_group_", "_switch")
		#选中资源组
		self.dptment.click_basic_operation_public_method(regroup, "resource_group_", "_span")
		self.check_delect_all()

		self.getElem.find_element_wait_and_click_EC("id", "delete_Resource")

	u'''点击资源组删除资源按钮
	   parameter:
	       - regroup:传入要被操作的资源组名称
	       - rename:资源名称
	       - deptname:传入要被操作的部门名称
	'''
	def click_regroup_del_resouce(self, regroup, rename, deptname='no'):
		time.sleep(2)

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		if deptname != 'no':
			#点击要操作部门的展开按钮
			self.dptment.click_basic_operation_public_method(deptname, "resource_group_", "_switch")
		#选中资源组
		self.dptment.click_basic_operation_public_method(regroup, "resource_group_", "_span")

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
			if tdtext == rename:
				xpath = "/html/body/div/div[2]/div[7]/div/table/tbody/tr[" + str(line) + "]/td[6]/input"
				time.sleep(2)
				self.getElem.find_element_wait_and_click_EC("xpath", xpath)
				break

	u'''勾选资源组全选删除框'''
	def check_delect_all(self):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "delect_all")

	u'''点击资源组检索按钮'''
	def click_regroup_query(self):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "query_Resource")

	u'''点击资源组重置按钮'''
	def click_regroup_reset(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "resetting")

	u'''资源组页面填写资源名称或IP
	   parameter:
	       - renameorip:资源名称或IP
	'''
	def set_rename_ip(self, renameorip):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear('id', "txtfortResourceAccountOrIp")
		self.getElem.find_element_wait_and_sendkeys('id', "txtfortResourceAccountOrIp", renameorip)

	u'''点击资源组添加资源的检索按钮'''
	def click_regroup_add_resouce_query(self):
		time.sleep(2)

		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_click_EC("id", "quick_Resource")

	u'''点击资源组添加资源的重置按钮'''
	def click_regroup_add_resouce_reset(self):

		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_click_EC("id", "resetting")

	u'''添加资源页面填写资源名称
	   parameter:
	       - rename:资源名称
	'''
	def set_rename(self, rename):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_clear('id', "fort_resource_name")
		self.getElem.find_element_wait_and_sendkeys('id', "fort_resource_name", rename)

	u'''添加资源页面填写资源ip
	   parameter:
	       - ipdress:资源ip
	'''
	def set_ip(self, ipdress):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_clear('id', "fort_resource_ip")
		self.getElem.find_element_wait_and_sendkeys('id', "fort_resource_ip", ipdress)

	u'''点击资源部门展开按钮'''
	def click_resource_depart_switch(self):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_click_EC("id", "user_tree_1_switch")

	u'''勾选部门框
	   parameter:
	       - deptname:传入要被勾选的部门名称
	'''
	def check_depart(self, deptname):
		self.click_resource_depart_switch()
		time.sleep(2)
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.click_public_method(deptname, "user_tree_", "_check")

	u'''勾选资源框或者部门框
	   parameter:
		   - rename:资源名称或者部门名称   
	'''
	def check_one_resource(self, rename):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		#获取table对象
		tableelem = self.getElem.find_element_with_wait_EC("id", "user_table")
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
			tdtext = tds[1].text
			if tdtext == rename:
				xpath = "/html/body/div[3]/div[2]/table/tbody/tr[" + str(line) + "]/td[1]/li/input"
				self.getElem.find_element_wait_and_click_EC("xpath", xpath)
				break

	u'''勾选全部资源框或者部门框'''
	def check_all_resource(self):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_click_EC("id", "user_check_all")

	u'''点击资源确定按钮'''
	def click_resource_okbutton(self):
		self.frameElem.switch_to_content()
		self.getElem.find_element_wait_and_click_EC("id", "okButton")

	u'''点击公共方法
	   parameter:
	       - name:传入要被操作的名称
	       - first:id的前半段字符
	       - end:id的后半段字符，可以不进行填写
	'''
	def click_public_method(self, name, first, end='no'):

		self.frameElem.from_frame_to_otherFrame("artIframe")

		#获取所有a标签的对象
		elems = self.driver.find_elements_by_tag_name("a")

		for elem in elems:
			elemtext = elem.get_attribute("title")
			elemid = elem.get_attribute("id")
			selemid = self.cnEn.cnCode(elemid)

			if name == elemtext:
				self.getElem.find_element_wait_and_click("id", elemid)

				if end != 'no':
					buttonid = first + filter(str.isdigit, selemid) + end
				else:
					buttonid = first + filter(str.isdigit, selemid)

				self.getElem.find_element_wait_and_click("id", buttonid)
				break
