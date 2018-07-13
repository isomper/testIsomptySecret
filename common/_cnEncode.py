#coding=utf-8
u''' 
#文件名：_cnEncode
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2015-09-14
#模块描述：字符转码（共通模块）
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class cnEncode:
    u'''字符转码'''
    
    def cnCode(self,cnStr):
        u'''字符转码使打印的中文能正常显示'''
        if isinstance(cnStr,unicode):
            return cnStr.encode('GBK')
        else:
            return cnStr.decode('utf-8').encode('GBK')
    
    u'''将浮点类型的对象转换为字符型
        Parameters:
            - enStr：转变的字符串
    '''        
    def is_float(self,enStr):
        if isinstance(enStr,float):
            en_str = int(enStr)
            enStr= str(en_str)
        return enStr