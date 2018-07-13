#coding=utf-8
u''' 
#文件名：_fileRead
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2015-09-14
#模块描述：文本文件读取和写入（共通模块）
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import time
from _cnEncode import cnEncode

class fileRead(object):
    u'''读取文本文件'''
    def get_ip_address(self):
        u'''获取文本文件test.conf中的IP地址'''
        #初始化ipAddress变量
        list = []
        
        #实例化chiEncode
        cnEcod = cnEncode()
        
        try:
            #打开文件
            fileObj = open("/testIsompSecret/common/test.conf","r")
            
            #读取文件所有行
            allLines = fileObj.readlines()
            
            #取出test.conf文件的内容放入list列表
            for line in allLines:
                list.append(line)
    
            #返回IP，ie驱动路径，google驱动路径等数据        
            return list 
            
             
        except IOError:
            print cnEcod.cnCode("test.conf文件不存在！")
            
        finally:
            fileObj.close()

class fileWrite(object):
    
    u'''写入文本文件'''
    def file_write(self,message):
        #实例化chiEncode
        cnEcod = cnEncode()
        
        #打开文件
        fileWriteObj = open("/testIsompSecret/log/isomp.log","a")
        
        try:
            fileWriteObj.write(message + '\n')
            
        except Exception as e:
            print cnEcod.cnCode("日志文件不存在！") + str(e)
            
        finally:
            fileWriteObj.close()

#if __name__ == "__main__":
#    addressList = fileRead().get_ip_address()
#    print addressList
#    print addressList[0]
#    print addressList[1]
#    print addressList[2]
#    print addressList[3]