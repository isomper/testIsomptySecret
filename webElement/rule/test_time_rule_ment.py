#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/9/1
#模块描述：时间规则
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
from datetime import datetime
from xlrd import xldate_as_tuple
sys.path.append("/testIsomp/common/")
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
sys.path.append("/testIsomp/webElement/process/")
from test_access_approval_ment import Accapproval
#导入用户元素类
sys.path.append("/testIsomp/webElement/user/")
from userElement import UserPage

class TimeRule(object):
	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.tableElem = tableElement(driver)
		self.cmf = commonFun(driver)
		self.cnEn = cnEncode()
		self.acproval = Accapproval(driver)
		self.user = UserPage(driver)

	u'''点击批量删除'''
	def click_bulkdel_time(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "delete_rule_time")

	u'''填写时间规则名称
	   Parameters:
            - rulename:时间规则名称
	'''
	def set_rulename(self, rulename):
		name = self.cnEn.is_float(rulename)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear("id", "fortRuleTimeName")
		self.getElem.find_element_wait_and_sendkeys("id", "fortRuleTimeName", name)

	u'''选择部门
	   Parameters:
            - deptname:部门名称
	'''
	def select_depart(self, deptname):
		name = self.cnEn.is_float(deptname)
		self.select_depart_right_common("department_name", "tree_1_switch", name)
		time.sleep(2)

	u'''启动日期
	   Parameters:
            - type：t代表今天，c代表clear，q代表确定，默认选择今天
            - starttime:启动日期
	'''
	def start_date(self, types, starttime=None):
		time.sleep(2)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		# 时间控件的fram的xpath
		# fxpath = "//iframe[@hidefocus='true']"
		fxpath = "/html/body/div/iframe"
		# 日期控件table的xpath路径
		txpath = "/html/body/div/div[3]/table"
		status = self.cnEn.is_float('0')
		type = self.cnEn.is_float(types)
		if starttime != None:
			# 转成datetime对象
			date = datetime(*xldate_as_tuple(starttime, 0))
			start = date.strftime('%Y-%m-%d %H:%M:%S')
			self.option_time_rule("fortStartTime", fxpath, status, type, txpath, start)
		else:
			self.option_time_rule("fortStartTime", fxpath, status, type, txpath)

	u'''结束日期
	   Parameters:
            - type：t代表今天，c代表clear，q代表确定，默认选择今天
            - endtime:结束日期设定的日期，格式为2016-9-7 11:42:42
	'''
	def date_of_termination(self, types, endtime):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		# 时间控件的fram的xpath
		fxpath = "//iframe[@hidefocus='true']"
		# 日期控件table的xpath路径
		txpath = "/html/body/div/div[3]/table"
		status = self.cnEn.is_float('0')
		type = self.cnEn.is_float(types)
		# 转成datetime对象
		date = datetime(*xldate_as_tuple(endtime, 0))
		end = date.strftime('%Y-%m-%d %H:%M:%S')
		self.option_time_rule("fortEndTime", fxpath, status, type, txpath, end)

	u'''设置状态类型
	   Parameters:
            - status: 状态类型0代表禁止使用，1代表允许使用
	'''
	def set_status_type(self, status):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		statu = self.cnEn.is_float(status)
		selem = self.getElem.find_element_with_wait_EC("id", "fortAccessType")
		self.selectElem.select_element_by_value(selem, statu)

	u'''设置时间
	   Parameters:
            - method: 设置方式 option的value值
            - weeks: 星期(可多选)option的value值
            - hours: 小时(可多选)
	'''
	def set_time(self, methods, weeks, hours='no'):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		#设置时间方式
		method = self.cnEn.is_float(methods)
		selem = self.getElem.find_element_with_wait_EC("id", "method")
		self.selectElem.select_element_by_value(selem, method)
		#设置日期
		week = weeks.split()
		if methods == "weeks":
			for data in week:
				welem = self.getElem.find_element_with_wait_EC("id", "fortWeeks")
				self.selectElem.select_element_by_value(welem, data)
		elif methods == "days":
			for data in week:
				welem = self.getElem.find_element_with_wait_EC("id", "fortDays")
				self.selectElem.select_element_by_value(welem, data)
		if hours != 'no':
			#设置小时
			hour = hours.split()
			for hr in hour:
				helem = self.getElem.find_element_with_wait_EC("id", "fortHours")
				self.selectElem.select_element_by_value(helem, hr)

	u'''取消时间
	   Parameters:
            - method: 设置方式 option的value值
            - weeks: 星期(可多选)option的value值
            - hours: 小时(可多选)
	'''
	def deselect_time(self, methods, weeks, hours='no'):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		#设置日期
		week = weeks.split()
		if methods == "weeks":
			for data in week:
				welem = self.getElem.find_element_with_wait_EC("id", "fortWeeks")
				self.selectElem.deselect_element_by_value(welem, data)
		elif methods == "days":
			for data in week:
				welem = self.getElem.find_element_with_wait_EC("id", "fortDays")
				self.selectElem.deselect_element_by_value(welem, data)
		if hours != 'no':
			#设置小时
			hour = hours.split()
			for hr in hour:
				helem = self.getElem.find_element_with_wait_EC("id", "fortHours")
				self.selectElem.deselect_element_by_value(helem, hr)

	u'''填写描述信息
	   Parameters:
            - descrip:描述信息
	'''
	def set_descrip(self, descrip):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		description = self.cnEn.is_float(descrip)
		self.getElem.find_element_wait_and_clear("id", "fortDescription")
		self.getElem.find_element_wait_and_sendkeys("id", "fortDescription", description)

	u'''点击保存按钮'''
	def click_save_time(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "save_rule_time")

	u'''填写检索名称
	   Parameters:
            - timename:名称
	'''
	def set_search_timename(self, timename):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		name = self.cnEn.is_float(timename)
		self.getElem.find_element_wait_and_clear("id", "fortRuleTimeName")
		self.getElem.find_element_wait_and_sendkeys("id", "fortRuleTimeName", name)

	u'''点击检索按钮'''
	def click_search_time(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "retFortRuleTimeName")

	u'''点击重置'''
	def click_reset_time(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "resetting")

	u'''点击编辑按钮
	   Parameters:
	      - timename:时间规则名称
	'''
	def click_edit_time(self, timename):
		try:
			self.frameElem.from_frame_to_otherFrame("rigthFrame")
			row = self.acproval.find_name_by_row(timename, "fortRuleTimeName")
			update_xpath = "/html/body/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[1]"
			self.getElem.find_element_wait_and_click("xpath", update_xpath)
		except Exception:
			print("Click the Edit button to fail")

	u'''点击删除按钮
	   Parameters:
	      - timename:时间规则名称
	'''
	def click_del_time(self, timename):
		try:
			self.frameElem.from_frame_to_otherFrame("rigthFrame")
			row = self.acproval.find_name_by_row(timename, "fortRuleTimeName")
			del_xpath = "/html/body/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[2]"
			self.getElem.find_element_wait_and_click("xpath", del_xpath)
		except Exception:
			print("Click the Del button to fail")

	u'''选择部门公共方法
	   parameter:
	       - idname:填写框id
	       - swithid:部门展开按钮id
	       - deptname:部门名称
	'''
	def select_depart_right_common(self, idname, swithid, deptname):
		try:
			time.sleep(2)
			self.frameElem.from_frame_to_otherFrame("rigthFrame")
			self.getElem.find_element_wait_and_click_EC('id', idname)
			time.sleep(2)
			self.getElem.find_element_wait_and_click_EC('id', swithid)

			#获取所有a标签的对象
			elems = self.driver.find_elements_by_tag_name("a")

			for elem in elems:
				elemtext = elem.get_attribute("title")
				elemid = elem.get_attribute("id")

				if deptname == elemtext:
					self.getElem.find_element_wait_and_click("id", elemid)
					break

		except Exception as e:
			print "Department select error:" + str(e)

	u'''操作时间控件
        Parameters:
            - wdateId：日期控件input控件的ID值
            - fxpath：日期控件frame的xpath路径
            - status: 日期控件是否有时分秒
            - txpath：日期控件table的xpath路径
            - time：设定的日期，格式为2016-9-7 11:42:42
            - type：t代表今天，c代表clear，q代表确定，默认选择今天
    '''
	def option_time_rule(self,wdateId,fxpath,status='0',type='t',txpath = None,dtime = None):
		self.getElem.find_element_wait_and_click("id",wdateId)
		frame = self.driver.find_element_by_xpath(fxpath)
		self.driver.switch_to_frame(frame)

		if type == 't':
			self.getElem.find_element_wait_and_click("id","dpTodayInput")
		elif type == 'c':
			self.getElem.find_element_wait_and_click("id","dpClearInput")
		elif type == 'q':
			if dtime is not None:
				list = dtime.split()
				ymdList = list[0].split("-")
				hmsList = list[1].split(":")
				#年
				tYear = ymdList[0]
				#月
				tMon = ymdList[1]
				#日
				tDay = ymdList[2]
				#时
				tHour = hmsList[0]
				#分
				tMin = hmsList[1]
				#秒
				tSen = hmsList[2]

				dTitle = self.getElem.find_element_with_wait("id","dpTitle").find_elements_by_tag_name("input")

				#设定月
				dTitle[0].clear()
				dTitle[0].send_keys(tMon)

				#设定年
				dTitle[1].clear()
				dTitle[1].send_keys(tYear)
				time.sleep(2)
				self.frameElem.from_frame_to_otherFrame("rigthFrame")
				if wdateId == "fortStartTime":
					self.getElem.find_element_wait_and_click_EC("id", "fortStartTime")
				elif wdateId == "fortEndTime":
					self.getElem.find_element_wait_and_click_EC("id", "fortEndTime")
				self.driver.switch_to_frame(frame)

				if txpath is not None:

					iStatus = False

					for itr in range(7):
						if itr != 0:
							for itd in range(7):
								ct = self.tableElem.get_table_cell_text(txpath,itr,itd)[0]

								#排除第一行大于7的
								if itr == 1 and int(ct) > 7:
									continue

								#排除倒数第二行小于15的
								if itr == 5 and int(ct) < 15:
									continue

								#排除最后一行小于15的
								if itr == 6 and int(ct) < 15:
									continue

								#如果跟给定的日期一致，点击日期
								if int(ct) == int(tDay):
									self.tableElem.get_table_cell_text(txpath,itr,itd)[1].click()
									iStatus = True
									break

								#找到日期后跳出循环
								if iStatus:
									break
		#日期控件是否有时分秒
		if status == '1':
			dTime = self.getElem.find_element_with_wait("id","dpTime").find_elements_by_tag_name("input")
			#设定小时
			dTime[0].clear()
			dTime[0].send_keys(tHour)
			#设定分钟
			dTime[2].clear()
			dTime[2].send_keys(tMin)
			#设定秒
			dTime[4].clear()
			dTime[4].send_keys(tSen)
			self.getElem.find_element_wait_and_click("id","dpOkInput")

	u'''给用户添加时间规则
        Parameters:
            - username：要编辑的用户名称
            - timerule：时间规则test值
    '''
	def edit_user_time_rule(self, username, timerule):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		name = self.cnEn.is_float(username)
		self.user.operate_edit(name)
		self.user.click_advanced_option()
		self.select_time_rule(timerule)
		self.user.save_button()
		self.cmf.click_login_msg_button()
		self.user.click_back_button()

	u'''选择时间规则
        Parameters:
            - timerule：时间规则test值
    '''
	def select_time_rule(self, timerule):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		timer = self.cnEn.is_float(timerule)
		select_elem = self.getElem.find_element_with_wait_EC('id',"fortRuleTimeId")
		self.selectElem.select_element_by_visible_text(select_elem, timer)