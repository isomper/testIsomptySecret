#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/07/07
#模块描述：组织定义部门
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
from _log import log
from _icommon import getElement,frameElement
from selenium.webdriver.common.action_chains import ActionChains


class Department(object):

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.frameElem = frameElement(driver)
		self.log = log()
		self.cnEn = cnEncode()

	u'''左边框点击部门'''
	def click_left_department(self):

		self.frameElem.from_frame_to_otherFrame("leftFrame")
		self.getElem.find_element_wait_and_click("id", "url0")

	u'''点击展开按钮'''
	def click_dept_switch(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click("id", "treeDemo_1_switch")

	u'''点击基本操作
	   parameter:
	       - deptname:传入要被操作的部门
	       - operation：代表基本操作0代表添加、1代表编辑、2代表上移、3代表下移、4代表删除
	'''
	def click_basic_operation(self, deptname, operation):

		if operation == 0:
			self.click_basic_operation_public_method(deptname, "addBtn_treeDemo_")
		elif operation == 1:
			self.click_basic_operation_public_method(deptname, "treeDemo_", "_edit")
		elif operation == 2:
			self.click_basic_operation_public_method(deptname, "toUpBtn_treeDemo_")
		elif operation == 3:
			self.click_basic_operation_public_method(deptname, "toDownBtn_treeDemo_")
		elif operation == 4:
			self.click_basic_operation_public_method(deptname, "treeDemo_", "_remove")

	u'''点击上移、下移按钮校验
	   parameter:
	       - deptname:传入要被操作的部门
	       - operation：代表基本操作2代表上移、3代表下移
	'''
	def click_up_button(self, deptname, operation):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")

		#获取所有a标签对象
		elems = self.driver.find_elements_by_tag_name("a")

		for elem in elems:
			elemtext = elem.get_attribute("title")
			elemid = elem.get_attribute("id")

			#判断传入要被操作的部门和获取的文本是否相等
			if deptname == elemtext:
				self.getElem.find_element_wait_and_click("id", elemid)
				#点击上移按钮
				if operation == 2:
					#移动次数
					locates = range(self.return_locate_line(deptname))
					self.move_down_check(elemid, locates, "toUpBtn_treeDemo_")
				#点击下移按钮
				elif operation == 3:
					locates = range(len(elems) - self.return_locate_line(deptname))
					self.move_down_check(elemid, locates, "toDownBtn_treeDemo_")
				break

	u'''上移、下移校验公用方法
	   parameter:
	       - elemid:a标签对象的id
	       - locates:移动次数
	       - idstr:下移按钮id的字符
	'''
	def move_down_check(self, elemid, locates, idstr):
		selemid = self.cnEn.cnCode(elemid)

		for locate in locates:
			buttonid = idstr + filter(str.isdigit, selemid)
			self.getElem.find_element_wait_and_click("id", buttonid)
			if locate == locates[-1]:
				break

	u'''返回在部门树中位于第几行
	   parameter:
	       - deptname:传入要被操作的部门
	'''
	def return_locate_line(self, deptname):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		elems = self.driver.find_elements_by_tag_name("a")
		#位于第几行
		locate = 0
		for elem in elems:
			elemtext = elem.get_attribute("title")
			locate = locate + 1
			if deptname == elemtext:
				return locate - 1

	u'''点击增加、编辑、删除、上移、下移的公共方法
	   parameter:
	       - deptname:传入要被操作的部门
	       - first:id的前半段字符
	       - end:id的后半段字符，可以不进行填写
	'''
	def click_basic_operation_public_method(self, deptname, first, end='no'):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")

		#获取所有a标签的对象
		elems = self.driver.find_elements_by_tag_name("a")

		for elem in elems:
			elemtext = elem.get_attribute("title")
			elemid = elem.get_attribute("id")
			selemid = self.cnEn.cnCode(elemid)
			time.sleep(2)

			if deptname == elemtext:
				self.getElem.find_element_wait_and_click("id", elemid)
				time.sleep(2)

				if end != 'no':
					buttonid = first + filter(str.isdigit, selemid) + end
				else:
					buttonid = first + filter(str.isdigit, selemid)
				time.sleep(2)
				self.getElem.find_element_wait_and_click("id", buttonid)
				time.sleep(2)
				break

	u'''在弹出框中填写内容
	   parameter:
	       - deptname:输入填写的部门名称
	'''
	def popup_sendkey(self, deptname):
		time.sleep(2)
		self.frameElem.switch_to_content()
		xpath = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div[2]/input"
		self.getElem.find_element_wait_and_sendkeys("xpath", xpath, deptname)

	u'''点击确定按钮'''
	def click_ok_button(self):
		time.sleep(2)
		self.frameElem.switch_to_content()
		xpath = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]"
		self.click_frame_public_method(u"消息", xpath)

	u'''清空部门文本框内容'''
	def clear_depart_text(self):
		time.sleep(2)
		self.frameElem.switch_to_content()
		xpath = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div[2]/input"
		self.getElem.find_element_wait_and_clear("xpath", xpath)

	u'''点击取消按钮'''
	def click_cancel_button(self):
		time.sleep(2)
		xpath = "/html/body/div[2]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]"
		self.click_frame_public_method(u"消息", xpath)

	#点击最外层警告按钮
	def click_Outermost_button(self, pagetext):
		self.frame_public_method(pagetext)

		# xpath = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button"
		# self.click_frame_public_method(pagetext, xpath)

	u'''弹窗的公用方法
	   Parameters:
	      - pagetext：页面弹框的title文本
	'''
	def frame_public_method(self, pagetext):
		time.sleep(2)
		self.frameElem.switch_to_content()
		#获取title集合
		divselems = self.driver.find_elements_by_class_name("aui_title")
		#获取table集合
		tableselems = self.driver.find_elements_by_class_name("aui_dialog")
		#是否点击确定按钮标识，如果为True说明已经点击确定按钮
		step = False

		#循环table集合
		for table in tableselems:
			#循环title集合
			for divselem in divselems:
				#获取title文本
				messagetext = divselem.get_attribute('textContent')
				if messagetext == pagetext:
					time.sleep(5)
					table.find_element_by_class_name("aui_state_highlight").click()
					step = True
					break
			if step is True:
				break

	u'''弹窗的公用方法
	   Parameters:
	      - pagetext：页面弹框的title文本
	      - xpath：弹窗元素的路径
	'''
	def click_frame_public_method(self, pagetext, xpath):

		self.frameElem.switch_to_content()
		divselems = self.driver.find_elements_by_class_name("aui_title")

		for divselem in divselems:

			messagetext = divselem.get_attribute('textContent')

			if messagetext == pagetext:
				self.driver.implicitly_wait(20)
				#鼠标移动到当前窗口
				actions = ActionChains(self.driver)
				actions.move_to_element(divselem).perform()
				time.sleep(1)
				self.getElem.find_element_wait_and_click_EC("xpath", xpath)
				break

	u'''多层弹窗类检查点
	   Parameters:
	      - type：定位弹窗中元素的类型
	      - elem：弹窗元素的名字或者路径
	      - data：excel一行的数据
	      - flag:没有检查点的测试项通过标识。Ture为通过，False为未通过
	      - pagetext：页面弹框的title文本
	'''
	def multil_div_check_point(self, type, elem, data, flag, pagetext):
		#检查点为空
		if data[1] == "":
			if flag:
				#测试点通过
				self.log.log_detail(data[0], True)
			else:
				#测试点没通过
				self.log.log_detail(data[0], False)
		#检查点不为空
		else:
			#判断文本内容是否一致
			elemText = self.getElem.find_element_wait_and_compare_text(type,elem,data)
			self.click_Outermost_button(pagetext)
			if elemText:
				# 页面的内容与检查点内容一致，测试点通过
				self.log.log_detail(data[0], True)
			else:
				#页面抓取到的内容与检查点不一致，测试点不通过
				self.log.log_detail(data[0], False)