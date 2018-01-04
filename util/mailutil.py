#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 发送邮件

import ConfigParser
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

config = ConfigParser.ConfigParser()
config.readfp(open("../config.properties", "rb"))
session_name = 'email'

# 第三方 SMTP 服务
mail_host = config.get(session_name,"email.host")  # 设置服务器
mail_user = config.get(session_name,"email.user")  # 用户名
mail_pass = config.get(session_name,"email.pwd")  # 口令

sender = config.get(session_name,"email.user")

##发送邮件，receivers是接受者数组，subject是邮件标题，content是邮件内容
def send_email(receivers,subject,content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"

##发送邮件，receivers是接受者数组，subject是邮件标题，content是邮件内容,from是发件人名称，to是收件人名称
def send_email_two(receivers,subject,content,fromwhere,to):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(fromwhere, 'utf-8')
    message['To'] = Header(to, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"
