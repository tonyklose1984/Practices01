# import smtplib
# import email.utils
# from email.mime.text import MIMEText
#
# msg = MIMEText('这里是消息的主体部分。')
# msg['To']=email.utils.formataddr(('admin','admin@example.com'))
# msg['From']=email.utils.formataddr(('Author','author@example.com'))
# msg['Subject']='Simple test message'
#
# server = smtplib.SMTP('mail')
# server.set_debuglevel(True)
#
# try:
#     server.sendmail()