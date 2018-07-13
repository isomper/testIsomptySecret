#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2018/1/11
#模块描述：资源时间规则
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsompSecret/common/")
from _icommon import getElement,selectElement,frameElement
from _cnEncode import cnEncode
from _log import log
sys.path.append("/testIsompSecret/webElement/process/")
from test_access_approval_ment import Accapproval
sys.path.append("/testIsompSecret/webElement/rule")
from test_command_rule_ment import CommandRule

class RetimeRule(object):
	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cnEn = cnEncode()
		self.acproval = Accapproval(driver)
		self.command = CommandRule(driver)
		self.log = log()

	u'''点击删除'''
	def click_bulkdel_retime(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "delete_rule_time_resource")

	u'''选择默认动作
		Parameters:
			- staut:0代表禁止登录，1代表允许登录
	'''
	def select_default_type(self, state):
		try:
			valu = self.cnEn.is_float(state)
			self.frameElem.from_frame_to_otherFrame("rigthFrame")
			selem = self.getElem.find_element_with_wait_EC("id", "defaultType")
			self.selectElem.select_element_by_value(selem, valu)
		except Exception:
			print("Select default action failure")

	u'''点击运行状态'''
	def click_running_state(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "ruleState")

	u'''填写每月开始日期
		Parameters:
			- starttime:每月的开始时间
	'''
	def set_month_start_time(self, starttime):
		valu = self.cnEn.is_float(starttime)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear_EC("id", "fortMonthStartTime")
		self.getElem.find_element_wait_and_sendkeys("id", "fortMonthStartTime", valu)

	u'''填写每月结束日期
		Parameters:
			- endtime:每月的结束时间
	'''
	def set_month_end_time(self, endtime):
		valu = self.cnEn.is_float(endtime)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear_EC("id", "fortMonthEndTime")
		self.getElem.find_element_wait_and_sendkeys("id", "fortMonthEndTime", valu)

	u'''选择每周开始日期
		Parameters:
			- starttime:每周的开始时间
	'''
	def set_week_start_time(self, starttime):
		valu = self.cnEn.is_float(starttime)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		selem = self.getElem.find_element_with_wait_EC("id", "fortWeekStartTime")
		self.selectElem.select_element_by_value(selem, valu)

	u'''选择每周结束日期
		Parameters:
			- endtime:每周的结束时间
	'''
	def set_week_end_time(self, endtime):
		valu = self.cnEn.is_float(endtime)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		selem = self.getElem.find_element_with_wait_EC("id", "fortWeekEndTime")
		self.selectElem.select_element_by_value(selem, valu)

	u'''填写每天开始时间
		Parameters:
			- starttime:每天的开始时间
	'''
	def set_day_start_time(self, starttime):
		valu = self.cnEn.is_float(starttime)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear_EC("id", "fortDayStartTime")
		self.getElem.find_element_wait_and_sendkeys("id", "fortDayStartTime", valu)

	u'''填写每天结束时间
		Parameters:
			- endtime:每天的结束时间
	'''
	def set_day_end_time(self, endtime):
		valu = self.cnEn.is_float(endtime)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear_EC("id", "fortDayEndTime")
		self.getElem.find_element_wait_and_sendkeys("id", "fortDayEndTime", valu)

	u'''选择动作
		Parameters:
			- staut:0代表禁止登录，1代表允许登录
	'''
	def select_action(self, state):
		valu = self.cnEn.is_float(state)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		if valu == '1':
			self.getElem.find_element_wait_and_click_EC("id", "ruleTypePass")
		elif valu == '0':
			self.getElem.find_element_wait_and_click_EC("id", "ruleTypeDeny")

	u'''点击保存'''
	def click_save_retime(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "save_rule_time")

	u'''填写检索的资源名称
		Parameters:
			- rename:资源名称
	'''
	def set_query_rename(self, rename):
		resname = self.cnEn.is_float(rename)
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.getElem.find_element_wait_and_clear_EC("id", "fortResourceName")
		self.getElem.find_element_wait_and_sendkeys("id", "fortResourceName", resname)

	u'''勾选某个资源
		Parameters:
			- rename:资源名称
	'''
	def check_resource(self, rename):
		self.frameElem.from_frame_to_otherFrame("artIframe")
		self.set_query_rename(rename)
		self.command.click_check_resource()
		self.getElem.find_element_wait_and_click_EC("id", "resource_check_all")
		self.command.check_sure_button()

	u'''点击操作的公共方法
		parameter:
			- value:序号
			- statu:代表点击的操作，1代表勾选复选框；2代表上移；3代表下移；4代表插入；5代表编辑
	'''
	def click_option_method(self, value, status):
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
					xpath = ".//*[@id='content_table']/tbody/tr[" + str(line) + "]/td[1]/input[1]"
				#上移
				elif statu == '2':
					xpath = ".//*[@id='content_table']/tbody/tr[" + str(line) + "]/td[8]/a[1]"
				#下移
				elif statu == '3':
					xpath = ".//*[@id='content_table']/tbody/tr[" + str(line) + "]/td[8]/a[2]"
				#插入
				elif statu == '4':
					xpath = ".//*[@id='content_table']/tbody/tr[" + str(line) + "]/td[8]/a[3]"
				#编辑
				elif statu == '5':
					xpath = ".//*[@id='content_table']/tbody/tr[" + str(line) + "]/td[8]/a[4]"

				self.getElem.find_element_wait_and_click_EC("xpath", xpath)
				break

	u'''校验资源时间规则结果
		parameter:
			- data:数据集
	'''
	def check_resource_time_rule(self, data):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		row = self.acproval.select_resoure_sso(data[1])
		xpath = "//*[@id='content_table']/tbody/tr[" + str(row*2) + "]/td/div/table/tbody/tr/td[2]/a[1]/img"
		isExsit = self.getElem.is_element_exsit("xpath", xpath)
		if isExsit == True:
			self.log.log_detail(data[0], True)
		else:
			self.log.log_detail(data[0], True)