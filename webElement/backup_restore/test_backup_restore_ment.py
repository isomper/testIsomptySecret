#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2018/1/24
#模块描述：备份还原
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
sys.path.append("/testIsompSecret/common/")
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import CommonSuiteData
sys.path.append("/testIsomp/webElement/rule")
from test_command_rule_ment import CommandRule
sys.path.append("/testIsompSecret/webElement/user/")
from userElement import UserPage

class Backuprestore(object):
	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)
		self.cnEn = cnEncode()
		self.comsuit = CommonSuiteData(self.driver)
		self.command = CommandRule(self.driver)
		self.tableElem = tableElement(driver)
		self.log = log()
		self.userElem = UserPage(self.driver)

	u'''点击自动备份开关'''
	def auto_backup_switch(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "btn_qh")

	u'''勾选系统配置'''
	def check_sys_config(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		values = self.check_common()
		if values[0] == None:
			self.getElem.find_element_wait_and_click_EC("id", "configBackUp")
		if values[1] != None:
			self.getElem.find_element_wait_and_click_EC("id", "databaseBackUp")

	u'''勾选实体配置'''
	def check_entity_config(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		values = self.check_common()
		if values[0] != None:
			self.getElem.find_element_wait_and_click_EC("id", "configBackUp")
		if values[1] == None:
			self.getElem.find_element_wait_and_click_EC("id", "databaseBackUp")

	u'''勾选实体配置和系统配置'''
	def check_all_config(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		values = self.check_common()
		if values[0] == None:
			self.getElem.find_element_wait_and_click_EC("id", "configBackUp")
		if values[1] == None:
			self.getElem.find_element_wait_and_click_EC("id", "databaseBackUp")

	u'''勾选实体或者系统配置公共方法'''
	def check_common(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		selem = self.getElem.find_element_with_wait_EC("id", "configBackUp")
		value = selem.get_attribute('checked')
		selemdb = self.getElem.find_element_with_wait_EC("id", "databaseBackUp")
		valuedb = selemdb.get_attribute('checked')
		list = [value, valuedb]
		return list

	u'''勾选实体或者系统配置
		parameter:
			- stauts:勾选配置信息1代表系统配置2代表实体配置，3代表系统配置和实体配置
	'''
	def check_config(self, stauts):
		staut = self.cnEn.is_float(stauts)
		if staut == '1':
			self.check_sys_config()
		elif staut == '2':
			self.check_entity_config()
		else:
			self.check_all_config()

	u'''选择备份方式
		parameter:
			- stauts:value属性值，1代表一次性执行，2代表周期性执行
	'''
	def select_backup_mode(self, stauts):
		staut = self.cnEn.is_float(stauts)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		selem = self.getElem.find_element_with_wait_EC("id", "backUpType")
		self.selectElem.select_element_by_value(selem, staut)

	u'''选择执行小时
		parameter:
			- stauts:value属性值
	'''
	def select_hour(self, stauts):
		staut = self.cnEn.is_float(stauts)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		selem = self.getElem.find_element_with_wait_EC("id", "startHour")
		self.selectElem.select_element_by_value(selem, staut)

	u'''填写分钟
		parameter:
			- minute:分钟
	'''
	def set_minute(self, minute):
		minu = self.cnEn.is_float(minute)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear_EC("id", "startMinute")
		self.getElem.find_element_wait_and_sendkeys("id", "startMinute", minu)

	u'''选择执行方式
		parameter:
			- staut:0代表按天，1代表按周，2代表按月，3代表按年
	'''
	def select_execu_mode(self, staut):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		if staut == 0:
			self.getElem.find_element_wait_and_click_EC("id", "dayradio")
		elif staut == 1:
			self.getElem.find_element_wait_and_click_EC("id", "weekradio")
		elif staut == 2:
			self.getElem.find_element_wait_and_click_EC("id", "monthRadio")
		else:
			self.getElem.find_element_wait_and_click_EC("id", "yearRadio")

	u'''选择存储位置
		parameter:
			- stauts:value属性值1代表本地备份2代表ftp备份
	'''
	def select_storage_location(self, stauts):
		staut = self.cnEn.is_float(stauts)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		selem = self.getElem.find_element_with_wait_EC("id", "backUpLocation")
		self.selectElem.select_element_by_value(selem, staut)

	u'''填写远程路径
		parameter:
			- path:远程路径
	'''
	def set_remote_path(self, path):
		pat = self.cnEn.is_float(path)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear_EC("id", "path")
		self.getElem.find_element_wait_and_sendkeys("id", "path", pat)

	u'''填写服务器IP
		parameter:
			- ip:服务器IP
	'''
	def set_ftpip(self, ip):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear_EC("id", "ip")
		self.getElem.find_element_wait_and_sendkeys("id", "ip", ip)

	u'''填写连接用户名
		parameter:
			- minute:连接用户名
	'''
	def set_name(self, name):
		nam = self.cnEn.is_float(name)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear_EC("id", "username")
		self.getElem.find_element_wait_and_sendkeys("id", "username", nam)

	u'''填写连接口令
		parameter:
			- password:连接口令
	'''
	def set_password(self, password):
		pwd = self.cnEn.is_float(password)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear_EC("id", "password")
		self.getElem.find_element_wait_and_sendkeys("id", "password", pwd)

	u'''填写确认口令
		parameter:
			- minute:分钟
	'''
	def set_password_again(self, password):
		pwd = self.cnEn.is_float(password)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear_EC("id", "passwordAgain")
		self.getElem.find_element_wait_and_sendkeys("id", "passwordAgain", pwd)

	u'''点击立刻备份'''
	def click_backup_immediately(self):
		time.sleep(3)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "back_up_now")

	u'''点击保存'''
	def click_save(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "back_up_save")

	u'''选择系统备份还原或者查看备份文件
		parameter:
			- staut:0代表系统备份还原，1代表查看备份文件
	'''
	def select_backup_menu(self, staut):
		time.sleep(3)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		if staut == 0:
			self.getElem.find_element_wait_and_click_EC("id", "tit1")
		elif staut == 1:
			self.getElem.find_element_wait_and_click_EC("id", "tit2")

	u'''点击操作列操作
		Parameters:
			- filename:文件名称
			- value:1代表下载，2代表删除，3代表还原
	'''
	def click_operat_file(self,filename, value):
		time.sleep(2)

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		row = 1
		selems = self.driver.find_elements_by_name("file")
		for selem in selems:
			idvalue = selem.get_attribute('id')
			row = row +1
			if idvalue == filename:
				xpath = ".//*[@id='content_rt02']/div/table/tbody/tr[" + str(row) + "]/td[7]/input[" + str(value) + "]"
		self.getElem.find_element_wait_and_click_EC("xpath", xpath)
		time.sleep(1)

	u'''下载上传完成后点击操作列操作
		Parameters:
			- filename:文件名称
			- value:1代表下载，2代表删除，3代表还原
	'''
	def upload_click_operat_file(self,filename, value):

		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		row = 1
		filenames = ""+filename[:-6] + ""+filename+""
		selems = self.driver.find_elements_by_name("file")
		for selem in selems:
			idvalue = selem.get_attribute('id')
			row = row +1
			if idvalue == filename or idvalue == filenames:
				xpath = ".//*[@id='content_rt02']/div/table/tbody/tr[" + str(row) + "]/td[7]/input[" + str(value) + "]"
		self.getElem.find_element_wait_and_click_EC("xpath", xpath)
		time.sleep(1)

	u'''点击还原系统配置'''
	def click_restore_sys_config(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "deleConfig1")

	u'''点击清空数据库'''
	def click_reset_database(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "resetDataBase1")

	u'''点击清空数据库'''
	def click_reset_audit(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "delAuditFile1")

	u'''填写syslogip
		parameter:
			- syslogip:syslogip
	'''
	def set_syslogip(self, syslogip):
		ip = self.cnEn.is_float(syslogip)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear_EC("id", "host")
		self.getElem.find_element_wait_and_sendkeys("id", "host", ip)

	u'''填写syslog端口
		parameter:
			- port:syslog端口
	'''
	def set_port(self, port):
		sysport = self.cnEn.is_float(port)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear_EC("id", "port")
		self.getElem.find_element_wait_and_sendkeys("id", "port", sysport)

	u'''点击syslog保存'''
	def click_syslog_save(self):
		time.sleep(2)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "save_syslog")

	u'''获取syslogip值'''
	def get_syslog_port(self):
		time.sleep(2)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		selem = self.getElem.find_element_with_wait_EC("id", "port")
		value = selem.get_attribute("value")
		return value

	u'''获取文件名称'''
	def get_file_name(self):
		time.sleep(2)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		selem = self.getElem.find_element_with_wait_EC("xpath", ".//*[@id='content_rt02']/div/table/tbody/tr[2]")
		value = selem.get_attribute('id')
		return value

	u'''编辑syslog
		parameter:
			- ip:syslogip
			- port:端口
	'''
	def set_syslog(self, port, ip='no'):
		time.sleep(2)
		self.comsuit.switch_to_moudle(u'系统配置', u'关联服务')
		self.command.click_left_rule(1)
		if ip != 'no':
			self.set_syslogip(ip)
		self.set_port(port)
		self.click_syslog_save()
		self.frameElem.switch_to_content()
		self.cmf.click_msg_button(1)

	u'''检验syslog端口是否为备份之前信息
		parameter:
			- port:端口
			- checklog:检验信息
	'''
	def check_syslog_content(self, port, checklog):
		time.sleep(2)
		self.comsuit.switch_to_moudle(u'系统配置', u'关联服务')
		self.command.click_left_rule(1)
		elemText = self.get_syslog_port()
		strdata3 = self.cnEn.is_float(port)
		if elemText == strdata3:
			self.log.log_detail(checklog, True)
		else:
			self.log.log_detail(checklog, False)

	u'''校验用户或者角色信息
		Parameters:
			- namevalue:传入的要被查询名称
			- name:表格列的name属性
			- checklog:日志信息
		return：定位该名称位于第几行
	'''
	def check_content(self,namevalue, name, checklog):
		time.sleep(2)
		self.cmf.select_menu(u"运维管理", u"用户")
		row = self.cmf.find_row_by_name(namevalue, name)
		if row != 0:
			self.log.log_detail(checklog, True)
		else:
			self.log.log_detail(checklog, False)

	u'''填写用户信息
		parameters:
			account : 用户账号
			name : 用户名称
			pwd : 用户密码
			agpwd : 确认密码
	'''
	def set_user_info(self, account, name, pwd, agpwd):
		time.sleep(1)
		self.comsuit.switch_to_moudle(u"运维管理", u"用户")
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.userElem.add_button()
		self.userElem.set_user_account(account)
		self.userElem.set_user_name(name)
		self.userElem.set_user_pwd(pwd)
		self.userElem.set_user_enquire_pwd(agpwd)
		self.userElem.save_button()
		self.frameElem.switch_to_content()
		self.cmf.click_login_msg_button()

	u'''点击用户操作列对应的删除按钮
		parameters:
			- account : 用户账号
	'''
	def del_user_info(self, account):
		time.sleep(1)
		self.comsuit.switch_to_moudle(u"运维管理", u"用户")
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.userElem.operate_delete(account)
		self.frameElem.switch_to_content()
		self.cmf.click_msg_button(1)
		self.frameElem.switch_to_content()
		self.cmf.click_msg_button(1)

	u'''点击备份还原配置文件的删除
		parameters:
			- filename : 文件名称
			- loginfo : 日志信息
	'''
	def del_backup_file(self, filename, loginfo):
		self.click_operat_file(filename, 2)
		self.frameElem.switch_to_content()
		self.cmf.click_msg_button(1)
		self.frameElem.switch_to_content()
		self.cmf.click_msg_button(1)
		time.sleep(1)
		self.log.log_detail(loginfo, True)

	u'''执行还原操作
		parameters:
			- filename :执行还原的文件名称
			- loginfo :日志信息
			- stauts :状态1代表执行操作列按钮2代表进行上传后操作列按钮
	'''
	def execute_restore(self, filename, loginfo, stauts=1):
		time.sleep(2)
		self.comsuit.switch_to_moudle(u'系统配置', u'备份还原')
		self.command.click_left_rule(0)
		self.select_backup_menu(1)
		if stauts == 1:
			self.click_operat_file(filename, 3)
		elif stauts == 2:
			self.upload_click_operat_file(filename, 3)
		time.sleep(10)
		self.frameElem.switch_to_content()
		time.sleep(10)
		self.getElem.find_element_with_wait_EC("classname", "aui_state_highlight")
		self.cmf.click_msg_button(1)
		self.log.log_detail(loginfo, True)

	u'''配置备份信息
		parameters:
			- data :数据文件集
			- backMsg :保存成功的弹出框信息
			- flag :无检查点的测试项标识，如果为True说明通过
	'''
	def config_backup(self, data, backMsg, flag):
		time.sleep(2)
		self.comsuit.switch_to_moudle(u'系统配置', u'备份还原')
		self.command.click_left_rule(0)
		self.check_config(data[12])
		self.select_backup_mode(data[4])
		self.backup_time(data[5], data[6])
		self.select_storage_location(data[7])
		self.click_save()
		time.sleep(3)
		self.frameElem.switch_to_content()
		self.cmf.test_win_check_point("xpath", backMsg, data, flag)
		self.click_backup_immediately()
		time.sleep(3)
		self.frameElem.switch_to_content()
		self.cmf.click_msg_button(1)
		self.log.log_detail(data[9], True)
		self.select_backup_menu(1)

	u'''执行日期
		Parameters:
			- type :t代表今天，c代表clear，q代表确定，默认选择今天
			- backuptime :执行日期设定的日期，格式为2016-9-7 11:42:42
	'''
	def backup_time(self, types, backuptime):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		# 时间控件的fram的xpath
		fxpath = "//iframe[@hidefocus='true']"
		# 日期控件table的xpath路径
		txpath = "/html/body/div/div[3]/table"
		status = self.cnEn.is_float('0')
		type = self.cnEn.is_float(types)
		# 转成datetime对象
		date = datetime(*xldate_as_tuple(backuptime, 0))
		end = date.strftime('%Y-%m-%d %H:%M:%S')
		self.option_time("backUpTime", fxpath, status, type, txpath, end)

	u'''操作时间控件
		Parameters:
			- wdateId：日期控件input控件的ID值
			- fxpath：日期控件frame的xpath路径
			- status: 日期控件是否有时分秒
			- txpath：日期控件table的xpath路径
			- time：设定的日期，格式为2016-9-7 11:42:42
			- type：t代表今天，c代表clear，q代表确定，默认选择今天
	'''
	def option_time(self,wdateId,fxpath,status='0',type='t',txpath = None,dtime = None):
		time.sleep(2)
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
				self.getElem.find_element_wait_and_click_EC("id", "backUpTime")
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
									time.sleep(2)
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

	u'''上传操作
		parameters:
			- filename :执行还原的文件名称
			- loginfo :日志信息
	'''
	def backup_file_upload(self, filename, loginfo):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		value = "C:\Users\圆圆\Downloads\\" + filename+""
		time.sleep(1)
		self.getElem.find_element_wait_and_sendkeys("id", "backUpFile", value)
		time.sleep(2)
		self.getElem.find_element_wait_and_click_EC("id", "up_file")
		time.sleep(5)
		self.frameElem.switch_to_content()
		self.cmf.click_msg_button(1)
		time.sleep(1)
		self.log.log_detail(loginfo, True)

