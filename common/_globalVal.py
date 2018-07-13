#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


sys.path.append("/testIsompSecret/common/")
from _transCoding import jsonTranscoding
from _initDriver import initDriver

u'''设置全局变量'''
class globalValue():
	
	u'''设置全局变量
			parameters:
				hostUrl : 访问的主机的url
				browerType : 浏览器类型
	'''
	def set_value(self,hostUrl,browerType):
		global host
		global brower

		host = hostUrl
		brower = browerType
		
	#获取全局变量	
	def get_value(self):
		return host,brower