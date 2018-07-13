#coding=utf-8
u''' 
#文件名：_icommon
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2016-04-04
#模块描述：自定义封装方法（通用模块）
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsompSecret/common/")
from _cnEncode import cnEncode
from _log import log

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#获取定位元素
class getElement(object):
    def __init__(self,driver):
        #selenium驱动
        self.driver = driver
        self.log = log()
    
    u'''等待元素出现后再定位元素
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - timeout:超时前等待的时间
        return：查找的元素对象
    '''    
    def find_element_with_wait(self,type,value,timeout=1):
        if type == "xpath":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_xpath(value))
        elif type == "id":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_id(value))
        elif type == "name":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_name(value))
        elif type == "tagname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_elements_by_tag_name(value))
        elif type == "classname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_class_name(value))
        elif type == "css":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_css_selector(value))
        elif type == "link":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_link_text(value))
        elif type == "plt":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_partial_link_text(value))

    u'''等待元素出现后再点击元素
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - timeout:超时前等待的时间
        return：定位元素并点击该元素
    '''
    def find_element_with_wait_clickable_and_click(self,type,value,timeout=10):
            if type == "id":
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.ID, value))).click()
            elif type == "xpath":
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, value))).click()
            elif type == "name":
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.NAME, value))).click()
            elif type == "tagname":
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.TAG_NAME, value))).click()
            elif type == "classname":
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, value))).click()
            elif type == "css":
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, value))).click()
            elif type == "link":
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.LINK_TEXT, value))).click()
            elif type == "plt":
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, value))).click()
    
    u'''等待元素出现后再定位元素EC
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - timeout:超时前等待的时间
        return：定位元素并点击该元素
    '''
    def find_element_with_wait_EC(self,type,value,timeout=10):
            if type == "id":
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, value)))
            elif type == "xpath":
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, value)))
            elif type == "name":
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, value)))
            elif type == "tagname":
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, value)))
            elif type == "classname":
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            elif type == "css":
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
            elif type == "link":
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
            elif type == "plt":
                return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
    
    u'''等待元素出现后再定位元素并发送键值
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - key：发送的字符或者键盘的键值
            - timeout:超时前等待的时间 
        return：定位元素并发送键值
    '''    
    def find_element_wait_and_sendkeys(self,type,value,key,timeout=1):
        if type == "xpath":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_xpath(value)).send_keys(key)
        elif type == "id":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_id(value)).send_keys(key)
        elif type == "name":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_name(value)).send_keys(key)
        elif type == "tagname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_elements_by_tag_name(value)).send_keys(key)
        elif type == "classname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_class_name(value)).send_keys(key)
        elif type == "css":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_css_selector(value)).send_keys(key)
        elif type == "link":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_link_text(value)).send_keys(key)
        elif type == "plt":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_partial_link_text(value)).send_keys(key)

    u'''填写文本框的内容
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - key:文本框内容
            - timeout:超时前等待的时间
    '''
    def find_element_sendkyes_EC(self, type, value, key, timeout=10):

        if type == "id":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, value))).send_keys(key)
        elif type == "xpath":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, value))).send_keys(key)
        elif type == "name":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, value))).send_keys(key)
        elif type == "tagname":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, value))).send_keys(key)
        elif type == "classname":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, value))).send_keys(key)
        elif type == "css":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, value))).send_keys(key)
        elif type == "link":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, value))).send_keys(key)
        elif type == "plt":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value))).send_keys(key)
    
    u'''等待元素出现后再定位元素并点击
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - timeout:超时前等待的时间
        return：定位元素并点击该元素
    '''    
    def find_element_wait_and_click(self,type,value,timeout=1):
        if type == "xpath":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_xpath(value)).click()
        elif type == "id":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_id(value)).click()
        elif type == "name":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_name(value)).click()
        elif type == "tagname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_elements_by_tag_name(value)).click()
        elif type == "classname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_class_name(value)).click()
        elif type == "css":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_css_selector(value)).click()
        elif type == "link":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_link_text(value)).click()
        elif type == "plt":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_partial_link_text(value)).click()

    u'''等待元素出现后再定位元素并点击EC
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - timeout:超时前等待的时间
        return：定位元素并点击该元素
    '''
    def find_element_wait_and_click_EC(self,type,value,timeout=10):
            if type == "id":
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, value))).click()
            elif type == "xpath":
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, value))).click()
            elif type == "name":
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, value))).click()
            elif type == "tagname":
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, value))).click()
            elif type == "classname":
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, value))).click()
            elif type == "css":
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, value))).click()
            elif type == "link":
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, value))).click()
            elif type == "plt":
                WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value))).click()

    u'''等待元素出现后再定位元素并获取元素的文本
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - timeout:超时前等待的时间  
        return：获取定位元素的文本
    '''    
    def find_element_wait_and_get_text(self,type,value,timeout=1):
        if type == "xpath":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_xpath(value)).text
        elif type == "id":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_id(value)).text
        elif type == "name":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_name(value)).text
        elif type == "tagname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_elements_by_tag_name(value)).text
        elif type == "classname":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_class_name(value)).text
        elif type == "css":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_css_selector(value)).text
        elif type == "link":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_link_text(value)).text
        elif type == "plt":
            return WebDriverWait(self.driver,timeout).until(lambda x:x.find_element_by_partial_link_text(value)).text

    u'''等待文本出现并与数据文本比较
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - data: 比较文本
            - timeout:超时前等待的时间
        return：文本内容一致返回true，文本内容不一致返回false
    '''

    def find_element_wait_and_compare_text(self, type, value, data, timeout=5):
        try:
            if type == "xpath":
                return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.XPATH, value), data[1]))
            elif type == "id":
                return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.ID, value), data[1]))
            elif type == "name":
                return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.NAME, value), data[1]))
            elif type == "tagname":
                return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.TAG_NAME, value), data[1]))
            elif type == "classname":
                return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.CLASS_NAME, value), data[1]))
            elif type == "css":
                return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, value), data[1]))
            elif type == "link":
                return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.LINK_TEXT, value), data[1]))
            elif type == "plt":
                return WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element((By.PARTIAL_LINK_TEXT, value), data[1]))
        except Exception:
            return False

    u'''清空文本框的内容
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - timeout:超时前等待的时间
    '''
    def find_element_wait_and_clear(self, type, value, timeout=5):

        if type == "id":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, value))).click()
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, value))).clear()
        elif type == "xpath":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, value))).click()
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, value))).clear()
        elif type == "name":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, value))).click()
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, value))).clear()
        elif type == "tagname":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, value))).click()
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, value))).clear()
        elif type == "classname":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, value))).click()
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, value))).clear()
        elif type == "css   ":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, value))).click()
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, value))).clear()
        elif type == "link":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, value))).click()
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, value))).clear()
        elif type == "plt":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value))).click()
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value))).clear()
    
    u'''清空文本框的内容
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - timeout:超时前等待的时间
    '''
    def find_element_wait_and_clear_EC(self, type, value, timeout=5):
    
        if type == "id":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, value))).clear()
        elif type == "xpath":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, value))).clear()
        elif type == "name":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.NAME, value))).clear()
        elif type == "tagname":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.TAG_NAME, value))).clear()
        elif type == "classname":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, value))).clear()
        elif type == "css":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, value))).clear()
        elif type == "link":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.LINK_TEXT, value))).clear()
        elif type == "plt":
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value))).clear()

    u'''元素是否存在
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - timeout:超时前等待的时间
        return:true代表元素出现，false代表找不到元素
    '''
    def is_element_exsit(self,type,value,timeout=3):
        isExsit = False
        
        try:
            element = self.find_element_with_wait(type,value)
            
            if element != False:
                isExsit = True
        except Exception as e:
            self.log.error_detail("element is not exsit:",value)
        return isExsit

#select元素
class selectElement(object):

    def __init__(self,driver):
        #selenium驱动
        self.driver = driver

    u'''根据索引选择
        Parameters:
            - selem:定位到的select元素
            - index:select的索引，例0,1,2,从0开始计数
    '''
    def select_element_by_index(self, selem, index):
        return Select(selem).select_by_index(index)

    u'''根据索引取消选择
        Parameters:
            - selem:定位到的select元素
            - index:select的索引，例0,1,2,从0开始计数
    '''
    def deselect_element_by_index(self, selem, index):
        return Select(selem).deselect_by_index(index)
    
    u'''根据value值取消选择
        Parameters:
            - selem:定位到的select元素
            - value：option的value值
    '''    
    def deselect_element_by_value(self,selem,value):
        return Select(selem).deselect_by_value(value)

    u'''根据文本值取消选择
        Parameters:
            - selem:定位到的select元素
            - text：页面的文本值
    '''
    def deselect_element_by_text(self, selem, text):
        Select(selem).deselect_by_visible_text(text)

    u'''判断select元素是否被选中
        parameter:
            - type:定位的类型，如id,name,tag name,class name,css,xpath等
            - value：页面的元素值
            - timeout:超时前等待的时间
        return:true代表元素选中，false代表元素没有选中
    '''
    def select_element_check(self, type,value,timeout=1):
        try:
            if type == "xpath":
                return WebDriverWait(self.driver,timeout).until(EC.element_located_to_be_selected((By.XPATH,value)))
            elif type == "id":
                return WebDriverWait(self.driver,timeout).until(EC.element_located_to_be_selected((By.ID,value)))
            elif type == "name":
                return WebDriverWait(self.driver,timeout).until(EC.element_located_to_be_selected((By.NAME,value)))
            elif type == "tagname":
                return WebDriverWait(self.driver,timeout).until(EC.element_located_to_be_selected((By.TAG_NAME,value)))
            elif type == "classname":
                return WebDriverWait(self.driver,timeout).until(EC.element_located_to_be_selected((By.CLASS_NAME,value)))
            elif type == "css":
                return WebDriverWait(self.driver,timeout).until(EC.element_located_to_be_selected((By.CSS_SELECTOR,value)))
            elif type == "link":
                return WebDriverWait(self.driver,timeout).until(EC.element_located_to_be_selected((By.LINK_TEXT,value)))
            elif type == "plt":
                return WebDriverWait(self.driver,timeout).until(EC.element_located_to_be_selected((By.PARTIAL_LINK_TEXT,value)))
        except Exception:
            return False

    u'''根据value选择
        Parameters:
            - selem:定位带的Select元素
            - value:select选项中的value属性值
    '''
    def select_element_by_value(self,selem,value):
        return Select(selem).select_by_value(value)
    
    u'''根据text选择
            Parameters:
                - selem:定位带的Select元素
                - text:select选项中的文本值
        '''
    
    def select_element_by_visible_text(self,selem,text):
        return Select(selem).select_by_visible_text(text)
    
    u'''获取select中的option数量
        Parameters:
            - selem:定位到的select元素
        Return:返回select元素的option数量
    '''
    def get_options_count(self,selem):
        
        options_list = selem.find_elements_by_tag_name("option")

        return len(options_list)
    
    u'''获取select选中的option文本
        Parameters:
            - selem:定位到的select元素
            - index:选择的option的索引
        Return：select元素中的index对应的text
    '''
    def get_option_text(self,selem,index):
        options_list = selem.find_elements_by_tag_name("option")
        
        for cnt,option in enumerate(options_list):
            if index == cnt:
                selem_text = option.text
                
        return selem_text
    
    u'''获取select所有option文本
        Parameters:
            - selem:定位到的select元素
        Return: select元素中的所有option的text列表
    '''
    def get_all_option_text(self,selem):
        options_list = selem.find_elements_by_tag_name("option")
        
        return [option_text_list.text for option_text_list in options_list]

    u'''获取select选中的option的value
        Parameters:
            - selem:定位到的select元素
            - index:选择的option的索引
        Return：select元素中的index对应的value值
    '''
    def get_option_value(self,selem,index):
        options_list = selem.find_elements_by_tag_name("option")
        
        for cnt,option in enumerate(options_list):
            if index == cnt:
                selem_value = option.get_attribute("value")
                
        return selem_value
        
    u'''获取select中的所有option的value
        Parameters:
            - selem:定位到的select元素
        Return: select元素中的所有option的value列表
    '''
    def get_all_option_value(self,selem):
        options_list = selem.find_elements_by_tag_name("option")
        
        return [option_value_list.get_attribute("value") for option_value_list in options_list]
    
    u'''选中select中的所有的option
        Parameters:
            - selem:定位到的select元素
    '''    
    def select_all_option(self,selem):
        options = selem.find_elements_by_tag_name("option")
        for option in options:
            Select(selem)._setSelected(option)

    u'''自定义选择select中的option
        Parameters:
            - selem:定位到的select元素
            - options_list:option索引数组
    '''
    def select_user_defined_option(self,selem,options_list):
        options = selem.find_elements_by_tag_name("option")
        for option_index in options_list:
            Select(selem)._setSelected(options[option_index])

#frame元素
class frameElement(object):

    def __init__(self,driver):
        #selenium驱动
        self.driver = driver
        self.getElem = getElement(driver)
    
    u'''定位到topFrame'''
    def switch_to_top(self):
        #如果content1的frame加载完毕，定位到content1的frame
        if self.getElem.is_element_exsit("id","content1"):
            self.driver.switch_to_frame("content1")
            
        if self.getElem.is_element_exsit("id","topFrame"): 
            self.driver.switch_to_frame("topFrame")

    u'''定位到mainFrame'''
    def switch_to_main(self):
        if self.getElem.is_element_exsit("id","content1"):
            self.driver.switch_to_frame("content1")
            
        if self.getElem.is_element_exsit("id","mainFrame"):
            self.driver.switch_to_frame("mainFrame")
    
    u'''定位到leftFrame'''
    def switch_to_left(self):
        self.switch_to_main()
        if self.getElem.is_element_exsit("id","leftFrame"):
            self.driver.switch_to_frame("leftFrame")
        
    u'''定位到rightFrame'''
    def switch_to_right(self):
        self.switch_to_main()
        if self.getElem.is_element_exsit("id","rightFrame"):
            self.driver.switch_to_frame("rightFrame")
    
    u'''定位到rigthFrame'''
    def switch_to_rigth(self):
        self.switch_to_main()
        if self.getElem.is_element_exsit("id","rigthFrame"):
            self.driver.switch_to_frame("rigthFrame")
        
    u'''定位到bottomFrame'''
    def switch_to_bottom(self):
        if self.getElem.is_element_exsit("id","content1"):
            self.driver.switch_to_frame("content1")
        if self.getElem.is_element_exsit("id","bottomFrame"):
            self.driver.switch_to_frame("bottomFrame")

    u'''返回上级frame'''
    def switch_to_content(self):
        self.driver.switch_to_default_content()
        
    u'''定位到artIframe'''
    def switch_to_artIframe(self):
        self.switch_to_content()
        if self.getElem.is_element_exsit("id","artIframe"):
            self.driver.switch_to_frame("artIframe")
    
    u'''从一个frame跳转到其他frame
        Parameters:
            - frameName:要跳转到的frame的名字      
    '''
    def from_frame_to_otherFrame(self,frameName):
        time.sleep(2)
        self.switch_to_content()
        time.sleep(1)
        if frameName == "mainFrame":
            #定位到mainFrame
            self.switch_to_main()
            
        elif frameName == "bottomFrame":
            #定位到bottomFrame
            self.switch_to_bottom()
            
        elif frameName == "topFrame":
            #定位到topFrame            
            self.switch_to_top()
            
        elif frameName == "leftFrame":
            #定位到leftFrame            
            self.switch_to_left()
        
        elif frameName == "rightFrame":
            #定位到rightFrame            
            self.switch_to_right()
            
        elif frameName == "rigthFrame":
            #定位到rightFrame            
            self.switch_to_rigth()
        elif frameName == "artIframe":
            self.switch_to_artIframe()

#table元素
class tableElement(object):
    
    def __init__(self,driver):
        #selenium驱动
        self.driver = driver

    u'''获取表格中的所有行对象
        Parameters:
            - table_xpath:定位table的xpath
        Return: table的所有行对象
    '''
    def get_table_rows(self,table_xpath):
        get_elem = getElement(self.driver)
        
        #定位到table
        table_elem = get_elem.find_element_with_wait_EC("xpath",table_xpath)
        #获取table中的所有行
        row_elems = table_elem.find_elements_by_tag_name("tr")
             
        return row_elems

    u'''获取表格中一列的文本内容
        Parameters:
            - table_xpath:定位table的xpath
            - row:行号
            - col:列号  
        Return: table指定行的列中的文本,table列的列对象
    '''
    def get_table_cell_text(self,table_xpath,row,col):
        
        get_rows = tableElement(self.driver)
        
        #获取表格中的所有行
        row_elems = get_rows.get_table_rows(table_xpath)
        
        #获取行中的所有列
        col_elems = row_elems[row].find_elements_by_tag_name("td")               
            
        return col_elems[col].text,col_elems[col]

    u'''获取表格中的行数
        Parameters:
            - table_xpath:定位table的xpath
        Return: table的行数
    '''
    def get_table_rows_count(self,table_xpath):
        
        get_rows = tableElement(self.driver)

        #获取表格中的所有行
        row_elems = get_rows.get_table_rows(table_xpath)

        return len(row_elems)

    u'''定位表格中的某一列的select对象
        Parameters:
            - row:表格的行
            - col:某一个行的一列
            - index:select选择账号的索引号
    '''
    def get_table_td_select(self,row,col,index):
        
        frameElem = frameElement(self.driver)
        
        tx = "html/body/div[1]/div[7]/div[2]/div[1]/table"
        
        #定位到列
        tdElem = self.get_table_cell_text(tx,row,col)[1]
        tdElem.click()
        
        #定位列的select
        seElem = tdElem.find_elements_by_tag_name("select")

        selectElem = selectElement(self.driver)
        #选择账号
        selectElem.select_element_by_index(seElem[0],index)

#通用函数
class commonFun(object):
    
    def __init__(self,driver):
        #selenium驱动
        self.driver = driver
        self.cn = cnEncode()
        self.log = log()
        self.getElem = getElement(driver)
        self.frameElem = frameElement(driver)
        self.selectElem= selectElement(driver)

    u'''选择角色
        Parameters:
            - index:下拉列表的索引（0,1,2）
    '''
    def select_role(self,index):
        self.getElem.find_element_wait_and_click("id","js_z")
        role = self.getElem.find_element_with_wait("id","js_x")
        selectElem = selectElement(self.driver)
        selectElem.select_element_by_index(role,index)

    u'''通过角色名称选择角色
        Parameters:
            - text:角色名称
    '''    
    def select_role_by_text(self,text):
        self.frameElem.from_frame_to_otherFrame("topFrame")
        
        self.getElem.find_element_wait_and_click("id","js_z")
        role = self.getElem.find_element_with_wait("id","js_x")
        selectElem = selectElement(self.driver)
        selectElem.select_element_by_visible_text(role,text)
        
    u'''获取开关的状态
        Parameters:
            - elem:开关对应的元素对象
    
        return: 0代表开关关闭，1代表开关打开
    '''
    def switch_status(self,type,value):
        status = 1
        
        switch = self.getElem.find_element_with_wait(type,value)
        
        #获取开关class的属性
        switch_value = switch.get_attribute('class')
        
        if switch_value == "switch_off":
            status = 0
        
        return status
        
    u'''列表中的操作项选择，可以选择操作列中某一个项目    
        Parameters:
            - elem：定位到table中对应的列对象
            - index: 点击索引（0,1,2代表操作列内的项目）
    '''
    def click_operate(self,table_xpath,row,col,index):
        table_elem = tableElement(self.driver)
        cell_elem = table_elem.get_table_cell_text(table_xpath,row,col)[1]
        op = cell_elem.find_elements_by_tag_name("input")[index]
        op.click()
        
    u'''点击分页中的按钮
        Parameters:
            - type：first表示首页，last表示尾页，up表示上一页，
                    down表示下一页，jump表示跳转按钮
    '''
    def click_paging(self,type):
        time.sleep(1)
        
        pageDiv = self.getElem.find_element_with_wait("id","pager")
        pagerBtn = pageDiv.find_elements_by_tag_name("input")
        
        #点击首页
        if type == "first":
            pagerBtn[2].click()
            
        #点击上一页
        elif type == "up":
            pagerBtn[3].click()
            
        #点击下一页
        elif type == "down":
            pagerBtn[4].click()
        
        #点击尾页
        elif type == "last":
            pagerBtn[5].click()
        
        #点击跳转
        elif type == "jump":
            pagerBtn[0].click()
        
    u'''菜单选择
        Parameters:
            - levelText1：1级菜单文本
            - levelText2：2级菜单文本 
            - levelText3：3级菜单文本           
    '''
    def select_menu(self,levelText1,levelText2='no',levelText3='no'):
        #进入topframe
        frameElem = frameElement(self.driver)
        frameElem.from_frame_to_otherFrame("topFrame")
        
        #点击一级菜单
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,levelText1))).click()
        
        #如果有2级菜单，再点击2级菜单
        if levelText2 != 'no':
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,levelText2))).click()
        
        #如果有3级菜单，根据名称点击3级菜单
        if levelText3 != 'no':
            frameElem.from_frame_to_otherFrame("leftFrame")
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,levelText3))).click()
        
    u'''操作时间控件
        Parameters:
            - wdateId：日期控件input控件的ID值
            - fxpath：日期控件frame的xpath路径
            - status: 日期控件是否有时分秒
            - txpath：日期控件table的xpath路径
            - time：设定的日期，格式为2016-9-7 11:42:42
            - type：t代表今天，c代表clear，q代表确定，默认选择今天 
    '''
    def select_time(self,wdateId,fxpath,status='0',type='t',txpath = None,time = None):
        
        self.getElem.find_element_wait_and_click("id",wdateId)
        self.driver.switch_to_default_content()
        
        frame = self.driver.find_element_by_xpath(fxpath)
        self.driver.switch_to_frame(frame)
    
        if type == 't':
            self.getElem.find_element_wait_and_click("id","dpTodayInput")
        elif type == 'c':
            self.getElem.find_element_wait_and_click("id","dpClearInput")
        elif type == 'q':
            if time is not None:
                list = time.split()
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
                
                #设定年
                dTitle[1].clear()
                dTitle[1].send_keys(tYear)
                #设定月
                dTitle[0].clear()
                dTitle[0].send_keys(tMon)
                self.getElem.find_element_wait_and_click_EC("id", "dpTitle")
                if txpath is not None:
                
                    table_elem = tableElement(self.driver)
                                    
                    iStatus = False
                                   
                    for itr in range(7):
                        if itr != 0:
                            for itd in range(7):
                                ct = table_elem.get_table_cell_text(txpath,itr,itd)[0]
                                                
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
                                    table_elem.get_table_cell_text(txpath,itr,itd)[1].click()
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
            
    u'''弹窗类检查点
        Parameters:
            - type：定位弹窗中元素的类型
            - elem：弹窗元素的名字或者路径
            - data：excel一行的数据
            - flag:没有检查点的测试项通过标识。Ture为通过，False为未通过           
    '''
    def click_login_msg_button(self):
        #确定按钮
        self.driver.switch_to_default_content()
        OKBTN = "//div[@id='aui_buttons']/button[1]"
        return self.getElem.find_element_wait_and_click('xpath',OKBTN)

    u'''点击弹框按钮
          Parameters:
              -index数字开关0代表点击取消，1代表点击确定
    '''
    
    def click_msg_button(self,index):
        if index == 1:
            return self.click_login_msg_button()
        elif index == 0:
            NOBTN = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]"
            return self.getElem.find_element_wait_and_click('xpath', NOBTN)

    u'''弹窗类检查点
        Parameters:
            - type：定位弹窗中元素的类型
            - elem：弹窗元素的名字或者路径
            - data：excel一行的数据
            - flag:没有检查点的测试项通过标识。Ture为通过，False为未通过           
    '''
    def test_win_check_point(self,type,elem,data,flag):        

        #检查点为空
        if data[1] == "":
            if flag:
                #测试点通过
                self.log.log_detail(data[0],True)
            else:
                #测试点没通过
                self.log.log_detail(data[0],False)
                
        #检查点不为空
        else:
            #判断文本内容是否一致
            elemText = self.getElem.find_element_wait_and_compare_text(type,elem,data)
            self.click_msg_button(1)
            if elemText:
                # 页面的内容与检查点内容一致，测试点通过
                self.log.log_detail(data[0], True)
            else:
                #页面抓取到的内容与检查点不一致，测试点不通过
                self.log.log_detail(data[0],False)
        
    u'''表格内容存在类检查点
        Parameters:
            - type：定位表格中元素的类型
            - elem：弹窗元素的名字或者路径
            - data：excel一行的数据
            - flag:没有检查点的测试项通过标识。Ture为通过，False为未通过           
    '''
    def table_check_point(self,type,elem,data,flag):
        pass
    
    u'''
    勾选页面上所有checkbox
    #去掉最后一个checkbox的勾选，checkbox.pop().click()
    '''
    def select_all_checkbox(self):
        try:
            checkboxs = self.driver.find_elements_by_css_selector('input[type=checkbox]')
            for checkbox in checkboxs: 
                if checkbox.is_selected() == False and \
                    self.getElem.is_element_exsit('css','input[type=checkbox]') == True:
                    checkbox.click()
        except Exception as e:
            self.log.error_detail("checkbox is not visible",e)

    u'''点击返回按钮'''
    def back(self):
        try:
            self.frameElem.switch_to_content()
            self.frameElem.switch_to_main()
            time.sleep(1)
            self.getElem.find_element_wait_and_click("id", "history_skip")
        except Exception:
            print("Click the return button to fail")            

    u'''select右边框检查点
        Parameters:
            - type：定位右边框中元素的类型
            - elem：右边框元素的名字或者路径
            - data：excel一行的数据
            - flag:没有检查点的测试项通过标识。Ture为通过，False为未通过
    '''
    def select_check_point(self, type, elem, data, flag):
        # 检查点为空
        if data[1] == "":
            if flag:
                # 测试点通过
                self.log.log_detail(data[0], True)
            else:
                # 测试点没通过
                self.log.log_detail(data[0], False)

        # 检查点不为空
        else:
            # 右框中的文本内容
            optin = self.getElem.find_element_with_wait(type, elem)
            allText = self.selectElem.get_all_option_text(optin)
            for num in range(len(allText)):
                if allText[num] == data[1]:
                    # 页面的内容与检查点内容一致，测试点通过
                    self.log.log_detail(data[0], True)
                else:
                    # 页面抓取到的内容与检查点不一致，测试点不通过
                    self.log.log_detail(data[0], False)

    u'''点击批量删除
        Parameters:
            - id：定位删除按钮的id
    '''
    def bulkdel(self, id):
        try:
            self.frameElem.switch_to_content()
            self.frameElem.switch_to_main()
            self.getElem.find_element_wait_and_click_EC("id", id)
        except Exception:
            print("Failed to hit the batch delete button")            

    u'''勾选全选框'''
    def check_all(self):
        try:
            self.frameElem.switch_to_content()
            self.frameElem.switch_to_main()
            time.sleep(1)
            self.getElem.find_element_wait_and_click_EC("id", "checkbox")
        except Exception:
            print("Select the check box failure")

    u'''判断名称是否存在
       Parameters:
          - namevalue:传入的要被查询名称
          - name:表格列的name属性
       return：true代表存在，false代表不存在
    '''
    def is_namevalue_exsit(self, namevalue, name):
        isExsit = False
        self.frameElem.switch_to_content()
        self.frameElem.switch_to_main()
        try:
            text_list = self.driver.find_elements_by_name(name)
            time.sleep(1)
            for fortNameValue in text_list:
                fortNameValue_text = fortNameValue.text
                if fortNameValue_text == namevalue:
                    isExsit = True
                    break
        except Exception:
            print (namevalue + "is not exsit.")
        return isExsit

    u'''查询已存在名称位于第几行
       Parameters:
          - namevalue:传入的要被查询名称
          - name:表格列的name属性
       return：定位该名称位于第几行
    '''
    def find_row_by_name(self, namevalue, name):
        time.sleep(2)
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        row = 0
        try:
            if self.is_namevalue_exsit(namevalue, name):
                text_list = self.driver.find_elements_by_name(name)
                for fortNameValue in text_list:
                    row = row + 1
                    fortNameValue_text = fortNameValue.text
                    if fortNameValue_text == namevalue:
                        break
        except Exception:
            print (namevalue + "is not exsit.")
        return row

# if __name__ == "__main__" :
#    #启动页面
#    browers = initDriver().open_driver()

# 登陆操作开始
#    getElem = getElement(browers)
#    a = getElem.find_element_with_wait("id","loginMethod")

#    selectElem = selectElement(browers)
#    selectElem.select_element_by_index(a,0)
# print selectElem.get_options_count(a)
# print cnEncode().cnCode(selectElem.get_option_text(a,0))
# print cnEncode().cnCode(selectElem.get_all_option_text(a)[0])
# print cnEncode().cnCode(selectElem.get_all_option_text(a)[1])

#    pwd = "html/body/div[2]/div[3]/form/table/tbody[2]/tr[4]/td/input"
    #getElem.find_element_and_sendkeys("id","username","isomper")
#    getElem.find_element_wait_and_sendkeys("id","username","a")
#    getElem.find_element_wait_and_sendkeys("xpath",pwd,"1")
#    getElem.find_element_wait_and_click("id","do_login")
#登陆操作结束

#    frameElem = frameElement(browers)
#    frameElem.switch_to_bottom()
    #aa = getElem.find_element("classname","lt")
#    frameElem.from_frame_to_otherFrame("topFrame")
#    getElem.find_element_and_click("xpath","html/body/div[1]/div/div[2]/ul/li[2]/span/a")
#    getElem.find_element_and_click("xpath","html/body/div[1]/div/div[2]/ul/li[2]/p/a[1]")
#    frameElem.from_frame_to_otherFrame("mainFrame")
    
    #登陆后选择用户角色
#    common = commonFun(browers)
#    common.select_role(2)
#    common.select_role(2)
#    common.select_role(0)
#    swithvalue = common.switch_status()
#    print swithvalue
    
#    print getElem.find_element("id","hostName").text
#    frameElem.from_frame_to_otherFrame("mainFrame")
#    getElem.find_element_and_sendkeys("id","fortUserAccountOrName","a")
#    b = getElem.find_element("id","fortRoleId")
#    selectElem.select_element_by_index(b,2)
    
    #用户页面的添加按钮
#    userAdd_xpath = r"html/body/form/div/div[5]/input[1]"
#    getElem.find_element_wait_and_click("xpath",userAdd_xpath)
    
#    #用户页面的表格
#    table_elem = tableElement(browers)
#    tx = "html/body/form/div/div[7]/div[2]/div/table"
#    print table_elem.get_table_cell_text(tx,0,1)
#    print table_elem.get_table_rows_count(tx)

    
    #用户页面的表格
#    table_elem = tableElement(browers)
#    tx = "html/body/form/div/div[7]/div[2]/div/table"
    
    #返回两个返回值的第一个
    #cell_text = table_elem.get_table_cell_text(tx,0,6)[0]
    
    #返回两个返回值的第二个
    #cell_elem = table_elem.get_table_cell_text(tx,1,8)[1]
    #print table_elem.get_table_cell_text(tx,1,1)[0]
    
    #用户页面的角色选择开始
#    common.click_operate(cell_elem,1)
#    se = getElem.find_element("id","Roles")
#    selectElem.select_element_by_index(se,1)
#    #用户页面的角色选择结束
    
    #用户列表的锁定开关
#    switch_status = common.switch_status(cell_elem)
#    print switch_status
    
    #返回两个返回值分别放进cell_text和cell_elem
    #cell_text,cell_elem = table_elem.get_table_cell_text(tx,0,6)
    
    

    #print cell_elem
#    print cnEncode().cnCode(table_elem.get_table_cell_text(tx,0,7))
#    print table_elem.get_table_rows_count(tx)

    #部门选择
#    getElem.find_element_wait_and_click("id","department_name")
#    #getElem.find_element_wait_and_click("id","query_zijiedian")
#    getElem.find_element_wait_and_click("id","tree_1_switch")
#    getElem.find_element_wait_and_click("link",u"测试部门a")
    
    #点击分页的首页，上一页，下一页，尾页，跳转
#    getElem.find_element_with_wait("id","goto_text").clear()
#    getElem.find_element_wait_and_sendkeys("id","goto_text","2")
#    common.click_paging("jump")
#    common.click_paging("up")
#    common.click_paging("down")
#    common.click_paging("first")    
#    common.click_paging("last") 

    #选择菜单
    #common.select_menu(u"系统配置",u"备份还原")
#    common.select_menu(u"系统配置",u"系统状态",u"关机重启")
#    common.select_menu(u"运维管理",u"用户")
    
#    #用户导入开始
#    #时间控件
#    frameElem.from_frame_to_otherFrame("rightFrame")
#    #点击导入
#    getElem.find_element_wait_and_click("id","importTemp")
#    #在浏览上传中输入文件名
#    getElem.find_element_wait_and_sendkeys("name","filePath","user_import_temp.xls")
#    #点上传按钮
#    getElem.find_element_wait_and_click("id","btn_sc")
#    #起始行
#    getElem.find_element_wait_and_sendkeys("id","st","1")
#    #结束行
#    getElem.find_element_wait_and_sendkeys("id","en","2")
#    #点提交按钮
#    getElem.find_element_wait_and_click("id","btn_tj")
#    #用户导入结束
    
    
#    common.select_time("backUpTime","html/body/div[2]/iframe",'c')
#    frameElem.from_frame_to_otherFrame("rigthFrame")
#    common.select_time("backUpTime","html/body/div[2]/iframe",'t')
    
#    frameElem.from_frame_to_otherFrame("rigthFrame")
#    frame_xpath = "html/body/div[2]/iframe"
#    table_xpath = "html/body/div/div[3]/table"

#    #默认选择今天
#    common.select_time("backUpTime",frame_xpath)
#    frameElem.from_frame_to_otherFrame("rigthFrame")
#    #根据日期来设定
#    common.select_time("backUpTime",frame_xpath,'q',table_xpath,"2016-10-31 12:30:10")

    
#退出操作
    #getElem.find_element_wait_and_click("id","logout")