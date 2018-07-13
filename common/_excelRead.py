#coding=utf-8
u''' 
#文件名：_excelRead
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2014-10-31
#模块描述：Excel读取（共通模块）
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlrd

class excelRead:
    #获取excel数据
    def get_excel_data(self,dataUrl,sheetName):  
        #数据和行数
        Data = []
        try:
            #打开excel表格
            xlsx_data = xlrd.open_workbook(dataUrl)
            #根据sheet名字获取表格数据
            xlsx_table = xlsx_data.sheet_by_name(sheetName)
            #获取excel的总行数
            xrows = xlsx_table.nrows
            
            for irow in range(xrows):
                Data.append(xlsx_table.row_values(irow))

            return Data
            
        except IOError as e:
            print "excel file error:%s,%s"%(e.args[0],e.args[1])
            #print cnd.chiCode("xlsx数据文件不存在")
            
            
#data = ExcelData().getExcelData()

#for i in range(len(data)):
#    print data[i]
