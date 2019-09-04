#coding:utf-8

import smtplib
import string


HOST = "smtp.163.com"
SUBJECT = "Test email from Python"
TO = "tonghua711@163.com"
FROM = "tonghua711@163.com"
text = "Python rules them all!"
BODY = "\r\n".join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ))
#
# BODY = string.join(( "From: %s" % FROM,"To: %s" % TO,"Subject: %s" % SUBJECT ,"",text), "\r\n")
#
server = smtplib.SMTP()
server.connect(HOST,"25")
# server.starttls()
server.login("tonghua711@163.com","********")
server.sendmail(FROM, [TO], BODY)
server.quit()