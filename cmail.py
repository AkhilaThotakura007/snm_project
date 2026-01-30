app_password ='avqj qnfd jiok fpyg'
import smtplib
from email.message import EmailMessage #class which is used to define  mail format 
def send_mail(to,subject,body): 
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('akhilathotakura2@gmail.com',app_password)
    msg=EmailMessage()
    msg['FROM']='akhilathotakura2@gmail.com'
    msg['SUBJECT']= subject
    msg['TO']= to
    msg.set_content(body)
    server.send_message(msg)
    server.close()
