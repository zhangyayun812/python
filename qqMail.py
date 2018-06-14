# -*- coding: utf-8 -*-


"""邮件发送
Usage:
qqMail <receivers> <subject> <msg> 

"""

from docopt import docopt
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL




if __name__ == '__main__':
    # 将绑定交互参数
    arguments = docopt(__doc__)
    receivers = arguments['<receivers>']
    subject = arguments['<subject>']
    msg = arguments['<msg>']
    mail_host = 'smtp.qq.com'
    mail_port = '465'
    mail_user = '415449304@qq.com'
    mail_passwd = 'ukiuopnvdqoibjcd'
    sender = '415449304@qq.com'
    
    smtpObj = SMTP_SSL()#将传输内容加密，QQ强制要求的
    smtpObj.connect(mail_host, mail_port)
    smtpObj.login(mail_user, mail_passwd)
    msg = MIMEText(msg, "plain", 'utf-8')
    #必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件
    #通过header编码，防止主题中出现中文乱码
    msg["Subject"] = Header(subject, 'utf-8')
    msg["From"] = sender
    msg["To"] = receivers
    smtpObj.sendmail(sender, receivers, msg.as_string())
    print('发送完成')

