#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsompSecret/webElement/login/")
from loginElement import loginPage

sys.path.append("/testIsompSecret/common")
from _icommon import commonFun
from _log import log
sys.path.append("/testIsompSecret/testSuite/common_suite_file/")
from common_suite_file import CommonSuiteData

class testLogin(object):
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.loginFun = loginPage(self.driver)
        self.cmf = commonFun(self.driver)
        self.dataFile = dataFileName()
        self.comsuit = CommonSuiteData(self.driver)

    u'''获取测试数据
    	Parameters:
    		- sheetname:sheet名称
    		return：表格数据
    '''
    def get_table_data(self,sheetname):
        filePath = self.dataFile.get_login_test_data_url()
        loginData = self.dataFile.get_data(filePath,sheetname)
        return loginData

    u'''登陆的div弹窗的xpath'''
    def login_msg(self):
        login_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        return login_msg
    
    u'''根据访问方式类型登录测试
            parameters:
                sheetname : 表单名称
    '''
    def login_type(self,sheetname):
        loginMes = self.login_msg()
        loginData = self.get_table_data(sheetname)
        #无检查点的测试项标识，如果为True说明通过
        flag = False
        for dataRow in range(len(loginData)):
            #把单行的数据赋值给列表data
            data = loginData[dataRow]
            
            try:
                #如果不是第一行标题，则读取数据
                if dataRow != 0:
                    if sheetname == 'default':
                        self.comsuit.login_secadmin()
                        self.comsuit.switch_to_moudle(u'运维管理', u'用户')
                        self.comsuit.userElem.change_user_status_off("gyrloginad1")
                        self.comsuit.user_quit()
                        self.loginFun.login(data)
                    elif sheetname == 'ad':
                        self.loginFun.ad_login(data)
                    elif sheetname == 'pwd_ad':
                        self.loginFun.ad_pwd_login(data)
                    elif sheetname == 'radius':
                        self.loginFun.radius_pwd_login(data)
                        
                        #如果登陆成功，点击退出
                    if self.loginFun.is_login_success():
                        self.loginFun.quit()
                        #设定没有检查点的测试项通过
                        flag = True
                        
                    self.cmf.test_win_check_point("xpath",loginMes,data,flag)
                    
                    #清空标识状态
                    flag = False
                    
            except Exception as e: 
                print ("User login fail: ") + str(e)

    #登陆测试
    def login(self):
        self.log.log_start("login")
        u'''可以循环设定数据测试系统登录'''
        sheets_name = ['ad','pwd_ad','radius','default']
        for sheetname in sheets_name:
            self.login_type(sheetname)
        self.log.log_end("login")