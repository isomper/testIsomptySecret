#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2018/1/9
#模块描述：地址规则
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
sys.path.append("/testIsompSecret/webElement/process/")
from test_access_approval_ment import Accapproval
#导入用户元素类
sys.path.append("/testIsompSecret/webElement/user/")
from userElement import UserPage

class AddressRule(object):
	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)
		self.cnEn = cnEncode()
		self.acproval = Accapproval(driver)
		self.user = UserPage(driver)

	u'''点击批量删除'''
	def click_bulkdel_address(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "delete_rule_address")

	u'''点击编辑按钮
		Parameters:
			- addressname:地址规则名称
	'''
	def click_edit_address(self, addressname):
		try:
			self.frameElem.from_frame_to_otherFrame("rigthFrame")
			row = self.acproval.find_name_by_row(addressname, "fortRuleAddressName")
			update_xpath = ".//*[@id='content_table']/tbody/tr[" + str(row) + "]/td[5]/input[1]"
			time.sleep(3)
			self.getElem.find_element_wait_and_click("xpath", update_xpath)
		except Exception:
			print("Click the Edit button to fail")

	u'''点击删除按钮
		Parameters:
			- addressname:时间规则名称
	'''
	def click_del_address(self, addressname):
		try:
			self.frameElem.from_frame_to_otherFrame("rigthFrame")
			row = self.acproval.find_name_by_row(addressname, "fortRuleAddressName")
			del_xpath = ".//*[@id='content_table']/tbody/tr[" + str(row) + "]/td[5]/input[2]"
			self.getElem.find_element_wait_and_click("xpath", del_xpath)
		except Exception:
			print("Click the Del button to fail")

	u'''填写检索名称
		Parameters:
			- addressname:名称
	'''
	def set_search_addressname(self, addressname):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		name = self.cnEn.is_float(addressname)
		self.getElem.find_element_wait_and_clear("id", "rule_address_id")
		self.getElem.find_element_wait_and_sendkeys("id", "rule_address_id", name)

	u'''点击检索按钮'''
	def click_search_address(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "rule_address")

	u'''填写地址规则名称
		Parameters:
			- rulename:规则名称
	'''
	def set_rulename(self, rulename):
		name = self.cnEn.is_float(rulename)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear("id", "fortRuleAddressName")
		self.getElem.find_element_wait_and_sendkeys("id", "fortRuleAddressName", name)

	u'''选择IP规则
		Parameters:
			- stauts:1代表勾选IP掩码，2代表勾选IP区间，3代表IP掩码和IP区间
	'''
	def checkbox_ip_rule(self, stauts):
		staut = self.cnEn.is_float(stauts)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		if staut == '1':
			self.getElem.find_element_wait_and_click_EC("id", "one_ip")
		elif staut == '2':
			self.getElem.find_element_wait_and_click_EC("id", "duo_ip")
		else:
			self.getElem.find_element_wait_and_click_EC("id", "one_ip")
			self.getElem.find_element_wait_and_click_EC("id", "duo_ip")

	u'''点击增加多个IP'''
	def click_add_more_ip(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "add_ip_mask")

	u'''填写ip地址
		Parameters:
			- iplist:所填写的IP列表集合
	'''
	def set_ip(self, iplist):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		#获取所有页面IP地址集合
		fortips = self.driver.find_elements_by_name("fortIp")
		ipaddress = iplist.split()
		self.ip_mask_common(fortips, ipaddress)

	u'''填写ip地址掩码
		Parameters:
			- masklist:所填写的IP掩码value值列表集合
	'''
	def set_ip_mask(self, masklist):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		#获取所有页面IP掩码集合
		fortMasks = self.driver.find_elements_by_name("fortMask")
		masklists = masklist.split()
		self.ip_mask_common(fortMasks, masklists)

	u'''填写IP地址和掩码公共方法
		Parameters:
			- ipsets:页面IP段集合
			- dataipsets:列表数据集合
	'''
	def ip_mask_common(self, ipsets, dataipsets):
		#获取页面集合长度
		ipsetth = len(ipsets)
		fortth = 0
		#循环ip掩码进行填写操作
		for ipset in ipsets:
			if fortth < ipsetth and dataipsets[fortth] != 'no':
				fortips = self.driver.find_elements_by_name("fortIp")
				if ipsets == fortips:
					ipset.clear()
				ipset.send_keys(dataipsets[fortth])
				fortth = fortth + 1

	u'''点击增加多个IP段'''
	def click_add_ip_segment(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "add_ip_range")

	u'''填写起始段IP
		Parameters:
			- ipstartlist:所填写的起始段IP列表集合
	'''
	def set_ip_start(self, ipstartlist):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		ipstarts = ipstartlist.split()
		self.ip_segment_common("fortIpStart", ipstarts)

	u'''填写结束段IP
		Parameters:
			- ipendlist:所填写的结束段IP列表集合
	'''
	def set_ip_end(self, ipendlist):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		ipends = ipendlist.split()
		self.ip_segment_common("fortIpEnd", ipends)

	u'''填写区间段IP公共方法
		Parameters:
			- ipsetname:页面IP段name属性
			- dataipsets:列表数据集合
	'''
	def ip_segment_common(self, ipsetname, dataipsets):
		#获取所有页面IP段集合
		ipsets = self.driver.find_elements_by_name(ipsetname)
		#获取IP段集合长度
		ipsetsth = len(ipsets)
		fortth = 0
		#循环进行段ip填写操作
		for ipset in ipsets:
			if fortth < ipsetsth:
				ipset.clear()
				ipset.send_keys(dataipsets[fortth])
				fortth = fortth + 1

	u'''点击测试'''
	def click_test(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "test_ip")

	u'''填写测试ip地址
		Parameters:
			- testip:ip地址
	'''
	def set_ip_test(self, testip):
		ip = self.cnEn.is_float(testip)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear("id", "testIp")
		self.getElem.find_element_wait_and_sendkeys("id", "testIp", ip)

	u'''填写描述信息
		Parameters:
			- description:描述信息
	'''
	def set_description(self, description):
		descript = self.cnEn.is_float(description)
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_clear("id", "fortDescription")
		self.getElem.find_element_wait_and_sendkeys("id", "fortDescription", descript)

	u'''点击保存'''
	def click_save(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "save_rule_address")

	u'''点击返回'''
	def click_back(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "history_skip")

	u'''给用户添加地址规则
		Parameters:
			- username：要编辑的用户名称
			- adrerule：地址规则名称
	'''
	def edit_user_address_rule(self, username, adrerule):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		name = self.cnEn.is_float(username)
		self.user.operate_edit(name)
		self.user.click_advanced_option()
		self.select_adress_rule(adrerule)
		self.user.save_button()
		self.cmf.click_login_msg_button()
		self.user.click_back_button()

	u'''选择地址规则
		Parameters:
			- adrerule：地址规则名称
	'''
	def select_adress_rule(self, adrerule):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		addressrule = self.cnEn.is_float(adrerule)
		select_elem = self.getElem.find_element_with_wait_EC('id',"fortRuleAddressId")
		self.selectElem.select_element_by_visible_text(select_elem, addressrule)