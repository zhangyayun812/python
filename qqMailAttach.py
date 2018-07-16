# -*- coding: utf-8 -*-


"""邮件发送
Usage:
qqMail <receivers> <subject> <msg> <img>

"""

from docopt import docopt
from email.mime.text import MIMEText
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL
from email import encoders




if __name__ == '__main__':
    # 将绑定交互参数
    arguments = docopt(__doc__)
    receivers = arguments['<receivers>']
    subject = arguments['<subject>']
    msg = arguments['<msg>']
    img = arguments['<img>']
    mail_host = 'smtp.qq.com'
    mail_port = '465'
    mail_user = '415449304@qq.com'
    mail_passwd = 'ukiuopnvdqoibjcd'
    sender = '415449304@qq.com'
    
    smtpObj = SMTP_SSL()#将传输内容加密，QQ强制要求的
    smtpObj.connect(mail_host, mail_port)
    smtpObj.login(mail_user, mail_passwd)
    # 邮件对象
    msgAttach = MIMEMultipart()
    
    #必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件
    #通过header编码，防止主题中出现中文乱码
    msgAttach["Subject"] = Header(subject, 'utf-8')
    msgAttach["From"] = sender
    msgAttach["To"] = receivers
    # 邮件正文是MIMEText
    msgAttach.attach(MIMEText(msg, "plain", 'utf-8'))

    with open(img, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename=img)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=img)
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msgAttach.attach(mime)

    smtpObj.sendmail(sender, receivers, msgAttach.as_string())
    print('发送完成')

