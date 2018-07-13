#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common")
from _icommon import getElement,selectElement,frameElement,commonFun
from _log import log
sys.path.append("/testIsompSecret/webElement/role/")
from test_roledf import Role
sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

class testSecretUserRole(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.frameElem = frameElement(driver)
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.role = Role(driver)
		self.dataFile = dataFileName()

	u'''获取数据
	Parameters:
		- sheetname:sheet名称
		return：表格数据
	'''
	def get_table_data(self,sheetname):
		filePath = self.dataFile.get_common_suite_test_data_url()
		fileData = self.dataFile.get_data(filePath,sheetname)
		return fileData

	#编辑运维角色
	def edit_operation_role(self):
		#日志开始记录
		self.log.log_start("edit_operation_role")
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		time.sleep(1)
		#点击编辑按钮
		editXpath = "html/body/form/div/div[6]/div[2]/div/table/tbody/tr[2]/td[6]/input"
		self.getElem.find_element_wait_and_click_EC('xpath',editXpath)
		self.role.set_tree_demo_switch('treeDemo_1_switch')
		time.sleep(1)
		#去掉监控、回放、阻断、下载
		self.role.set_input_click('1001010000002')
		self.role.set_input_click('1001010000003')
		self.role.set_input_click('1001010000010')
		self.role.set_input_click('1001010000013')
		self.role.save_role_button()
		self.log.log_detail(u"编辑运维角色",True)
		self.log.log_end("edit_operation_role")

	#添加系统管理员角色
	def set_sysAdmin_role(self):
		#日志开始记录
		self.log.log_start("set_sysAdmin_role")
		time.sleep(1)
		self.role.role_add_button()
		self.role.edit_rolename(u'系统管理员')
		self.role.edit_shortname(u'系管')
		#勾选组织定义和用户
		self.role.set_tree_demo_switch('treeDemo_3_switch')
		time.sleep(1)
		self.role.set_tree_demo_switch('treeDemo_4_check')
		self.role.set_tree_demo_check('treeDemo_8_check')
		#用户去掉角色
		self.role.set_input_click('1002020000008')
		#勾选流程控制
		self.role.set_tree_demo_switch('treeDemo_20_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_20_check')
		#去掉全部历史
		self.role.set_tree_demo_check('treeDemo_24_check')
		#口令计划
		self.role.set_tree_demo_switch('treeDemo_25_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_25_check')
		self.driver.execute_script("window.scrollBy(1000,0)","")
		#勾选系统配置
		self.role.set_tree_demo_switch('treeDemo_38_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_38_check')
		#去掉初始化设置
		self.role.set_tree_demo_switch('treeDemo_54_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_56_check')
		#去掉维护配置role.
		self.role.set_tree_demo_check('treeDemo_59_check')
		self.role.set_tree_demo_switch('treeDemo_38_switch')
		#选择密码包角色
		self.role.set_other_role(u'密码包接收人')
		time.sleep(1)
		#保存角色
		self.role.save_role_button()
		self.log.log_detail(u"添加系统管理员角色",True)
		self.log.log_end("set_sysAdmin_role")

	#添加安全保密管理员角色
	def set_secAdmin_role(self):
		#日志开始记录
		self.log.log_start("set_secAdmin_role")
		time.sleep(1)
		self.role.role_add_button()
		self.role.edit_rolename(u'安全保密管理员')
		self.role.edit_shortname(u'安保')
		#运维管理用户
		self.role.set_tree_demo_switch('treeDemo_3_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_8_check')
		#只勾选删除、编辑、用户状态、证书
		self.role.set_input_click('1002020000001')
		self.role.set_input_click('1002020000004')
		self.role.set_input_click('1002020000005')
		self.role.set_input_click('1002020000006')
		self.role.set_input_click('1002020000007')
		self.role.set_input_click('1002020000008')
		#资源、授权（不勾选可访问外部报表）、规则定义
		self.role.set_tree_demo_check('treeDemo_9_check')
		self.role.set_tree_demo_check('treeDemo_10_check')
		self.role.set_input_click('1002040000009')
		self.role.set_tree_demo_check('treeDemo_11_check')
		#配置审计、运维审计只勾选审计删除，命令详情，审批记录，查看历史，键盘记录，文件传输
		self.role.set_tree_demo_switch('treeDemo_16_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_17_check')
		self.role.set_input_click('1003010000003')
		self.role.set_input_click('1003010000004')
		self.role.set_input_click('1003010000011')
		self.role.set_input_click('1003010000014')
		self.role.set_tree_demo_check('treeDemo_18_check')
		self.role.set_tree_demo_switch('treeDemo_16_switch')
		time.sleep(1)
		#流程控制（全部历史）
		self.role.set_tree_demo_switch('treeDemo_20_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_24_check')
		#计划任务只勾选备份文件查看、备份文件下载
		self.role.set_tree_demo_switch('treeDemo_25_switch')
		time.sleep(1)
		self.role.set_tree_demo_switch('treeDemo_26_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_27_check')
		self.role.set_input_click('1005010100001')
		self.role.set_input_click('1005010100002')
		self.role.set_input_click('1005010100003')
		self.role.set_input_click('1005010100005')
		time.sleep(1)
		self.role.set_input_click('1005010100007')
		self.role.set_input_click('1005010100008')
		self.role.set_input_click('1005010100009')
		self.role.set_input_click('1005010100010')
		self.role.set_tree_demo_check('treeDemo_28_check')
		time.sleep(1)
		self.role.set_input_click('1005010200001')
		self.role.set_input_click('1005010200002')
		self.role.set_input_click('1005010200003')
		self.role.set_input_click('1005010200005')
		time.sleep(1)
		self.role.set_input_click('1005010200007')
		self.role.set_input_click('1005010200008')
		self.role.set_input_click('1005010200009')
		time.sleep(1)
		#系统配置（审计存留）
		self.role.set_tree_demo_switch('treeDemo_38_switch')
		time.sleep(1)
		self.role.set_tree_demo_switch('treeDemo_59_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_60_check')
		#策略配置
		self.role.set_tree_demo_switch('treeDemo_65_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_65_check')
		self.role.set_tree_demo_switch('treeDemo_38_switch')
		time.sleep(1)
		#选择密码包角色
		self.role.set_other_role(u'解密密钥接收人')
		time.sleep(1)
		#保存角色
		self.role.save_role_button()
		self.log.log_detail(u"添加安全保密管理员角色",True)
		self.log.log_end("set_secAdmin_role")

	#添加安全审计员角色
	def set_sysAudit_role(self):
		#日志开始记录
		self.log.log_start("set_sysAudit_role")
		time.sleep(1)
		self.role.role_add_button()
		self.role.edit_rolename(u'安全审计员')
		self.role.edit_shortname(u'安审')
		#运维管理（用户只勾选删除、编辑、用户状态、证书）
		self.role.set_tree_demo_switch('treeDemo_3_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_8_check')
		#只勾选删除、编辑、用户状态、证书
		self.role.set_input_click('1002020000001')
		self.role.set_input_click('1002020000004')
		self.role.set_input_click('1002020000005')
		self.role.set_input_click('1002020000006')
		self.role.set_input_click('1002020000007')
		self.role.set_input_click('1002020000008')
		self.role.set_tree_demo_switch('treeDemo_3_switch')
		time.sleep(1)
		#审计管理（配置审计，告警归纳）
		self.role.set_tree_demo_switch('treeDemo_16_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_18_check')
		self.role.set_tree_demo_check('treeDemo_19_check')
		self.role.set_tree_demo_switch('treeDemo_16_switch')
		time.sleep(1)
		#报表管理
		self.role.set_tree_demo_switch('treeDemo_30_switch')
		time.sleep(1)
		self.role.set_tree_demo_check('treeDemo_31_check')
		#保存角色
		self.role.save_role_button()
		self.log.log_detail(u"添加安全审计员角色",True)
		self.log.log_end("set_sysAudit_role")

	#添加涉密用户
	def add_secret_user(self):

		#日志开始记录
		self.log.log_start("add_secret_user")
		#获取用户测试数据
		secretData = self.get_table_data("add_user")
		self.frameElem.from_frame_to_otherFrame("topFrame")
		self.cmf.select_menu(u"运维管理", u"用户")

		for dataRow in range(len(secretData)):
			data = secretData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 and dataRow < 4:
					self.role.add_sercret_user(data[3], data[1], data[4], data[9])
					self.log.log_detail(data[0], True)

			except Exception as e:
				print ("add_secret_user fail:" + str(e))

		self.log.log_end("add_secret_user")

