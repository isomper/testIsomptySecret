#coding=utf-8
u''' 
#文件名：_initDriver
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2015-12-09
#模块描述：日志模块（共通模块）
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import time
import logging
import logging.config

from _fileRead import *
from _cnEncode import cnEncode

class log(object):
    
    def __init__(self):
        self.cn = cnEncode()
        logging.config.fileConfig("/testIsompSecret/common/logging.conf")
        self.logger = logging.getLogger('simpleExample')
        self.logger_console = logging.getLogger('consoleLogExample')
        

    #日志记录开始
    def log_start(self,caseName): 
        msg = caseName + "----start"
        
        self.logger.info(msg)


    #日志记录结束
    def log_end(self,caseName):    
        msg = caseName + "----end\n"
        
        self.logger.info(msg)

        
#    u'''日志的详细内容
#        Parameters:
#            - msg：日志信息
#            - flag：判定通过或未通过的标识，True代表通过，False代表未通过
#    '''
#    def log_detail(self,msg,flag):
#        #获取当前时间
#        iTime = time.strftime('%Y-%m-%d %X',time.localtime())
#        
#        #通过信息
#        passMsg = "["+ iTime + "]" + self.cn.cnCode(msg) + self.cn.cnCode(u"---------测试通过")
#
#        #未通过信息
#        unPassMsg = "[" + iTime + "]" + self.cn.cnCode(msg) + self.cn.cnCode(u"---------测试未通过")
#        
#        if flag:
#            #写通过信息进日志
#            fileWrite().file_write(passMsg)
#            print passMsg
#            
#        else:
#            #写未通过信息进日志
#            fileWrite().file_write(unPassMsg)
#            print unPassMsg
            

    u'''日志的详细内容
        Parameters:
            - msg：日志信息
            - flag：判定通过或未通过的标识，True代表通过，False代表未通过
    '''
    def log_detail(self,msg,flag):
        #通过信息
        passMsg = self.cn.cnCode(msg) + self.cn.cnCode(u"---------测试通过")

        #未通过信息
        unPassMsg = self.cn.cnCode(msg) + self.cn.cnCode(u"---------测试未通过")
        
        if flag:
            #通过信息写入日志
            self.logger.info(passMsg)
            
        else:
            #未通过信息写入日志
            self.logger.info(unPassMsg)
        
    def error_detail(self,msg_,errorMsg):
        msg = self.cn.cnCode(msg_) + str(errorMsg)
        self.logger_console.info(msg)
            

#if __name__ == "__main__":
