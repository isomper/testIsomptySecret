#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：顾亚茹
#生成日期：2017-07-18
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
from selenium.webdriver.common.action_chains import ActionChains

sys.path.append("/testIsompSecret/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

class AuthorizationPage():
    #------------------------------检索-----------------------------------
    #名称检索class
    SEARCH_NAME = "cx_text_w92"
    #用户账号或名称检索
    SEARCH_ACCOUNT_OR_NAME = "authorization_user_name"
    #资源名称检索
    SEARCH_RESOURCE_NAME = "authorization_resource_name"
    #资源IP检索
    SEARCH_RESOURCE_IP = "authorization_resource_ip"
    #资源账号检索
    SEARCH_RESOURCE_ACCOUNT = "authorization_account_name"
    #检索按钮CLASS
    SEARCH_BUTTON = "js_btn"
    #重置按钮
    RESET_BUTTON = "resetting"
    #添加按钮
    ADD_BUTTON = "addAuthorization"
    #删除按钮
    DELETE_BUTTON = "delete_authorization"
    #全选按钮
    CHECK_ALL_BUTTON = "checkbox"
    #----------------------------授权编辑页面------------------------------
    #授权名称CLASS
    AUTHORIZATION_NAME = "percent_w168"
    #部门
    AUTHORIZATION_DEP = "department_name"
    #添加用户
    ADD_USER = "btn_tjyh"
    #选择用户页面/访问审批检索账号/用户名
    SEARCH_USER = "fort_user_account"
    #检索按钮
    SEARCH_USER_BUTTON = "quick_user"
    #用户选择页面全选按钮
    USER_CHECK_ALL = "user_check_all"
    #确认按钮CLASS
    OK_BUTTON = "aui_state_highlight"
    #用户页面返回按钮
    USER_BACK_BUTTON = "//table[@class='aui_dialog']/tbody/tr[3]/td[1]/div/button[@id='cancelButton']"
    #用户界面确认按钮class
    SELECT_PAGE_OK_BUTTON = "aui_state_highlight"
    #用户界面返回按钮
    SELECT_PAGE_BACK_BUTTON = "cancelButton"
    #用户组添加按钮
    USER_GROUP_ADD_BUTTON = "btn_tjyhz"
    #用户组部门展开箭头
    USER_DEP_SHOW_ARROW = "userGroup_1_switch"
    #添加资源
    ADD_RES_BUTTON = "btn_tjzyzy"
    #资源页面检索资源IP
    SEARCH_RES_IP = "fortResourceIp"
    #资源检索按钮
    RES_SEARCH_BUTTON = "quick_query"
    #资源选择页面全选按钮
    RES_CHECK_ALL = "resource_check_all"
    #删除资源
    DEL_RES_BUTTON = "del_resource"
    #添加资源组
    ADD_RES_GROUP_BUTTON = "btn01_tjyhz"
    #资源组部门展开按钮
    RES_GROUP_DEP_SHOW_BUTTON = "resourceGroup_1_switch"
    #添加资源账号
    ADD_RES_ACCOUNT = "btn_tjzy"
    #选择账号页面资源检索
    RES_ACCOUNT_RES_SEARCH = "fortResourceName"
    RES_ACCOUNT_RES_IP_SEARCH = "fortResourceIp"
    RES_ACCOUNT_RES_ACCOUNT_SEARCH = "fortAccountName"
    #资源账号部门展开按钮
    RES_ACCOUNT_DEP_SHOW_BUTTON = "treeDemoResource_1_switch"
    #删除资源账号
    DEL_RES_ACCOUNT = "del_account"
    #关联子节点
    ASSOCIATE_CHILD_NODE = "query_child"
    #保存按钮
    SAVE_BUTTON = "save_authorization"
    #每页显示全部
    PAGE_PER_SHOW = "page_select"
    #全选按钮
    SELECT_ALL_BUTTON = "checkbox"
    #清空部门按钮
    CLEAN_DEP = "clean_tree_data"
    #返回按钮
    BACK_BUTTON = "history_skip"
#----------------------------------访问审批-------------------------------
    #开关状态
    APPROVEL_SWITCH = "btn_qh"
    #添加审批级别
    ADD_APPROVAL_LEVELS_BUTTON = "add_level"
    #重置审批
    RESET_APPROVEL = "refresh"
    #设置审批级别中的审批人个数class
    APPROVER_NUM = "sel"
    #访问审批保存按钮
    APPROVEL_SAVE_BUTTON = "save_access_approval"
    #访问审批返回按钮
    APPROVEL_BACK_BUTTON = "//html/body/div[1]/div[4]/input[3]"
#-----------------------------双人审批----------------------------------------
    #关联状态
    RELATION_STATE = "related_flag"
    #账号或名称
    ACCOUNT_OR_NAME = "nameOrAccount"
    #检索
    DOUBLE_APPROVEL_QUERY = "fast_querry"
    #审批人
    ALL_APPROVER = "choseAll_approver"
    #被审批人
    ALL_CANDIDATE = "choseAll_candidate"
    #是否启动关联
    START_OR_NOT_ASSOCIATION = "enabled"
    #建立关联
    CREATE_RELATE = "create_relate"
    #取消关联
    DEL_RELATE = "del_relate"
    #关闭叉号
    AUI_CLOSE = "aui_close"
    #子页面返回按钮
    CHILD_PAGE_BACK_BUTTON = "history_skip"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.actions = ActionChains(self.driver)
        self.tableElem = tableElement(self.driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)
    
    u'''点击按钮公用部分
            parameters :
                type : 定位方式
                value : 值
    '''
    def click_button_common(self,type,value):
        var_button = self.getElem.find_element_with_wait_EC(type,value)
        if var_button.is_displayed():
            var_button.click()
    
    u'''点击添加按钮'''
    def add_button(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            self.click_button_common('id',self.ADD_BUTTON)
        except Exception as e:
            print ("user add button error: ") + str(e)

    u'''点击删除按钮'''
    def del_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click("id",self.DELETE_BUTTON)
            time.sleep(1)
        except Exception as e:
            print ("Delete button error: ") + str(e)
    
    u'''勾选全选按钮'''
    def check_all(self):
        try:
            check_all = self.getElem.find_element_with_wait_EC('id',self.CHECK_ALL_BUTTON)
            if check_all.is_displayed():
                time.sleep(1)
                check_all.click()
        except Exception as e:
            print("Click checkall button error: ") + str(e)

    '''点击检索按钮'''     
    def click_search_button(self):
        try:
            self.click_button_common('classname',self.SEARCH_BUTTON)
            time.sleep(1)
        except Exception as e:
            print ("search button is error: ") + str(e)

    u'''点击重置按钮'''
    def click_reset_button(self):
        try:
            self.click_button_common('id',self.RESET_BUTTON)
        except Exception as e:
            print ("click reset button error: ") + str(e)

    u'''每页选择全部'''
    def page_select_all(self):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            
            #选择每页显示全部
            selem = self.getElem.find_element_with_wait_EC('id',self.PAGE_PER_SHOW)
            self.selectElem.select_element_by_value(selem,'1000')
            
        except Exception as e:
            print ("page select all error: ") + str(e)

    u'''获取行数'''
    def get_rows(self):
        try:
            table_xpath = "//table[@id='content_table']"
            rows = self.tableElem.get_table_rows_count(table_xpath)
            return rows
        except Exception as e:
            print ("get tables row error: ") + str(e)

    u'''保存按钮'''
    def save_button(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            save_elem = self.getElem.find_element_with_wait_EC('id',self.SAVE_BUTTON)
            if save_elem.is_displayed():
                time.sleep(1)
                save_elem.click()
        except Exception as e:
            print ("Authorization save button error: ") + str(e)
            
    u'''返回按钮'''
    def back_button(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            back_elem = self.getElem.find_element_with_wait_EC('id',self.BACK_BUTTON)
            if back_elem.is_displayed():
                time.sleep(1)
                back_elem.click()
        
        except Exception as e:
            print ("Authorization back button error: ") + str(e)

    u'''点击全选按钮'''
    def select_all_button(self):
        try:
            self.click_button_common('id',self.SELECT_ALL_BUTTON)
        except Exception as e:
            print ("select all button error: ") + str(e)

    u'''点击授权操作列对应的按钮
        parameters:
            name : 授权名称
            index : 操作功能按钮对应的input位置
    '''
    def auth_operate_list(self,name,index):
        reName = self.cnEnde.is_float(name)
        row = self.cmf.find_row_by_name(reName, "fortAuthorizationName")
        
        update_xpath = "//table[@id='content_table']/tbody/tr[" + str(row-1) + "]/td[6]/input[" + index + "]"
        self.click_button_common('xpath',update_xpath)
    
    u'''点击授权操作列对应的编辑按钮
        parameters:
            name : 授权名称
    '''
    def operate_edit(self,name):
        try:
            self.auth_operate_list(name,"1")
        except Exception as e:
            print("Click authorization operation edit button fail") + str(e)

    u'''点击授权操作列对应的访问审批按钮
        parameters:
            name : 授权名称
    '''    
    def operate_access_approval(self,name):
        try:
           self.auth_operate_list(name,"2")
        except Exception as e:
            print("Click authorization operation access approval button fail") + str(e)

    u'''点击授权操作列对应的双人审批按钮
        parameters:
            name : 授权名称
    '''     
    def operate_double_approval(self,name):
        try:
            self.auth_operate_list(name,"3")
        except Exception as e:
            print("Click authorization operation double people approval button fail") + str(e)

    u'''点击授权操作列对应的用户按钮
        parameters:
            name : 授权名称
    '''     
    def operate_user(self,name):
        try:
            self.auth_operate_list(name,"4")
        except Exception as e:
            print("Click authorization operation user button fail") + str(e)
    
    u'''点击授权操作列对应的用户组按钮
        parameters:
            name : 授权名称
    '''     
    def operate_user_group(self,name):
        try:
            self.auth_operate_list(name,"5")
        except Exception as e:
            print("Click authorization operation user group button fail") + str(e)
    
    u'''点击授权操作列对应的资源按钮
        parameters:
            name : 授权名称
    '''     
    def operate_res(self,name):
        try:
            self.auth_operate_list(name,"6")
        except Exception as e:
            print("Click authorization operation resource button fail") + str(e)

    u'''点击授权操作列对应的资源组按钮
        parameters:
            name : 授权名称
    '''     
    def operate_res_group(self,name):
        try:
            self.auth_operate_list(name,"7")
        except Exception as e:
            print("Click authorization operation resource group button fail") + str(e)

    u'''点击授权操作列对应的资源账号按钮
        parameters:
            name : 授权名称
    '''     
    def operate_res_account(self,name):
        try:
            self.auth_operate_list(name,"8")
        except Exception as e:
            print("Click authorization operation res account button fail") + str(e)
    
    u'''查询已存在名称位于第几行
       Parameters:
          - namevalue:传入的要被查询名称
          - name:表格列的name属性
       return：定位该名称位于第几行
    '''
    def find_row_by_name(self, namevalue, name):
        row = 0
        try:
            if self.cmf.is_namevalue_exsit(namevalue, name):
                parent_table = self.getElem.find_element_with_wait_EC("id","content_table")
                text_list = parent_table.find_elements_by_name(name)
                for fortNameValue in text_list:
                    row = row + 1
                    fortNameValue_text = fortNameValue.text
                    if fortNameValue_text == namevalue:
                        break
        except Exception:
            print namevalue + "is not exsit."
        return row
    
    def click_auth_checkbox(self,name):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        rename = self.cnEnde.is_float(name)        
        row = 0
        try:
            parent_table = self.getElem.find_element_with_wait_EC("id","content_table")
            trs = text_list = parent_table.find_elements_by_tag_name("tr")
            for i in range(len(trs)):
                row = row + 1
                path = "//table[@id='content_table']/tbody/tr[" + str(row) + "]/td[3]/span[1]"
                
                if self.getElem.is_element_exsit("xpath",path):
                    name_elem = self.getElem.find_element_with_wait_EC("xpath",path)
                    if name_elem.text == rename:
                        update_xpath = "//table[@id='content_table']/tbody/tr[" + str(row) + "]/td[1]/span[1]/input[1]"
                        time.sleep(1)
                        selem = self.getElem.find_element_with_wait_EC('xpath',update_xpath)
                        if selem.is_selected() == False:
                            selem.click()
                            break

        except Exception:
            print rename + "is not exsit."

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
            print ("Set authorization common text error: ") + str(revar_text) + str(e)
    
    u'''授权名称检索框
            parameters : 
                name : 授权名称
    '''
    def set_search_auth_name(self,name):
        return self.set_common_func(name,'classname',self.SEARCH_NAME)

    '''用户账号或名称检索框
        parameters:
            accountName : 用户账号或名称
    '''
    def set_search_accountorname(self,accountName):
        return self.set_common_func(accountName,'id',self.SEARCH_ACCOUNT_OR_NAME)
    
    '''资源名称检索框
        parameters:
            resName : 资源名称
    '''
    def set_search_res_name(self,resName):
        
        return self.set_common_func(resName,'id',self.SEARCH_RESOURCE_NAME)
    
    '''资源IP检索框
        parameters:
            resIp : 资源IP
    '''
    def set_search_res_ip(self,resIp):
        
        return self.set_common_func(resIp,'id',self.SEARCH_RESOURCE_IP)

    '''资源账号检索框
        parameters:
            resAccount : 资源账号
    '''
    def set_search_res_account(self,resAccount):
        
        return self.set_common_func(resAccount,'id',self.SEARCH_RESOURCE_ACCOUNT)
    
    u'''设置检索条件
            parameters :
                condition : 检索条件
                status ： 检索类型
    '''
    def set_query_conditon(self,condition,status):
        restatus = self.cnEnde.is_float(status)
        if restatus == '0':
            return self.set_search_auth_name(condition)
        elif restatus == '1':
            return self.set_search_accountorname(condition)
        elif restatus == '2':
            return self.set_search_res_name(condition)
        elif restatus == '3':
            return self.set_search_res_ip(condition)
        elif restatus == '4':
            return self.set_search_res_account(condition)

    u'''填写授权名称
        parameters:
            name : 授权名称
    '''      
    def set_auth_name(self,name):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        return self.set_common_func(name,'classname',self.AUTHORIZATION_NAME)
    
    u'''获取部门a标签
       parameter:
           deptname:部门名称
    '''
    def get_tag_by_a(self, deptname):
        try:
            #获取所有a标签的对象
            elems = self.driver.find_elements_by_tag_name("a")
    
            for elem in elems:
                elemtext = elem.get_attribute("title")
                elemid = elem.get_attribute("id")
    
                if deptname == elemtext:
                    self.click_button_common('id',elemid)
                    break
    
        except Exception as e:
            print "Get tag a error:" + str(e)

    u'''获取部门箭头的展开状态'''
    def get_element_attribute(self,idname):
        selem = self.getElem.find_element_with_wait_EC('id',idname)
        selem_class = selem.get_attribute('class')
        arrow_type = selem_class.split('_')[-1]
        return arrow_type
    
    u'''填写部门
        parameters:
            deptname : 部门名称
    '''
    def set_dep(self,deptname,status='0'):
        try:
            restatus = self.cnEnde.is_float(status)
            redeptname = self.cnEnde.is_float(deptname)
            self.click_button_common('id',self.AUTHORIZATION_DEP)
            time.sleep(1)
            #选择ROOT部门
            if restatus == '0':
                self.click_button_common('id',"tree_1_span")               

            elif restatus == '1':
                if self.get_element_attribute('tree_1_switch') == "close":
                    self.getElem.find_element_wait_and_click_EC('id','tree_1_switch')
                self.get_tag_by_a(deptname)
                
        except Exception as e:
            print "set department error : " + str(e)
    
    u'''点击添加用户按钮'''
    def click_add_user(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            self.click_button_common('id',self.ADD_USER)
        except Exception as e:
            print ("Click add user button error : ") + str(e)
    
    u'''点击添加用户页面部门显示按钮'''
    def click_user_show_arrow(self):
        self.frameElem.switch_to_artIframe()
        try:
            if self.get_element_attribute("user_tree_1_switch") == "close":
                self.click_button_common('id',"user_tree_1_switch")
            
        except Exception as e:
            print ("Click user department button error : ") + str(e)
    
    u'''勾选用户部门'''
    def select_user_depmt(self,userDepmt):
        self.click_user_show_arrow()
        self.click_depmt_tree_checkbox("user_tree",userDepmt)
        
    u'''选择用户页面(访问审批)账号/用户名检索条件
        parameters : 
            userName : 用户账号/用户名
    '''
    def set_select_user_name(self,userName):
        self.frameElem.switch_to_artIframe()
        return self.set_common_func(userName,'id',self.SEARCH_USER)
    
    u'''选择用户页面检索按钮'''
    def set_select_user_search_button(self):
        self.frameElem.switch_to_artIframe()
        try:
            self.click_button_common('id',self.SEARCH_USER_BUTTON)
        except Exception as e:
            print ("Click user search button error: ") + str(e)
    
    u'''选择用户页面全选按钮'''
    def set_user_check_all_button(self):
        try:
            self.click_button_common('id',self.USER_CHECK_ALL)
        except Exception as e:
            print ("Click user checkall button error: ") + str(e)
            
    u'''选择用户页面确认按钮'''
    def set_ok_button(self):
        self.frameElem.switch_to_content()
        try:
            self.click_button_common('classname',self.SELECT_PAGE_OK_BUTTON)
        except Exception as e:
            print ("Click user confirm button error: ") + str(e)
    
    u'''选择用户页面返回按钮'''
    def set_back_button(self):
        self.frameElem.switch_to_content()
        try:
            self.click_button_common('id',self.SELECT_PAGE_BACK_BUTTON)          
        except Exception as e:
            print ("Click user page back button error: ") + str(e)
    
    u'''点击添加用户组按钮'''
    def click_add_user_group(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            self.click_button_common('id',self.USER_GROUP_ADD_BUTTON)
        except Exception as e:
            print ("Click add user group button error : ") + str(e)
    
    u'''点击用户组部门显示按钮'''
    def click_show_user_dep(self):
        self.frameElem.switch_to_artIframe()
        try:
            if self.get_element_attribute(self.USER_DEP_SHOW_ARROW) == "close":
                self.click_button_common('id',self.USER_DEP_SHOW_ARROW)
            
        except Exception as e:
            print ("Click user group department button error : ") + str(e)
    
    u'''选择资源树勾选框
            parameters : 
                type : 父元素id值
                nameValue ： 名字(用户、资源、资源组、用户组)
    '''
    def click_depmt_tree_checkbox(self,type,nameValue):
        self.frameElem.switch_to_artIframe()
        reName = self.cnEnde.is_float(nameValue)
        try:
            elem = self.getElem.find_element_with_wait_EC("id",type)
            elem_list = elem.find_elements_by_css_selector("a[target='_blank']")
            for selem in elem_list:
                #获取a标签的id
                selem_id = selem.get_attribute('id')
                #获取a标签的title
                selem_title = selem.get_attribute("title")
                #获取勾选框的id或者部门展开箭头id
                var_id = selem_id[:-1] + "check"#end_str
                if selem_title == reName:
                    #勾选checkbox
                    self.getElem.find_element_wait_and_click_EC('id',var_id)
        except Exception as e:
            print ("Click department tree checkbox error: ") + str(e)
    
    u'''选择用户组
            parameters :
                userGroupName : 用户组名称
    '''
    def select_user_group(self,userGroupName):
        self.click_show_user_dep()
        self.click_depmt_tree_checkbox("userGroup",userGroupName)

    u'''点击添加资源按钮'''
    def click_add_res(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            add_res = self.getElem.find_element_with_wait_EC('id',self.ADD_RES_BUTTON)
            if add_res.is_displayed():
                time.sleep(1)
                add_res.click()            
        except Exception as e:
            print ("Click add resource button error : ") + str(e)
    
    u'''点击资源部门的显示箭头'''
    def click_res_show_arrow(self):
        self.frameElem.switch_to_artIframe()
        try:
            if self.get_element_attribute("treeDemoResource_1_switch") == "close":
                self.click_button_common('id',"treeDemoResource_1_switch")
            
        except Exception as e:
            print ("Click resource department button error : ") + str(e)
    
    u'''勾选资源部门'''
    def select_res_depmt(self,resDepmt):
        self.click_res_show_arrow()
        self.click_depmt_tree_checkbox("treeDemoResource",resDepmt)
    
    u'''设置选择资源页面IP检索条件
        parameters : 
            resIp : 资源Ip
    '''
    def set_select_res_ip(self,resIp):
        self.frameElem.switch_to_artIframe()
        return self.set_common_func(resIp,'id',self.SEARCH_RES_IP)
    
    u'''设置选择资源页面名称检索条件
        parameters : 
            resName : 资源名称
    '''
    def set_select_res_name(self,resName):
        return self.set_common_func(resName,'id',self.RES_ACCOUNT_RES_SEARCH)
    
    u'''选择资源or资源账号页面检索按钮'''
    def set_select_res_search_button(self):
        try:
            self.frameElem.switch_to_artIframe()
            self.getElem.find_element_with_wait_clickable_and_click('id',self.RES_SEARCH_BUTTON)
        except Exception as e:
            print ("Click resource or resAccount search button error : ") + str(e)
    
    u'''资源or资源账号选择页面全选按钮'''
    def set_res_check_all_button(self):
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.RES_CHECK_ALL)
        except Exception as e:
            print ("Click resource or resAccount checkall button error : ") + str(e)
    
    u'''选择资源组
            parameters :
                resGroupName : 资源组名称
    '''
    def select_res_group(self,resGroupName):
        self.click_res_group_show_arrow()
        self.click_depmt_tree_checkbox("resourceGroup",resGroupName)
    
    u'''点击添加资源组按钮'''
    def click_add_res_group(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            time.sleep(1)
            self.click_button_common('id',self.ADD_RES_GROUP_BUTTON)
        except Exception as e:
            print ("Click add resource group button error : ") + str(e)
    
    u'''点击添加资源组部门展开按钮'''
    def click_res_group_show_arrow(self):
        self.frameElem.switch_to_artIframe()
        try:
            if self.get_element_attribute(self.RES_GROUP_DEP_SHOW_BUTTON) == "close":
                self.getElem.find_element_with_wait_clickable_and_click('id',self.RES_GROUP_DEP_SHOW_BUTTON)
            
        except Exception as e:
            print ("Click resource group department arrow button error : ") + str(e)
    
    u'''点击添加资源账号按钮'''
    def click_add_res_account(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            time.sleep(1)
            self.click_button_common('id',self.ADD_RES_ACCOUNT)
        except Exception as e:
            print ("Click add res account button error : ") + str(e)
    
    u'''设置选择资源账号页面账号检索条件
        parameters : 
            resAccount : 资源账号
    '''
    def set_select_res_account(self,resAccount):
        self.frameElem.switch_to_artIframe()
        return self.set_common_func(resAccount,'id',self.RES_ACCOUNT_RES_ACCOUNT_SEARCH)
    
    u'''点击删除资源按钮'''
    def click_del_res(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.DEL_RES_BUTTON)
        except Exception as e:
            print ("Click del res button error : ") + str(e)
    
    u'''点击删除资源账号按钮'''
    def click_del_res_account(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            self.getElem.find_element_with_wait_clickable_and_click('id',self.DEL_RES_ACCOUNT)
        except Exception as e:
            print ("Click del res account button error : ") + str(e)

    u'''勾选checkbox
            parameters :
                value : id值
    '''
    def click_checkbox(self,value):
        try:
            checkbox = self.getElem.find_element_with_wait_EC("id",value)
            if checkbox.is_selected() == False:
                checkbox.click()
            
        except Exception as e:
            print ("checkbox selected error: ") + str(checkbox) + str(e)

    u'''勾选关联子节点'''
    def click_associate_child_node(self):
        self.click_checkbox(self.ASSOCIATE_CHILD_NODE)

    u'''通过检索条件获取行数
            parameters:
                varName : 查找条件(账号或名称)
                nameValue : name属性的value值
    '''    
    def search_direct_by_condition(self,varName,nameValue):
        self.frameElem.from_frame_to_otherFrame("mainFrame")

        row = 0
        reName = self.cnEnde.is_float(varName)
        try:

            #查找name属性为nameValue的所有元素
            var_elems = self.driver.find_elements_by_name(nameValue)
            for index in range(len(var_elems)):
                varValue_text = var_elems[index].text
                if varName in varValue_text:
                    row = row + 1
            return row
        except Exception as e:
            print ("No condition is ") + str(reName) + str(e)
    
    u'''通过授权名称获取行数'''
    def search_direct_by_auth_name(self,authName):
        return self.search_direct_by_condition(authName,"fortAuthorizationName")
    
    u'''通过用户名/账号获取行数'''
    def search_direct_by_user_name(self,userName):
        return self.search_direct_by_condition(userName,"fortUserNames")
    
    u'''通过资源名称获取行数'''
    def search_direct_by_res_name(self,resName):
        return self.search_direct_by_condition(resName,"fortResources")
    
    u'''通过资源IP获取行数'''
    def search_direct_by_res_ip(self,resIp):
        return self.search_direct_by_condition(resIp,"fortResources")

    u'''通过资源账号获取行数'''
    def search_direct_by_res_account(self,resAccount):
        return self.search_direct_by_condition(resAccount,"fortResources")
    
    u'''设置检索条件
            parameters :
                condition : 检索条件
                status ： name类型(0:授权名称name属性，1:用户名/账号name属性)
    '''
    def set_query_name(self,condition,status):
        restatus = self.cnEnde.is_float(status)
        if restatus == '0':
            return self.search_direct_by_auth_name(condition)
        elif restatus == '1':
            return self.search_direct_by_user_name(condition)
        elif restatus == '2':
            return self.search_direct_by_res_name(condition)
        elif restatus == '3':
            return self.search_direct_by_res_ip(condition)
        elif restatus == '4':
            return self.search_direct_by_res_account(condition)
    
#------------------------------------------------------------------------
    
    u'''获取指定属性的文本内容
            parameters:
                type : 定位方式
                value ： 值
    '''
    def get_cert_var_text(self,type,value):
        try:

            cert_var_text = self.getElem.find_element_with_wait_EC(type,value).text
            return cert_var_text
        
        except Exception as e:
            print ("Get cert var text error: ") + str(cert_var_text) + str(e)
    
    u'''获取授权名称'''
    def get_auth_name_text(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        return self.get_cert_var_text('classname',self.AUTHORIZATION_NAME)

#----------------------------------访问审批---------------------------------
    u'''点击添加审批级别'''
    def click_add_approval_level(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            level_button = self.getElem.find_element_with_wait_EC('id',self.ADD_APPROVAL_LEVELS_BUTTON)
            if level_button.is_displayed():
                time.sleep(1)
                level_button.click()
        except Exception as e:
            print ("Click add approval level button error: ") + str(e)
    
    u'''点击重置审批按钮'''
    def click_approvel_reset_button(self):
        try:
            self.click_button_common('id',self.RESET_APPROVEL)
        except Exception as e:
            print ("Click reset approvel button error: ") + str(e)
    
    u'''点击添加审批人
            parameters :
                level :审批级别
    '''
    def click_add_approval(self,level):
        relevel = self.cnEnde.is_float(level)
        level_xpath = "//div[@id='content']/div[" + relevel + "]/div[1]/input[1]"
        try:
            self.click_button_common('xpath',level_xpath)
        except Exception as e:
            print ("Click add approval button error: ") + str(e)
    
    u'''设置级别中的审批人个数
            parameters : 
                selem : select元素
                value : option的value值
    '''
    def set_approver_num(self,level,value):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        relevel = self.cnEnde.is_float(level)
        revalue = self.cnEnde.is_float(value)
        level_xpath = "//div[@id='content']/div[" + relevel + "]/div[3]/select[1]"
        
        try:
            selem = self.getElem.find_element_with_wait_EC('xpath',level_xpath)
            self.selectElem.select_element_by_value(selem,revalue)
        except Exception as e:
            print("Set approver num error: ") + str(e)
    
    u'''点击删除审批级别
            parameters :
                level :审批级别
    '''    
    def click_del_approvel(self,level):
        relevel = self.cnEnde.is_float(level)
        level_xpath = "//div[@id='content']/div[" + relevel + "]/div[1]/input[2]"
        try:
            self.click_button_common('xpath',level_xpath)
        except Exception as e:
            print("Click del approvel button error: ") + str(e)
    
    u'''访问审批保存按钮'''
    def approval_save_button(self):        
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            save_elem = self.getElem.find_element_with_wait_EC('id',self.APPROVEL_SAVE_BUTTON)
            if save_elem.is_displayed():
                time.sleep(1)
                save_elem.click()
        except Exception as e:
            print ("Click approvel save button error: ") + str(e)

    u'''访问审批返回按钮'''
    def approval_back_button(self):        
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        try:
            back_elem = self.getElem.find_element_with_wait_EC('xpath',self.APPROVEL_BACK_BUTTON)
            if back_elem.is_displayed():
                time.sleep(1)
                back_elem.click()
        except Exception as e:
            print ("Click approvel back button error: ") + str(e)
    
    u'''设置动态运行开关状态
            parameters : 
                status_ : 开关状态
    '''
    def switch_status_common(self,status_):
        status = self.cmf.switch_status('id',self.APPROVEL_SWITCH)
        switch_elem = self.getElem.find_element_with_wait_EC('id',self.APPROVEL_SWITCH)
        if status != status_:
            switch_elem.click()
    
    u'''设置动态运行开关状态为开'''
    def set_switch_on(self):
        self.switch_status_common(1)
    
    u'''设置动态运行开关状态为关'''
    def set_switch_off(self):
        self.switch_status_common(0)
    
    u'''资源账号开关状态'''
    def res_account_status(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.driver.execute_script("window.scrollBy(1000,0)","")
        time.sleep(1)
        parent_elem = self.getElem.find_element_with_wait_EC("id","add_account_page")
        elems = parent_elem.find_elements_by_class_name("switch_off")
        for elem in elems:
            if elem.is_displayed():
                elem.click()
            
    u'''获取value值'''
    def get_value(self,type,value):
        selem = self.getElem.find_element_with_wait_EC(type,value)
        value_text = selem.get_attribute('value')
        return value_text
    
    u'''获取访问审批value值
            parameters :
                name : 授权名称
    '''
    def get_access_approvel_value(self,name):
        row = self.cmf.find_row_by_name(name,"fortAuthorizationName")
        
        update_xpath = "//table[@id='content_table']/tbody/tr[" + str(row-1) + "]/td[6]/input[2]"
        
        try:
            text = self.get_value("xpath",update_xpath)
            return text
        
        except Exception as e:
            print ("Get access approvel value error: ") + str(e)
    

#------------------------------------双人审批----------------------------------
    u'''选择状态
            parameters : 
                value : option的value值(2:全部,1:未关联,0:已关联)
    '''
    def select_status(self,value):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        revalue = self.cnEnde.is_float(value)
        selem = self.getElem.find_element_with_wait_EC('id',self.RELATION_STATE)
        try:
            self.selectElem.select_element_by_value(selem,revalue)
        except Exception as e:
            print ("Select relation state error: ") + str(e)
    
    u'''双人授权账号或名称检索'''
    def double_approvel_account_or_name(self,accountName):
        return self.set_common_func(accountName,'id',self.ACCOUNT_OR_NAME)
    
    u'''双人授权检索按钮'''
    def double_approvel_query(self):
        self.click_button_common('id',self.DOUBLE_APPROVEL_QUERY)
    
    u'''勾选全部审批人'''
    def click_all_approver(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.click_checkbox(self.ALL_APPROVER)
    
    u'''勾选全部被审批人'''
    def click_all_candidate(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.click_checkbox(self.ALL_CANDIDATE)
    
    u'''通过账号获取用户所在行数
            parameters : 
                table_xpath :定位table的xpath
                column_index :用户账号所在的列序号(从0开始)
                account : 勾选的账号
    '''
    def get_row_by_account(self,table_xpath,column_index,account):
        self.frameElem.switch_to_artIframe()
        try:
            table_num = self.tableElem.get_table_rows_count(table_xpath)
            for row in range(table_num):
                cell_text = self.tableElem.get_table_cell_text(table_xpath,row,column_index)[0]
                if cell_text == account:
                    return row+1
                    break
        
        except Exception as e:
            print ("Get row number error: ") + str(e)

    u'''勾选用户账号对应的checkbox
            parameters : 
                accountStr : 勾选的账号
                table_xpath :定位table的xpath
                column_index :用户账号所在的列序号(从0开始)
                index : 勾选框所在的列序号(从1开始)
    '''    
    def select_approver_checkbox(self,accountStr,table_xpath,column_index,index):
        reaccountList = self.cnEnde.is_float(accountStr)
        accountList = reaccountList.split(',')
        try:
            for account in accountList:
                row = self.get_row_by_account(table_xpath,column_index,account)
                index_xpath = "//tfoot[@id='tab_content']/tr[" + str(row) + "]/td[" + str(index) + "]/input[1]"
                approver_elem = self.getElem.find_element_with_wait_EC('xpath',index_xpath)
                if approver_elem.is_selected() == False:
                    time.sleep(1)
                    approver_elem.click()
        except Exception as e:
            print ("User Defined error: ") + str(e)
    
    u'''根据账号名称勾选审批人'''
    def select_approver_test(self,accountStr):
        table_xpath = "//tfoot[@id='tab_content']"
        self.select_approver_checkbox(accountStr,table_xpath,2,1)
    
    u'''根据账号名称勾选被审批人'''
    def select_candidate_test(self,accountStr):
        table_xpath = "//tfoot[@id='tab_content']"
        self.select_approver_checkbox(accountStr,table_xpath,2,2)
    
    u'''勾选是否启动关联'''
    def click_start_association(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        checkbox = self.getElem.find_element_with_wait_EC("id",self.START_OR_NOT_ASSOCIATION)
        try:
            if checkbox.is_selected() == False:
                checkbox.click()
                self.cmf.click_login_msg_button()
        except Exception as e:
            print ("Click start association error: ") + str(e)
    
    u'''点击建立关联'''
    def click_create_relate(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.click_button_common('id',self.CREATE_RELATE)
    
    u'''取消关联'''
    def click_quit_relate(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.click_button_common('id',self.DEL_RELATE)
        
    u'''点击关闭按钮'''
    def click_close_button(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.click_button_common('id',self.AUI_CLOSE)
        
    u'''点击子页面返回按钮'''
    def click_child_page_back_button(self):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        page_back_button = self.getElem.find_element_with_wait_EC('id',self.CHILD_PAGE_BACK_BUTTON)
        if page_back_button.is_displayed():
            time.sleep(1)
            page_back_button.click()
    
    u'''获取双人审批value值
            parameters :
                name : 授权名称
    '''
    def get_double_approvel_value(self,name):
        row = self.cmf.find_row_by_name(name,"fortAuthorizationName")
        
        update_xpath = "//table[@id='content_table']/tbody/tr[" + str(row-1) + "]/td[6]/input[3]"
        
        try:
            text = self.get_value("xpath",update_xpath)
            return text
        
        except Exception as e:
            print ("Get access approvel value error: ") + str(e)