import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_em(tp, tm):
    sender = 'dndxops@sina.com'
    receiver = 'zhuhuahua168@163.com,zoumolin008@163.com'
    smtpserver = 'smtp.sina.com'
    port = 465
    username = 'dndxops@sina.com'
    password = 'a30473b170e71983'
    mail_title = '10086流量查询短信接口告警' + tm

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')
    gjnr = "告警时间：" + tm + " 流量查询短信接口异常详情请见附件"
    # 邮件正文内容
    message.attach(MIMEText(gjnr, 'plain', 'utf-8'))

    # 构造附件2（附件为JPG格式的图片）
    att2 = MIMEText(open(tp, 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename=' + tp
    message.attach(att2)
    smtpObj = smtplib.SMTP_SSL(smtpserver, port)  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
    smtpObj.connect(smtpserver)
    smtpObj.login(username, password)
    smtpObj.sendmail(sender, receiver, message.as_string())
    print("告警邮件发送成功！！！")
    smtpObj.quit()
