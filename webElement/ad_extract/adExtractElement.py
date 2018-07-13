#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：顾亚茹
#生成日期：2018-01-08
#模块描述：AD定时抽取
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log
sys.path.append("/testIsompSecret/webElement/sso/")
from keyapi import Command


class AdExtractPage():
    #连接/属性
    CONNECT_TAB = "connect_tab"
    #发现
    DISCOVER_TAB = "find_tab"
    #历史记录
    HISTORY_TAB = "history_tab"
    #域服务器IP
    SERVER_IP = "ip"
    #域服务器端口
    SERVER_PORT = "port"
    #Base DN
    BASE_DN = "base_dn"
    #管理员
    SERVER_ADMIN = "admin"
    #管理员口令
    SERVER_PWD = "admin_pwd"
    #用户归属节点1
    USER_HOME_NODE1 = "//td[@id='nodes']/div[1]/input[1]"
    #用户归属节点2
    USER_HOME_NODE2 = "//td[@id='nodes']/div[2]/input[1]"
    #查询条件
    QUERY_CONDTION = "query_criteria"
    #子树查询
    SUBTREE_QUERY = "subtree_query"
    #添加多个节点
    ADD_MULI_NODE = "add_node"
    #删除节点
    DEL_NODE = "del_node"
    #获取所有节点
    GET_ALL_NODE = "get_all_node"
    #AD对象属性查询
    AD_ATTRI_QUERY = "btn_high"
    #查询对象
    QUERY_OBJ = "query_obj"
    #查询属性列表
    QUERY_ATTR_LIST = "btn_cx"
    #用户属性映射
    USER_ATTR_MAP = "btn_ys"
    #用户账号映射
    USER_ACCOUNT_MAP = "fort_user_account"
    #用户名称映射
    USER_NAME_MAP = "fort_user_name"
    #立即发现
    FIND_IMMDIATE = "find_immdiately"
    #已选账号列表账号检索
    SELECTED_ACCOUNT = "query_imported_criteria"
    #已选账号列表检索按钮
    SELECTED_QUERY_BUTTON = "query_imported"
    #已选账号列表重置按钮
    SELECTED_RESET_BUTTON = "imported_resetting"
    #AD域发现账号列表账号检索
    NEW_ACCOUNT = "query_new_criteria"
    #AD域发现账号列表检索按钮
    NEW_QUERY_BUTTON = "query_new"
    #AD域发现账号列表重置按钮
    NEW_RESET_BUTTON = "new_resetting"
    #过滤账号列表账号检索
    FILTER_ACCOUNT = "query_filter_criteria"
    #过滤账号列表检索按钮
    FILTER_QUERY_BUTTON = "query_filter"
    #过滤账号列表重置按钮
    FILTER_RESET_BUTTON = "filter_resetting"
    #AD域发现账号列表到已选账号列表左移按钮
    NEW_TO_SELECTED = "add_imported"
    #已选账号列表到AD域发现账号列表右移按钮
    SELECTED_TO_NEW = "del_imported"
    #AD域发现账号列表到过滤账号列表右移按钮
    NEW_TO_FILTER = "add_filtration"
    #过滤账号列表到AD域发现账号列表左移按钮
    FILTER_TO_NEW = "del_filtration"
    #AD域发现账号列表框
    NEW_LADP_USERS = "new_ldap_user"
    #已选账号列表框
    SELECTED_LADP_USERS = "imported_ldap_user"
    #过滤账号列表框
    FILTER_LADP_USERS = "filter_ldap_user"
    #初始化密码
    INIT_SECRET = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/ \
    tbody/tr[2]/td[2]/div/div[2]/input[1]"
    #清空历史记录
    CLEAR_HISTORY = "clear_history"
    #点击定时quartz_tab
    QUARTZ_TAB = "quartz_tab"
    #执行时间(选择小时)
    SELECT_HOUR = "startHour"
    #执行时间(选择分钟)
    SELECT_MINUTE = "startMinute"
    #周期发现按钮
    FIND_BY_QUARTZ = "find_by_quartz"
    #关闭定时
    QUARTZ_OFF = "quartz_off"

    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.command = Command()
        self.tableElem = tableElement(self.driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)

    u'''点击连接/属性按钮'''
    def connect_tab(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.CONNECT_TAB)
        except Exception as e:
            print ("Click connect tab button error: ") + str(e)

    u'''点击发现按钮'''
    def discover_tab(self):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            self.getElem.find_element_with_wait_clickable_and_click("id",self.DISCOVER_TAB)
        except Exception as e:
            print ("Click discover tab button error: ") + str(e)

    u'''点击历史记录按钮'''
    def history_tab(self):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            self.getElem.find_element_with_wait_clickable_and_click("id",self.HISTORY_TAB)
        except Exception as e:
            print ("Click history tab button error: ") + str(e)

    u'''勾选子树查询'''
    def subtree_query(self):
        try:
            selem = self.getElem.find_element_with_wait_EC("id",self.SUBTREE_QUERY)
            if selem.is_selected() == False:
                selem.click()
        except Exception as e:
            print ("Click subtree query error: ") + str(e)

    u'''取消勾选子树查询'''
    def quit_subtree_query(self):
        try:
            selem = self.getElem.find_element_with_wait_EC("id",self.SUBTREE_QUERY)
            if selem.is_selected():
                selem.click()
        except Exception as e:
            print ("Click quit subtree query error: ") + str(e)

    u'''填写变量内容
        parameters:
            var_text : 变量内容
            type : 定位方式
            value : 定位方式对应的值
    '''      
    def set_common_func(self,var_text,type,value):
        try:
            revar_text = self.cnEnde.is_float(var_text)
            var_elem =self.getElem.find_element_with_wait_EC(type,value)
            var_elem.clear()
            var_elem.send_keys(revar_text)
        except Exception as e:
            print ("Set AD config common text error: ") + str(revar_text) + str(e)

    u'''设置服务器地址'''
    def set_address_ip(self,ip):
        return self.set_common_func(ip,"id",self.SERVER_IP)

    u'''设置服务器端口'''
    def set_address_port(self,port):
        return self.set_common_func(port,"id",self.SERVER_PORT)

    u'''设置BASE DN'''
    def set_base_dn(self,baseDn):
        return self.set_common_func(baseDn,"id",self.BASE_DN)

    u'''设置管理员账号'''
    def set_admin(self,admin):
        return self.set_common_func(admin,"id",self.SERVER_ADMIN)

    u'''设置管理员密码'''
    def set_admin_pwd(self,adminPwd):
        return self.set_common_func(adminPwd,"id",self.SERVER_PWD)

    u'''设置用户归属节点1'''
    def set_home_node1(self,homeNode):
        return self.set_common_func(homeNode,"xpath",self.USER_HOME_NODE1)

    u'''设置用户归属节点2'''
    def set_home_node2(self,homeNode):
        return self.set_common_func(homeNode,"xpath",self.USER_HOME_NODE2)

    u'''设置用户查询条件'''
    def set_query_condition(self,cond):
        return self.set_common_func(cond,"id",self.QUERY_CONDTION)

    u'''点击AD域对象属性查询'''
    def ad_attri_query(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.AD_ATTRI_QUERY)
        except Exception as e:
            print ("Click ad attri query error: ") + str(e)

    u'''点击添加多个节点'''
    def add_muli_node(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.ADD_MULI_NODE)
        except Exception as e:
            print ("Click add muli node error: ") + str(e)

    u'''点击删除节点'''
    def del_node(self):
        try:
            if self.getElem.is_element_exsit("id",self.DEL_NODE):
                self.getElem.find_element_with_wait_clickable_and_click("id",self.DEL_NODE)
        except Exception as e:
            print ("Click ad attri query error: ") + str(e)

    u'''设置查询条件'''
    def set_query_obj(self,obj):
        return self.set_common_func(obj,"id",self.QUERY_OBJ)

    u'''点击查询属性列表'''
    def query_attri_list(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.QUERY_ATTR_LIST)
        except Exception as e:
            print ("Click query attri list error: ") + str(e)

    u'''点击用户属性映射'''
    def user_attri_map(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.USER_ATTR_MAP)
        except Exception as e:
            print ("Click user attri map error: ") + str(e)

    u'''设置用户账号映射'''
    def set_account_map(self,accountMap):
        return self.set_common_func(accountMap,"id",self.USER_ACCOUNT_MAP)

    u'''设置用户名称映射'''
    def set_name_map(self,nameMap):
        return self.set_common_func(nameMap,"id",self.USER_NAME_MAP)

    u'''点击立即发现'''
    def click_find_immdiate(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.FIND_IMMDIATE)
        except Exception as e:
            print ("Click find immdiate error: ") + str(e)

    u'''设置已选账号查询条件'''
    def set_selected_account(self,selectACCOUNT):
        return self.set_common_func(selectACCOUNT,"id",self.SELECTED_ACCOUNT)

    u'''点击已选账号检索按钮'''
    def click_selected_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.SELECTED_QUERY_BUTTON)
        except Exception as e:
            print ("Click selected query button error: ") + str(e)

    u'''点击已选账号重置按钮'''
    def click_selected_reset_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.SELECTED_RESET_BUTTON)
        except Exception as e:
            print ("Click selected reset button error: ") + str(e)

    u'''设置AD发现列表查询条件'''
    def set_new_account(self,newAccount):
        return self.set_common_func(newAccount,"id",self.NEW_ACCOUNT)

    u'''点击AD域发现列表检索按钮'''
    def click_new_query_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.NEW_QUERY_BUTTON)
        except Exception as e:
            print ("Click new query button error: ") + str(e)

    u'''点击AD域发现列表重置按钮'''
    def click_new_reset_button(self):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            self.getElem.find_element_with_wait_clickable_and_click("id",self.NEW_RESET_BUTTON)
        except Exception as e:
            print ("Click new reset button error: ") + str(e)

    u'''设置过滤账号列表查询条件'''
    def set_filter_account(self,filterAccount):
        return self.set_common_func(filterAccount,"id",self.FILTER_ACCOUNT)
    
    u'''点击过滤账号列表检索按钮'''
    def click_filter_query_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.FILTER_QUERY_BUTTON)
        except Exception as e:
            print ("Click filter query button error: ") + str(e)
    
    u'''点击过滤账号列表重置按钮'''
    def click_filter_reset_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.FILTER_RESET_BUTTON)
        except Exception as e:
            print ("Click filter reset button error: ") + str(e)

    u'''点击AD域发现账号列表到已选账号列表左移按钮'''
    def new_to_selected(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.NEW_TO_SELECTED)
        except Exception as e:
            print ("Click ad to selected left button error: ") + str(e)

    u'''点击已选账号列表到AD域发现账号列表右移按钮'''
    def select_to_new(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.SELECTED_TO_NEW)
        except Exception as e:
            print ("Click selected to ad right button error: ") + str(e)

    u'''点击AD域发现账号列表到过滤账号列表右移按钮'''
    def new_to_filter(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.NEW_TO_FILTER)
        except Exception as e:
            print ("Click ad to filter right button error: ") + str(e)

    u'''点击过滤账号列表到AD域发现账号列表左移按钮'''
    def filter_to_new(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.FILTER_TO_NEW)
        except Exception as e:
            print ("Click filter to new left button error: ") + str(e)

    u'''点击清空历史按钮'''
    def clear_history_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.CLEAR_HISTORY)
        except Exception as e:
            print ("Click clear history button error: ") + str(e)
    
    u'''设置用户密码'''
    def set_pwd(self,pwd):
        self.frameElem.switch_to_content()
        return self.set_common_func(pwd,"xpath",self.INIT_SECRET)

    u'''获取列表中li的个数
        Parameters:
            - ul_id:定位ul的id
        return: li的个数
    '''
    def get_li_count(self,ul_id):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        #定位到ul
        ul_elem = self.getElem.find_element_with_wait_EC("id",ul_id)
        #获取ul中的所有li
        li_elems = ul_elem.find_elements_by_tag_name("li")
        return len(li_elems)

    u'''已选账号列表和过滤列表中账号数目:
        parameters:
            - type:ul框的类型(0:已选账号列表,1:过滤账号列表)
    '''
    def get_account_count(self,type):
        reType = self.cnEnde.is_float(type)
        if reType == "0":
            return self.get_li_count(self.SELECTED_LADP_USERS)
        elif reType == "1":
            return self.get_li_count(self.FILTER_LADP_USERS)

    u'''选中指定的账号
        Parameters:
            - value:定位ul的id
            - accountText:选中的账号
    '''
    def select_ul_li(self,value,accountText):
        accountList = accountText.split(',')
        row = 0
        try:
            elem = self.getElem.find_element_with_wait_EC("id",value)
            elem_list = elem.find_elements_by_tag_name("li")
            for selem in elem_list:
                row = row + 1
                span_xpath = "//ul[@id='" + value + "']/li[" + str(row) + "]/span[1]"
                span_text = self.getElem.find_element_wait_and_get_text("xpath",span_xpath)
                for account in accountList:
                    if span_text == account:
                        li_xpath = "//ul[@id='" + value + "']/li[" + str(row) + "]"
                        self.getElem.find_element_with_wait_clickable_and_click("xpath",li_xpath)
                        break
        except Exception as e:
            print ("Select account error: ") + str(e)

    u'''选中账号的类型:
        parameters:
            - type:ul框的类型(0:AD域发现账号列表,1:已选账号列表,2:过滤账号列表)
    '''
    def select_type(self,type,accountText):
        retype = self.cnEnde.is_float(type)
        if retype == "0":
            self.select_ul_li(self.NEW_LADP_USERS,accountText)
        elif retype == "1":
            self.select_ul_li(self.SELECTED_LADP_USERS,accountText)
        else:
            self.select_ul_li(self.FILTER_LADP_USERS,accountText)
    
    u'''点击定时按钮'''
    def quartz_tab(self):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            self.getElem.find_element_with_wait_clickable_and_click("id",self.QUARTZ_TAB)
        except Exception as e:
            print ("Click quartz tab button error: ") + str(e)
    
    u'''设置小时'''
    def set_hour(self,hour):
        try:
            rehour = self.cnEnde.is_float(hour)
            selem = self.getElem.find_element_with_wait_EC("id",self.SELECT_HOUR)
            self.selectElem.select_element_by_visible_text(selem,rehour)
        except Exception as e:
            print ("Set hour error: ") + str(e)
    
    u'''设置分钟'''
    def set_minute(self,minute):
        return self.set_common_func(minute,"id",self.SELECT_MINUTE)
    
    u'''设置执行方式'''
    def set_execute_type(self,type):
        try:
            retype = self.cnEnde.is_float(type)
            type_xpath = "//div[@id='duo_div']/table/tbody/tr[2]/td[2]/" + \
            "input[" + retype + "]"
            self.getElem.find_element_with_wait_clickable_and_click("xpath",\
            type_xpath)
        except Exception as e:
            print ("Set execute type error : ") + str(e)
    
    u'''判断checkbox或者radio是否被选中'''
    def checkbox_is_selected(self,value):
        elem = self.getElem.find_element_with_wait_EC("xpath",value)
        if elem.is_selected() == False:
            elem.click()
    
    u'''设置执行日期:
            parameters:
                - ExType:周期执行方式
                - oneText:设置星期、日期、月份
                - twoType:设置月份
    '''
    def set_execute_date(self,ExType,oneText,twoType):
        retype = self.cnEnde.is_float(ExType)
        retwoType = self.cnEnde.is_float(twoType)
        try:
            xpath_str = "//div[@id='duo_div']/div[" + retype
            if oneText !="":
                oneList = oneText.split(",")
                for oneType in oneList:
                    reoneType = self.cnEnde.is_float(oneType)
                    elem_xpath = xpath_str + "]/table[1]/tbody/tr/td[2]/input[" + reoneType + "]"
                    self.checkbox_is_selected(elem_xpath)
                if retwoType != "" :
                    input_xpath = xpath_str + "]/table[2]/tbody/tr/td[2]/input[" + retwoType + "]"
                    self.checkbox_is_selected(input_xpath)
        except Exception as e:
            print ("Set execute date error: ") + str(e)
        
    u'''点击周期发现'''
    def find_by_quartz(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.FIND_BY_QUARTZ)
        except Exception as e:
            print ("Click find by quartz button error: ") + str(e)
            
    u'''点击关闭定时'''
    def quartz_off(self):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            self.getElem.find_element_with_wait_clickable_and_click("id",self.QUARTZ_OFF)
        except Exception as e:
            print ("Click quartz off button error: ") + str(e)