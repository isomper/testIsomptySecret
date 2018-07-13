#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/7/18
#模块描述：资源
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName
sys.path.append("/testIsompSecret/common")
from _icommon import commonFun,frameElement
from _log import log
sys.path.append("/testIsompSecret/webElement/resource/")
from test_resource_common import Resource
from test_linux_ment import LinuxResource

class testLinuxResource(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.frameElem = frameElement(driver)
		self.resource = Resource(driver)
		self.linux = LinuxResource(driver)
		self.data = dataFileName()

	u'''提示内容框元素路径'''
	def div_msg(self):
		div_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		return div_msg

	u'''获取测试数据
	   Parameters:
	      - sheetname:sheet名称
	   return：表格数据
	'''
	def get_resource_table_data(self, sheetname):
		dataFile = dataFileName()
		resourcePath = dataFile.get_linux_resource_test_data_url()
		resourceData = dataFile.get_data(resourcePath, sheetname)
		return resourceData

	u'''添加linux资源'''
	def add_linux_resource_001(self):

		#日志开始记录
		self.log.log_start("add_resource")
		#获取添加资源测试数据
		resourceData = self.get_resource_table_data("add_linux_resource")
		#保存成功的弹出框
		resourceMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(resourceData)):
			data = resourceData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.resource.click_add_edit_button()
					self.resource.select_resource_type(data[2])
					self.linux.add_edit_linux_resource(data)
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", resourceMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("add_resource fail:" + str(e))

		self.log.log_end("add_resource")

	u'''编辑linux资源'''
	def edit_linux_resource_002(self):

		#日志开始记录
		self.log.log_start("edit_resource")
		#获取添加资源测试数据
		resourceData = self.get_resource_table_data("edit_linux_resource")
		#保存成功的弹出框
		resourceMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(resourceData)):
			data = resourceData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.resource.click_add_edit_button(data[2])
					self.linux.add_edit_linux_resource(data)
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", resourceMsg, data, flag)
					self.cmf.back()
			except Exception as e:
				print ("edit_resource fail:" + str(e))

		self.log.log_end("edit_resource")

	u'''检验linux资源'''
	def check_linux_resource_003(self):

		#日志开始记录
		self.log.log_start("check_linux_resource")
		#获取检验资源测试数据
		resourceData = self.get_resource_table_data("check_linux_resource")
		#保存成功的弹出框
		resourceMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		#点击添加按钮
		self.resource.click_add_edit_button()
		#选择debian类型
		self.resource.select_resource_type("Debian")

		for dataRow in range(len(resourceData)):
			data = resourceData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.linux.check_linux_resource(dataRow, data)
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", resourceMsg, data, flag)
			except Exception as e:
				print ("check_linux_resource fail:" + str(e))

		self.cmf.back()

		self.log.log_end("check_linux_resource")

	u'''查询资源'''
	def query_resource_004(self, dataPath, sheetName):

		#日志开始记录
		self.log.log_start("query_resource")
		#获取添加资源测试数据
		resourceData = self.data.get_data(dataPath, sheetName)

		for dataRow in range(len(resourceData)):
			data = resourceData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					if dataRow == 1:
						self.resource.query_depart(data[1])
					if dataRow == 2:
						self.resource.click_child_node()
						self.resource.query_depart(data[1])
					if dataRow == 3:
						self.resource.query_type(data[2], data[3], data[4])
					if dataRow >= 4 and dataRow <= 7:
						self.resource.query_ip_rename(data[5])
					if dataRow == 8:
						self.resource.query_type(data[2], data[3], data[4])
						self.resource.query_ip_rename(data[5])
					self.resource.click_resource_query()
					self.resource.click_reset()
					self.log.log_detail(data[0], True)
			except Exception as e:
				print ("query_resource fail:" + str(e))
		self.resource.click_resource_query()
		self.log.log_end("query_resource")

	u'''删除资源'''
	def del_resource_005(self, dataPath, sheetName):

		#日志开始记录
		self.log.log_start("del_resource")
		#获取添加资源测试数据
		resourceData = self.data.get_data(dataPath, sheetName)
		#保存成功的弹出框
		resourceMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(resourceData)):
			data = resourceData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.resource.click_del_button(data[2])
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", resourceMsg, data, flag)
					self.cmf.click_msg_button(1)
			except Exception as e:
				print ("del_resource fail:" + str(e))

		self.log.log_end("del_resource")

	u'''全选删除资源'''
	def bulkdel_resource_006(self):

		#日志开始记录
		self.log.log_start("bulkdel_resource")
		#获取添加资源测试数据
		resourceData = self.get_resource_table_data("bulkdel_resource")
		#保存成功的弹出框
		resourceMsg = self.div_msg()

		#无检查点的测试项标识，如果为True说明通过
		flag = False

		for dataRow in range(len(resourceData)):
			data = resourceData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.cmf.check_all()
					self.cmf.bulkdel("delete_resource")
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", resourceMsg, data, flag)
					self.cmf.click_msg_button(1)
			except Exception as e:
				print ("bulkdel_resource failure:" + str(e))

		self.log.log_end("bulkdel_resource")

