#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/8/17
#模块描述：流程控制下的查询
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
sys.path.append("/testIsompSecret/webElement/resource/")
from test_resource_common import Resource

class Flowcontrol(object):
	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)
		self.cnEn = cnEncode()
		self.resource = Resource(driver)

	u'''查询审批状态
	   Parameters:
	      - status:审批状态文本
	'''
	def query_approval_status(self, status):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		statu = self.cnEn.is_float(status)
		selem = self.getElem.find_element_with_wait_EC("id", "fortApprovalStatus")
		self.selectElem.select_element_by_visible_text(selem, statu)

	u'''查询申请类型
	   Parameters:
	      - type:申请类型value值-1代表请选择，0代表双人授权，1代表访问审批，2代表命令审批，3代表审计下载审批
	'''
	def query_application_type(self, type):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		value = self.cnEn.is_float(type)
		selem = self.getElem.find_element_with_wait_EC("id", "fortApplyType")
		self.selectElem.select_element_by_value(selem, value)

	u'''查询申请人
	   Parameters:
	      - aplname:申请人名称
	'''
	def query_applicant(self, aplname):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		name = self.cnEn.is_float(aplname)
		self.getElem.find_element_wait_and_clear("id", "fortApplicantName")
		self.getElem.find_element_wait_and_sendkeys("id", "fortApplicantName", name)

	u'''查询审批人
	   Parameters:
	      - approver:审批人名称
	'''
	def query_approver(self, approver):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		name = self.cnEn.is_float(approver)
		self.getElem.find_element_wait_and_clear("id", "fortApproverName")
		self.getElem.find_element_wait_and_sendkeys("id", "fortApproverName", name)

	u'''查询目标IP
	   Parameters:
	      - targetip:目标IP
	'''
	def query_targetip(self, targetip):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		target= self.cnEn.is_float(targetip)
		self.getElem.find_element_wait_and_clear("id", "fortResourceIp")
		self.getElem.find_element_wait_and_sendkeys("id", "fortResourceIp", target)

	u'''查询流程号
	   Parameters:
	      - number:流程号
	'''
	def query_process_number(self, number):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		processid = self.cnEn.is_float(number)
		self.getElem.find_element_wait_and_clear("id", "fortProcessApprovalId")
		self.getElem.find_element_wait_and_sendkeys("id", "fortProcessApprovalId", processid)

	u'''查询部门
	   Parameters:
	      - deptname:部门名称
	'''
	def query_process_depart(self, deptname):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		depart = self.cnEn.is_float(deptname)
		time.sleep(4)
		self.resource.select_depart_common("department_name", "tree_1_switch", depart)

	u'''查询审批时间
	   Parameters:
	      - year:年的value值
	      - month:月的value值
	      - day:日的value值
	'''
	def query_time(self, year, month='no', day='no'):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		y = self.cnEn.is_float(year)
		yselem = self.getElem.find_element_with_wait_EC("id", "fortLogYear")
		self.selectElem.select_element_by_value(yselem, y)
		if month != 'no':
			m = self.cnEn.is_float(month)
			if int(m) < 10:
				m = '0' + str(m)

			dselem = self.getElem.find_element_with_wait_EC("id", "fortLogMonth")
			self.selectElem.select_element_by_value(dselem, m)
		if day != 'no':
			d = self.cnEn.is_float(day)
			selem = self.getElem.find_element_with_wait_EC("id", "fortLogDay")
			self.selectElem.select_element_by_value(selem, d)

	u'''点击高级'''
	def click_advanced(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "btn_qh")

	u'''点击检索'''
	def click_process_search(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "quick_check")

	u'''点击重置'''
	def click_process_reset(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.getElem.find_element_wait_and_click_EC("id", "resetting")

	u'''流程任务查询
	   Parameters:
	      - data:excel一行数据集
	'''
	def query_process_task(self, data):
		self.driver.implicitly_wait(5)
		self.cmf.select_menu(u"流程控制", u"流程任务")
		self.click_advanced()
		if data[2] != 'no':
			self.query_approval_status(data[2])
		if data[3] != 'no':
			self.query_applicant(data[3])
		if data[4] != 'no':
			self.query_process_depart(data[4])
		if data[5] != 'no':
			self.query_process_number(data[5])
		if data[6] != 'no':
			self.query_application_type(data[6])
		if data[7] != 'no':
			self.query_targetip(data[7])
		if data[8] != 'no':
			self.query_time(data[8], data[9], data[10])
		self.click_process_search()
		self.click_process_reset()

	u'''申请历史查询
	   Parameters:
	      - data:excel一行数据集
	'''
	def query_apply_history(self, data):
		self.driver.implicitly_wait(5)
		self.cmf.select_menu(u"流程控制", u"申请历史")
		self.click_advanced()
		if data[1] != 'no':
			self.query_approval_status(data[1])
		if data[2] != 'no':
			self.query_approver(data[2])
		if data[3] != 'no':
			self.query_targetip(data[3])
		if data[4] != 'no':
			self.query_process_number(data[4])
		if data[5] != 'no':
			self.query_application_type(data[5])
		if data[6] != 'no':
			self.query_time(data[6], data[7], data[8])
		self.click_process_search()
		self.click_process_reset()

	u'''个人历史查询
	   Parameters:
	      - data:excel一行数据集
	'''
	def query_personal_history(self, data):
		self.driver.implicitly_wait(5)
		self.cmf.select_menu(u"流程控制", u"个人历史")
		self.query_common(data)

	u'''全部历史查询
	   Parameters:
	      - data:excel一行数据集
	'''
	def query_all_history(self, data):
		self.driver.implicitly_wait(5)
		self.cmf.select_menu(u"流程控制", u"全部历史")
		self.query_common(data)

	u'''部门历史查询
	   Parameters:
	      - data:excel一行数据集
	'''
	def query_department_history(self, data):
		self.driver.implicitly_wait(5)
		self.cmf.select_menu(u"流程控制", u"部门历史")
		self.query_common(data)

	u'''查询公共方法
	   Parameters:
	      - data:excel一行数据集
	'''
	def query_common(self, data):
		self.click_advanced()
		if data[2] != 'no':
			self.query_approval_status(data[2])
		if data[3] != 'no':
			self.query_applicant(data[3])
		if data[4] != 'no':
			self.query_approver(data[4])
		if data[5] != 'no':
			self.query_process_depart(data[5])
		if data[6] != 'no':
			self.query_process_number(data[6])
		if data[7] != 'no':
			self.query_targetip(data[7])
		if data[8] != 'no':
			self.query_application_type(data[8])
		if data[9] != 'no':
			self.query_time(data[9], data[10], data[11])
		self.click_process_search()
		self.click_process_reset()





