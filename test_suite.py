#coding=utf-8
#2.9体验版涉密
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import unittest
import HTMLTestRunner
import time
import os

sys.path.append("/testIsompSecret/common/")
from _mail import sendMail
from _transCoding import jsonTranscoding
from _initDriver import initDriver
from _globalVal import globalValue


class testSuite(unittest.TestCase):
    u'''运行所有测试用例集'''
    if __name__ == "__main__":
        #浏览器url和browername列表
        lists = jsonTranscoding().set_brower()
        #浏览器类型列表
        brower_type_list = jsonTranscoding().get_brower_type()
        timeFormat = '%Y-%m-%d %X'
        isTitle = time.strftime(timeFormat, time.localtime())
        #用例存放路径
        dir = "\\testIsompSecret\\testSuite"
        #报表存放路径
        report_dir = "\\testIsompSecret\\report\\"
        #判断report文件夹是否存在
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        for index in range(len(lists)):
            #浏览器url
            host_url = lists.keys()[index] 
            #浏览器名称
            brower_type = lists.values()[index]
            globalValue().set_value(host_url,brower_type)
            #浏览器详细类型
            brower_detail_type = brower_type_list[index]
            
            #定义测试报告的输出页面
            reportFile = report_dir + str(brower_detail_type.strip()) + "Report.html"
            rf = file(reportFile,'wb')
            loader = unittest.TestLoader()
            suite = unittest.TestSuite()
        
            package_tests = loader.discover(start_dir=dir,pattern='test*.py')
            suite.addTests(package_tests)

            runner = HTMLTestRunner.HTMLTestRunner(stream=rf,title=isTitle,description="Report_description")
            runner.run(suite)
            rf.close()
        #直接跑测试用例
        #unittest.TextTestRunner().run(suite)
        sendMail().send_mail()

