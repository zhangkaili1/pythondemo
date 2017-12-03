import os
import smtplib
import  unittest

import time
from email.header import Header

from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f=open(path,"rb")
    mail_body=f.read()
    f.close()
    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header('自动化测试报告','utf-8')
    msg['From']='bwftest126@126.com'
    msg['To']='zhakl'

    smtp=smtplib.SMTP()
    smtp.connect("smtp.126.com")
    smtp.login("bwftest126@126.com","abc123asd654")
    smtp.sendmail( 'bwftest126@126.com','shen11huiming@126.com', msg.as_string())
    print("...")






if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    suite = unittest.defaultTestLoader.discover("./day5", pattern='*Test.py')
    base_path=os.path.dirname(__file__)
    path=base_path+"/report/report"+now+".html"
    file=open(path,'wb')
    HTMLTestRunner(stream=file, verbosity=1, title="海盗商城测试报告", description=None).run(suite)
    file.close()
    send_mail(path)
