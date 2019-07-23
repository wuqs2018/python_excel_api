import smtplib
from email.mime.text import MIMEText
import time;

class SendEmail:
	global send_user
	global email_host
	global password

	email_host = 'SMTP.qq.com'
	send_user = ''
	password = ''

	def send_mail(self, user_list, sub, content):
		user = '<'+send_user+'>'
		message = MIMEText(content, 'plain', 'utf-8')
		message['Subject'] = sub
		message['From'] = user
		message['To'] = ';'.join(user_list)

		server = smtplib.SMTP()
		server.connect(email_host)
		server.login(send_user, password)
		server.sendmail(user, user_list, message.as_string())
		server.close()

	def send_main(self, pass_list, fail_list):
		pass_num = float(len(pass_list))
		fial_num = float(len(fail_list))
		count_num = pass_num + fial_num
		pass_result = "%.2f%%" %(pass_num/count_num*100)
		fail_result = "%.2f%%" %(fial_num/count_num*100)
		user_list = ['XXXXXX@qq.com']
		time_data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
		sub = '接口自动化测试报告' + time_data
		content = '此次一共运行接口个数为%d个，通过个数为%d个，失败个数为%d个，通过率为%s, 失败率为%s' %(count_num, pass_num, fial_num, pass_result, fail_result)
		self.send_mail(user_list, sub, content)
