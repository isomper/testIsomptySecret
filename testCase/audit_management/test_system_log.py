#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/audit_management")
from systemLogElement import SystemLogPage

sys.path.append("/testIsompSecret/webElement/user")
from userElement import UserPage

sys.path.append("/testIsompSecret/testSuite")
from common_suite_file import CommonSuiteData
sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

class testSystemLog():
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.cnEnde = cnEncode()
		self.userElem = UserPage(driver)
		self.systemLog = SystemLogPage(self.driver)
		self.tableElem = tableElement(self.driver)
		self.selectElem = selectElement(driver)
		self.dataFile = dataFileName()
		self.frameElem = frameElement(self.driver)
		self.loginFun = loginPage(self.driver)
		self.commonSuite = CommonSuiteData(self.driver)
	
	u'''校验没有弹出框类型用例是否通过
			parameters: 
				data : 检查点
				count :正确的行数
	'''
	def check_without_pop_up(self,count,data):
		#获取行数
		table_count = str(self.systemLog.get_table_count())
		if count == table_count:
			self.cmf.test_win_check_point("","",data,True)
		else:
			self.cmf.test_win_check_point("","",data,False)

	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
			return：表格数据
	'''
	def get_table_data(self,sheetname):
		dataFile = dataFileName()
		filePath = dataFile.get_system_log_test_url()
		queryData = dataFile.get_data(filePath,sheetname)
		return queryData

	u'''配置审计检索功能'''
	def system_log_query_001(self):#query_type
		#日志开始记录
		self.log.log_start("SystemLogQuery_001")
		#获取配置审计检索的数据
		ad_data = self.get_table_data("system_log_query")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(ad_data)):
			data = ad_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.systemLog.select_date(data[2])
					if data[4] != "":
						self.userElem.set_dep(data[4])
						#data[4]代表是否勾选子节点(no代表不勾选)
						if data[3] != "no" :
							self.userElem.click_child_node()
					self.systemLog.select_system_log_type(data[5])
					self.systemLog.click_query()
					#判断测试项是否通过
					self.check_without_pop_up(data[6],data)
					#清空标识状态
					flag = False
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.userElem.click_reset_button()
			except Exception as e:
				print ("System Log query fail: ") + str(e)
		self.log.log_end("SystemLogQuery_001")