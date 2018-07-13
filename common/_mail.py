#coding=utf-8
'''
发送html文本邮件
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import smtplib  
from email.mime.text import MIMEText   
from email.mime.multipart import MIMEMultipart  
from email.mime.image import MIMEImage  
from email.mime.application import MIMEApplication

sys.path.append("/testIsompSecret/common/")
from _log import log

u'''发送邮件'''
class sendMail:
	def __init__(self):
		self.log = log()

	def send_mail(self):
		#设置发送服务器
		server  = "smtp.sbr-info.com"
		#登录人账号
		username = 'chenyuanyuan@sbr-info.com'
		#设置登录人密码
		password = 'yuanyuan123'
		#设置发送人
		sender = username
		#设置接收人
		toList = ['chenyuanyuan@sbr-info.com']
		#设置邮件标题
		content = 'python unit test !'
		msg = MIMEMultipart()
		msg['Subject'] = content
		msg['From'] = sender
		msg['To'] = ','.join(toList)
		#遍历报表名称
		rootdir = "\\testIsompSecret\\report\\"
		try:
			for filename in os.listdir(rootdir):
				fp = open(rootdir+filename,'rb')
				htmlpart = MIMEApplication(fp.read())
				htmlpart.add_header('Content-Disposition', 'attachment', filename=filename)
				msg.attach(htmlpart)
				fp.close()
		except Exception:
			print "report filepath is not exist!"
		
		#发送邮件
		try:
			smtp = smtplib.SMTP()
			smtp.connect(server)
			smtp.login(username,password)
			smtp.sendmail(sender,toList,msg.as_string())
		except Exception as msg:
			self.log.print_detail("email send fail:",msg)
		finally:
			smtp.quit()

if __name__ == "__main__":
	sendMail().send_mail()